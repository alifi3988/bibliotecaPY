from datetime import datetime
import os
import time
from objetosProjeto.db.leitoresDB import pesquisaCamposLeitorID
from objetosProjeto.db.livroDB import pesquisaCamposLivroID
from objetosProjeto.db.retiradaLivroDB import devolucaoLivroSQL, recuperacaoDadosRetirada, renovacaoLivroSQL

# inicial da devolução ou renovação de livros
def inicialDevolucao(codigoLivro = 'vazio', cpfLeitor = 'vazio'):
    os.system("cls")
    while True:
        print("="*52)
        print("* * * D E V O L U Ç Ã O / R E N O V A Ç Ã O * * *".center(52))
        print("="*52)
        print("Aperte [0] para voltar ao menu.")
        # verificando, se os parâmetos estiverem vazio, vai perguntar os valores
        if cpfLeitor == 'vazio':
            
            # entrada de dados CPF
            cpfLeitor = input("Informe o CPF do Leitor: ")
            if cpfLeitor == '0':
                break
            
            # pesquisando no banco de dados
            retornoLeitor = pesquisaCamposLeitorID('cpf', cpfLeitor)
            
            # validação do retorno 
            if retornoLeitor == False:
                print("CPF não foi localizado!")
                inicialDevolucao() # voltando ao início
            # mostrando os dados para confirmação
            else:
                print("-"*52)
                print(f"Nome Leitor: {retornoLeitor[0][1]}")
                print("-"*52)
                # confirmando
                resp = input("Está correto [S/N]? ").strip().upper()
                if resp != 'S' and resp != '0':
                    inicialDevolucao()
                if resp == '0':
                    break
        else:
            # se os dados do parâmetro estiver com valores, virá direto
            print(f"CPF Leitor: {cpfLeitor}")
        # pegando os dados do Livro
        if codigoLivro == 'vazio':
            codigoLivro = int(input("Informe o código do Livro: "))
            if cpfLeitor == 0:
                break
        
        # buscando no BD
        retornaLivro = pesquisaCamposLivroID(codigoLivro)
        
        # realizando a verificação dos dados
        if retornaLivro == True:
            print("-"*52)
            print(f"Titulo: {retornaLivro[0][1]}")
            print("-"*52)
            resp = input("Está correto [S/N]? \n>>").strip().upper()
            if resp != 'S' and resp != '0':
                inicialDevolucao()
            if resp == '0':
                break
        # pegando o ID Leitor 
        idLeitor = retornoLeitor[0][0]
        
        dadosRetirada = recuperacaoDadosRetirada(codigoLivro, idLeitor) # dados da retirada de livro
        
        if dadosRetirada != False:
            dataDevolucao = dadosRetirada[0][3]
        else:
            print("NÃO FOI POSSÍVEL LOCALIZAR OS DADOS!")
            time.sleep(3)
            inicialDevolucao()
            
        devRenov = int(input("Será DEVOLVIDO[1] ou RENOVADO[2]? "))
        if devRenov == 1 or devRenov == 2:
            
            # devolução
            if devRenov == 1:
                if devolucaoLivro(codigoLivro,idLeitor, cpfLeitor) == True:
                    print("DEVOLUÇÃO REGISTRADA!".center(52))
                    time.sleep(3)
                    break
                else:
                    print("NÃO FOI POSSÍVEL REALIZAR A DEVOLUÇÃO!".center(52))
                    time.sleep(3)
                    inicialDevolucao()
            
            # renovação 
            elif devRenov == 2:
                if renovacaoLivro(codigoLivro,idLeitor, cpfLeitor, dataDevolucao) == True:
                    print("RENOVAÇÃO REALIZADA!".center(52))
                    time.sleep(3)
                    break
                else:
                    print("ERRO, NÃO FOI POSSÍVEL RENOVAR!".center(52))
                    time.sleep(3)
                    inicialDevolucao()
        else:
            print("Foi informado um valor errado, verifique!")
            time.sleep(3)
            inicialDevolucao(codigoLivro, cpfLeitor)
        
# devolução de livro    
def devolucaoLivro(codigoLivro, idLeitor, cpfLeitor):
    os.system("cls")
    print("="*52)
    print("* * * D E V O L U Ç Ã O * * *".center(52))
    print("="*52)
    print(f"Leitor: {cpfLeitor}")
    print(f"Livro: {codigoLivro}")
    print("="*52)
    resp = input("Continuar a operação de devolução? [S/N] \n>> ").strip().upper()
    if resp != 'S' and resp != '0':
        print("Voltando...")
        time.sleep(3)
        inicialDevolucao()
    if resp == '0':
        return False
    # realizando a devolução
    if devolucaoLivroSQL(idLeitor, codigoLivro) == True:
        return True
    else:
        return False
    
# renovação da retirada    
def renovacaoLivro(codigoLivro,idLeitor, cpfLeitor, dataDevolucao):
    os.system("cls")
    print("="*52)
    print("* * * R E N O V A Ç Ã O * * *".center(52))
    print("="*52)
    print(f"Leitor: {cpfLeitor}")
    print(f"Livro: {codigoLivro}")
    print("="*52)
    resp = input("Continuar a operação de renovação? [S/N] \n>> ").strip().upper()
    if resp != 'S' and resp != '0':
        print("Voltando...")
        time.sleep(3)
        inicialDevolucao()
    if resp == '0':
        return False
        
    dias = int(input("Informe a quantos dias será add: "))
    if dias == 0:
        return False

    # realizando a renovação
    if renovacaoLivroSQL(dataDevolucao, idLeitor, codigoLivro, dias) == True:
        return True
    else:
        return False