# importação
import time
import xlsxwriter
from datetime import date

# MONTAGEM DO ARQUIVO EM EXCEL
def montagemArquivoExcel(dados, nomeArquivo):
    # referência: https://acervolima.com/python-criar-e-escrever-em-arquivo-excel-usando-o-modulo-xlsxwriter/
    
    # será definido esse caminho para o usuário: C:\Users\alifi\Downloads para salvar os documentos
    
    try:
        # colocarei o nome do arquivo como um padrão de nome e dataAtual
        nomeArquivo = f'{nomeArquivo}_{date.today()}.xlsx'
        
        # criação do arquivo
        arquivoXLSX = xlsxwriter.Workbook(nomeArquivo)
        arquivo = arquivoXLSX.add_worksheet()
        
        # criando um cabeçalho (linha, coluna e valor)
        arquivo.write(0, 0, 'Código Livro')
        arquivo.write(0, 1, 'Título')
        arquivo.write(0, 2, 'Autor')
        arquivo.write(0, 3, 'Editora')
        arquivo.write(0, 4, 'Anolançamento')
        arquivo.write(0, 5, 'Data de registro')
        arquivo.write(0, 6, 'Status')
        
        # preenchendo o arquivo
        linha = 1
        for i in dados:
            coluna = 0
            for j in i:
                arquivo.write(linha, coluna, j)
                coluna = coluna + 1
            linha= linha + 1
        
        # fechando o arquivo
        arquivoXLSX.close()
        return nomeArquivo
    except:
        print("Erro na criação do arquivo!")
        time.sleep(3)
        return False
    
    
