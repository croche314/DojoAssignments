from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^create_user$',create_user, name='create_user'),
	url(r'^login_user$',login_user, name='login_user')
]