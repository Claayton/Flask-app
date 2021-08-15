from flask.templating import render_template
from flask_login import login_user
from flask import redirect, url_for, flash
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm


@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
                            
@app.route('/login/', methods=['GET', 'POST'])
@lm.user_loader
def login(nothing):
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in!')
    else:
        flash('Invalid Login!')
    return render_template('login.html',
                            form=form)

"""
# CREATE
@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    i = User('Clayton Garcia da Silva', 'claaytongarcia@gmail.com', 'claaytong', '123456')
    db.session.add(i)
    db.session.commit()
    return 'ok'"""

"""
READ
@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    r = User.query.filter_by(password='123456').first()
    print(r)
    print(r.username)
    print(r.name)
    print(r.password)
    print(r.email)
    print(r.id)
    return 'ok'"""

"""
UPDATE
@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    r = User.query.filter_by(password='123456').first()
    r.name = 'Julia R.'
    db.session.add(r)
    db.session.commit()
    return 'ok'"""
"""
DELETE
@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    r = User.query.filter_by(password='123456').first()
    r.name = 'Julia R.'
    db.session.delete(r)
    db.session.commit()
    return 'ok'"""

@app.route('/register')
def register():
    return render_template('register.html')

