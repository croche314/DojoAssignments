from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def validate_email(self, email):
		emailValid = re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',email)

		if emailValid != None:
			print 'Valid email! =>', email
			return True
		else:
			print 'Invalid email! =>', email
			return False

class User(models.Model):
	email = models.EmailField(max_length=50)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = UserManager()

