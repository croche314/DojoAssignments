from __future__ import unicode_literals

from django.db import models
from ..login_reg .models import User

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	students = models.ManyToManyField(User,related_name='courses')
	num_of_students = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

