from flask.templating import render_template
from flask import redirect, url_for, flash
from flask_login.utils import login_required, current_user

from app import app, db

from app.models.tables import User, Tasks
from app.models.forms import AddTaskForm

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

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = AddTaskForm()
    user_task = Tasks.query.filter_by(task=form.task.data).first()
    if user_task:
        flash('This Task already exist!')
    else:
        if form.validate_on_submit():
            t = Tasks('id', current_user.id)
            db.session.add(t)
            db.session.commit()
            flash('Add!')
            return redirect(url_for('profile'))
    return render_template('profile.html',
                            form=form)
