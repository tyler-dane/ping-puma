from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ping
from pings.forms import PingForm, PingFormExpanded, PingFromTemplateForm, bound_form


def index(request):
    """TODO comment"""
    pings = Ping.objects.order_by('subject')

    if request.method == 'POST':
        ping_form_expanded = PingFormExpanded(request.POST)
        if ping_form_expanded.is_valid():
            ping_form_expanded.save()
            return redirect('/pings/add-ping')
        else:
            print('Invalid form')
    else:
        ping_form_expanded = PingFormExpanded(initial={
            'subject': 'Give your Ping a subject',
            'body': 'Enter message details here',
            'is_template': False
        })
        context = {'pings': pings, 'ping_form_expanded': ping_form_expanded}
        return render(request, 'pings/index.html', context)


def templates(request):
    """returns Ping templates"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    context = {'ping_templates': ping_templates}
    return render(request, 'pings/ping_templates.html', context)


def add_ping(request):
    """creates custom ping, saves to DB, and redirects to index"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    if request.method == 'POST':
        subject = request.POST["subject"]
        body = request.POST["body"]
        is_template = get_template_bool(request)

        ping_form = PingForm(
            {'subject': subject, 'body': body, 'is_template': is_template})
        if ping_form.is_valid():
            ping_form.save()
            return redirect('/pings')
        else:
            print('Invalid form')
    else:
        ping_form = PingForm(initial={'subject': 'temp subject'})

        context = {'ping_templates': ping_templates, 'ping_form': ping_form}
        return render(request, 'pings/add_ping.html', context)


def add_ping_from_template(request):
    current_templates = Ping.objects.filter(is_template=True).order_by('subject')

    if request.method == 'POST':
        # save to DB
        context = {}
        return render_to_response('add_ping_from_template.html', context)
    else:
        ping_template = PingForm()
        print('ping_template:', ping_template)
        context = {'current_templates': current_templates,
                   'ping_template': ping_template}
        return render(request, 'pings/add_ping_from_template.html', context)


def history(request, guest_id):
    """
    returns list of recently-added Pings by loading a template,
    filling context and returning an HttpResponse object
    """
    recent_pings = Ping.objects.order_by('-created_time')[:5]
    context = {'recent_pings': recent_pings}
    return render(request, 'pings/history.html', context)


###########################
# Utility Functions       #
###########################
def get_template_bool(request):
    if "is_template" in request.POST:  # only present if user checked on form
        return True
    else:
        return False
