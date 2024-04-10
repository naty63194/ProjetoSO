# Importação da biblioteca sqlite3 com o alias lite
import sqlite3 as lite

# Conexão com o banco de dados 'dados.db'
con = lite.connect('dados.db')

# Lista de dados de exemplo a serem inseridos no banco de dados
lista = ['Joao', 'joao@mail.com', 123456789, "12/19/2023"]

# Função para inserir informações no banco de dados
def inserir_info(i):
    # Abertura da conexão com o banco de dados utilizando a declaração 'with'
    with con:
        # Criação de um cursor para executar comandos SQL
        cur = con.cursor()
        # Definição da consulta SQL para inserção de dados na tabela 'formulario'
        query = 'INSERT INTO formulario(nome, email, telefone, dia_em) VALUES(?,?,?,?)'
        # Execução da consulta com os dados passados como parâmetro
        cur.execute(query, i)

# Função para acessar e retornar todas as informações da tabela 'formulario'
def mostrar_info():
    # Inicialização de uma lista vazia para armazenar os dados recuperados do banco de dados
    lista = []
    # Abertura da conexão com o banco de dados utilizando a declaração 'with'
    with con:
        # Criação de um cursor para executar comandos SQL
        cur = con.cursor()
        # Definição da consulta SQL para seleção de todos os dados da tabela 'formulario'
        query = "SELECT * FROM formulario"
        # Execução da consulta
        cur.execute(query)
        # Recuperação de todos os resultados da consulta
        informacao = cur.fetchall()
        
        # Laço de repetição para percorrer os resultados e adicioná-los à lista
        for i in informacao:
            lista.append(i)
    # Retorno da lista contendo os dados recuperados do banco de dados
    return lista

# Função para atualizar informações no banco de dados
def atualizar_info(i):
    # Abertura da conexão com o banco de dados utilizando a declaração 'with'
    with con:
        # Criação de um cursor para executar comandos SQL
        cur = con.cursor()
        # Definição da consulta SQL para atualizar dados na tabela 'formulario'
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=? WHERE id=?"
        # Execução da consulta com os dados passados como parâmetro
        cur.execute(query, i)

# Função para deletar informações do banco de dados
def deleta_info(i):
    # Abertura da conexão com o banco de dados utilizando a declaração 'with'
    with con:
        # Criação de um cursor para executar comandos SQL
        cur = con.cursor()
        # Definição da consulta SQL para deletar dados na tabela 'formulario'
        query = "DELETE FROM formulario WHERE id=?"
        # Execução da consulta com os dados passados como parâmetro
        cur.execute(query, i)
