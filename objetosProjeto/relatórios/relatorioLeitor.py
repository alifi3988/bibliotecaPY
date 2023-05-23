

import os
import time

from objetosProjeto.db.relatoriosDB import recupearando_todos_leitores
from objetosProjeto.relatórios.montagemArquivos import montagemArquivoExcel


def gerar_relatorio_leitor():
    while True:
        os.system("cls")
        print("="*52)
        print("* * * R E L A T Ó R I O S   L E I T O R * * *".center(52))
        print("="*52)
        print("Para voltar ao menu, informe [0]")
        print('''Informe a opção de acordo com o desejado: \n[1] - Todos os Leitores \n[2] - Sair''')
        opcao = input('>> ')

         # chamando as funções de acordo com o selecionado
        if opcao == '1':
            resultado = relatorio_total()
            if resultado == False:
                print("Erro na geração de relatório. Verifique!")
                time.sleep(3)
                break
            elif resultado == True:
                break
        
        elif opcao == '2':
            break

def relatorio_total():
    os.system("cls")
    print("="*52)
    print("* * * R E L A T Ó R I O   G E R A L * * *".center(52))
    print("="*52)
    # realizando a criação do arquivo
    dadosRecuperado = recupearando_todos_leitores()
    if dadosRecuperado != False:
        # chamar para realizar o relatorio
        respCriacaoArquivo = montagemArquivoExcel(dadosRecuperado, 'RelatorioGeralLeitores')
        if respCriacaoArquivo != False:
            print(f"Arquivo criado! {respCriacaoArquivo}")
            time.sleep(3)
            return True
    return False

        

        

 