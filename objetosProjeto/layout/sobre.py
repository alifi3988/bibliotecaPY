import os
import time
from click import pause


def sobreAplicacao():
    
    frase = '''Aplicação desenvolvido por: \n\nÁLIFI AUGUSTO ESTEVAM DOS SANTOS\nRA: 2840482023005 \nalifi.santos@fatec.sp.gov.br\n\nRAFAEL AUGUSTO PEREIRA RODRIGUES\n2840482023032\nrafael.rodrigues81@fatec.sp.gov.br\n\nO projeto foi desenvolvido para a matéria de Tópicos Especiais em \nInformática, com o PROF. ME. FABRÍCIO GUSTAVO HENRIQUE.\nÉ um Sistema básico para Biblioteca, onde o usuário irá realizar \noperações fáceis (CADASTRO DE USUÁRIOS, LEITORES E LIVROS), \nalém de buscar por esses dados e exportar para um arquivo em Excel e \nJSON, e quando necessário DESABILITAR algum dos possíveis dados.\n\nFATEC Riebirão Preto/SP'''    
    
    
    
    
    
    
    os.system("cls")
    print("="*70)
    print(" * * * S O B R E * * * ".center(70))
    print("="*70)
    print(f"{frase:^}")
    pause()