from datetime import date
import os
import time
from objetosProjeto.db.leitoresDB import insertLeitor
from objetosProjeto.entitys.leitor import Leitor

def cadastroLeitor():
    while(True):
        os.system("cls")
        print("="*52)
        print(" * * * C A D A S T R O   D E   L E I T O R * * * ".center(52))
        print("="*52)
        print("Para voltar, informe[0].")
        print("_"*52)
        nome = input("Nome: ")
        if nome == '0':
            break
        idade = int(input("Idade: "))
        if idade == 0:
            break
        cpf = input("CPF: ")
        if cpf == '0':
            break
        email = input("Email: ")
        if cpf == '0':
            break
        telefone = input("Telefone com DDD: ")
        if cpf == '0':
            break
        cidade = input("Cidade: ")
        if cpf == '0':
            break
        uf = input("UF: ")
        if cpf == '0':
            break
        print("_"*52)
        
        # verificando
        leitor = Leitor( nome, idade, cpf, email, telefone, cidade, uf, date.today())
        
        if insertLeitor(leitor) == True:
            print("Cadastro foi realizado com sucesso!")
            time.sleep(2)
            break
        else:
            print("Erro no cadastro. Verifique os dados!")
            time.sleep(2)

        print("="*52)
        print("Deseja realizar novamente? [S/N]")
        resp = input(">>").strip().upper()
        if resp != "S":
            break

