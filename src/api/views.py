import datetime

from altcha import ChallengeOptions, create_challenge
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def altcha_challenge(request):
    options = ChallengeOptions(
        expires=datetime.datetime.now() + datetime.timedelta(hours=1),
        max_number=100000,  # this should be made configurable in the .env file
        hmac_key=settings.ALTCHA_HMAC_KEY,
    )
    challenge = create_challenge(options)
    return Response(challenge.__dict__)
