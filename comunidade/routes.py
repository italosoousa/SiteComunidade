from flask import render_template, request, flash, redirect, url_for
from comunidade import app, database, bcrypt
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario
from flask_login import login_user, logout_user, current_user

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
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login realizado com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            # Redirecionando para a página inicial
            return redirect(url_for('home'))
        else:
            flash('Falha no login. E-mail ou Senha Incorretos', 'alert-danger')


    # Valida se o usuário criou a conta     # Valida se estamos clicando no botão certo
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        # Exibindo mensagem de bem sucedido         # Pegando o e-mail do usuário
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        # Redirecionando para a página inicial
        return redirect(url_for('home'))
    return render_template('login.html', form_criarconta=form_criarconta, form_login= form_login)

@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout Feito com Sucesso', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/post/criar')
def criar_post():
    return render_template('criarpost.html')