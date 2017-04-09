from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..book_reviews.models import User
import bcrypt, re
# Create your views here.
def start(request):
	return render(request, 'login/login.html')

def register(request):
	name = request.POST['txt_name']
	alias = request.POST['txt_alias']
	email = request.POST['txt_email']
	password = request.POST['txt_password']
	confirm_pw = request.POST['txt_confirm_pw']

	if len(name)<1 or len(alias)<1 or len(email)<1 or len(password)<1 or len(confirm_pw)<1:
		messages.warning(request,'Please make sure all fields are not blank')
		return redirect('login:start')
	elif password != confirm_pw:
		messages.warning(request,'passwords must match')
		return redirect('login:start')
	else:
		new_user = User.objects.create(name=name,alias=alias,email=email,password=password)
		request.session['user_id'] = new_user.id
		request.session['alias'] = new_user.alias
		request.session['email'] = new_user.email
		messages.success(request,'New user created! Welcome!')
		return redirect('/books')


def login(request):
	email = request.POST['txt_email']
	password = request.POST['txt_password']

	this_user = User.objects.get(email=email)
	if this_user.password == password:
		request.session['user_id'] = this_user.id
		request.session['alias'] = this_user.alias
		request.session['email'] = this_user.email
		return redirect('/books')
	else:
		messages.warning(request,'invalid login')
		return redirect('login:start')

def logout(request):
	request.session.flush()
	messages.success(request,'Logged out successfully')
	return redirect('login:start')