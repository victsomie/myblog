#!flask/bin/python
from flask import render_template, session, redirect, request
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
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
            '''
