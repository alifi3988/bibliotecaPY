import time
import os
from objetosProjeto.layout.devolucaoRenovacaoLayout import inicialDevolucao
from objetosProjeto.layout.leitorLayout import cadastroLeitor
from objetosProjeto.layout.livroLayout import cadastroLivro
from objetosProjeto.layout.retiradaLayout import inicioRetirada
from objetosProjeto.relatórios.relatorioLivros import gerar_relatorio

# criação do menu
def menuInicial():
    while(True):
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
        print("[7] - Relatório de Retirada")
        print("[8] - Baixa Livro e Leitor")
        print("[0] - Sair")
        print("="*52)
        resposta = input(">>").strip()

        # realizando as verificações
        lista = ['1', '2', '3', '4', '5', '6', '0']
        if (lista.__contains__(resposta)):
            if resposta == '1':
                cadastroLivro()
            elif resposta == '0':
                exit()
            elif resposta == '2':
                cadastroLeitor()
            elif resposta == '3':
                inicioRetirada()
            #elif resposta == '4':
                #devolucaoRenovacao()
            elif resposta == '5':
                gerar_relatorio()
            #elif resposta == '6':
                #relatorioUsuario()'''
        else:
            print(f"Resposta informada [{resposta}] não está correto.\nVerifique!")
            time.sleep(3)
