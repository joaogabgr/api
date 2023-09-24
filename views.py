from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from models import Usuarios, Posts


def verificarPeril():
    perfil = Usuarios.query.filter_by(email=session['usuario_logado']).first()
    return perfil

@app.route('/')
def index():
    return render_template('index.html', perfil=verificarPeril())

@app.route('/ircBrasil')
def ircBrasil():
    return render_template('ircBrasil.html', perfil=verificarPeril())

@app.route('/faq')
def faq():
    with open("docs/askFaq.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()

    askFaq = []

    for i in range(0, len(texto), 2):
        askFaq.append([texto[i - 1], texto[i]])

    return render_template('faq.html', askFaq=askFaq, perfil=verificarPeril())


@app.route('/comunidade')
def comunidade():
    lista = Posts.query.order_by(Posts.id.desc())
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('comunidade.html', posts=lista)
    else:
        return render_template('blog.html', posts=lista, perfil=verificarPeril())


@app.route('/proadi')
def proadi():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('proadi')))
    else:
        return render_template('proadi.html', perfil=verificarPeril())

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(email=request.form['email']).first()
    if usuario:
        if request.form['email'] == usuario.email and request.form['password'] == usuario.senha:
            session['usuario_logado'] = usuario.email
            if request.form['proxima'] == 'None':
                return render_template('index.html', perfil=verificarPeril())
            else:
                proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina, perfil=verificarPeril())
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/registrar')
def registrar():
    return render_template('registrar.html', perfil=verificarPeril())

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    email = request.form['email']
    nome = request.form['nome']
    senha = request.form['password']

    if Usuarios.query.filter_by(email=email).first():
        return redirect(url_for('login', perfil=verificarPeril()))
    
    novo_user = Usuarios(email=email, nome=nome, senha=senha)
    db.session.add(novo_user)
    db.session.commit()

    return redirect(url_for('index', perfil=verificarPeril()))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))


@app.route('/comentar', methods=['POST', ])
def comentar():
    fk_email = session['usuario_logado']
    nascimento = request.form['nascimento']
    nome_filho = request.form['nome']
    comentario = request.form['comentario']

    usuario = Usuarios.query.filter_by(email=fk_email).first()
    nome = usuario.nome
    
    if request.form['transplante'] == "":
        novo_post = Posts(fk_email=fk_email, nome=nome, nascimento=nascimento, nome_filho=nome_filho, comentario=comentario)
    else:
        transplante = request.form['transplante']
        novo_post = Posts(fk_email=fk_email, nome=nome, transplante=transplante, nascimento=nascimento, nome_filho=nome_filho, comentario=comentario)

    db.session.add(novo_post)
    db.session.commit()


    return redirect(url_for('comunidade', perfil=verificarPeril()))
