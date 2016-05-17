#!flask/bin/python
from flask import render_template, session, redirect, request, escape, url_for
from app import app



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user =User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                       form = form, name = session.get('name'),
                       known = session.get('known', False))










@app.route('/home') #[Route decorator] This registers the function as a route
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
