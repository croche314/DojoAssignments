from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', start),
	url(r'^register$',register),
	url(r'^login$',login),
	url(r'^logout$',logout),
	url(r'^books$',index),
	url(r'books/add$',new_book),
	url(r'^books/create$',create_book),
	url(r'^books/(?P<book_id>\d+)$',show_book),
	url(r'books/add_review/(?P<book_id>\d+)$',add_review),
	url(r'reviews/(?P<review_id>\d+)/delete$',destroy_review),
	url(r'users/(?P<user_id>\d+)$',show_user)
]