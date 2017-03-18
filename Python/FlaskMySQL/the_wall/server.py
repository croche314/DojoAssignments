from flask import Flask,render_template,redirect,request,session,flash
from mysqlconnection import MySQLConnector
import re,datetime
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app,'the_wall_db')

@app.route('/')
def display_login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.clear()
	print 'Empty Session:', session
	flash('Successfully logged out')
	return redirect('/')

@app.route('/auth_login', methods=['GET','POST'])
def auth_login():
	user_email = request.form['html_email']
	user_password = request.form['html_password']

	query = "SELECT * FROM users WHERE email='" + user_email + "'"
	user = mysql.query_db(query)
	print "Invalid user:", user

	if len(request.form['html_email']) < 1:
		flash('* Email cannot be blank')
		print 'Email cannot be blank'
		return redirect('/')
	if len(request.form['html_password']) < 1:
		flash('* Password cannot be blank')
		return redirect('/')
	if len(request.form['html_password']) < 6:
		flash('* Password must be at least 6 characters long')
		return redirect('/') 
	if len(user) < 1:
		flash("* username doesn't exist")
		return redirect('/')
	if user[0]['password'] == request.form['html_password']:
		user = user[0]
		# convert query into session keys,values
		for item in user:
			session[item] = user[item]

		for x in session:
			print x,session[x]

		return redirect('/wall')
	else:
		flash('* Invalid password')
		return redirect('/')	

@app.route('/wall', methods=['GET','POST'])
def index():
	# Get and display all messages
	query = "SELECT first_name,last_name,email,messages.id AS message_id,message, messages.created_at FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
	all_messages = mysql.query_db(query)
	# Get and display all comments (within their message)
	comment_query = "SELECT first_name,last_name,email,message,messages.created_at AS message_created,comment,comments.user_id AS comment_user,comments.message_id,comments.created_at AS comment_created FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON messages.id = comments.message_id ORDER BY comment_created DESC"
	all_comments = mysql.query_db(comment_query)
	print 'All_comments:',all_comments
	
		
	return render_template('wall.html', all_messages=all_messages,all_comments=all_comments)

@app.route('/post_message/<id>', methods=['POST'])
def post_new_message(id):
	new_message = request.form['html_message']
	query = "INSERT INTO messages (user_id,message,created_at,updated_at) VALUES (:user_id,:new_message,:created_at,:updated_at)"
	data = {
			'user_id': id,
			'new_message': new_message,
			'created_at': datetime.datetime.now(),
			'updated_at': datetime.datetime.now()
	}
	insert_msg = mysql.query_db(query,data)
	if insert_msg > 0:
		flash('Message successfully created!')
		return redirect('/wall')
	else:
		flash('Error submitting message!')
		return redirect('/wall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def post_new_comment(message_id):
	new_comment = request.form['html_comment']
	query = "INSERT INTO comments (user_id,message_id,comment,created_at,updated_at) VALUES (:user_id,:message_id,:comment,:created_at,:updated_at)"
	data = {
			'user_id': session['id'],
			'message_id': message_id,
			'comment' : request.form['html_comment'],
			'created_at': datetime.datetime.now(),
			'updated_at': datetime.datetime.now()
	}

	create_comment = mysql.query_db(query,data)
	return redirect('/wall')

app.run(debug=True)
