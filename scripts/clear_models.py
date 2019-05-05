from django.core.management.base import BaseCommand
from pings.models import Guest, Company, Ping

def run():
    """Removes models from database"""
    Guest.objects.all().delete()
    Company.objects.all().delete()
    Ping.objects.all().delete()
