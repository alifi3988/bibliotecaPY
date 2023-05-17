import collections
from datetime import date
from tqdm import tqdm
import time
import os
from getpass import getpass
from entitys.usuario import Usuario
from db.usuarioDB import *
from db.conexaoDB import insercaoDadosTabelas, recuperarDadosExpecificos

# mostrando o menu do login
def menuLogin():
    os.system("cls")
    print('''====================================================\n* * * M E N U   L O G I N * * *\n====================================================\nSelecione a opção:''')
    print('''[1] - Login
    [2] - Cadastro de Login
    [0] - Sair
    ====================================================''')
    resposta = input(">>")
    if resposta == "0":
        print("Finalizando o Sistema....")
        time.sleep(5)
        os.close()
    elif resposta == "1":
        login()
    elif resposta == "2":
        cadastroUsuario()
    else:
        print("Erro na informação passada! Tente novamente!")
        time.sleep(5)
        menuLogin()

# realizando o login
def login():
    os.system("cls")
    print('''====================================================
           * * * L O G I N * * *\n====================================================\nInforme os dados:''')
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()
    print('''====================================================''')
    for i in tqdm(range(10)):
        time.sleep(1)

    Obj = recuperarDadosExpecificos(recuperarDadosUsuarioExpecifico(login))
    print(Obj)

    # buscando no banco de dados o valores solictiado, buscará o login, para depois verificar a senha

# realizando o cadastro de login com o BD
def cadastroUsuario():
    while True:
        os.system("cls")
        print('''====================================================\n* * * C A D A S T R O   U S U Á R I O * * *\n====================================================\nInforme os dados corretamente''')
        nome = input("Nome: ").strip()
        login = input("Login: ").strip().lower()
        while(True):
            senha = getpass("Senha: ").strip()
            senhaII = getpass("Repita: ").strip()
            if senha.__eq__(senhaII):
                print("Senha são compatíveis!")
                time.sleep(2)
                break
            else:
                print("Senhas NÃO são compatíveis! Tente novamente")
                print("====================================================")
                time.sleep(5)

        # após colher os dados, será registrado no banco de dados
        usuario = Usuario(nome, login, senha, date.today(), False)
        #Criptografia não está conseguindo ser armazenada, verificar!
        #usuario.criptografarSenha()

        # verificando
        if inserirUsuario(usuario) == True:
            print("Cadastro foi realizado com sucesso!")
            for i in range(1,6):
                print(f"{i}",end="...")
                time.sleep(1)
            break
        else:
            print("Erro no registro. Verifique os dados!")
        while(True):
            print("Deseja tentar novamente? [S/N]")
            resp = input(">>").strip().upper()
            if resp == "N":
                break


    menuLogin()