import time
import os
from livroLayout import *
from leitorLayout import *


# criação do menu
def menuInicial():
    os.system("cls")
    print("="*52)
    print("* * * M E N U   I N I C I A L * * *".center(52))
    print("="*52)
    print("Informe conforme desejado")
    print("[1] - Cadastro de Livro")
    print("[2] - Cadastro de Leitor")
    print("[3] - Retirada de Livro")
    print("[4] - Devolução/Renovação")
    print("[5] - Relatório de Livros")
    print("[6] - Relatório de Leitor")
    print("[0] - Sair")
    print("="*52)
    resposta = input(">>").strip()

    # realizando as verificações
    lista = ['1', '2', '3', '4', '5', '6', '0']
    if (lista.__contains__(resposta)):
        if resposta == '1':
            cadastroLivro()
            menuInicial()
        elif resposta == '0':
            os.close()
        elif resposta == '2':
            cadastroLeitor()
            print("Teste realizado")
        '''elif resposta == '3':
            retiradaLivro()
        elif resposta == '4':
            devolucaoRenovacao()
        elif resposta == '5':
            relatorioLivros()
        elif resposta == '6':
            relatorioUsuario()'''
    else:
        print(f"Resposta informada [{resposta}] não está correto. Verifique!")
        time.sleep(5)
        menuInicial()
