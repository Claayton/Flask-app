import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('secret_key')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/mitmirror".format(
    os.getenv('mysql_username'),
    os.getenv('mysql_password'),
    os.getenv('mysql_server'))

email_mitmirrortests = os.getenv('email_mitmirrortests')
password_mitmirrortests = os.getenv('password_mitmirrortests')
