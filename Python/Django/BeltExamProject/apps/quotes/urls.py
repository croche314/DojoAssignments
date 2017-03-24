from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'logout$',logout,name='logout'),
	url(r'create_quote$',create_quote,name='create_quote'),
	url(r'show_user/(?P<user_id>\d+)$',show_user,name='show_user'),
	url(r'add_to_favorites/(?P<quote_id>\d+)$',add_to_favorites,name='add_to_favorites'),
	url(r'remove_from_favorites/(?P<quote_id>\d+)$',remove_from_favorites,name='remove_from_favorites')
]