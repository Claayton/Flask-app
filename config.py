DEBUG = True

import env

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/mitmirror".format(env.mysql_username, env.mysql_password, env.mysql_server)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = env.secret_key
