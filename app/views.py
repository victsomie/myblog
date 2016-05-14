#!flask/bin/python
from flask import render_template
from app import app

@app.route('/') #[Route decorator] This registers the function as a route
@app.route('/home') #[Route decorator] This registers the function as a route
def home():
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('home.html', user=user)
