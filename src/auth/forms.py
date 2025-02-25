from altcha import verify_solution
from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm


class AltchaAuthenticationForm(AuthenticationForm):
    altcha = forms.CharField()

    def clean(self):
        altcha = self.cleaned_data.get('altcha')
        if not altcha:
            raise forms.ValidationError('Altcha is required.')

        try:
            verified, err = verify_solution(altcha, settings.ALTCHA_HMAC_KEY, True)
            if not verified:
                raise forms.ValidationError(f'Invalid Altcha solution. Error: {err}')
        except Exception as err:
            raise forms.ValidationError(f'Altcha validation failed: {err}')

        super().clean()
        return self.cleaned_data
