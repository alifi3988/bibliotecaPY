# Importações
import sqlite3
import time


# Realizando a criação de um banco de dados local (abrindo e fechando)
def criacaoBD():
    conn = sqlite3.connect('biblioteca.db')
    conn.close()
    return True

# Criação automática de tables uteis na aplicação
def criacaoTabelasDB(sql):
    # verificando a criação do BD
    conn = sqlite3.connect('biblioteca.db')

    # Criando através de Scripts
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except:
        print("Tabela Já Existe")
    # Fechando a conexão com o banco de dados
    conn.close()
    return True

# Criação geral para facilitar
def criacaoTables():

    # Criação inicial
    criacaoBD()
    if criacaoTabelasDB():
        print("Conexão realizada! \nTabela já está disponível!")
        return True
    return False

# inserção no banco de dados
def insercaoDadosTabelas(sqlScript):
    try:
        # conexão com o bd
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute(sqlScript)
        # gravando no bd
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro para inseir dados na table! (conexaoDB.py)")
        time.sleep(5)
        return False

# buscando os dados da table e retornando em forma de lista
def recuperarDadosExpecificos(sqlScript):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute(sqlScript)
    for linha in cursor.fetchall():
        objeto = linha
    conn.close()

    return objeto

# ================================================================================
# ================================================================================

# Referência https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco