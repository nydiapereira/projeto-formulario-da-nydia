# importando o banco de dados SQLite
import sqlite3 as lite

# criando a conexão com o banco de dados
con = lite.connect('banco.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE formulario(id INT PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT, dia_em_DATE, estado TEXT, assunto TEXT)")
    