from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index, name=''),
	url(r'^courses/add_new$', add_new_course, name='add_new'),
	url(r'^(?P<id>\d+)/destroy$',destroy_confirm, name='destroy_confirm'),
	url(r'^(?P<id>\d+)/destroy/confirmed$',destroy, name='destroy'),
	url(r'^enroll$', enroll_form,name='enroll'),
	url(r'^commit_enroll$',commit_enroll, name='commit_enroll')
]