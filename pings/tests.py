import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Company, Guest, Ping

# Utility methods
company1 = Company.objects.create(
    company_name='Polar Enterprises',
    city='Madison',
    timezone='America/Chicago'
)

guest1 = Guest.objects.create(
    id=101,
    company=company1,
    first_name='Clark',
    last_name ='Kent',
    email='superman00001@hotmail.com',
    room_number=404,
    start_time=timezone.now,
    end_time=timezone.now
)


class GuestModelTests(TestCase):
    def test_field_was_updated_with_json_value(self):
        print(guest1.email)



