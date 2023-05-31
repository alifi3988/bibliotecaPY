import collections
from lxml import html
import os
import time
from click import pause
import requests
from objetosProjeto.db.conexaoDB import BKPBancoDeDados, RecuperarBancoDeDados
from objetosProjeto.db.leitoresDB import recuperarTodosLeitores
from objetosProjeto.db.livroDB import recuperarTodosLivros
from objetosProjeto.db.retiradaLivroDB import recuperarTodasRetiradas
from objetosProjeto.db.tableWebDB import criacaoTBWEB, insercaoDadosTBWEB, recuperarDadosWebBD
from objetosProjeto.db.usuarioDB import modificarStatus, recuperarSomenteIDUsuario, recuperarTodosDados
import json
import zipfile

# criação de um arquivo geral
def menuAdmSistema():
    while True:
        os.system("cls")
        # criação dos diretórios principais
        #criarDiretorioProjeto()
        
        print("="*52)
        print("* * * A D M I N I S T R A D O R * * * ".center(52))
        print("="*52)
        print("[1] - Importar todos os dados do BD | JSON")
        print("[2] - Exportar Banco de dados")
        print("[3] - Importar WEB")
        print("[4] - Liberação de usuario")
        print("[5] - Extração WEB")
        print("[0] - Sair")
        print("-"*52)
        resp = input(">> ").strip()
        
        # verificação
        if resp == '1':
            # crição do diretório desejado JSON            
            arquivoJSON = importarJSON()
            
            if arquivoJSON != False:
                print("Realizado com sucesso...".center(52))
                time.sleep(3)

            else:
                print("Erro para realizar o procedimento!".center(52))
                time.sleep(3)
                
        elif resp == '2':
            exportarBanco()
            
        elif resp == '3':
            importarBD()
            
        elif resp == "4":
            liberacaoUsuario()
        
        elif resp == '5':
            exportarWeb()

        elif resp == '0':
            print("Saindo do ADMINISTRADOR!".center(52))
            time.sleep(3)
            break


# importação de usuários
def importarJSON():
    os.system("cls")
    print("="*52)
    print(" * * * I M P O R T A R   J S O N   * * *".center(52))
    print("="*52)
    criarDiretorioProjetoJson()
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
        print("ERRO PARA RECUPERAÇÃO DE DADOS!".center(52))
        time.sleep(3)
    # finalização
    
    try:
        # realizando a conversão para Json e compactando
        zf = os.path.join(os.sep, 'c:\\bibliotecaDados\\json', 'jsonDadosBiblioteca.zip')

        arquivoZip = zipfile.ZipFile(zf,'w')
        
        with open("c:\\bibliotecaDados\\json\\jsonbancoBiblioteca.json", "w") as arquivo:     
            json.dump(bancoBiblioteca, arquivo, indent=4)
        arquivoZip.write("c:\\bibliotecaDados\\json\\jsonbancoBiblioteca.json")
        arquivoZip.close()
        print("Arquivo Compactado!".center(52))
        time.sleep(3)
        
        return bancoBiblioteca
    
    except:
        print("Houve erro! Verifique! [menuAdministrativo/importarJSON()]")
        time.sleep(3)
    
# expostação banco de dados
def exportarBanco():
    os.system("cls")
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
    
# criação do diretório para exportação do JSON
def criarDiretorioProjetoJson():
    try:
        os.makedirs
        dir = os.path.join(os.sep, "c:\\", 'bibliotecaDados')
        dr2 = os.path.join(os.sep, "c:\\bibliotecaDados", 'json')
        
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(dr2):
            os.makedirs(dr2)

            
        print(f"Diretório criado: {dir} | {dr2}")
        time.sleep(3)
        
        return True
    except:
        print("Erro: menuAdministrativo.py/criarDiretorioProjeto()")
        time.sleep(3)
        return False
  
def criarDiretorioProjetoBD():
    try:
        os.makedirs
        dir = os.path.join(os.sep, "c:\\", 'bibliotecaDados')
        dr3 = os.path.join(os.sep, "c:\\bibliotecaDados", 'bd')
        
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(dr3):
            os.makedirs(dr3)
            
        print(f"Diretório criado: {dir} | {dr3}")
        time.sleep(3)
        
        return True
    except:
        print("Erro: menuAdministrativo.py/criarDiretorioProjeto()")
        time.sleep(3)
        return False
    
  
