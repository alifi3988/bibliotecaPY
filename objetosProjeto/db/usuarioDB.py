from objetosProjeto.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, modificacaoTable, recuperarDados


# Criação da table
def criacaoTBUsuarios():
    sql = """CREATE TABLE tb_usuarios (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome                TEXT NOT NULL,
        login               VARCHAR(20) NOT NULL UNIQUE,
        senha               TEXT NOT NULL,
        dataCriacao         DATE NOT NULL,
        statusAssociativo   BOOL NOT NULL
    );"""
    if criacaoTabelasDB(sql) == True:
        print("Tabela usuarios - ok")

# Inserção de dados
def inserirUsuario(usuario):

    sql = f'''INSERT INTO tb_usuarios(nome, login, senha, dataCriacao, statusAssociativo) 
    VALUES ('{usuario.getNome()}','{usuario.getLogin()}','{usuario.getSenha()}','{usuario.getDataCriacao()}','{usuario.getStatusAssociativo()}')'''

    if insercaoDadosTabelas(sql) == True:
        return True
    else:
        return False

# Recuperação de dados expecíficos
def recuperarDadosUsuarioExpecifico(str):
    return f"SELECT * FROM tb_usuarios WHERE login = '{str}'"

# recuperando todos os dados
def recuperarTodosDados():
    sql = 'SELECT * FROM tb_usuarios;'
    
    dados = recuperarDados(sql)
    
    if dados != False:
        return dados
    else:
        return False

def recuperarSomenteIDUsuario(usuario):
    sql =recuperarDadosUsuarioExpecifico(usuario)

    dados = recuperarDados(sql)
    
    if dados != False:
        return dados
    else:
        return False

def modificarStatus(usuario):
    sql = f"UPDATE tb_usuarios SET statusAssociativo = '{True}' WHERE login = '{usuario}' "
    return modificacaoTable(sql)
    