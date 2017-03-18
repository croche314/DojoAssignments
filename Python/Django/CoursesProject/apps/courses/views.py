from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
	all_courses = Course.objects.all().order_by('name')
	context = {
		"all_courses": all_courses
	}
	return render(request, 'courses/index.html', context)

def add_new_course(request):
	if request.method == 'POST':
		Course.objects.create(name=request.POST['txt_name'],description=request.POST['txt_description'])
		messages.add_message(request,messages.SUCCESS,'Course successfully created!')
		return redirect('/')
	else:
		print '*' * 50
		print 'Error: add_new_course if statement'
		print '*' * 50

		return redirect('/')

def destroy_confirm(request,id):
	query = Course.objects.get(id=id)
	context = {
		'this_course': query
	}
	return render(request, 'courses/confirm_destroy.html',context)

def destroy(request,id):
	Course.objects.filter(id=id).delete()
	print '*' * 50
	print '\tRow Successfully Deleted!'
	print '*' * 50
	messages.success(request,'Course successfully deleted!')
	return redirect('/')
