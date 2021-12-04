python3 -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt;
echo "FLASK_APP=run.py
FLASK_ENV=development
secret_key=aquivoceescreveumachavesupersecreta" > .env;
flask db init;
flask db migrate;
flask db upgrade;
flask run;
