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
def atualizar_info(i):
    with con:
        cur =con.cursor()
        query="UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=? WHERE id=?"
        cur.execute(query,i)
    
    
#deletar infarmacoes
def deleta_info(i):
    with con:
        cur =con.cursor()
        query="DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
        






