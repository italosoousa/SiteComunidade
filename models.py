from main import database
from datetime import datetime

# Tabela usuraios que herda de databasse.Model
class Ususario(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  username = database.Column(database.String, nullable=False) # nullable == not null
  email = database.Column(database.String, nullable=False, unique=True) # unique, permite que tenha somente um e-mail
  senha = database.Column(database.String, nullable=False)
  foto_perfil = database.Column(database.String, default='default.jpg')


class Post(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  titulo = database.Column(database.String, nullable=False)
  corpo = database.Column(database.Text, nullable=False) # String para texto pequenos e Text para textos grandes
  data_criacao = database.Column(database.DateTime, nullabel=False, default=datetime.utcnow) # Coloca o horário em que foi criado
    