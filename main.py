from flask import Flask, render_template
from forms import FormCriarConta, FormLogin
# Importando as classe criadas com o forms

app = Flask(__name__)

# Criando um token para previnir ataques 
app.config['SECRET_KEY'] = '2f29ddb0e4ab691fb698426797d484cc'

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
    return render_template('login.html', form_criarconta=form_criarconta, form_login= form_login)

if __name__ == "__main__":
    app.run(debug=True)