from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^',index, name=''),
	url(r'add$',new_book, name='add'),
	url(r'create$',create_book, name='create'),
	url(r'(?P<book_id>\d+)$',show_book, name='show_book'),
	url(r'add_review/(?P<book_id>\d+)$',add_review, name='add_review'),
	url(r'reviews/(?P<review_id>\d+)/delete$',destroy_review, name='delete'),
	url(r'users/(?P<user_id>\d+)$',show_user, name='show_user')
]