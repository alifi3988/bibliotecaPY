import os
from objetosProjeto.db.leitoresDB import pesquisaCamposLeitorID
from objetosProjeto.db.livroDB import pesquisaCamposLivroID
from objetosProjeto.db.retiradaLivroDB import retiradaLivroSQL
from objetosProjeto.entitys.leitor import Leitor
from objetosProjeto.entitys.retirada import Retirada
from datetime import date, time

def inicioRetirada(cpfLeitor='vazio'):
    os.system("cls")
    while True:
        print("="*52)
        print(" * * * R E T I R A D A  D E  L I V R O * * *".center(52))
        print("="*52)
        if cpfLeitor == 'vazio':
            cpfLeitor = input("Infome o CPF do Leitor: ")
        else:
            print(f"CPF: {cpfLeitor}")
        # realizará primeiro a busca pelo CPF para localizar o leitor
        retornoLeitor = pesquisaCamposLeitorID('cpf', cpfLeitor)
        if retornoLeitor == False:
            print('Leitor não foi localizado. Verifique!')
            inicioRetirada()
        else:
            # Verificação
            print('-'*52)
            print(f"Nome Leitor: {retornoLeitor[0][1]}")
            print(f"CPF: {retornoLeitor[0][2]}")
            print('-'*52)
            resp= input("Os dados confirmam? [S/N]").strip().upper()
            if resp != "S":
                inicioRetirada()

            leitorID = retornoLeitor[0][0] # pegando o id do leitor para ser utilizado
        print("Dados do Leitor OK")
        codigoLivro = int(input("Informe o número do Livro: "))
        
        # realizará a busca pelo Código do Livro para localizá-lo
        retornoLivro = pesquisaCamposLivroID(codigoLivro)
        print(retornoLivro)
        
        if retornoLeitor == False:
            print('Livro não foi localizado. Verifique!')
            inicioRetirada(cpfLeitor)
        else:
            
            # verificação se o livro está já sendo utilizado por alguém
            if retornoLivro[0][3] != 'False':
                print(retornoLivro[0][3])
                print("O livro informado se encontra ocupado. Verique antes de continuar...")
                time.sleep(5)
                break
            else:
                print(retornoLivro)
                # Verificação
                print('-'*52)
                print(f"Título Livro: {retornoLivro[0][1]}")
                print(f"Autor: {retornoLivro[0][2]}")
                print('-'*52)
                resp= input("Os dados confirmam? [S/N]").strip().upper()
                if resp != "S":
                    inicioRetirada(cpfLeitor)
                # criação de um leitor
                livroCodigo = codigoLivro[0][0]
                
            dias = int(input("Informe quantos dias para devolução: "))
            retirada = Retirada(leitorID, livroCodigo, (date.today()), (date.today() + dias), True)
            if retiradaLivroSQL(retirada):
                print("REGISTRADO!".center(52))
                time.sleep(3)
                break
            else:
                print("Houve erro no registro. Verifique os dados!".center(52))
                print("-"*52)
                print("Dados informados...")
                print(f"CPF: {cpfLeitor}")
                print(f"CÓDIGO DO LIVRO: {codigoLivro}")
                print("-"*52)
                
                break