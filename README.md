# Altcha for Django login PoC

This is a proof of concept for using the [Altcha](https://altcha.org) captcha for
the login form of a [Django](https://www.djangoproject.com/) application with a
[Django REST framework](https://www.django-rest-framework.org/). At the same time
this also demonstrates how to use Altcha in Django forms in general. But the
intention for this proof of concept was to protect the login from brute force attacks,
additional to other measures that should be in place
(e.g. [axes](https://django-axes.readthedocs.io)).

## Setup & running the app

Assuming you are already familiar with developing in Python and Django, this is
what you need to do to start the demo:

1. Create and activate a virtual env (if you don't want to clutter your global or other envs)
2. Install the requirements in requirements.txt
3. Go to the src/ folder and run `python manage.py runserver`

Now you can go to http://localhost:8000/admin/ and log in, using the Django's
admin login form, extended by the Altcha widget.

## General approach

Integrating Altcha captchas in this scenario boils down to doing two things:

* providing an API endpoint that generates challenges, using the
  [altcha](https://pypi.org/project/altcha/) library
* including the `<altcha-widget>` provided as a web component by Altcha

Other scenarios are possible too. E.g. if the server generates the challenge
on form load and provides the JSON data for the widget in-line, no separate
endpoint is needed. Also, in this simple scenario we are just using the plain
captcha mechanism, without additional spam detection.
Refer to the references below for more details.

## Detailed approach

In more detail, this is what we did to our basic Django + DRF web app:

* add altcha to the Python requirements and download the minified version
  of the altcha.js library containing the widget, to serve as static contnet
  (see requirements.txt and src/statich/auth/js/altcha.min.js)
* provide an `altcha/` endpoint through the `altcha_challenge` API view
  (see src/api/urls.py and api/views.py)
* create a customized `AltchaAuthenticationForm` based on Django's default
  `AuthenticationForm`, adding the Altcha verification before the actual
  authentication verification (see src/auth/forms.py)
* create a customized templated for the login page, based on Django's default
  login template. This is the file in src/templates/auth/altcha_login.html,
  and it is a copy of django/contrib/admin/templates/admin/login.html in the
  site_packages, modified by the following two things:
  * in the `extrahead` block we add the altcha.min.js script
  * in the form, after the password field, we add the `<alchta-widget>` tag,
    providing the /api/altcha endpoint, where the widget gets its challenge
* create a custom `AltchaLoginView` based on Django's default `LoginView`,
  using our customized authentication form and template
  (see src/auth/views.py)

## References

Further stuff to read up on, besides the Altcha website, listed in the intro:

* Altcha docs: [Website Integration](https://altcha.org/docs/website-integration/)
* Altcha docs: [Server TLDR](https://altcha.org/docs/server-tldr/), or
  [Server Integration](https://altcha.org/docs/server-integration/) for more details
* [ALTCHA Server Demo for Python](https://github.com/altcha-org/altcha-starter-py) repo
  on GitHub, specifically the
  [app.py](https://github.com/altcha-org/altcha-starter-py/blob/main/app.py) file
