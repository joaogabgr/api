from app import db

class Usuarios(db.Model):
    email = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_email = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=True)
    transplante = db.Column(db.Date, nullable=True)
    nascimento = db.Column(db.Date, nullable=False)
    nome_filho = db.Column(db.String(255), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    denuncia = db.Column(db.Boolean, default=False)

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_email = db.Column(db.String(255), nullable=False)
    fk_id = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=True)
    comentario = db.Column(db.Text, nullable=False)
    denuncia = db.Column(db.Boolean, default=False)
