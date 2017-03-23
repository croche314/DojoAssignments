from __future__ import unicode_literals
from django.shortcuts import redirect
from django.db import models
import re
from django.contrib import messages


# Create your models here.
class UserManager(models.Manager):
	def validate_name(request,self,name):
		if len(name) < 1: # name is empty
			print '-' * 50
			print request
			print '-' * 50
			messages.add_message(self,messages.WARNING,'name fields are required')
			return redirect('/')
		elif len(name) < 2: #name is less than two characters long
			messages.warning(self,'name fields must be at least 2 characters long')
			return redirect('/')
		else: 
			name_valid = re.search(r'^[a-zA-z]+', name)
			if name_valid != None:
				print '-' * 50
				print 'Valid name!'
				print '-' * 50
				return True
			else:
				print '-' * 50
				print 'Invalid name!'
				print '-' * 50
				messages.add_message(self,messages.INFO,'Names can only contain letters')
				return redirect('/')

	def validate_email(request,self,email):
		emailValid = re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',email)
		if emailValid == None:
			messages.add_message(self,messages.WARNING,'Invalid Email!')
			return False
		else:
			print 'Valid Email!'
			return True

	def validate_password(request, self, password, confirm_pass):
		if len(password) < 8:
			messages.warning(self,'password must be at least 8 characters long')
			return redirect('/')
		elif password != confirm_pass:
			messages.warning(self, 'passwords must match!')
			return redirect('/')
		else: # password is valid and both match
			print '-' * 50
			print 'Valid password(s)!'
			print '-' * 50
			return True


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	objects = UserManager()

