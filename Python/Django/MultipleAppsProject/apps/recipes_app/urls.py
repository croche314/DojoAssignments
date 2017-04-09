from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'logout$',logout,name='logout'),
	url(r'new_recipe$',new_recipe, name='new_recipe'),
	url(r'create_recipe$',create_recipe,name='create_recipe')
]
