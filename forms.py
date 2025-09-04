from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# É preciso deginir o FlaskForm dentro da classe não ter que declarar o __init__
class FormCriarConta(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired])
  email = StringField('E-mail', validators=[DataRequired, Email])
  senha = PasswordField('Senha', validators=[DataRequired, Length(6, 20)])
  cofirmar_senha = PasswordField('Confirmação de senha', validators=[DataRequired, EqualTo])
  botao_subimit = SubmitField('Criar conta')

class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired, Email])
  senha = PasswordField('Senha', validators=[DataRequired, Length(6, 20)])
  botao_login = SubmitField('Criar conta')