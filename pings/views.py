from django.shortcuts import render, redirect, render_to_response

from .models import Ping, Company, Guest
from pings.forms import PingForm


def index(request):
    """TODO comment"""
    pings = Ping.objects.order_by('subject')
    companies = Company.objects.all()
    guests = Guest.objects.all()

    if request.method == 'POST':
        ping_form_expanded = PingForm(request.POST)
        if ping_form_expanded.is_valid():
            ping_form_expanded.save()
            return redirect('/pings/add-ping')
        else:
            print('Invalid form')
    else:
        ping_form = PingForm(initial={
            'subject': 'Enter subject here',
            'body': 'Enter message details here.\n\nAfter clicking Send Custom Ping, you can view it under'
                    ' the Custom Ping History list on this page or by looking for the message surrounded '
                    'by *****s in your terminal',
            'is_template': False
        })
        context = {
            'companies': companies,
            'guests': guests,
            'pings': pings,
            'ping_form': ping_form
        }
        return render(request, 'pings/index.html', context)


def templates(request):
    """returns Ping templates"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    context = {'ping_templates': ping_templates}
    return render(request, 'pings/ping_templates.html', context)


def add_ping(request):
    """creates ping, saves to DB, and redirects to index"""
    ping_templates = Ping.objects.filter(is_template=True).order_by('subject')
    if request.method == 'POST':

        subject = request.POST["subject"]
        body = request.POST["body"]
        company = request.POST["company"]
        guest = request.POST["guest"]
        is_template = get_template_bool(request)
        ping_form = PingForm(
            {'subject': subject,
             'body': body,
             'is_template': is_template,
             'company': company,
             'guest': guest
             }
        )

        if ping_form.is_valid():
            ping_form.save()
            return redirect('/pings')
        else:
            print('Invalid form')
    else:
        ping_form = PingForm(initial={'subject': 'Enter a subject'})

        context = {'ping_templates': ping_templates, 'ping_form': ping_form}
        return render(request, 'pings/add_ping.html', context)


def add_ping_from_template(request):
    current_templates = Ping.objects.filter(is_template=True).order_by('subject')

    if request.method == 'POST':
        context = {}
        return render_to_response('add_ping_from_template.html', context)
    else:
        ping_template = PingForm()
        print('ping_template:', ping_template)
        context = {'current_templates': current_templates,
                   'ping_template': ping_template}
        return render(request, 'pings/add_ping_from_template.html', context)


###########################
# Utility Functions       #
###########################
def get_template_bool(request):
    if "is_template" in request.POST:  # only present if user checked form
        return True
    else:
        return False

