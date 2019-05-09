from django import forms
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render, render_to_response

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


def bound_form(request, id):
    ping = get_object_or_404(Ping)
    ping_template = PingForm(instance=ping)
    context = {'ping_template': ping_template}
    return render_to_response('pings/add_ping_from_template.html', context)



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