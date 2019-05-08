from django import forms
from django.forms import ModelForm
from pings.models import Ping


class PingForm(ModelForm):
    class Meta:
        model = Ping
        fields = ('subject', 'body', 'is_template')

    def save(self, commit=True):
        ping = super(PingForm, self).save(commit=False)
        ping.subject = self.cleaned_data['subject']
        ping.body = self.cleaned_data['body']

        if commit:
            ping.save()
        return ping






class PingFromTemplateForm(forms.Form):
    pass
#     subject = forms.CharField(max_length=100)
#     body = forms.CharField(widget=forms.Textarea, max_length=5000)
#
#     def save(self, commmit=True):
#         ping = super(PingFromTemplateForm, self).save(commit=False)
#         ping.subject = self.cleaned_data['subject']
#         ping.body = self.cleaned_data['body']
#
#         if commmit:
#             ping.save()
#         return ping