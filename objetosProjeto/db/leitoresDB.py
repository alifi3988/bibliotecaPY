
# criação da tabela Leitores
from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas


def criacaoTBLeitores():
    sql =  """CREATE TABLE tb_leitores (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome        TEXT NOT NULL,
        idade       INTEGER,
        cpf         VARCHAR(11) NOT NULL,
        email       TEXT NOT NULL,
        fone        TEXT,
        cidade      TEXT,
        uf          VARCHAR(2) NOT NULL,
        criado_em   DATE NOT NULL
    );  """
    if criacaoTabelasDB(sql) == True:
        print("Tabela leitores - ok")

# Inserção de dados na tabela
def insertLeitor(leitor):
    sql = f'''Insert into tb_leitores (nome, idade, cpf, email, fone, cidade, uf, criacao_em) 
    Values('{leitor.getNome()}', {leitor.getIdade()}, '{leitor.getCpf()}', '{leitor.getEmail()}',
    '{leitor.getTelefone()}', '{leitor.getCidade()}', '{leitor.getUf()}', '{leitor.getData}')'''

    if insercaoDadosTabelas(sql):
        return True
    else:
        return False
