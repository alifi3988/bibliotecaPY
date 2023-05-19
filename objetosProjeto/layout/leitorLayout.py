from datetime import date
import time
from objetosProjeto.db.leitoresDB import insertLeitor
from objetosProjeto.entitys.leitor import Leitor

def cadastroLeitor():
    print("="*52)
    print(" * * * C A D A S T R O   D E   L E I T O R * * * ".center(52))
    print("="*52)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone com DDD: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    data = date.today 
    # verificando
    leitor = Leitor( nome, idade, cpf, email, telefone, cidade, uf, data)
    
    if insertLeitor(leitor) == True:
        print("Cadastro foi realizado com sucesso!")
        for i in range(1,6):
            print(f"{i}",end="...")
            time.sleep(2)
            break
    else:
        print("Erro no cadastro. Verifique os dados!")
        print("Deseja tentar novamente? [S/N]")
        resp = input(">>").strip().upper()

