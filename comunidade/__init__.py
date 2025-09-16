from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

# Criando um token para previnir ataques 
app.config['SECRET_KEY'] = '2f29ddb0e4ab691fb698426797'

# Criando o banco de dados, para que ele também use a versão local
if os.getenv('DATABASE_URL'):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app) # banco de dados
bcrypt = Bcrypt(app) # crypto da senha
login_manager = LoginManager(app) # faz as validações dos logins
login_manager.login_view = 'login' 
login_manager.login_message_category = 'alert-info'

from comunidade import routes
from comunidade import models

