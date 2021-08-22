from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# O MigrateComand só esta funcionando até a versão 'Flask-Migrate==2.6.0'

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

bcpt = Bcrypt(app)

from app.models import tables, forms
from app.controllers import login, home
