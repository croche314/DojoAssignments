from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.

class Recipe(models.Model):
	user = models.ForeignKey(User, related_name='my_recipes')
	image_url = models.FilePathField()
	recipe_title = models.CharField(max_length=50)
	recipe_text = models.TextField()
	recipe_make_time = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)