
# criação da tabela Leitores
from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, recuperarDados

# criação do banco de dados
def criacaoTBLeitores():
    sql =  """CREATE TABLE tb_leitores (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome        TEXT NOT NULL,
        idade       INTEGER,
        cpf         VARCHAR(11) NOT NULL UNIQUE,
        email       TEXT NOT NULL,
        fone        TEXT,
        cidade      TEXT,
        uf          VARCHAR(2) NOT NULL,
        criado_em   DATE NOT NULL
    );  """
    if criacaoTabelasDB(sql) == True:
        print("Tabela leitores - ok")

# pesquisr no banco por um campo expecífico
def pesquisaCamposLeitor(campo, valor):
    sql = f'''SELECT * FROM tb_leitores
    WHERE {campo} = '{valor}' '''
    
    retornoDados = recuperarDados(sql)
    
    if retornoDados == False:
        return False
    return retornoDados # será retornado uma lista

# retornará somente o ID
def pesquisaCamposLeitorID(campo, valor):
    sql = f'''SELECT id, nome, cpf FROM tb_leitores
    WHERE {campo} = '{valor}' '''
    
    retornoDados = recuperarDados(sql)
    
    if retornoDados == False:
        return False
    return retornoDados # será retornado uma lista
    
# Inserção de dados na tabela
def insertLeitor(leitor):
    sql = f'''Insert into tb_leitores (nome, idade, cpf, email, fone, cidade, uf, criado_em) 
    Values('{leitor.getNome()}', {leitor.getIdade()}, '{leitor.getCpf()}', '{leitor.getEmail()}',
    '{leitor.getTelefone()}', '{leitor.getCidade()}', '{leitor.getUf()}', '{leitor.getData()}')'''

    if insercaoDadosTabelas(sql):
        return True
    else:
        return False

def recuperarTodosLeitores():
    sql = 'SELECT * FROM tb_leitores'
    dados = recuperarDados(sql)
    
    if dados != False:
        return dados
    else:
        return False
