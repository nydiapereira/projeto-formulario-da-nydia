# importando SQLite
import sqlite3 as lite

# CRUD
# CREATE = Inserir
# READ = Ler
# READY = Editar/Acessar
# UPDATE = Atualizar
# DELETE = Deletar

# criando a conexão com o banco de dados
con = lite.connect('banco.db')

lista = [1, 'Joaquim', 'j@j.com', 119999-9999, '01/01/2022', 'SP', 'Gostaria de o consultar pessoalmente']