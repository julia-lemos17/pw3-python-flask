# Comentário no Python
# Importando o Flask para a aplicação
from flask import Flask,render_template
# Carregando o Flask na variável "app "
# Declarando  variável no python
app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente python (Já existem)
# __name__ representa o nome da aplicação

# Criando a rota principal do site
@app.route('/')
# def cria funções no python
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/consoles')
def consoles():
    return render_template('console.html')

# Iniciando o servidor na porta 5000
if __name__ =='__main__':
    # O if está verificando se o arquivo gravado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# O método .run() inicia o servidor