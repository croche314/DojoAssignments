from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'emails_db')
app.secret_key = "secret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
	email = request.form['email']
	email_valid = re.search(r'.+\@.+\..+', email)
	print email_valid
	if email_valid == None:
		flash('Invalid email')
		print 'Invalid email!'
		return redirect('/')
	else:
		print 'Valid email!'
		query = "INSERT INTO emails (email_address,created_at) VALUES ('" + email + "',NOW())"
		mysql.query_db(query)
		flash('The email address you entered (' + email + ') is a valid email address! Thank You!')
		return redirect('/success')

@app.route('/success', methods=['GET'])
def display_all_emails():
	all_emails = mysql.query_db('SELECT * FROM emails')
	print all_emails
	email_id = all_emails[0]['id']
	print "ID:",email_id

	for x in all_emails:
		print x['email_address']
	return render_template('success.html', all_emails=all_emails)


app.run(debug=True)