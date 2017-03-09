from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def process_form():
	print "successful post"
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	if request.form['comments'] == "":
		comments = "N/A"
	else:
		comments = request.form['comments']
	
	return render_template('result.html',name=name,location=location,language=language,comments=comments)





app.run(debug=True)