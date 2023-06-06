import os
import time
from objetosProjeto.db.relatoriosDB import recuperando_relatorio_retirada
from objetosProjeto.relatórios.montagemArquivos import montagemArquivoExcelRetirada


def gerar_relatorio_retirada():
    os.system("cls")
    print("="*52)
    print("* * * R E L A T Ó R I O   R E T I R A D A * * *".center(52))
    print("="*52)
    # realizando a criação do arquivo
    dadosRecuperado = recuperando_relatorio_retirada()
    if dadosRecuperado != False:
        # chamar para realizar o relatorio
        respCriacaoArquivo = montagemArquivoExcelRetirada(dadosRecuperado, 'RelatorioGeralRetirada')
        if respCriacaoArquivo != False:
            print(f"Arquivo criado! {respCriacaoArquivo}")
            time.sleep(3)
            return True
    return False
