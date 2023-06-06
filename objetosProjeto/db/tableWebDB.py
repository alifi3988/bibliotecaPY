import time
from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, recuperarDados

# criação da table
def criacaoTBWEB():
    sql = """CREATE TABLE tb_livrosWEB (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(255) NOT NULL UNIQUE,
        autor               VARCHAR(255) NOT NULL UNIQUE,
        statusAssociativo   BOOL NOT NULL
    ); """
    
    if criacaoTabelasDB(sql) == True:
        time.sleep(2)
        
def insercaoDadosTBWEB(titulo, autor, status=True):
    sql = f'''INSERT INTO tb_livrosWEB(titulo, autor, statusAssociativo)
    VALUES ('{titulo}', '{autor}', '{status}')'''
    if insercaoDadosTabelas(sql) == True:
        return True
    return False
        
def recuperarDadosWebBD():
    sql = f"SELECT * FROM tb_livrosWEB"
    listaDados = recuperarDados(sql)
    
    if listaDados != False:
        return listaDados
    return False