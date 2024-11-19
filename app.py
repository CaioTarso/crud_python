import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='',
    database='bd_crud_py'
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
nome_produto = "toddynho"
valor = 7
comando = f'UPDATE vendas SET valor = {valor}  WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# DELEATE
'''nome_produto = "toddynho"
comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()'''

cursor.close()
conexao.close()