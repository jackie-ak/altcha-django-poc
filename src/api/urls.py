from rest_framework import routers

from django.urls import include, path

from .views import altcha_challenge

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('altcha/', altcha_challenge, name='altcha'),
]
