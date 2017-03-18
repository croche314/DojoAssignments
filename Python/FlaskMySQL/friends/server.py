from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = 'secret'

@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	print friends
	return render_template('index.html', all_friends=friends)

@app.route('/friends',methods=['GET','POST'])
def create():
	# write query as a string. Notice how we have multiple values
	# we want to insert into our query
	query = "INSERT INTO friends (first_name,last_name,occupation,created_at,updated_at) VALUES (:first_name,:last_name,:occupation,NOW(),NOW())"
	# We'll then create a dictionary of data from the POST data received.
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'occupation': request.form['occupation']
	}
	# Run query, with dictionary values injected into the query
	mysql.query_db(query,data)
	friends = mysql.query_db("SELECT * FROM friends")
	return render_template('index.html', all_friends=friends)

@app.route('/friends/<friend_id>', methods=['GET','POST'])
def show(friend_id):
	# Write query to select specific user by id. At every point where
	# we want to insert data, we write "." an variable name.
	query = "SELECT * FROM friends WHERE id = :specific_id"
	# Then define a dictionary with key that mathes :variable_name in query
	data = {'specific_id': friend_id}
	# Run query with inserted data.
	friends = mysql.query_db(query,data)
	# Friends should be a list with a single object,
	# so we pass the value at [0] to our template under alias one_friend.
	print friends[0]
	return render_template('friend.html', one_friend=friends[0])

@app.route('/update/<friend_id>', methods=['GET','POST'])
def render_update(friend_id):
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id': friend_id}
	friends = mysql.query_db(query,data)
	return render_template('update_friend.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['GET','POST'])
def update(friend_id):
	query = "UPDATE friends SET first_name=:first_name,last_name=:last_name,occupation=:occupation WHERE id=:id"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'occupation': request.form['occupation'],
			'id': friend_id
		}
	mysql.query_db(query,data)
	return redirect('/')

@app.route('/delete/<friend_id>')
def delete(friend_id):
	query = "DELETE FROM friends WHERE id=:id"
	data = {'id': friend_id}
	mysql.query_db(query,data)
	return redirect('/')

app.run(debug=True)

