from flask.templating import render_template
from flask_login import login_user, logout_user
from flask import redirect, url_for, flash, request
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm


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

@app.route('/online', methods=['GET', 'POST'])
def online():
    if request.method == 'POST':
        print('disconect!')
        return redirect(url_for('logout'))
    return render_template('online.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # funciona mas não esta certo
    if User.is_authenticated:
        return redirect(url_for('online'))
    elif form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            # funciona mas não esta certo
            User.is_authenticated = True
        else:
            flash('Invalid Login!')
        # funciona mas não esta certo
        if User.is_authenticated:
            return redirect(url_for('online'))
    return render_template('login.html',
                            form=form)


# Não tenho certeza se este é o lugar dessa função, (não entendi muito bem oq ela faz)mas funcionou.
@lm.user_loader
def load_user(user_id):
    # funciona mas não esta certo
    return User.query.get(user_id)

@app.route('/logout/')
def logout():
    logout_user()
    User.is_authenticated = False
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
