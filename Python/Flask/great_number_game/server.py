from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def init_game():
	session.clear()
	answer = random.randrange(1,101)
	session['answer'] = answer
	print "new session['answer']:", session['answer']
	return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guess():
	session['guess'] = request.form['txt_num']
	message = ''

	answer = int(session['answer'])
	guess = int(session['guess'])
	print "answer:", session['answer']
	print "guess:", session['guess'] 

	if guess < answer:
		message = "Too low!"
	elif guess > answer:
		message = "Too high!"
	else:
		message = guess, 'was the number!'
		return render_template('correct.html', message=message)

	return render_template('guess.html', guess=guess,answer=answer,message=message)

@app.route('/correct', methods=['POST'])
def correct():
	return render_template('/')

app.run(debug=True)

