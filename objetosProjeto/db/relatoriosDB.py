
from objetosProjeto.db.conexaoDB import recuperarDados

# recuperando todos os dados
def recupearando_todos_dados():
    consulta = '''SELECT *
    FROM tb_livros'''
    resultado = recuperarDados(consulta)

    # verificação do resultado obtido
    if resultado != False:
        return resultado
    return False

# recuperando somente os retirados
def recuperando_dados_retirados():
    consulta = "SELECT * FROM tb_livros WHERE statusAssociativo == 'False'"
    
    resultado = recuperarDados(consulta)

    #verificação do resultado obtido
    if resultado != False:
        return resultado
    return False

# recuperando os dados não retirados
def recuperando_dados_nao_retirados():
    consulta = "Select * FROM tb_livros WHERE statusAssociativo == 'True'"
    resultado = recuperarDados(consulta)

    #verificação do resultado obtido
    if resultado != False:
        return resultado
    return False




