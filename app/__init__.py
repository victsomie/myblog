from flask import Flask
app = Flask(__name__)

@app.route('/') #[Route decorator] This registers the function as a route
def index():
    return '<h1>Hello World!</h1>'
@app.route('/about')
def about():
    return '<h1>This is about</h1>'
@app.route('/last')
def last():
    return '<h1>Finally last page</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


#The following enables debugging either by setting that flag on the application
if __name__ == '__main__':
    app.run(debug=True)
    """
    Or passing that as a parameter
    """

