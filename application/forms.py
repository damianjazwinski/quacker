from django import forms
from application.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
import urllib
import json


class UserPanelForm(forms.ModelForm):
    image_link = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Link to profile photo',
            'class': 'form-control'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'rows': '4',
            'cols': '40',
            'placeholder': 'About me',
            'class': 'form-control'
        }))

    class Meta:
        model = Profile
        fields = ('image_link', 'description',)


class RegisterForm(UserCreationForm):
    captcha = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']

        error = False

        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': captcha
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if not result['success']:
            error = True

        if error:
            raise forms.ValidationError('Captha validation error')

        return captcha