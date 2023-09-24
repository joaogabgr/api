from app import db

class Usuarios(db.Model):
    email = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_email = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=True)
    transplante = db.Column(db.Date, nullable=True)
    nascimento = db.Column(db.Date, nullable=False)
    nome_filho = db.Column(db.String(255), nullable=False)
    comentario = db.Column(db.String(550), nullable=False)
