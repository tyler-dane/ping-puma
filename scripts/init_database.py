import json
import datetime
from pings.models import Guest, Company, Ping


def run():
    init_companies()
    init_guests()
    init_ping_templates()


def init_companies():
    """creates Company model for each item in JSON"""
    companies = json.load(open('pings/static/companies.json'))
    for c in companies:
        Company.objects.create(**c)
        print(Company.city)


def init_guests():
    """formats and creates Guest model for each item in JSON"""
    guests = json.load((open('pings/static/guests_formatted.json')))
    cleaned_guest_data = clean_guest_data(guests)
    for g in cleaned_guest_data:
        Guest.objects.create(**g)


def init_ping_templates():
    """creates new Ping template model for each item in JSON"""
    pings_templates = json.load(open('pings/static/ping_templates.json'))
    for i in pings_templates:
        body = "".join("{}".format(val) for key, val in i["body"].items())
        Ping.objects.create(
            subject=i["subject"],
            body=body,
            employee_name=""
        )
        print("'%s' Ping created " % i["subject"])


def clean_guest_data(guest_list):
    """returns Django-compatible DateTimeField object by converting
    epoch to date.time.datetime"""

    with open('pings/static/guests_formatted.json', 'r') as file:
        json_data = json.load(file)

        for i in json_data:
            i['startTimestamp'] = datetime.datetime.fromtimestamp(i['startTimestamp'])
            i['endTimestamp'] = datetime.datetime.fromtimestamp(i['endTimestamp'])
        print(json_data)
    return json_data



# TODO delete before submitting
def manual_test():
    print('creating Company...')
    company1 = Company.objects.create(
        id=92,
        company='Polar Enterprises',
        city='Madison',
        timezone='America/Chicago'
    )
    print(company1.city)

    company2_json = {
        "id": 212,
        "company": "Hotel California",
        "city": "Santa Barbara",
        "timezone": "US/Pacific"
    }

    company2 = Company.objects.create(**company2_json)
    print(company2.timezone)
