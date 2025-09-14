from comunidade import database, app
from comunidade.models import Usuario

with app.app_context():
  usuario = Usuario.query.first()
  print(usuario.email)

