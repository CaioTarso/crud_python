from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = conexao.cursor()

#CRUD



# CREATE
"""nome_produto = "toddynho"
valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados"""

# READ
'''comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco
print(resultado)'''

# UPDATE
'''idVendas = 3
valor = 9
comando = f'UPDATE vendas SET valor = {valor}  WHERE idVendas = {idVendas}'
cursor.execute(comando)
conexao.commit()'''

# DELEATE
'''nome_produto = "toddynho"
comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()'''

cursor.close()
conexao.close()