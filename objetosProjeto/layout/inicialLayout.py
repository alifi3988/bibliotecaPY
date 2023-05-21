import time
import os
from tqdm import tqdm

from objetosProjeto.db.leitoresDB import criacaoTBLeitores
from objetosProjeto.db.livroDB import criacaoTBLivros
from objetosProjeto.db.retiradaLivroDB import criacaoTBRetirada
from objetosProjeto.db.usuarioDB import criacaoTBUsuarios


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
    criacaoTBLeitores()
    criacaoTBLivros()
    criacaoTBUsuarios()
    criacaoTBRetirada()

    for i in tqdm(range(5)):
        time.sleep(1)
    # criação do banco e das tabelas

def finalizacaoApresentacao(nome):
    print(f'Seja Bem-Vindo(a) ao Sistema, {nome}!'.center(52))
    time.sleep(2)
