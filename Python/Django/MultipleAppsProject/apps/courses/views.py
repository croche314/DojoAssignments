from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from ..login_reg.models import User 
from django.core.urlresolvers import reverse

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
		return redirect(reverse('courses:'))
	else:
		print '*' * 50
		print 'Error: add_new_course if statement'
		print '*' * 50

		return redirect(reverse('courses:'))

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
	return redirect(reverse('courses:'))

def enroll_form(request):
	if 'user_id' in request.session:
		user_id = request.session['user_id']
		current_user = User.objects.get(id=user_id)
	else:
		user_id = 1

	query_all_users = User.objects.all()
	query_all_courses = Course.objects.all()
	context = {
		'all_users': query_all_users,
		'all_courses': query_all_courses,
		'user_id': user_id
	}

	return render(request, 'courses/enroll.html', context)

def commit_enroll(request):
	user_id = request.POST['select_user']
	course_id = request.POST['select_course']
	print '-' * 50
	print 'user_id:',user_id
	print 'course_id:', course_id
	print '-' * 50

	this_course = Course.objects.get(id=course_id)
	this_user = User.objects.get(id=user_id)
	this_user.courses.add(this_course)
	this_course.num_of_students += 1
	this_course.save()

	# num_of_students = len(this_course.students.all())
	# print '-' * 50
	# print num_of_students
	# print '-' * 50

	return redirect(reverse('courses:enroll'))
