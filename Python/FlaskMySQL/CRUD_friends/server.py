from flask import Flask,render_template,session,flash,redirect,request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	all_friends = mysql.query_db('SELECT * FROM friends')
	return render_template('index.html', all_friends=all_friends)

@app.route('/friends', methods=['POST'])
def create():
	first_name = request.form['html_first_name']
	last_name = request.form['html_last_name']
	email = request.form['html_email']

	query = "INSERT INTO friends (first_name,last_name,email,created_at) VALUES ('" + first_name + "','" + last_name + "','" + email + "',NOW())"
	new_friend = mysql.query_db(query)
	print "New friend created at ID:", new_friend
	flash("You made a new friend!")
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit_friend(id):
	query = "SELECT id,first_name,last_name,email FROM friends WHERE id = " + id
	this_friend = mysql.query_db(query)
	this_friend = this_friend[0]
	print this_friend

	return render_template('edit_friend.html',this_friend=this_friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name=:first_name,last_name=:last_name,email=:email WHERE id=" + id
	data = {
			'first_name': request.form['html_first_name'],
			'last_name': request.form['html_last_name'],
			'email': request.form['html_email']
	}
	mysql.query_db(query, data)
	print "Friend (" + id + ") updated!"
	flash("Friend("+id+") updated!")
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id=" + id
	mysql.query_db(query)
	print "Deleted friend (" + id + ")!"
	flash("Deleted friend (" + id + ")! They are now dead to you.")

	return redirect('/')

app.run(debug=True)