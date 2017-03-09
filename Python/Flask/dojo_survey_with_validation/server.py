from flask import Flask, render_template, request, redirect, flash, session, url_for
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comments'] = request.form['comments']
	if len(request.form['name']) < 1:
		flash('Type your name in stupid...')
		valid_name = False
	else:
		valid_name = True

	if len(request.form['comments']) > 120:
		flash('Please limit your comments to 120 characters')
		valid_comments = False
	else:
		valid_comments = True

	if valid_name == False or valid_comments == False:
		return redirect('/')
	else: 
		return redirect('/result')


@app.route('/result', methods=['GET','POST'])
def display_results():
	print "successful post"
	name = session['name']
	location = session['location']
	language = session['language']
	if session['comments'] == "":
		comments = "N/A"
	else:
		comments = session['comments']
	
	return render_template('result.html',name=name,location=location,language=language,comments=comments)


app.run(debug=True)