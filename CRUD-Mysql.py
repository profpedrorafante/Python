import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd-python'
)

cursor = conexao.cursor()
#CREATE
nome_produto = input('Informe o nome do produto: ')
valor = int(input('Informe o valor do produto: '))
comando = f'insert into vendas (nome_produto, valor) values ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()
######
#READ
comando = 'select * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)


cursor.close()
conexao.close()