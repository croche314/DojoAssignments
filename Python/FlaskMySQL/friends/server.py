from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySqlConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template('index.html')

app.route('/friends',methods=['POST'])
def create():
	# add a friends to the database
	return redirect('/')

app.run(debug=True)

