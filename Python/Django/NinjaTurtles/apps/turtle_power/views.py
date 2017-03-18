from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'turtle_power/index.html')

def ninja(request, color):
	print '*' * 50
	print color
	print '*' * 50

	if color == 'orange':
		img_file = 'michelangelo.jpg'
		turtle = 'Michelangelo'
	elif color == 'red':
		img_file = 'raphael.jpg'
		turtle = 'Raphael'
	elif color == 'purple':
		img_file = 'donatello.jpg'
		turtle = 'Donatello'
	elif color == 'blue':
		img_file = 'leonardo.jpg'
		turtle = 'Leonardo'
	else:
		img_file = 'notapril.jpg'
		turtle = "April =-("

	context = {
		'img_file': img_file,
		'turtle': turtle
	}

	return render(request,'turtle_power/ninja.html',context)