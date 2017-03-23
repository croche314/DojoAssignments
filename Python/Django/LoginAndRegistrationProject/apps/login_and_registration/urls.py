from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^registration$',validate_registration),
	url(r'^register$',register_new_user),
	url(r'^success$', success),
	url(r'^login$',login)
]