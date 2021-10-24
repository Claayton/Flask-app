from flask_migrate import Migrate
from app.models.tables import db

def init_app(app):
    migrate = Migrate(app, db)
    return app
