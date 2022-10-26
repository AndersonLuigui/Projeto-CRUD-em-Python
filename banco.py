# IMPORTANDO SQLite
import sqlite3 as lite


# CRIANDO CONEXÃO
con = lite.connect('dados.db')

# CRIANDO TABELA
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")


