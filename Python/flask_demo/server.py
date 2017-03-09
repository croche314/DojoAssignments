from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    print "the index function has been called"
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def auth():
    server_email = request.form['html_email']
    server_password = request.form['html_password']
    if server_email == "user@gmail.com" and server_password == "123":
        return redirect('/costa_rica')
    else:
        return redirect('/guantanamo')

@app.route('/costa_rica')
def destination1():
    return render_template('tamarindo.html')


@app.route('/puerto_rico')
def destination2():
    return render_template('puerto_rico.html')

@app.route('/guantanamo')
def destination3():
    return render_template('guantanamo.html')

app.run(debug=True)
