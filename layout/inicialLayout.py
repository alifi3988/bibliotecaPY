from tqdm import tqdm
from db import usuarioDB
from db import livroDB
from db import leitoresDB
import time
import os


def finalizacaoApresentacao():
    str ='''
    Seja Bem-Vindo(a) ao Sistema!
    '''
    return str

def inicialApresentacao():
    os.system("cls")
    print("====================================================")
    print(" * * * S I S T E M A    B I B L I O T E C A * * *")
    print("====================================================")
    print("Verificando o banco de dados...")
    print("Carregando os dados pertinentes")
    print('''====================================================''')
    usuarioDB.criacaoTB()
    livroDB.criacaoTB()
    leitoresDB.criacaoTB()

    for i in tqdm(range(5)):
        time.sleep(1)
    # criação do banco e das tabelas


def finalizacaoApresentacao(nome):
    str =f'Seja Bem-Vindo(a) ao Sistema, {nome}!'
    return str