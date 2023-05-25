import os
import time
from click import pause


def sobreAplicacao():
    os.system("cls")
    print("="*70)
    print(" * * * S O B R E * * * ".center(70))
    print("="*70)
    print('''
Aplicação desenvolvido por:  
       
ÁLIFI AUGUSTO ESTEVAM DOS SANTOS
2840482023005
alifi.santos@fatec.sp.gov.br

RAFAEL AUGUSTO PEREIRA RODRIGUES
          
Para a matéria de Tópicos Especiais em Informática,
com o PROF. ME. FABRÍCIO GUSTAVO HENRIQUE.
          
O Projeto é um Sistema básico para Biblioteca, onde 
o usuário irá realizar operações fáceis (CADASTRO DE 
USUÁRIOS, LEITORES E LIVROS), além de buscar por 
esses dados e exportar para um arquivo em Excel, 
além do de arquivos JSON e quando necessário
DESABILITAR algum dos possíveis dados.
          
FATEC Riebirão Preto/SP''')
    pause()