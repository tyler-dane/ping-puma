from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from .models import Ping, Company, Guest
from pings.forms import PingForm


def index(request):
    """Instantiates and saves ping form"""
    pings = Ping.objects.order_by('subject')
    companies = Company.objects.all()
    guests = Guest.objects.all()

    if request.method == 'POST':
        ping_form = PingForm(request.POST)
        if ping_form.is_valid():
            ping_form.save()
            return redirect('/pings/add-ping')
        else:
            # uses placeholders (to avoid coercing variables into message),
            # key mappings (so variables can be in any order or omitted altogether), and
            # wraps message with `gettext` (to enable translation)
            # in effort to provide more useful error
            raise ValidationError(_('Invalid form value: %(value)s'), code='invalid')
    else:
        ping_form = PingForm(initial={
            'subject': 'Enter subject here',
            'body': 'Enter message details here',
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

def history(request):
    """returns history of sent Pings"""
    custom_ping_history = Ping.objects.filter(is_template=False).order_by('subject')
    context = {'custom_ping_history': custom_ping_history}
    return render(request, 'pings/history.html', context)

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
            raise ValidationError(_('Invalid form value: %(value)s'), code='invalid')
    else:
        ping_form = PingForm(initial={'subject': 'Enter a subject'})

        context = {'ping_templates': ping_templates, 'ping_form': ping_form}
        return render(request, 'pings/add_ping.html', context)


###########################
# Utility Functions       #
###########################


def get_template_bool(request):
    if "is_template" in request.POST:  # only present if user checked form
        return True
    else:
        return False

