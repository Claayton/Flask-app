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
    # Parte que le as task do db:
    user_task_all = Tasks.query.filter_by(user_id=current_user.id).all()

    # Parte que adicona tasks no db:
    form = AddTaskForm()
    user_task = Tasks.query.filter_by(task=form.task.data).first()
    if user_task:
        flash('This Task already exist!')
    if form.validate_on_submit():
        ct = Tasks(form.task.data, current_user.id)
        db.session.add(ct)
        db.session.commit()
        flash('Add!')
    return render_template('profile.html',
                            form=form, task_message=user_task_all)
