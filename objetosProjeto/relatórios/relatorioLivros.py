import os
import time
from objetosProjeto.db.relatoriosDB import *
from objetosProjeto.relatórios.montagemArquivos import montagemArquivoExcel

# Função para gerar o relatório de livros | Menu de relatórios
def gerar_relatorio_livros():
    while True:
        os.system("cls")
        print("="*52)
        print("* * * R E L A T Ó R I O S   L I V R O S * * *".center(52))
        print("="*52)
        print("Para voltar ao menu, informe [0]")
        print('''Informe a opção de acordo com o desejado: \n[1] - Todos os Livros \n[2] - Somente os retirados \n[3] - Somente os disponíveis''')
        opcao = input('>> ')
        
        # chamando as funções de acordo com o selecionado
        if opcao == '1':
            resultado = relatorioGeral()
            if resultado == False:
                print("Erro na geração de relatório. Verifique!")
                time.sleep(3)
                break
            elif resultado == True:
                break
            
        elif opcao == '2': #where false
            resultado = relatorioLivrosRetirados()
            if resultado == False:
                print("Erro na geração de relatório. Verifique!")
                time.sleep(3)
                break
            elif resultado == True:
                break
            
        elif opcao == '3': #where true
            resultado = relatorioLivrosDisponiveis()
            if resultado == False:
                print("Erro na geração de relatório. Verifique!")
                time.sleep(3)
                break
            elif resultado == True:
                break
        elif opcao == '0':
            break
        
        else:
            print('Opção inválida. Tente novamente!')

# ===============================================================================================================#
#                                    RELATÓRIOS  GERAL  DE  LIVROS
# ===============================================================================================================#
# relatorio geral
def relatorioGeral():
    os.system("cls")
    print("="*52)
    print("* * * R E L A T Ó R I O   G E R A L * * *".center(52))
    print("="*52)
    # realizando a criação do arquivo
    dadosRecuperado = recupearando_todos_dados()
    if dadosRecuperado != False:
        # chamar para realizar o relatorio
        respCriacaoArquivo = montagemArquivoExcel(dadosRecuperado, 'RelatorioGeralLivros')
        if respCriacaoArquivo != False:
            print(f"Arquivo criado! {respCriacaoArquivo}")
            time.sleep(3)
            return True
    return False

# ===============================================================================================================#
#                                   RELATÓRIOS  DOS  LIVROS  RETIRADOS                                  
# ===============================================================================================================#
# relatorio geral
def relatorioLivrosRetirados():
    os.system("cls")
    print("="*52)
    print("* * * R E L A T Ó R I O   R E T I R A D O S * * *".center(52))
    print("="*52)
    # realizando a criação do arquivo
    dadosRecuperado = recuperando_dados_retirados()
    if dadosRecuperado != False:
        # chamar para realizar o relatorio
        respCriacaoArquivo = montagemArquivoExcel(dadosRecuperado, 'RelatorioLivrosRetirados')
        if respCriacaoArquivo != False:
            print(f"Arquivo criado! {respCriacaoArquivo}")
            time.sleep(3)
            return True
    return False
            
# ===============================================================================================================#
#                                 RELATÓRIOS  DOS  LIVROS  NÃO  RETIRADOS                                  
# ===============================================================================================================#
# relatorio geral
def relatorioLivrosDisponiveis():
    os.system("cls")
    print("="*52)
    print("* * * R E L A T Ó R I O   D I S P O N Í V E I S * * *".center(52))
    print("="*52)
    # realizando a criação do arquivo
    dadosRecuperado = recuperando_dados_nao_retirados()
    if dadosRecuperado != False:
        # chamar para realizar o relatorio
        respCriacaoArquivo = montagemArquivoExcel(dadosRecuperado, 'RelatorioLivrosDisponiveis')
        if respCriacaoArquivo != False:
            print(f"Arquivo criado! {respCriacaoArquivo}")
            time.sleep(3)
            return True
    return False
            

    