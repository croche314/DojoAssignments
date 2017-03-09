from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/ninja')
def index():
	return render_template('index.html', img_file='tmnt.png')

@app.route('/ninja/<username>')
def show_user_profile(username):
	if username == 'blue':
		img_file = 'leonardo.jpg'
		turtle = 'Leonardo'
	elif username == 'orange':
		img_file = 'michelangelo.jpg'
		turtle = 'Michaelangelo'
	elif username == 'red':
		img_file = 'raphael.jpg'
		turtle = 'Raphael'
	elif username == 'purple':
		img_file = 'donatello.jpg'
		turtle = 'Donatello'
	else:
		img_file = 'notapril.jpg'
		turtle = "April :-("

	return render_template('ninja.html', img_file=img_file, turtle=turtle)




app.run(debug=True)