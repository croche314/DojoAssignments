from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^ninja/(?P<color>[a-zA-z]+)$', ninja)
]