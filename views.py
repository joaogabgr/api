from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from models import Usuarios, Posts, Comentarios


def verificarPeril():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['usuario_logado']).first()


# RODAR PAGINAS HTML

@app.route('/')
def index():
    return render_template('index.html', perfil=verificarPeril())

@app.route('/ircBrasil')
def ircBrasil():
    return render_template('ircBrasil.html', perfil=verificarPeril())

@app.route('/faq')
def faq():
    with open("static/docs/askFaq.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()

    askFaq = []

    for i in range(0, len(texto), 2):
        askFaq.append([texto[i - 1], texto[i]])

    return render_template('faq.html', askFaq=askFaq, perfil=verificarPeril())


@app.route('/comunidade')
def comunidade():
    lista = Posts.query.order_by(Posts.id.desc())
    return render_template('comunidade.html', posts=lista, perfil=verificarPeril())


@app.route('/proadi')
def proadi():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('proadi')))
    else:
        return render_template('proadi.html', perfil=verificarPeril())

@app.route('/admin')
def admin():
    return render_template('admin.html', perfil=verificarPeril())

@app.route('/administrar', methods=['POST',])
def administrar():
    usuario = Usuarios.query.filter_by(email=request.form['email']).first()
    if usuario:
        if usuario.admin == True:
            flash('O usuário já é um administrador.')
            return render_template('admin.html', perfil=verificarPeril())
        usuario.admin = True
        db.session.commit()
        flash('O usuário foi promovido a administrador com sucesso!')
        return render_template('admin.html', perfil=verificarPeril())
    else:
        flash('O email inserido não está associado a uma conta. Por favor, verifique o email.')
        return render_template('admin.html', perfil=verificarPeril())

# SISTEMA DE LOGIN

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
            return render_template(f'{proxima_pagina}.html'.format(), perfil=verificarPeril())
        else:
            flash('A senha inserida esta incorreta. Por favor, tente novamente.')
            return redirect(url_for('login'))
    else:
        flash('O email inserido não está associado a uma conta. Por favor, verifique o email ou crie uma nova conta.')
        return redirect(url_for('registrar'))


@app.route('/registrar')
def registrar():
    return render_template('registrar.html', perfil=verificarPeril())

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    email = request.form['email']
    nome = request.form['nome']
    senha = request.form['password']
    admin = False

    if Usuarios.query.filter_by(email=email).first():
        flash('O email inserido já está associado a uma conta existente. Por favor, faça login.')
        return redirect(url_for('login', perfil=verificarPeril()))
    
    novo_user = Usuarios(email=email, nome=nome, senha=senha, admin=admin)
    db.session.add(novo_user)
    db.session.commit()

    session['usuario_logado'] = email
    return redirect(url_for('index', perfil=verificarPeril()))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))


# FAZER POST E COMENTARIO

@app.route('/postar', methods=['POST', ])
def postar():
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

@app.route('/processar', methods=['POST', 'GET'])
def processar():
    id = request.args.get('q')  
    return redirect(url_for('comentario', q=id))

@app.route('/comentario', methods=['POST', 'GET'])
def comentario():
    id = request.args.get('q')  
    post = Posts.query.filter_by(id=id).first()

    comentarios = Comentarios.query.filter_by(fk_id=id).all()
    comentarios.reverse()

    return render_template('comentario.html',id=id, post=post, perfil=verificarPeril(), comentarios=comentarios)

@app.route('/comentar', methods=['POST',])
def comentar():
    fk_id = request.form['id']
    fk_email = session['usuario_logado']
    comentario = request.form['boxcomentar']

    usuario = Usuarios.query.filter_by(email=fk_email).first()
    nome = usuario.nome
    
    novo_comentario = Comentarios(fk_email=fk_email,fk_id=fk_id, nome=nome, comentario=comentario)

    db.session.add(novo_comentario)
    db.session.commit()
    
    return redirect(url_for('comentario', q=fk_id))



# DELETAR POST/ COMENTARIO

@app.route('/deletarpost', methods=['POST', 'GET'])
def deletarpost():
    id = request.args.get('q')
    post = Posts.query.filter_by(id=id).first()
    comentario = Comentarios.query.filter_by(fk_id=id).all()
    for i in comentario:
        db.session.delete(i)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('comunidade', perfil=verificarPeril()))


@app.route('/editarpost', methods=['POST', 'GET'])
def editarpost():
    id = request.form['id']
    post = Posts.query.filter_by(id=id).first()
    post.comentario = request.form['comentario']
    post.nascimento = request.form['nascimento']
    post.nome_filho = request.form['nome']
    if request.form['transplante'] != "":
        post.transplante = request.form['transplante']
    else:
        post.transplante = None
    db.session.commit()
    return redirect(url_for('comentario', q=id))

@app.route('/deletarcomentario', methods=['POST',])
def deletarcomentario(): 
    id = request.form['comentario.id']
    fk_id = request.form['id']
    comentario = Comentarios.query.filter_by(id=id).first()
    db.session.delete(comentario)
    db.session.commit()
    return redirect(url_for('comentario', q=fk_id))

@app.route('/editarcomentario', methods=['POST', 'GET'])
def editarcomentario():
    id = request.form['comentario.id']
    fk_id = request.form['id']
    comentario = Comentarios.query.filter_by(id=id).first()
    comentario.comentario = request.form['comentario']
    db.session.commit()
    return redirect(url_for('comentario', q=fk_id))