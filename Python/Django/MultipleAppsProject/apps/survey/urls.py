from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^result$',result),
    url(r'^reset_counter$',reset_counter)
]