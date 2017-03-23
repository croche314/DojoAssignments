from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', start),
	url(r'create_user$',create_user),
	url(r'index$',index),
	url(r'logout$',logout),
	url(r'login$',login),
	url(r'create_secret$', create_secret),
	url(r'popular$',show_popular_secrets),
	url(r'create_like/(?P<secret_id>\d+)$',create_like),
	url(r'delete/(?P<secret_id>\d+)$',delete_secret)
]