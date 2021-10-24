from flask_bcrypt import Bcrypt

bcpt = Bcrypt()

def init_app(app):
    bcpt.init_app(app)
    return app
