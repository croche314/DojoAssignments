from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'secret'
import re

@app.route('/')
def index():
	session.clear()
	return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']

	if len(session['email']) == 0:
		return render_template('index.html', email_message='*Email is required')
	if len(session['first_name']) == 0:
		return render_template('index.html', first_name_message='*First name is required')
	if len(session['last_name']) == 0:
		return render_template('index.html', last_name_message='*Last name is required')
	if len(session['password']) == 0:
		return render_template('index.html', password_message='*Password is required')
	if len(session['confirm_password']) == 0:
		return render_template('index.html', confirm_password_message='Confirm password is required')

	# valid email?
	email_valid = re.search(r'[\w.-]+@[\w.-]+.\w+',session['email'])
	print email_valid
	if email_valid == None:
		return render_template('index.html', email_message="*Invalid email address")
	# valid names?
	name_valid = re.search(r"^[a-zA-Z]+$", session['first_name'])
	if not name_valid:
		return render_template('index.html', first_name_message='*Names can only contain letters, unless you are a robot...')
	name_valid = re.search(r"^[a-zA-Z]+$", session['last_name'])
	if not name_valid:
		return render_template('index.html', last_name_message='*Names can only contain letters, unless you are a robot...')
	# password over 8 characters?
	if len(session['password']) < 8:
		return render_template('index.html', password_message="*Passwords must be at least 8 characters long")
	# passwords match?
	if session['password'] != session['confirm_password']:
		return render_template('index.html', confirm_password_message='Passwords must match')

	# if all pass, redirect to success
	return redirect('/success')

@app.route('/success', methods=['GET','POST'])
def success():
	return render_template('success.html')

app.run(debug=True)

