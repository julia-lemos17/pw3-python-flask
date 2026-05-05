#importando o flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# carregando o SQLAlchemy em uma variável
db = SQLAlchemy()

# Criando uma classe para representar a entidade games no banco
class Game(db.Model):
    #Definindo os atributos (colunas) da tabela
    #Schema
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    # Inicializando as variáveis na classe
    def __init__(self,titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade