#importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

#criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE)")
