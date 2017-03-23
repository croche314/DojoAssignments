from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, 'email_validation/index.html')

def validate(request):
	server_email = request.POST['txt_email']
	valid = User.objects.validate_email(server_email)
	
	if valid:
		User.objects.create(email=server_email)
		messages.add_message(request, messages.SUCCESS,'The email address you entered (' + server_email + ') is a valid email address! Thank You!')
		return redirect('/success')
	else:
		messages.add_message(request,messages.ERROR,'Invalid Email!')
		return redirect('/')

def success(request):
	query = User.objects.all()
	context = {
		'all_emails': query
	}
	return render(request, 'email_validation/success.html', context)

def delete(request,id):
	print '-' * 50
	print 'This is delete!'
	print '-' * 50

	User.objects.filter(id=id).delete()
	messages.add_message(request,messages.INFO,'Record deleted!')
	return redirect('/')
