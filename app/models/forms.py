from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password' , validators=[InputRequired()])
    remember_me = BooleanField('remember-me')

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    lastname = StringField('lastname')
    email = EmailField('email', validators=[InputRequired()])
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    confirm = PasswordField('password', validators=[InputRequired()])
    terms = BooleanField('terms', validators=[InputRequired()])