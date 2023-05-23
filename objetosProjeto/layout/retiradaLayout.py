import os
from objetosProjeto.db.leitoresDB import pesquisaCamposLeitorID
from objetosProjeto.db.livroDB import modificacaoStatusLivro, pesquisaCamposLivroID
from objetosProjeto.db.retiradaLivroDB import retiradaLivroSQL
from objetosProjeto.entitys.leitor import Leitor
from objetosProjeto.entitys.retirada import Retirada
from datetime import date, timedelta
import time

def inicioRetirada(cpfLeitor='vazio'):
    os.system("cls")
    while True:
        print("="*52)
        print(" * * * R E T I R A D A  D E  L I V R O * * *".center(52))
        print("="*52)
        print("Digite [0] para voltar ao menu.")
        print("-"*52)
        # verificação, pois esse método pode ser chamado com o cpf já informado
        if cpfLeitor == 'vazio':
            cpfLeitor = input("Infome o CPF do Leitor: ")
            if cpfLeitor == '0':
                break
        else:
            print(f"CPF: {cpfLeitor}")
            
        # realizará primeiro a busca pelo CPF para localizar o leitor
        retornoLeitor = pesquisaCamposLeitorID('cpf', cpfLeitor)
        if retornoLeitor == False:
            print('Leitor não foi localizado. Verifique!')
            time.sleep(2)
            inicioRetirada()
        else:
            # Verificação, se foi encontrado será mostrado as infromações básicas para validação
            print('-'*52)
            print(f"Nome Leitor: {retornoLeitor[0][1]}")
            print(f"CPF: {retornoLeitor[0][2]}")
            print('-'*52)
            resp= input("Os dados confirmam? [S/N]").strip().upper()
            if resp != "S" and resp != '0':
                inicioRetirada()
            elif resp == '0':
                break
            
            # tem que realizar um busca, verificando se o Leitor está já com lagum livro retirado,
            # isso impossibilita de retirar novos até devolver??? regra de negócio???
            
                
             # pegando o id do leitor para ser utilizado
            leitorID = retornoLeitor[0][0]
        
        # pegando o código do livro para realizar a busca
        codigoLivro = int(input("Informe o número do Livro: "))
        if codigoLivro == 0:
            break
        
        # realizará a busca pelo Código do Livro para localizá-lo
        retornoLivro = pesquisaCamposLivroID(codigoLivro)
        
        # validação do resultado obtido
        if retornoLivro == False:
            print('Livro não foi localizado. Verifique!')
            inicioRetirada(cpfLeitor)
        else:
            
            # Verificação
            print('-'*52)
            print(f"Título Livro: {retornoLivro[0][1]}")
            print(f"Autor: {retornoLivro[0][2]}")
            print('-'*52)
            resp= input("Os dados confirmam? [S/N]").strip().upper()
            if resp != "S" and resp != '0':
                inicioRetirada()
            elif resp == '0':
                break
            
            
            # verificação se o livro está já sendo utilizado por alguém
            if retornoLivro[0][3] == 'False':
                print("O livro informado se encontra ocupado. Verique antes de continuar".center(52))
                time.sleep(3)
                break
            
            # informando qauntos dias ficará com o livro
            dias = int(input("Informe quantos dias para devolução: "))
            
            # criação para inserir no banco de dados
            retirada = Retirada(leitorID, codigoLivro, (date.today()), (date.today() + timedelta(dias)), True)
            
            # verificação da inserção no banco de dados
            if retiradaLivroSQL(retirada) == True:
                print("REGISTRADO!".center(52))
                # relizando a modificação no Livro, colocando como False, ou seja, está retirado
                modificacaoStatusLivro(codigoLivro)
                time.sleep(3)
                break
            else:
                print("Houve erro no registro. Verifique os dados!".center(52))
                print("-"*52)
                print("Dados informados...")
                print(f"CPF: {cpfLeitor}")
                print(f"CÓDIGO DO LIVRO: {codigoLivro}")
                print("-"*52)
                time.sleep(4) # mudar depois para esperar um "enter"
                break
        break