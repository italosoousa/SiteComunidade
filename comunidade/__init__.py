from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Criando um token para previnir ataques 
app.config['SECRET_KEY'] = '2f29ddb0e4ab691fb698426797'
# Onde vai ficar o banco de dados no aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app) # banco de dados
bcrypt = Bcrypt(app) # crypto da senha
login_manager = LoginManager(app) #

from comunidade import routes
from comunidade import models

