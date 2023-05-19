import collections
from datetime import date
from click import pause
from tqdm import tqdm
import time
import os
from getpass import getpass
from objetosProjeto.db.usuarioDB import inserirUsuario, recuperarDadosUsuarioExpecifico
from objetosProjeto.db.conexaoDB import recuperarDados
from objetosProjeto.entitys.usuario import Usuario
from objetosProjeto.layout.inicialLayout import finalizacaoApresentacao
from objetosProjeto.layout.menuLayout import menuInicial

# mostrando o menu do login
def menuLogin():
    os.system("cls")
    print("="*52)
    print("* * * M E N U   L O G I N * * *".center(52))
    print("="*52)
    print("Selecione a opção:")
    print('''[1] - Login\n[2] - Cadastro de Login\n[0] - Sair''')
    print("="*52)
    resposta = input(">>")
    if resposta == "0":
        print("Finalizando o Sistema....")
        #time.sleep()
        exit()
        
    elif resposta == "1":
        login()
    elif resposta == "2":
        if cadastroUsuario() == True:
            return True
    else:
        print("Erro na informação passada! Tente novamente!")
        time.sleep(5)
        menuLogin()

# realizando o login
def login():
    while(True):
        os.system("cls")
        print("="*52)
        print("* * * L O G I N * * *".center(52))
        print("="*52)
        print("Informe os dados.\nInfome [0] em qualquer um dos campos para voltar.")
        loginUsuario = input("Login: ").strip()
        # voltando
        if loginUsuario == "0": menuLogin()
        
        senhaUsuario = getpass("Senha: ").strip()
        print("="*52)
        
        # voltando
        if senhaUsuario == "0": menuLogin()

        lista = recuperarDados(recuperarDadosUsuarioExpecifico(loginUsuario)) # copiando a lista
        if lista != False:
            if len(lista) != 0 and lista[0][2] == loginUsuario and lista[0][3] == senhaUsuario:
                print("Dados conferem com o informado!".center(52))
                nomeUsuario = lista[0][1]
                finalizacaoApresentacao(nomeUsuario)
                time.sleep(3)
                break
                
        print("Dados não conferem!".center(52))
        time.sleep(3)
    menuInicial()

# realizando o cadastro de login com o BD
def cadastroUsuario():
    while True:
        os.system("cls")
        print("="*52)
        print("* * * C A D A S T R O   U S U Á R I O * * *".center(52))
        print("="*52)
        print("Informe os dados corretamente.\nInforme [0] para voltar.")
        nome = input(" Nome: ").strip()
        if nome == '0':
            break
        login = input(" Login: ").strip().lower()
        if login == '0':
            break
        while(True):
            senha = getpass(" Senha: ").strip()
            senhaII = getpass(" Repita: ").strip()
            if senha.__eq__(senhaII):
                print("Senha são compatíveis!".center(52))
                time.sleep(2)
                break
            else:
                print("Senhas NÃO são compatíveis! Tente novamente".center(52))
                print("="*52)
                time.sleep(5)

        # após colher os dados, será registrado no banco de dados
        usuario = Usuario(nome, login, senha, date.today(), False)
        #Criptografia não está conseguindo ser armazenada, verificar!
        #usuario.criptografarSenha()

        # verificando
        if inserirUsuario(usuario) == True:
            print("Cadastro foi realizado com sucesso!".center(52))
            for i in range(1,6):
                print(f"{i}",end="...")
                time.sleep(1)
            break
        else:
            print("Erro no registro. Verifique os dados!")
            print("Deseja tentar novamente? [S/N]")
            resp = input(">>").strip().upper()

        # se apertar N ou qualuqer coisa diferente de S ou s será encerrado o processo de loop
        if resp != "S":
            break
    # após o while mostrará o menu do login
    menuLogin()
    