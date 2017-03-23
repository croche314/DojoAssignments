from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'validate$',validate),
	url(r'success$',success),
	url(r'delete/(?P<id>\d+)$',delete)
]