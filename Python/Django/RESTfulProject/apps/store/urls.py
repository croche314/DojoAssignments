from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^new$',new),
	url(r'^create$', create),
	url(r'^show/(?P<id>\d+)$',show),
	url(r'^edit/(?P<id>\d+)$',edit),
	url(r'^update/(?P<id>\d+)$',update),
	url(r'^destroy/(?P<id>\d+)$',destroy)

]