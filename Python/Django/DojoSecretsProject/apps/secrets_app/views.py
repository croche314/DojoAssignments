from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret, Like
import bcrypt, re
from django.core.urlresolvers import reverse

# Create your views here.
def start(request):
	return render(request, 'secrets_app/start.html')

def create_user(request):
	first_name = request.POST['txt_first_name']
	last_name = request.POST['txt_last_name']
	email = request.POST['txt_email']
	emailValid = re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',email)
	password = request.POST['txt_password']
	confirm_pword = request.POST['txt_confirm_password']

	if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password) < 1 or len(confirm_pword) < 1:
		messages.warning(request,'All fields are required')
		return redirect('/')
	elif emailValid == None:
		messages.warning(request,'Invalid email format')
		return redirect('/')
	elif len(password) < 6:
		messages.warning(request,'password must be at least 6 characters')
		return redirect('/')
	elif password != confirm_pword:
		messages.warning(request,'passwords must match')
		return redirect('/')
	else:
		new_user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
		request.session['user_id'] = new_user.id
		request.session['user_name'] = new_user.first_name
		return redirect('/index')

def index(request):
	all_users_query = User.objects.all()
	all_secrets_query = Secret.objects.all().order_by('-created_at')
	all_likes_query = Like.objects.all()

	context = {
		'all_users': all_users_query,
		'all_secrets': all_secrets_query,
		'all_likes': all_likes_query
	}
	return render(request, 'secrets_app/index.html', context)

def logout(request):
	# request.session.flush()
	return redirect('/')

def login(request):
	this_email = request.POST['txt_email']
	this_password = request.POST['txt_password']
	this_user = User.objects.get(email=this_email)

	request.session['user_id'] = this_user.id
	request.session['user_email'] = this_user.email
	request.session['user_name'] = this_user.first_name

	print '*' * 50
	print 'session[id]:', request.session['user_id']
	print 'session[name]:',request.session['user_name']
	print '*' * 50
	return redirect('/index')

def create_secret(request):
	this_user_id = User.objects.get(id=request.session['user_id'])
	this_secret_text = request.POST['txt_secret_text']

	Secret.objects.create(secret_text=this_secret_text,user=this_user_id)
	messages.success(request,"Secret created! Don't worry, we can keep a secret...")

	return redirect('/index')

def delete_secret(request, secret_id):
	delete_this = Secret.objects.filter(id=secret_id).delete()
	messages.success(request,'Secret deleted!')
	return redirect('/index')

def create_like(request,secret_id):
	this_user = User.objects.get(id=request.session['user_id'])
	this_secret = Secret.objects.get(id=secret_id)
	new_like = Like.objects.create(user=this_user,secret=this_secret)
	this_secret.num_of_likes += 1
	this_secret.save()

	messages.success(request,'You liked a secret!')

	return redirect('/index')

def show_popular_secrets(request):
	all_secrets_query = Secret.objects.all().order_by('-num_of_likes')

	context = {
		'all_secrets': all_secrets_query
	}

	return render(request, 'secrets_app/popular.html',context)




