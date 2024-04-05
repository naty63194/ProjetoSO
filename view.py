import sqlite3 as lite

con = lite.connect('dados.db')


lista=['Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010"]
#inserir informacoes
with con:
    cur =con.cursor()
    query='INSERT INTO formulario(nome, email, telefone, dia-em) VALUES(?,?,?,?)'
    cur.execute(query, lista)
    

