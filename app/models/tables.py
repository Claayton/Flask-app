from logging import NullHandler
from flask_login import UserMixin
from flask.scaffold import F
from app import db, lm

@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        
    def __repr__(self):
        return f'<User {self.username}>'


class ToDo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, task, user_id):
        self.content = task
        self.user_id = user_id

    def __repr__(self):
        return f'<Task {self.id}>'


class Friend(db.Model):
    __tablename__ = 'friend'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)
    friend = db.relationship('User', foreign_keys=friend_id)
