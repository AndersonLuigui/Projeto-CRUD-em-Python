# Importando o SQLite
from distutils.log import info
import sqlite3 as lite



# CRUD


# C = Creaty Inserir / Criar
# R = Ready ACESSAR / MOSTRAR
# U = Update/atualizar
# D = Delete = Deletar/apagar


# Criando conexão 
con = lite.connect('dados.db')






# Inserir informações
'''
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)
'''




# Acessar informações

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista


# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome, email, telefone, dia_em, estado, assunto WHERE id=?"
        cur.execute(query,i)
'''
lista = [1]
# Deletar informação
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query,lista)
'''