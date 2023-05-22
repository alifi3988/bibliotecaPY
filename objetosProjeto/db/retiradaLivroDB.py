
from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas

# criação da tabela
def criacaoTBRetirada():
    sql = '''CREATE TABLE tb_retirada(
        idLeitor            INTEGER NOT NULL,
        idLivro             INTEGER NOT NULL,
        dataRetirada        DATE NOT NULL,
        dataDevolucao       DATE NOT NULL,
        statusAssociativo   BOOL NOT NULL,
        CONSTRAINT pk_tbRetirada_double_key  PRIMARY KEY (idLeitor, idLivro),
        CONSTRAINT fk_tbRetirada_leitor FOREIGN KEY(idLeitor) REFERENCES tb_leitores(id),
        CONSTRAINT fk_tbRetirada_livro FOREIGN KEY(idLivro) REFERENCES tb_livros(id)
        )'''
    criacaoTabelasDB(sql)


# inserção de dados
def retiradaLivroSQL(retirada):
    sql = f'''INSERT INTO tb_retirada(idLeitor, idLivro, dataRetirada, dataDevolucao, statusAssociativo)
    VALUES({retirada.getIdLeitor()}, {retirada.getIdLivro()}, '{retirada.getDataRetirada()}', '{retirada.getDataEntrega()}', '{retirada.getStatusRetirada()}');'''
    # inserindo no banco de dados o registro
    if insercaoDadosTabelas(sql):
        return True
    else:
        return False
    