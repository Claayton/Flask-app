from flask.templating import render_template
from flask import redirect, url_for, flash, request
from flask_login.utils import login_required
from app import app, db, lm

from app.models.tables import User


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/online', methods=['POST', 'GET'])
@login_required
def online():
    if request.method == 'GET':
        return redirect(url_for('logout'))
    return render_template('online.html')