#from objetosProjeto.entitys.livro import Livro

from objetosProjeto.db.relatoriosDB import recupearando_todos_dados, recuperando_dados_nao_retirados, recuperando_dados_retirados


livros = []

# Função para gerar o relatório de livros
def gerar_relatorio(opcao):
    if opcao == '1 - todos':
        resultado = recupearando_todos_dados()
    elif opcao == '2 - retirados': #where false
        resultado = recuperando_dados_retirados()
    elif opcao == '3 - nao_retirados': #where true
        resultado = recuperando_dados_nao_retirados
    else:
        print('Opção inválida!')
        return
    
