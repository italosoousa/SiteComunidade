from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# É preciso deginir o FlaskForm dentro da classe não ter que declarar o __init__
class FormCriarConta(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmar_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarconta = SubmitField('Criar conta')

class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  lembrar_dados = BooleanField('Lembrar dados de acesso')
  botao_submit_login = SubmitField('Criar conta')