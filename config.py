import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('secret_key')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.sqlite3'

email_mitmirrortests = os.getenv('email_mitmirrortests')
password_mitmirrortests = os.getenv('password_mitmirrortests')
