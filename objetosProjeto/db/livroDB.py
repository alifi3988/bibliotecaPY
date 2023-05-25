from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, modificacaoTable, recuperarDados

# criação da tabela livros
def criacaoTBLivros():
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

# retornará somente o ID | é mais verificar se o ID ou livro está cadastrado
# para confirmar será retornado um
def pesquisaCamposLivroID(idValidar):
    sql = f'''SELECT id, titulo, autor, statusAssociativo FROM tb_livros
    WHERE id = {idValidar}'''
    
    retornoDados = recuperarDados(sql)
    
    if retornoDados == False:
        return False
    return retornoDados # será retornado uma lista

# inserção no banco de dados tb_livros
def insercaoLivro(livro):
    sql = f'''INSERT INTO tb_livros(titulo, autor, editora, anoLancamento, registrado, statusAssociativo) 
    VALUES('{livro.getTitulo()}','{livro.getAutor()}','{livro.getEditor()}',{livro.getAnoLancamento()},'{livro.getRegistrado()}','{livro.getStatusAssociativo()}')'''
    if insercaoDadosTabelas(sql) == True:
        return True
    else:
        return False

# modificar o StatusLivro
def modificacaoStatusLivro(idLivro):
    sql = f'''UPDATE tb_livros
    SET statusAssociativo = 'False'
    WHERE id = {idLivro}'''
    
    if modificacaoTable(sql) == True:
        return True
    else:
        return False

# pesquisartodos os livros
def recuperarTodosLivros():
    sql = 'SELECT * FROM tb_livros'
    dados = recuperarDados(sql)
    
    if dados != False:
        return dados
    else:
        return False
    
    