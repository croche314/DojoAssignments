from django.shortcuts import render
import random
from time import ctime

# Create your views here.
def index(request):
	request.session['gold'] = 0
	request.session['message'] = ""
	request.session['msg_count'] = 0
	return render(request,'ninja_gold/index.html')

def process_money(request,building):
		# print '*' * 50
		# print random_num
		# print '*' * 50
	print '*' * 50
	print 'Visited the', building, "!"
	print '*' * 50
	if building == 'farm':
		random_num = random.randrange(10,21)
	elif building == 'cave':
		random_num = random.randrange(5,11)
	elif building == 'house':
		random_num = random.randrange(2,6)
	elif building == 'casino':
		random_num = random.randrange(-50,51)
	else:
		print '*' * 50
		print 'Error in if building!...'
		print '*' * 50
		random_num = 0

	request.session['gold'] += random_num
	if random_num > 0:
		request.session['message'] += "Earned " + str(random_num) + " golds from the " + str(building) + "!"
	else:
		request.session['message'] += "Entered a casino and lost " + str(random_num) + " golds...Ouch.." 

	request.session['message'] += "..." + str(ctime()) + "<br>"


	return render(request,'ninja_gold/index.html')


