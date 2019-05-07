from django.forms import ModelForm
from pings.models import Company, Guest, Ping


class PingForm(ModelForm):
    class Meta:
        model = Ping
        fields = ['subject', 'body']

    def save(self, commit=True):
        ping = super(PingForm, self).save(commit=False)
        ping.subject = self.cleaned_data['subject']
        ping.body = self.cleaned_data['body']
        ping.employee_name = self.cleaned_data['employee_name']

        if commit:
            ping.save()
        return ping
