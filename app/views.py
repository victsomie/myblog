#!flask/bin/python
from flask import render_template, session, redirect, request, escape, url_for
from app import app

@app.route('/') #[Route decorator] This registers the function as a route
@app.route('/home') #[Route decorator] This registers the function as a route
def home():
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('home.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
            '''
@app.route('/log')
def log():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
