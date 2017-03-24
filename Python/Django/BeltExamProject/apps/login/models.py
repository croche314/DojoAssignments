from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	alias = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	date_of_birth = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	quote_count = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

