from click import pause

from db.conexaoDB import insercaoDadosTabelas, criacaoTabelasDB


# Criação da table
def criacaoTB():
    sql = """CREATE TABLE tb_usuarios (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome                TEXT NOT NULL,
        login               VARCHAR(20) NOT NULL UNIQUE,
        senha               TEXT NOT NULL,
        dataCriacao         DATE NOT NULL,
        statusAssociativo   INTEGER NOT NULL
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
def recuperarDadosUsuarioExpecifico(login):
    return f"SELECT * FROM tb_usuarios WHERE login = '{login}'"
