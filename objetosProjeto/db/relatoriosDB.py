
# recuperando todos os dados
from objetosProjeto.db.conexaoDB import recuperarDados


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



#recuperando todos os leitores
def recupearando_todos_leitores():
    consulta = '''SELECT *
    FROM tb_leitores'''
    resultado = recuperarDados(consulta)

    # verificação do resultado obtido
    if resultado != False:
        return resultado
    return False

def recuperando_relatorio_retirada():
    consulta = '''SELECT re.idLeitor, le.nome, re.idLivro, li.titulo, re.dataRetirada, re.dataDevolucao, re.statusAssociativo 
FROM tb_retirada re 
INNER JOIN tb_leitores le ON (re.idLeitor == le.id)
INNER JOIN tb_livros li ON (re.idLivro == li.id)'''
    resultado = recuperarDados(consulta)
    if resultado != False:
        return resultado
    return False
    
        


