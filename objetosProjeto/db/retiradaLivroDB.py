
from datetime import datetime, timedelta
from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, modificacaoTable, recuperarDados

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
    VALUES({retirada.getIdLeitor()}, {retirada.getIdLivro()}, '{retirada.getDataRetirada()}', '{retirada.getDataEntrega()}', '{retirada.getStatusRetirada()}')'''
    
    # inserindo no banco de dados o registro
    if insercaoDadosTabelas(sql) == True:
        return True
    else:
        return False

# recuperação de dados
def recuperacaoDadosRetirada(codigoLivro, idLeitor):
    sql = f'''SELECT * 
    FROM tb_retirada 
    WHERE idLeitor = {idLeitor} AND idLivro = {codigoLivro} 
    AND statusAssociativo = '{True}' '''
    
    dados = recuperarDados(sql)
    
    if dados == False:
        return False
    else:
        return dados
    
# renovação
def renovacaoLivroSQL(dataDevolucao, idLeitor, codigoLivro, dias):

    # adicionando os dias
    data = (datetime.strptime(dataDevolucao,  '%Y-%m-%d').date() + timedelta(dias))

    sql =f'''UPDATE tb_retirada
    SET dataDevolucao = '{data}' 
    WHERE idLeitor = {idLeitor} AND idLivro = {codigoLivro} '''

    if modificacaoTable(sql) == True:
        return True
    else:
        return False
    
def devolucaoLivroSQL(idLeitor, codigoLivro):
    
    # atualização da tb_retirada
    sql =f'''UPDATE tb_retirada
    SET statusAssociativo = '{False}'
    WHERE idLeitor = {idLeitor} AND idLivro = {codigoLivro} '''
    
    # atualizção da tb_livro
    sqlLivro = f'''UPDATE tb_livros
    SET statusAssociativo = '{True}'
    WHERE id = {codigoLivro}'''
    
    modificacaoTable(sql)
    
    if modificacaoTable(sql) == True:
        if modificacaoTable(sqlLivro) == True:
            return True
    return False
    