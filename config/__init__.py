from config.database import database_infos as db

JSONIFY_PRETTYPRINT_REGULAR = True

CORS_HEADERS = 'Content-Type'

SECRET_KEY = db['secret_key']
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/{}".format(
                                                                db['username'],
                                                                db['password'],
                                                                db['server'],
                                                                db['name_db'])
