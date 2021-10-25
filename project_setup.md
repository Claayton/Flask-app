# Configuração do projeto
## Apos fazer o clone do projeto você precisará realizar algumas configurações na sua maquina antes de rodar o projeto:

*A primeira coisa a fazer é configurar um **Ambiente Virtual** para evitar possíveis conflitos entre versões:*
```
python3 -m venv venv 
```
*Em seguida você deverá **Ativar** esse ambiente:*
```
source venv/bin/activate 
```
*Agora instale as **bibliotecas e pacotes** necessários para rodar o projeto:*
```
pip install -r requirements.txt
```
*Você vai precisar de um arquivo para **alocar suas variáveis de ambiente**, use o comando abaixo para criá-lo:*
```
touch .env
```
*Dentro do arquivo .env criado acima vc deve escrever as seguintes variáveis:*
```
FLASK_APP=run.py
FLASK_ENV=development
secret_key=aquivoceescreveumachavesupersecreta
```
*Agora você precisa criar o banco de dados e fazer as migrações:
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```
*O projeto ja está configurado e pronto para ser testado em modo de desenvolvedor:*
```
flask run
```
