import pymsgbox as pymsgbox
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render_to_response

from pings.models import Ping


class PingForm(ModelForm):
    # add dropdown (ModelChoiceField) from Templates

    class Meta:
        model = Ping
        fields = ('subject', 'body', 'is_template', 'company', 'guest')

    def save(self, commit=True):
        ping = super(PingForm, self).save(commit=False)
        ping.subject = self.cleaned_data['subject']
        ping.body = self.cleaned_data['body']
        ping.guest = self.cleaned_data['guest']
        ping.company = self.cleaned_data['company']

        if commit:
            success_str = \
                "**********\n" \
                "Successfully sent the following Ping: \n \nSender: {} \nRecipient: {} \nMessage: {}\n" \
                "***********\n".format(
                    ping.company, ping.guest, ping.body)
            print(success_str)

            ping.save()

        return ping


def bound_form(request, id):
    ping = get_object_or_404(Ping)
    ping_template = PingForm(instance=ping)
    context = {'ping_template': ping_template}
    return render_to_response('pings/add_ping_from_template.html', context)

