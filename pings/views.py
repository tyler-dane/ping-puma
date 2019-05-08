import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import PingFromTemplateForm

from .models import Ping
from pings.forms import PingForm


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
    if request.method == 'POST':
        ping_form = PingForm(request.POST)
        if ping_form.is_valid():
            # save to DB and return to /pings view
            ping_form.save()
            return redirect('/pings')
        else:
            print('Form is not valid**')
    else:
        ping_form = PingForm

        return render(request, 'pings/add_ping.html', {'ping_form': ping_form})


def add_ping_from_template(request, ping):
    if request.method == 'POST':
        print('post')
        #form = PingFromTemplateForm(request.POST, instance=request.template_ping)
        ping.pk = None  # make copy of template ping object
        ping.save()
    else:
        print('not post')


def history(request, guest_id):
    """
    returns list of recently-added Pings by loading a template,
    filling context and returning an HttpResponse object
    """
    recent_pings = Ping.objects.order_by('-created_time')[:5]
    context = {'recent_pings': recent_pings}
    return render(request, 'pings/history.html', context)