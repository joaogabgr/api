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
