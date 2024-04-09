import sqlite3 as lite

con = lite.connect('dados.db')


lista=['Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010"]

#inserir informacoes
def inserir_info(i):
    with con:
        cur =con.cursor()
        query='INSERT INTO formulario(nome, email, telefone, dia_em) VALUES(?,?,?,?)'
        cur.execute(query,i)


#acessar informações
def mostrar_info():
    lista =[]
    with con:
        cur =con.cursor()
        query="SELECT * FROM formulario"
        cur.execute(query)
        informacao=cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista
            

#atualizar informacoes
with con:
    cur =con.cursor()
    query="UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query, lista)
    
#deletar inofrmacoes
with con:
    cur =con.cursor()
    query="DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)
    



