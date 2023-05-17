from db.conexaoDB import criacaoTabelasDB


def criacaoTB():
    sql = """CREATE TABLE tb_livros (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(30) NOT NULL,
        autor               VARCHAR(30) NOT NULL,
        editora             VARCHAR(30) NOT NULL,
        anoLancamento       INTEGER NOT NULL,
        registrado          DATE NOT NULL
    ); """
    if criacaoTabelasDB(sql) == True:
        print("Tabela livros - ok")