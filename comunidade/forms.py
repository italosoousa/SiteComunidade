from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade.models import Usuario

# É preciso deginir o FlaskForm dentro da classe não ter que declarar o __init__
class FormCriarConta(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmar_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarconta = SubmitField('Criar conta')

  def validate_email(self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
          raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça um login para continuar')

  def validate_username(self, username):
      usuario = Usuario.query.filter_by(email=username.data).first()
      if usuario:
          raise ValidationError('Usuário já cadastrado. Cadastre-se com outro usuário ou faça um login para continuar')

class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  lembrar_dados = BooleanField('Lembrar dados de acesso')
  botao_submit_login = SubmitField('Criar conta')