# Importações
import sqlite3


# Realizando a criação de um banco de dados local (abrindo e fechando)
def criacaoBD():
    try:
        conn = sqlite3.connect('biblioteca.db')
        conn.close()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Criação automática de tables uteis na aplicação
def criacaoTabelasDB(sql):
    # verificando a criação do BD
    conn = sqlite3.connect('biblioteca.db')

    # Criando através de Scripts
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        # Fechando a conexão com o banco de dados
        conn.close()
        return True
    except sqlite3.Error as er:
        print(er)
        conn.close()
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
    except sqlite3.Error as er:
        print("Erro na inserção de dados na tabela.")
        print(er)
        return False

# buscando os dados da table e retornando em forma de lista
def recuperarDados(sql):
        # coneção com o banco de dados
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        try:
            # executando sql
            cursor.execute(sql)
            
            # criando uma lista para armazenar o resultado
            listaDados = list()
            # passando os dados para um objeto
            for linha in cursor.fetchall():
                listaDados.append(linha)
            # fechando a conexão
            conn.close()
            # retornando uma lista com um dado só, no caso o usuário com o login informado
            if len(listaDados) == 0:
                return False
            return listaDados
        except sqlite3.Error as er:
            print("Erro na recuperação de dados.")
            print(f"Erro: {er}")
            return False
            
# ================================================================================
# ================================================================================

# Referência https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco
