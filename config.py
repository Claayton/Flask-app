DEBUG = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/testdb".format('root', '36214930_Cg', 'localhost')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'um-nome-bem-seguro'
