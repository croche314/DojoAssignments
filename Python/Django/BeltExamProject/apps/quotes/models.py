from __future__ import unicode_literals

from django.db import models
from .. login.models import User

# Create your models here.
class Quote(models.Model):
	author = models.CharField(max_length=50)
	message = models.TextField()
	posted_by = models.ForeignKey(User, related_name='all_my_quotes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Favorite(models.Model):
	user = models.ForeignKey(User, related_name='user_my_favorites')
	quote = models.ForeignKey(Quote, related_name='quote_my_favorites')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
