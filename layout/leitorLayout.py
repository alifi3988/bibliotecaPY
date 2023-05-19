from datetime import date
import time
from db.leitoresDB import criacaoTB, insertLeitor
from entitys.leitor import Leitor

def cadastroLeitor():
    print("\nCadastro de Leitor")
    nome = input("Nome do Leitor: ")
    idade = int(input("Idade do Leitor: "))
    cpf = input("CPF do Leitor: ")
    email = input("Email do Leitor: ")
    telefone = input("Telefone do Leitor: ")
    cidade = input("Cidade do Leitor: ")
    uf = input("UF do Leitor: ")
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

