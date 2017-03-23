from django.shortcuts import render
import datetime
from time import ctime

# Create your views here.

def index(request):
	date = ctime()
	context = {
		"date":date
	}
	return render(request, 'timedisplay/display_time.html', context)