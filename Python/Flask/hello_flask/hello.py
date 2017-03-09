from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html', name="Chris")

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/success2')
def success2():
	return render_template('success2.html')



app.run(debug=True)