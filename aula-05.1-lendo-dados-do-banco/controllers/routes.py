# Importando o Flask para a aplicação
from flask import render_template, request,redirect,url_for
#importando o model de Games
from models.database import Game

# Criando a função principal para inicializar as rotas


def init_app(app):
    # Variaveis globais
    listaConsoles = ['Playstation 5', 'Xbox One',
                     'Super Nintendo', 'Atari', '3DS']
    
    listaGames = [{"titulo": "CS-GO","ano": 2012, "categaria": "FPS online", "plataforma": "PC (Windows)"}]

    @app.route('/')
    # def cria funções no Python
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # Criando variáveis para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        # Lista de jogadores (uma lista é um vetor/array)
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
        # Enviando as variáveis para o HTML
        return render_template('games.html',
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # Criando um objeto
        console = {"Nome": "Playstation 2",
                   "Fabricante": "Sony",
                   "Ano": 2000}

        # Recebendo o valor do formulário
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
        return render_template('consoles.html',
                               console=console,
                               listaConsoles=listaConsoles)

    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        
        # Recebendo os dados do formulário e enviando para a página
        if request.method == 'POST':
            #Aqui ele irá gravar os dados na lista de jogos
            listaGames.append({'titulo': request.form.get('titulo'),'ano': request.form.get('ano'),'categoria': request.form.get('categoria'),'plataforma':request.form.get('plataforma')})
        #Aqui o usuário será redirecionado para página
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',listaGames = listaGames)
    
    #Rota para o crud(estoque de jogos)
    @app.route('/estoque', methods=['GET','POST'])
    def estoque():
        #Selecionando todos os jogos da tabela
        games = Game.query.all()
        return render_template('estoque.html',games=games)