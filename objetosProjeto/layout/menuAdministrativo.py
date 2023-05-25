import io
import os
from sqlite3 import connect
import sqlite3
import time
from objetosProjeto.db.conexaoDB import BKPBancoDeDados, RecuperarBancoDeDados
from objetosProjeto.db.leitoresDB import recuperarTodosLeitores
from objetosProjeto.db.livroDB import recuperarTodosLivros
from objetosProjeto.db.retiradaLivroDB import recuperarTodasRetiradas
from objetosProjeto.db.usuarioDB import recuperarTodosDados
import json
import zipfile

# criação de um arquivo geral
def menuAdmSistema():
    os.system("cls")
    while True:
        print("="*52)
        print("* * * A D M I N I S T R A D O R * * * ".center(52))
        print("="*52)
        print("[1] - Importar todos os dados do BD")
        print("[2] - Exportar Banco de dados")
        print("[3] - Importar Banco de dados")
        print("[0] - Sair")
        print("-"*52)
        resp = input(">> ").strip()
        
        # verificação
        if resp == '1':
            if importarJSON() == True:
                print("Realizado com sucesso...".center(52))
                time.sleep(3)

            else:
                print("Erro para realizar o procedimento!".center(52))
                time.sleep(3)
                
        elif resp == '2':
            exportarBanco()
            
            
        elif resp == '3':
            importarBD()

        elif resp == '0':
            print("Saindo do modo administrador...")
            time.sleep(3)
            break





# importação de usuários
def importarJSON():
    os.system("cls")
    print("="*52)
    print(" * * * I M P O R T A R   J S O N   * * *".center(52))
    print("="*52)
    
    bancoBiblioteca = {'Historico_Usuarios': [], 'Historico_Livro':[], 'Historico_Leitores':[], 'Historico_Retirada':[]}
    
    # usuarios
    usuariosRec = recuperarTodosDados()
    livrosRec = recuperarTodosLivros()
    leitoresRec = recuperarTodosLeitores()
    retiradosRec = recuperarTodasRetiradas()
    
    # passando os arquivos
    if usuariosRec != False:
        
        for i in usuariosRec:
            bancoBiblioteca['Historico_Usuarios'].append(
                {
                    'id': i[0],
                    'nome': i[1],
                    'login': i[2],
                    'senha':i[3],
                    'dataCriacao':i[4],
                    'statusAssociativo':i[5]
                }
            )

    if livrosRec != False:
        
        for i in livrosRec:
            bancoBiblioteca['Historico_Livro'].append(
                {
                    'id': i[0],
                    'titulo': i[1],
                    'autor': i[2],
                    'editora':i[3],
                    'anoLancamento':i[4],
                    'registrado':i[5],
                    'statusAssociativo':i[6]
                }
            )
    
    if leitoresRec != False:
        
        for i in leitoresRec:
            bancoBiblioteca['Historico_Leitores'].append(
                {
                    'id': i[0],
                    'nome': i[1],
                    'idade': i[2],
                    'cpf':i[3],
                    'email':i[4],
                    'fone':i[5],
                    'cidade':i[6],
                    'uf':i[7],
                    'criado_em':i[8]
                }
            )
   
    if retiradosRec != False:
        
        for i in retiradosRec:
            bancoBiblioteca['Historico_Retirada'].append(
                {
                    'idLeitor': i[0],
                    'idLivro': i[1],
                    'dataRetirada': i[2],
                    'dataDevolucao':i[3],
                    'statusAssociativo':i[4]
                }
            )
    else:
        print("ERRO PARA RECUPERAÇÃO DE DADOS PARA EXPORTAÇÃO!".center(52))
        time.sleep(3)
    # finalização
    
    
    # realizando a conversão para Json e compactando
    arquivoZip = zipfile.ZipFile('jsonDadosBiblioteca.zip', 'w', zipfile.ZIP_DEFLATED)
    
    with open("bancoBiblioteca.json", "w") as arquivo:     
        arquivoZip.write(json.dump(bancoBiblioteca, arquivo, indent=4))
        
        
    arquivoZip.close()
    return True
    

# expostação banco de dados
def exportarBanco():
    print("="*52)  
    print(" * * * EXPORTAÇÃO DO BANCO DE DADOS * * *".center(52))
    print("="*52)  
    
    if BKPBancoDeDados() == True:
        return True
    else:
        return False
  
# importação banco de dados
def importarBD():
    print("="*52)  
    print(" * * * IMPORTAÇÃO DO BANCO DE DADOS * * *".center(52))
    print("="*52)  
    
    print("Informe o nome do rquivo '.sql' para realizar a Importação: ")
    nome = input(">> ").strip()

    if RecuperarBancoDeDados(nome) == True:
        return True
    else:
        return False