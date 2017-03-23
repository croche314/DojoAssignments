from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index, name=''),
	url(r'^registration$',validate_registration, name='validate_registration'),
	url(r'^success$', success, name='success'),
	url(r'^login$',login, name='login')
]