from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^add_new$', add_new_course),
	url(r'^courses/(?P<id>\d+)/destroy$',destroy_confirm),
	url(r'^courses/(?P<id>\d+)/destroy/confirmed$',destroy)
]