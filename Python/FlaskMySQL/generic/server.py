from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	pass

app.run(debug=True)

