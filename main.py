from flask import Flask, render_template

app = Flask(__name__)

# Criando um token para previnir ataques 
app.config('SECRET_KEY') = '2f29ddb0e4ab691fb698426797d484cc'

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
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)