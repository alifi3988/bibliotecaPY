from db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas
from entitys.livro import Livro

# criação da tabela livros
def criacaoTB():
    sql = """CREATE TABLE tb_livros (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(255) NOT NULL,
        autor               VARCHAR(255) NOT NULL,
        editora             VARCHAR(255) NOT NULL,
        anoLancamento       INTEGER NOT NULL,
        registrado          DATA NOT NULL,
        statusAssociativo   BOOL NOT NULL
    ); """
    if criacaoTabelasDB(sql) == True:
        print("Tabela livros - ok")

# inserção no banco de dados tb_livros
def insercaoLivro(livro):
    sql = f'''INSERT INTO tb_livros(titulo, autor, editora, anoLancamento, registrado, statusAssociativo) 
    VALUES('{livro.getTitulo()}','{livro.getAutor()}','{livro.getEditor()}',{livro.getAnoLancamento()},'{livro.getRegistrado()}','{livro.getStatusAssociativo()}')'''
    print(sql)
    if insercaoDadosTabelas(sql) == True:
        return True
    else:
        return False
