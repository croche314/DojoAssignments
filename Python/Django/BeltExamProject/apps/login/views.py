from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt, re

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def new_user(request):
	return render(request, 'login/new_user.html')

def create_user(request):
	name = request.POST['txt_name']
	alias = request.POST['txt_alias']
	email = request.POST['txt_email']
	emailValid = re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',email)
	date_of_birth = request.POST['txt_date_of_birth']
	password = request.POST['txt_password']
	confirm_pw = request.POST['txt_confirm_password']

	if len(name)<1 or len(alias)<1 or len(email)<1 or len(date_of_birth)<1 or len(password)<1 or len(confirm_pw)<1:
		messages.warning(request,'Please make sure no fields are blank')
		return redirect('login:index')
	elif len(password)<6:
		messages.warning(request, 'password must be at least 6 characters')
		return redirect('login:index')
	elif emailValid == None:
		messages.warning(request, 'invalid email format')
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
			new_user = User.objects.create(name=name,alias=alias,email=email,date_of_birth=date_of_birth,password=hashed_pw,quote_count=0)
			print '-' * 50
			print 'new_user:',new_user
			print '-' * 50
			request.session['user_id'] = new_user.id
			request.session['alias'] = new_user.alias

			messages.success(request,'New user created! Welcome!')
			print 'new user created!'
			return redirect('quotes:index')
		except:
			messages.warning(request, 'hash pword problem')
			return redirect('login:index')
	return redirect('recipes:index')

def login_user(request):
	email = request.POST['txt_email']
	password = request.POST['txt_password']

	if len(email)<1 or len(password)<1:
		messages.warning(request, 'both login fields are required')
		return redirect('login:index')
	elif len(password)<6:
		messages.warning(request, 'password must be at least 6 characters')
		return redirect('login:index')
	else:
		try:
			this_user = User.objects.get(email=email)
			print '-' * 50
			print 'password',this_user.password
			print '-' * 50
			if this_user.password == bcrypt.hashpw(password.encode("UTF-8"),this_user.password.encode("UTF-8")):
				messages.success(request, 'You are logged in!')
				request.session['user_id'] = this_user.id
				request.session['alias'] = this_user.alias

				return redirect('quotes:index')
			else:
				messages.warning(request, 'invalid password, try again')

				return redirect('login:index')
		except:
			messages.warning(request, 'user not found')
			return redirect('login:index')

