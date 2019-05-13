from django.forms import ModelForm

from pings.models import Ping


class PingForm(ModelForm):
    class Meta:
        model = Ping
        fields = ('subject', 'body', 'is_template', 'company', 'guest')

    def save(self, commit=True):
        ping = super(PingForm, self).save(commit=False)

        if commit:
            try:
                ping.save()
                success_str = \
                    "**********\n" \
                    "Successfully sent the following Ping: \n \nSender: {} \nRecipient: {} \nMessage: {}\n" \
                    "***********\n".format(ping.company, ping.guest, ping.body)
                print(success_str)
            except ValueError:
                print("Invalid value found in PingForm")

        return ping

