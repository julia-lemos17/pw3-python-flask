from flask import render_template, request, redirect, url_for


def init_app(app):
    listaMusicas = [{"musica": "Die With a Smile",
         "cantor": "Lady Gaga & Bruno Mars", "genero": "Pop / Soul", "ano": 2024}]
    listaForm = ['Die with Smile', 'Lembrança boa',
                     'Numb', 'Shake it off', 'Passando pela prova']
    @app.route('/')
    # def cria funções no Python
    def home():
        return render_template('index.html')
    
    @app.route('/musicas')
    def musicas():
        # Criando variáveis para a rota de games
        musica = "Chuva de arroz"
        ano = 2015
        genero = "Sertanejo"
        # Lista de jogadores (uma lista é um vetor/array)
        cantores = ['Luan Santana', 'Bruno Mars', 'Cassiane', 'Linkin Park', 'Ferrugem']
        # Enviando as variáveis para o HTML
        return render_template('musicas.html',
                               musica=musica,
                               cantores=cantores,
                               genero=genero,
                               ano=ano
                               )
        
    @app.route('/formulario', methods=['GET', 'POST'])
    def formulario():
          # Criando um objeto
        musica = {"Nome": "Die with Smile",
                   "Cantor": "Bruno Mars e Lady Gaga",
                   "Ano": 2024}

        # Recebendo o valor do formulário
        if request.method == 'POST':
            if request.form.get('novaMusica'):
                listaForm.append(request.form.get('novaMusica'))
        return render_template('formulario.html', musica=musica, listaForm=listaForm)
    
    @app.route('/cadmusicas', methods=['GET','POST'])
    def cadmusicas():
        
        # Recebendo os dados do formulário e enviando para a página
        if request.method == 'POST':
            #Aqui ele irá gravar os dados na lista de jogos
            listaMusicas.append({'musica': request.form.get('musica'),'cantor': request.form.get('cantor'),'genero': request.form.get('genero'),'ano':request.form.get('ano')})
        #Aqui o usuário será redirecionado para página
            return redirect(url_for('cadmusicas'))
        return render_template('cadmusicas.html',listaMusicas = listaMusicas)
    
    
    
    
    
    
    
    
    