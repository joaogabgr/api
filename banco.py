import mysql.connector
from mysql.connector import errorcode

print("Conectando...")

try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2412'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `API`;")

cursor.execute("CREATE DATABASE `API`;")

cursor.execute("USE `API`;")

# criando tabelas
TABLES = {}
TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      email VARCHAR(255) PRIMARY KEY,
      nome VARCHAR(255) not null,
      senha VARCHAR(255) not null,
      admin BOOLEAN not null                
)''')

TABLES['Posts'] = ('''
      CREATE TABLE Posts (
      id INT PRIMARY KEY auto_increment,
      nome VARCHAR(255),
      fk_email VARCHAR(255) not null,
      transplante DATE,
      nascimento DATE not null,
      nome_filho VARCHAR(255) not null,
      comentario LONGTEXT not null,
      foreign key (fk_email) references usuarios(email)
)''')

TABLES['Comentarios'] = ('''
      CREATE TABLE Comentarios (
      id INT PRIMARY KEY auto_increment,
      fk_id INT not null,
      nome VARCHAR(255),
      fk_email VARCHAR(255) not null,
      comentario LONGTEXT not null,
      foreign key (fk_email) references usuarios(email),
      foreign key (fk_id) references posts(id)
)''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()