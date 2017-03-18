from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^process_money/(?P<building>[a-zA-Z]+)$',process_money)
]
