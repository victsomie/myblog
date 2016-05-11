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



if __name__ == '__main__':
    app.run(debug=True)
