from flask import redirect, url_for
from flask_login import UserMixin, login_required
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy

from app.ext.security import bcpt
from app.ext.auth import lm

from datetime import datetime
import env

db = SQLAlchemy()
    
@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    secondary_id = db.Column(db.Integer, nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False)
    is_active_user = db.Column(db.Boolean, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)


    def __init__(self, name, email, username, password_hash, date_joined):

        self.name = name
        self.email = email
        self.username = username
        self.password_hash = password_hash

        self.secondary_id = 0 # Configurar furturamente
        self.is_staff = False
        self.is_active_user = False # Configurar futuramente
        self.last_login = self.login_time() # Configurar futuramente
        self.date_joined = date_joined

        
    def __repr__(self):
        return f'<User {self.username}>'

    def find(self, find_username):
        return self.query.filter_by(username=find_username).first()

    def hash_password(self, password):
        self.password_hash = bcpt.generate_password_hash (password). decode ('utf-8')

    def verify_password(self, password):
        return bcpt.check_password_hash(self.password_hash, password)

    def create_secundary_id(self): # Configurar futuramente
        return self.id * self.id

    def login_time(self): # Configurar futuramente
        return datetime.today()
    
    def set_unable_password(self): # Configurar futuramente
        self.password_hash = 'None'

    def has_usable_password(self):
        if not self.password_hash == 'None':
            return True
        else:
            return False

    def set_password(self, new_password):
        self.hash_password = self.hash_password(new_password)

    def send_email(self, msg_subject, msg_message):
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import smtplib

        msg = MIMEMultipart()
        message = msg_message

        password = env.password_mitmirrortests
        msg['From'] = env.email_mitmirrortests
        msg['To'] = self.email
        msg['Subject'] = msg_subject

        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

    @login_required
    def get_profile(self):
        return redirect(url_for('bp_home.profile'))

    

class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, task, user_id):
        self.task = task
        self.user_id = user_id

    def __repr__(self):
        return f'<Task {self.id}>'


class Friend(db.Model):
    __tablename__ = 'friend'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

def init_app(app):
    db.init_app(app)
    return app