def liberacaoUsuario():
    while True:
        os.system("cls")
        print("="*52)  
        print(" * * * L I B E R A Ç Ã O   D E   U S U Á R I O * * *")
        print("="*52) 
        print("Informe o usuário que será realizado a liberação.")
        print("Ou infome [0] para voltar")
        usuario = input(">> ")
        
        if usuario =='0':
            break
        else:
            print("Pesquisando...")
            time.sleep(2)
            retorno = recuperarSomenteIDUsuario(usuario)
            
            if retorno != False:
                print("Usuario Localizado! Confirme os dados...")
                print("-"*52)
                print(f"Nome: {retorno[0][1]}")
                print(f"Usuário: {retorno[0][2]}")
                print("-"*52)
                while True:
                    resp = input("Correto? [S/N] \n>> ").strip().upper()
                    
                    if resp != "S" and resp != "N" and resp != '0':
                        print("Não reconheci o que foi informado! Informe novamente...")
                    
                    elif resp =='S':
                        break
                    
                    elif resp =='N':
                        liberacaoUsuario()
                        
                    elif resp == '0':
                        menuAdmSistema()
                        
                retorno = modificarStatus(usuario)
                
                if retorno == True:
                    print("Usuário foi ativado!")
                    time.sleep(2)
                    break
                else:
                    print("Falha para ativar o usuário!")
                    time.sleep(2)
            else:
                print("Usuário não foi localizado!")
                time.sleep(2)

# exportação Web
def exportarWeb():
    print("="*52)  
    print(" * * * EXPORTAÇÃO WEB * * *".center(52))
    print("="*52)  
    criacaoTBWEB()

    rec = requestAplicacao()
    
    if rec == True:
        print("Recuperação WEB Realizada!".center(52))
        
        dadosRecuperados = recuperarDadosWebBD()
        
        print("-"*98)
        print(f'{"DADOS RECUPERADOS WEB":^98}')
        print('-'*98)
        print(f'{"ID":^6} {"Titulo":<44} {"Autor":<40}')
        print('-'*98)

        for i in dadosRecuperados:
            idLivro = i[0]
            tituloLivro = i[1]
            autorUnico = i[2]
            print(f"{idLivro:^6} {tituloLivro:<44} {autorUnico:<40} ")
        print('-'*98)
        pause()
        return True
            
    else:
        print("Erro na Recuperação WEB!".center(52))
        time.sleep(3)
        return False

# importação de dados WEB
def requestAplicacao():
    
    try:
        url = "https://www.culturagenial.com/dicas-livros/"
  

        #Consulte o site e retorne o html para a variável 'page'
        page = requests.get(url)
        if page.status_code != 200:
            print("Erro na página informada!")
            return False
        else:
            tree = html.fromstring(page.text)
            links = tree.xpath("//div[@class='container content-wrap']//h2['.' and em and ',']//text()") # pegando os dados com essas infromações em comum
            
        num = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '11.', '12.', '13.', '14.', '15.',
            '16.', '17.', '18.', '19.', '20.', "\\n"]
        
        Livros = collections.namedtuple("Livros", ["titulo", "autor"])
        tituloLivro = ''
        autorLivro = ''
        
        listaLivros = list()
        
        for i in range (len(links)):
            palavraMontada = links[i]
            
            # se NÃO conter, quer dizer que é ou o nome do autor ou do livro
            if not num.__contains__(palavraMontada.strip()):
                
                # removendo da palavra ", de " e subistituindo por vazio ou seja ""
                if ", de " in palavraMontada:
                    palavraMontada = palavraMontada.replace(", de ", "")
                    autorLivro = f"{palavraMontada}"
                    
                else:
                    for j in num:
                        palavraMontada = palavraMontada.replace(j, "")
                    tituloLivro = f"{palavraMontada}"
                    tituloLivro = tituloLivro.strip()
                
            if autorLivro != '' and tituloLivro != '':
                livro = Livros(tituloLivro, autorLivro)
                listaLivros.append(livro)
                autorLivro = ''
                tituloLivro = ''
        
        for i in listaLivros:
            tituloUnico = i.titulo
            autorUnico = i.autor
            try:
                # inserindo no banco de dados
                insercaoDadosTBWEB(tituloUnico, autorUnico)
            except:
                print("Verifique a Inserção da na TB_-EWB")
                time.sleep(3)
        return True
        
    except:
        print("Deu algo errado, verificar")
        time.sleep(3)
        return False
    
