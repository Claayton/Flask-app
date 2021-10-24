from flask import Flask
from app.models import tables, forms
from app.ext import migrations
from app.ext import auth
from app.ext import security
from app.controllers import home
from app.controllers import login

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    tables.init_app(app)
    migrations.init_app(app)
    auth.init_app(app)
    security.init_app(app)

    app.register_blueprint(home.bp)
    app.register_blueprint(login.bp)
    return app
