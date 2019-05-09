from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ping
from pings.forms import PingForm, PingFromTemplateForm, bound_form


def index(request):
    """returns list of ping objects alphabetically by subject"""
    pings = Ping.objects.order_by('subject')
    context = {'pings': pings}
    return render(request, 'pings/index.html', context)


def templates(request):
    """returns Ping templates"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    context = {'ping_templates': ping_templates}
    return render(request, 'pings/ping_templates.html', context)


def add_ping(request):
    """creates custom ping, saves to DB, and redirects to index"""
    if request.method == 'POST':
        ping_form = PingForm(request.POST)
        if ping_form.is_valid():
            ping_form.save()
            return redirect('/pings')
        else:
            print('Invalid form')
    else:
        ping_form = PingForm

        return render(request, 'pings/add_ping.html', {'ping_form': ping_form})


def add_ping_from_template(request):
    current_templates = Ping.objects.filter(is_template=True).order_by('subject')

    if request.method == 'POST':
        # save to DB
        context = {}
        return render_to_response('add_ping_from_template.html', context)
    else:
        #TODO re-implement or delete pre-populated forms
        #ping = get_object_or_404(Ping)
        #ping_template = PingForm(instance=ping)
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


def old_add_ping_from_template(request):
    #TODO Delete
    current_templates = Ping.objects.filter(is_template=True).order_by('subject')

    if request.method == 'POST':
        ping_template = PingFromTemplateForm(request.POST)
        if ping_template.is_valid():
            subject = ping_template.cleaned_data['subject']
            print(subject)
            ping_template.save()
            return redirect('/pings')
        else:
            print('Invalid form')

    else:
        ping_template = PingFromTemplateForm
        context = {'current_templates': current_templates,
                   'ping_template': ping_template}
        return render(request, 'pings/add_ping_from_template.html', context)