from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired()])
    password = PasswordField('password' , validators=[DataRequired()])
    remember_me = BooleanField('remember-me')

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('lastname')
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm = PasswordField('password', validators=[DataRequired()])
    terms = BooleanField('terms')