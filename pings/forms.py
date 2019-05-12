from django.forms import ModelForm

from pings.models import Ping


class PingForm(ModelForm):
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
            ping.save()
            success_str = \
                "**********\n" \
                "Successfully sent the following Ping: \n \nSender: {} \nRecipient: {} \nMessage: {}\n" \
                "***********\n".format(
                    ping.company, ping.guest, ping.body)
            print(success_str)
        return ping

