from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
	request.session.flush()
	return render(request, 'login_and_registration/index.html')

def validate_registration(request):
	first_name_valid = False
	last_name_valid = False
	email_valid = False
	passwords_valid = False

	first_name_valid = User.objects.validate_name(request,request.POST['txt_first_name'])
	print 'first_name_valid: ',first_name_valid
	last_name_valid = User.objects.validate_name(request,request.POST['txt_last_name'])
	print 'last_name_valid:',last_name_valid

	if len(request.POST['txt_email']) < 1:
		messages.warning(request,'email is required')
	else:
		email_valid = User.objects.validate_email(request,request.POST['txt_email'])
		if email_valid == None:
			messages.warning(request,'Invalid Email address')
		else:
			email_valid  = True
			print 'email_valid:', email_valid

	if len(request.POST['txt_password']) < 1:
		messages.warning(request,'password fields are required')
	else:
		passwords_valid = User.objects.validate_password(request, request.POST['txt_password'], request.POST['txt_confirm_pass'])




	if first_name_valid == True and last_name_valid == True and email_valid == True and passwords_valid == True:
		register_new_user(request,request.POST['txt_first_name'], request.POST['txt_last_name'], request.POST['txt_email'], request.POST['txt_password'])
		messages.success(request,'You are now registered.')

		return redirect('/success')


	return redirect('/')

def register_new_user(request, first_name, last_name, email, password):
	# password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
	new_user = User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password )
	print '-' * 50
	print 'new user id:',new_user.id
	print '-' * 50
	request.session['user_id'] = new_user.id
	print "session[user_id]:", request.session['user_id']

def login(request):
	email = request.POST['txt_email']
	if len(email) < 1:
		messages.warning(request,'email is required')
		return redirect('/')

	email_valid = User.objects.validate_email(request,email)
	if email_valid == None:
		messages.warning(request,'Invalid Email address')
		return redirect('/')
	else: # email is valid format
		email_valid  = True
		this_user = User.objects.filter(email=email)
		
		if len(this_user) > 0:
			this_user = this_user[0]
		else:
			messages.warning(request,'Email not found.')
			return redirect('/')

	password = request.POST['txt_password']
	
	if password != this_user.password:
		messages.warning(request,'Invalid password.')
		return redirect('/')
	else:
		request.session['user_id'] = this_user.id
		messages.success(request,'You are now logged in.')
		return redirect('/success')
	return redirect('/success')

def success(request):
	if 'user_id' in request.session:
		this_user = User.objects.get(id=request.session['user_id'])
		request.session['user_name'] = this_user.first_name
		print '-' * 50
		print 'Successful Login!:'
		print 'id=>', request.session['user_id']
		print 'name=>', request.session['user_name']
		print '-' * 50
		return render(request, 'login_and_registration/success.html')
	else:
		redirect('/')

