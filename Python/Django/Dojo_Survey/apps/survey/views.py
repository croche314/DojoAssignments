from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	if 'submit_counter' not in request.session:
		request.session['submit_counter'] = 0
	return render(request,'survey/index.html')

def result(request):
	submit_counter = request.session['submit_counter']
	submit_counter += 1
	request.session['submit_counter'] = submit_counter

	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comments']
	return render(request,'survey/result.html')

def reset_counter(request):
	request.session['submit_counter'] = 0
	return redirect('/')