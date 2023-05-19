import time
import os
from datetime import datetime, date
from objetosProjeto.db.livroDB import insercaoLivro

from objetosProjeto.entitys.livro import Livro



# cadastro de livros
def cadastroLivro():
    while(True):
        os.system("cls")
        print("="*52)
        print("* * * C A D A S T R O  L I V R O * * *")
        print("="*52)
        print("Informe conforme solicitado.")
        print("_"*52)

        # colhendo os dados do livro
        titulo = input("Título: ")
        autor = input("Autor: ")
        editora = input("Editora: ")
        
        dataAtual = datetime.now() # pegando a data atual
        
        # verificação da data de lançamento
        while True:
            ano = input("Ano de lançamento: ")
            anoLancamento = datetime.strptime(ano, '%Y').year
            anoAtual = dataAtual.year
            
            if anoLancamento > anoAtual:
                print("Data informada incorreta. Informe novamente!")
            else:
                break
        
        # passando os dados para serem passados para serem registrados
        livro = Livro(titulo, autor, editora, anoLancamento, date.today(), True)
        
        if insercaoLivro(livro) == True:
            print("Livro foi inserido com sucesso!".center(52))
            time.sleep(2)
        else:
            print("Houve algum erro. Verifique os dados!".center(52))
            
        print("Deseja tentar novamente? [S/N]")
        resp = input(">>").strip().upper()
        
        # se apertar N ou qualuqer coisa diferente de S ou s será encerrado o processo de loop
        if resp != "S":
            break

    
# Retirada de Livro
# Relatório de Livros




