from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', start, name='start'),
	url(r'^register$',register, name='register'),
	url(r'^login$',login, name='login'),
	url(r'^logout$',logout, name='logout'),
]