from sqlalchemy.testing.pickleable import User

from comunidade import database, login_manager
from datetime import datetime
from flask_login import UserMixin

# mostrando para o login maneger que essa é a função do usuário
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


# Tabela usuraios que herda de databasse.Model
class Usuario(database.Model, UserMixin):
  id = database.Column(database.Integer, primary_key=True)
  username = database.Column(database.String, nullable=False) # nullable == not null
  email = database.Column(database.String, nullable=False, unique=True) # unique, permite que tenha somente um e-mail
  senha = database.Column(database.String, nullable=False)
  foto_perfil = database.Column(database.String, default='default.jpg')


class Post(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  titulo = database.Column(database.String, nullable=False)
  corpo = database.Column(database.Text, nullable=False) # String para texto pequenos e Text para textos grandes
  data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow) # Coloca o horário em que foi criado
    