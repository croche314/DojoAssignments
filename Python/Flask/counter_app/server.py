from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['POST', 'GET'])
def index():
	session['count'] += 1
	return render_template('index.html', count=session['count'],message=session)

@app.route('/plus_two', methods=['POST','GET'])
def plus_two():
	session['count'] +=1
	return redirect('/') 

@app.route('/reset', methods=['POST', 'GET'])
def reset():
	session.clear()
	session['count'] = 0
	return redirect('/')

app.run(debug=True)
