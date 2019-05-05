import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ping


def index(request):
    """returns list of ping objects alphabetically by subject"""
    ping_subjects = Ping.objects.order_by('subject')
    context = {'ping_subjects': ping_subjects}
    return render(request, 'pings/index.html', context)


def templates(request, guest_id):
    """returns serialized object as a JSON-formatted string"""
    json_data = json.load(open('pings/static/ping_templates.json'))
    template_data = json.dumps(json_data)
    context = {'template_data': template_data}
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
