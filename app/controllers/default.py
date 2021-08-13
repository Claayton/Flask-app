from flask.templating import render_template
from flask import redirect, url_for
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm


@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
                            
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    return 'ok'

@app.route('/register')
def register():
    return render_template('register.html')