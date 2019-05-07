from django.forms import ModelForm
from pings.models import Company, Guest, Ping


class PingForm(ModelForm):
    class Meta:
        model = Ping
        fields = ['subject', 'body']
