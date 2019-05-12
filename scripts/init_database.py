import json
import datetime
from pings.models import Guest, Company, Ping

placeholder_company = Company.objects.create(
    company="Placeholder Company",
    city="Placeholder City",
    timezone="Placeholder Timezone"
)

placeholder_guest = Guest.objects.create(
    firstName="Placeholder Guest",
    lastName="Placeholder Guest",
    reservation="Spam",
    email="ham@gmail.com",
    roomNumber=999,
    startTimestamp=datetime.datetime.now(),
    endTimestamp=datetime.datetime.now() + datetime.timedelta(days=2)
)

def run():

    init_companies()
    init_guests()
    init_ping_templates()


def init_companies():
    """creates Company model for each item in JSON"""
    companies = json.load(open('pings/static/companies.json'))
    for c in companies:
        Company.objects.create(**c)
    print("Company models created")


def init_guests():
    """formats and creates Guest model for each item in JSON"""
    guests = json.load((open('pings/static/guests_formatted.json')))
    cleaned_guest_data = clean_guest_data(guests)
    for g in cleaned_guest_data:
        Guest.objects.create(**g)
    print("Guest models created")


def init_ping_templates():
    """creates new Ping template model for each item in JSON"""
    pings_templates = json.load(open('pings/static/ping_templates.json'))
    for i in pings_templates:
        body = "".join("{}".format(val) for key, val in i["body"].items())
        Ping.objects.create(
            subject=i["subject"],
            body=body,
            is_template=True,
            company=placeholder_company,
            guest=placeholder_guest

        )
    print("Ping models created")


def clean_guest_data(guest_list):
    """returns Django-compatible DateTimeField object by converting
    epoch to date.time.datetime"""
    for i in guest_list:
        i['startTimestamp'] = datetime.datetime.fromtimestamp(i['startTimestamp'])
        i['endTimestamp'] = datetime.datetime.fromtimestamp(i['endTimestamp'])
    return guest_list
