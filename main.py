from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Criando um token para previnir ataques 
app.config['SECRET_KEY'] = '2f29ddb0e4ab691fb698426797'
# Onde vai ficar o banco de dados no aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://comunidade.db'

database = SQLAlchemy(app)

# Rota da página inicial
@app.route("/") # Esse é o caminho da página na qual eu quero alterar
def home():
    return render_template('home.html')

# Rota para a página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota para a página de usuários
@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['Italo', 'Bruna', 'Carlos', 'Ana']
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Colocando as classes dentro de variáveis para colocar no html
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    # Valida de o usuário fez o login       # Valida se estamos clicando no botão certo
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
         # Exibindo mensagem de bem sucedido           # Pegando o e-mail do usuário
        flash(f'Login realizado com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        # Redirecionando para a página inicial
        return redirect(url_for('home'))
    # Valida se o usuário criou a conta     # Valida se estamos clicando no botão certo
    if form_criarconta.validate_on_submit() and 'botao_submit_login' in request.form:
        # Exibindo mensagem de bem sucedido         # Pegando o e-mail do usuário
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        # Redirecionando para a página inicial
        return redirect(url_for('home'))
    return render_template('login.html', form_criarconta=form_criarconta, form_login= form_login)

if __name__ == "__main__":
    app.run(debug=True)