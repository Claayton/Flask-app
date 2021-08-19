from flask.templating import render_template
from flask_login import login_user, logout_user, login_required
from flask import redirect, url_for, flash, request
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm


@lm.user_loader
def load_user(user):
    return User.query.get(user)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            print('\033[32mLogado!\033[m')
            return redirect(url_for('online'))
        else:
            print('\033[31mInvalid Login!\033[m')
            flash('Invalid Login!')
    return render_template('login.html',
                            form=form)

@app.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    print('voce foi desconectado burro')
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
