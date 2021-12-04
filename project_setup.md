# Configuração do projeto
#### Após fazer o clone do projeto você precisará realizar algumas configurações na sua maquina antes de rodar o projeto:

O projeto foi desenvolvido utilizando Python 3.8.10, recomendo utilizar a mesma versão,
vc pode instalar o Python [nesse link](https://www.python.org/downloads/).

Outra coisa que preciso ressaltar é que o projeto foi desenvolvido em ambiente linux (Ubuntu 20.04) e vai ser muito mais simples rodar em um ambiente linux.

*Você vai precisar também de um ambiente virtual para evitar conflitos entre versões na tua maquina, utilize o comando a seguir para instalar o **virtualenv** caso ainda não tenha instalado*:
```
pip install virtualenv
```
 #### A maneira mais simples e rápida de rodar o projeto de uma vez é rodar um pequeno script pronto que já vai fazer tudo o que é necessário e colocar o projeto na porta http://127.0.0.1:5000/.

*Dentro do repositório é só rodar o seguinte comando:*
```
. install.sh
```

#### Caso prefira/precise rodar uma coisa de cada vez, primeira coisa a fazer é configurar um **Ambiente Virtual** para evitar possíveis conflitos entre versões:
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
*Você vai precisar de um arquivo para **alocar suas variáveis de ambiente**, use o comando abaixo para criá-lo e exportar as variáveis (Você pode/deve substituir a secret_key por uma de sua escolha, mas para teste não vai fazer diferença):*
```
echo "FLASK_APP=run.py
FLASK_ENV=development
secret_key=aquivoceescreveumachavesupersecreta" > .env
```
*Agora você precisa criar o banco de dados e fazer as migrações:*
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
