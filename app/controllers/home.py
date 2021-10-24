from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import redirect, url_for, flash, Blueprint
from flask_login.utils import login_required, current_user
from app.models.tables import db

bp = Blueprint('bp_home', __name__)

from app.models.tables import User, Tasks
from app.models.forms import AddTaskForm

@bp.route('/home')
@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/terms')
def terms():
    return render_template('terms.html')

@bp.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    # Parte que le as task do db:
    user_task_all = Tasks.query.filter_by(user_id=current_user.id).order_by(Tasks.id.desc()).all()

    # Parte que adicona tasks no db:
    formulario = AddTaskForm()
    user_task = Tasks.query.filter_by(task=formulario.task.data).first()
    if user_task:
        flash('This Task already exist!')
    if formulario.validate_on_submit():
        ct = Tasks(formulario.task.data, current_user.id)
        db.session.add(ct)
        db.session.commit()
        flash('Add!')
        return redirect(url_for('bp_home.profile'))
    return render_template(
        'profile.html',
        form=formulario,
        task_message=user_task_all
        )

@bp.route('/deletetask/<task_id>', methods=['GET', 'DELETE'])
@login_required
def delete_task(task_id):
    task = Tasks.query.filter_by(id=task_id).first()
    if not task:
        return 'error'

    task.task = "visconde"

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!')
    return redirect(url_for('bp_home.profile'))
