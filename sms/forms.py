from django import forms
from sms.models import Sms


class SimpleSmsForm(forms.ModelForm):

    class Meta:
        model = Sms
        fields = ['sender', 'recipient', 'content']


class SmsForm(forms.ModelForm):

    class Meta:
        model = Sms
        fields = ['recipient', 'content', 'sender', 'flash', 'secure', 'test']
