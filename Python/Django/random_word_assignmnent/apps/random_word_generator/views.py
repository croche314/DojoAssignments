from django.shortcuts import render, HttpResponse
import string, random

# Create your views here.
def index(request):
	request.session['attempts'] = 0
	if 'word' in request.session:
		del request.session['word']
	return render(request,'random_word_generator/index.html')

def generate(request):
	attempts = request.session['attempts']
	attempts += 1
	request.session['attempts'] = attempts

	print '*' * 50
	print 'Generating word...'
	print '*'*50

	random_word_arr = []

	for index in range(0,15):
		random_letter = random.choice(string.letters)
		random_word_arr.append(random_letter)

	random_word_str = "".join(random_word_arr)
	print random_word_str
	request.session['word'] = random_word_str

	return render(request,'random_word_generator/index.html')