
from objetosProjeto.db.conexaoDB import recuperarDados


def recupearando_todos_dados():
    consulta = '''Select id, titulo, autor, editora, anoLancamento, registrado, statusAssociativo
    From tb_livros'''
    resultado = recuperarDados(consulta)

    # verificação do resultado obtido
    if resultado != False:
        return resultado
    return False

def recuperando_dados_retirados():
    consulta = '''Select id, titulo, autor, editora, anoLancamento, registrado, 
    (Where statusAssociativo == False) From tb_livros'''
    resultado = recuperarDados(consulta)

    #verificação do resultado obtido
    if resultado != True:
        return resultado
    return False

def recuperando_dados_nao_retirados():
    consulta = '''Select id, titulo, autor, editora, anoLancamento, registrado, 
    (Where statusAssociativo == True) From tb_livros'''
    resultado = recuperarDados(consulta)

    #verificação do resultado obtido
    if resultado != False:
        return resultado
    return True




