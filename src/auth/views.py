from django.contrib.auth.views import LoginView

from .forms import AltchaAuthenticationForm


class AltchaLoginView(LoginView):
    authentication_form = AltchaAuthenticationForm
    template_name = 'auth/altcha_login.html'
