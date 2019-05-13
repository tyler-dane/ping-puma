import datetime

from django.urls import reverse
from django.test import TestCase
from .models import Company, Guest, Ping
from .forms import PingForm

#############################
# Utility objects & variables
#############################
company1 = Company.objects.create(
    company='Polar Enterprises',
    city='Madison',
    timezone='America/Chicago'
)

guest1 = Guest.objects.create(
    id=101,
    firstName='Clark',
    lastName ='Kent',
    reservation='101',
    email='superman00001@hotmail.com',
    roomNumber=404,
    startTimestamp=datetime.datetime.now(),
    endTimestamp=datetime.datetime.now() + datetime.timedelta(days=3)
)

ping1 = Ping.objects.create(
    subject='foo',
    body='bar',
    is_template=True,
    company=company1,
    guest=guest1
)

ping_form1 = PingForm


##############
# View tests #
##############
class PingsIndexViewTests(TestCase):
    def test_no_templates(self):
        """If no templates exist, an appropriate mesasge should be displayed"""
        response = self.client.get(reverse('pings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No templates")


##############
# Form tests #
##############
class PingFormTests(TestCase):
    def test_ping_form_contains_required_fields(self):
        """PingForm should contain all Ping fields"""
        self.assertContains(ping_form1.cleaned_data, ['subject, body, is_template, company, guest'])


###############
# Model tests #
###############
class GuestModelTests(Guest):
    #TODO
    def test_checked_in_within_last_24hrs_handles_edge_cases(self):
        # different time zones
        # offset server times
        # daylight savings times
        pass


class CompanyModelTests(Company):
    #TODO
    def test_company_fields_contain_requirements(self):
        # company, city, timezone
        pass


class PingModelTests(Ping):
    #TODO
    def test_ping_contains_proper_foreign_keys(self):
        # to Guest and Company
        pass


