from flask import Flask, render_template, request, redirect, session
import random, time
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET','POST'])
def index():
	session['gold'] = 0
	session['message'] = ""
	session['msg_count'] = 0
	print 'total gold:', session['gold']
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	building = request.form['building']
	print "********* it's a", building, "! ***********"

	session['msg_count'] += 1
	session['message'] += "(" + str(session['msg_count']) + ") " 

	# Farm
	if building == 'farm':
		random_num = random.randrange(10,21)
	# Cave
	elif building == 'cave':
		random_num = random.randrange(5,11)
	# House
	elif building == 'house':
		random_num = random.randrange(2,6)
	# Casino
	else:
		random_num = random.randrange(-50,51)

	session['gold'] += random_num
	if random_num > 0:
		session['message'] += "Earned " + str(random_num) + " golds from the " + str(building) + "!"
	else:
		session['message'] += "Entered a casino and lost " + str(random_num) + " golds...Ouch.." 

	session['message'] += "<br>"
	

	print "random_num:",random_num
	print 'total gold:', session['gold']
	return render_template('index.html')

app.run(debug=True)

