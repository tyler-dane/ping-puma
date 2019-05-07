import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Ping
from pings.forms import PingForm


def index(request):
    """returns list of ping objects alphabetically by subject"""
    ping_subjects = Ping.objects.order_by('subject')
    context = {'ping_subjects': ping_subjects}
    return render(request, 'pings/index.html', context)


def templates(request):
    """returns Ping templates"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    context = {'ping_templates': ping_templates}
    return render(request, 'pings/ping_templates.html', context)


def custom(request, guest_id):
    #TODO user render() in return

    response = "You're looking at custom ping: %s"
    return HttpResponse(response % guest_id)


def history(request, guest_id):
    """
    returns list of recently-added Pings by loading a template,
    filling context and returning an HttpResponse object
    """
    recent_pings = Ping.objects.order_by('-created_time')[:5]
    context = {'recent_pings': recent_pings}
    return render(request, 'pings/history.html', context)


def ping_form_test(request):
    print('request method: ', request.method)
    if request.method == 'POST':
        ping_form = PingForm(request.POST)
        print('ping_form: ', ping_form)
        if ping_form.is_valid():
            # process the data in form.cleaned_data as required
            text = ping_form.cleaned_data['body']
            ping_form.save()
            pings = Ping.objects.all()
            # redirect to a new URL:
            return render(request, 'pings/form_test.html', {'pings': pings})
        else:
            print('**form is not valid**')
    else:
        #ping_form = PingForm
        ping_form = Ping.objects.all()
        print('created new PingForm')

    return render(request, 'pings/form_test.html', {'ping_form': ping_form})
