from app import app


@app.route('/index')
@app.route('/')
def index():
    return 'Hello World!!'



@app.route('/test/', methods=['GET'])
def teste():
    return f'Olá, Marilene!!'
