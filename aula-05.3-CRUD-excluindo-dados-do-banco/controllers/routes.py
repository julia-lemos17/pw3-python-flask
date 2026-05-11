# Importando o Flask para a aplicação
from flask import render_template, request,redirect,url_for
#importando o model de Games
from models.database import Game,db,Console

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
    #Adicionando o parametro id a rota
    @app.route('/estoque/delete<int:id>')
    def estoque(id=None):
        #Verificando se o ID foi passado pra rota
        if id:
            game=Game.query.get(id) #Seleciona o jogo
            db.session.delete(game) #Deleta o jogo
            db.session.commit() #Confirma a exclusão
            return redirect(url_for('estoque')) #Redireciona para a página de estoque
        
        #Condição para verificar se o usuário está enviando uma requisição do tipo POST(cadastro)
        if request.method == 'POST':
            #Realiza o cadastro
            #Coletando os dados do formulário
            dados = request.form.to_dict()
            #Enviando os dados para o model
            newgame = Game(
                dados['titulo'],
                dados['ano'],
                dados['categoria'],
                dados['plataforma'],
                dados['preco'],
                dados['quantidade']
            )
            #Método do SQLAlchemy para adicionar o novo jogo ao banco de dados
            db.session.add(newgame)
            #Confirmação
            db.session.commit()
            return redirect(url_for('estoque'))
        #Selecionando todos os jogos da tabela
        games = Game.query.all()
        return render_template('estoque.html',games=games)
    
    @app.route('/estoque/editar', methods=['GET','POST'])
    def editar():
        return render_template('editGame.html')
    
    @app.route('/estoque_console', methods=['GET','POST'])
    def estoque_console():
        #Condição para verificar se o usuário está enviando uma requisição do tipo POST(cadastro)
        if request.method == 'POST':
            #Realiza o cadastro
            #Coletando os dados do formulário
            dado = request.form.to_dict()
            #Enviando os dados para o model
            newconsole = Console(
                dado['nome'],
                dado['ano'],
                dado['fabricante'],
                dado['preco']
            )
            #Método do SQLAlchemy para adicionar o novo console ao banco de dados
            db.session.add(newconsole)
            #Confirmação
            db.session.commit()
            return redirect(url_for('estoque_console'))
        #Selecionando todos os jogos da tabela
        consoles = Console.query.all()
        return render_template('estoque_console.html',consoles=consoles)