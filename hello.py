#!usr/bin/python
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/') #[Route decorator] This registers the function as a route
def index():
    return '<h1>Hello World!</h1>'
@app.route('/about')
def about():
    return '<h1>This is about</h1>'

@app.route('/jaribu')
def jaribu():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name



if __name__ == '__main__':
    app.run()
