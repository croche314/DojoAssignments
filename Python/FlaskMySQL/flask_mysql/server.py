from flask import Flask
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app,'world')

print mysql.query_db("SELECT * FROM countries")



app.run(debug=True)