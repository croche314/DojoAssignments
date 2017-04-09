from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt, re 

def index(request):
	return render(request, 'login/index.html')

def new_user(request):
	return render(request, 'login/new_user.html')

def create_user(request):
	first_name = request.POST['txt_first_name']
	last_name = request.POST['txt_last_name']
	cuisine = request.POST['txt_cuisine']
	password = request.POST['txt_password']
	confirm_pw = request.POST['txt_confirm_password']

	if len(first_name)<1 or len(last_name)<1 or len(cuisine)<1 or len(password)<1 or len(confirm_pw)<1:
		messages.warning(request,'Please make sure no fields are blank')
		return redirect('login:index')
	elif password != confirm_pw:
		messages.warning(request,'passwords must match')
		return redirect('login:index')
	else:
		# hash password
		try:
			hashed_pw = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
			print '-' * 50
			print 'hashed_pw:', hashed_pw
			print '-' * 50
			new_user = User.objects.create(first_name=first_name,last_name=last_name,cuisine=cuisine,password=hashed_pw)
			print '-' * 50
			print 'new_user:',new_user
			print '-' * 50
			request.session['user_id'] = new_user.id
			messages.success(request,'New user created! Welcome!')
			print 'new user created!'
			return redirect('recipes:index')
		except:
			messages.warning(request, 'hash pword problem')
			return redirect('login:index')
	return redirect('recipes:index')

def login_user(request):
	first_name = request.POST['txt_first_name']
	password = request.POST['txt_password']

	if len(first_name)<1 or len(password)<1:
		messages.warning(request, 'both login fields are required')
		return redirect('login:index')
	else:
		try:
			this_user = User.objects.get(first_name=first_name)
			if password == this_user.password:
				messages.success(request, 'You are logged in!')
				request.session['user_id'] = this_user.id

				return redirect('recipes:index')
			else:
				messages.warning(request, 'invalid password, try again')

				return redirect('login:index')
		except:
			messages.warning(request, 'user not found')
			return redirect('login:index')