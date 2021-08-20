from flask.templating import render_template
from flask_login import login_user, logout_user, login_required
from flask import redirect, url_for, flash
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('Invalid Username!')
        else:
            if user and user.password == form.password.data:
                if form.remember_me.data:
                    login_user(user, remember=True)
                else:
                    login_user(user)
                return redirect(url_for('online'))
            else:
                flash('Invalid Password!')
    return render_template('login.html',
                            form=form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        i = User(f'{form.name.data} {form.lastname.data}', form.email.data, form.username.data, form.password.data)
        db.session.add(i)
        db.session.commit()
        flash('Registered!')
    return render_template('register.html', 
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
