import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    'name_db': os.getenv('DATABASE'),
    'username': os.getenv('MYSQL_USERNAME'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'server': os.getenv('MYSQL_SERVER'),
    'secret_key': os.getenv('SECRET_KEY')
}
