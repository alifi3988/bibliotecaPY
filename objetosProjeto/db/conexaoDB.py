# Importações
import io
import sqlite3
import time
from bs4 import BeautifulSoup
from click import pause
import urllib.request
#from bs4 import BeautifulSoup

# Realizando a criação de um banco de dados local (abrindo e fechando)
def criacaoBD():
    try:
        conn = sqlite3.connect('biblioteca.db')
        conn.close()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Criação automática de tables uteis na aplicação
def criacaoTabelasDB(sql):
    # verificando a criação do BD
    conn = sqlite3.connect('biblioteca.db')

    # Criando através de Scripts
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        # Fechando a conexão com o banco de dados
        conn.close()
        return True
    except sqlite3.Error as er:
        print(er)
        conn.close()
        return False
        
# inserção no banco de dados
def insercaoDadosTabelas(sqlScript):
    try:
        # conexão com o bd
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute(sqlScript)
        
        # gravando no bd
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as er:
        print("Erro na inserção de dados na tabela.")
        print(er)
        return False

# buscando os dados da table e retornando em forma de lista
def recuperarDados(sql):
        # coneção com o banco de dados
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        try:
            # executando sql
            cursor.execute(sql)
            
            # criando uma lista para armazenar o resultado
            listaDados = list()
            # passando os dados para um objeto
            for linha in cursor.fetchall():
                listaDados.append(linha)
            # fechando a conexão
            conn.close()
            # retornando uma lista com um dado só, no caso o usuário com o login informado
            if len(listaDados) == 0:
                return False
            return listaDados
        except sqlite3.Error as er:
            print("Erro na recuperação de dados.")
            print(f"Erro: {er}")
            return False
   
# modificar table        
def modificacaoTable(sql):
        # coneção com o banco de dados
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        try:
            # executando sql
            resultado = cursor.execute(sql)

            # salvando a alteração
            conn.commit()
            
            # fechando a conexão
            conn.close()
            
            return True
        
        except sqlite3.Error as er:
            print("Erro na modificação dos dados.")
            print(f"Erro: {er}")
            return False
     
# BKP bd
def BKPBancoDeDados():
    
    try:
        conn = sqlite3.connect('biblioteca.db')
        
        # Open() function 
        with open("backupdatabase.sql", 'w') as p: 
                
            # iterdump() function
            for line in conn.iterdump(): 
                p.write('%s\n' % line)
            
        print(' Backup realizado com sucesso!'.center(52))   
        time.sleep(3) 
        conn.close() 
        return True
    
    except sqlite3.Error as er:
        print("Erro para realizar o BKP do Banco de dados")
        print(f"Erro: {er}")
        time.sleep(3)
        return False

# recuperar BD
def RecuperarBancoDeDados(nome):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        
        nomeArquivo = f"{nome}"

        f = io.open(nomeArquivo, 'r')
        sql = f.read()
        cursor.executescript(sql)

        print('Banco de dados recuperado com sucesso.')
        conn.close()
        return True
    except sqlite3.Error as er:
        print("Erro na recuperação. Ou o Banco e as tabelas já existem!")
        print(f"Mensagem: {er}")
        time.sleep(3)
        return False
    

def DadosWeb():
    #URL = "http://biblio.cps.sp.gov.br/"
    #URL = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"
    wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"
    pause()

    #Consulte o site e retorne o html para a variável 'page'
    page = urllib.request.urlopen(wiki)
    pause()

    #Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
    soup = BeautifulSoup(page, 'html5lib')
    pause()

    return True
    '''all_table = SoupStrainer.find_all('table')
    #gerando a lista em colunas
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]

    for row in table.findAll("tr"): #para tudo que estiver em <tr>
        cells = row.findAll('td') #variável para encontrar <td>
    if len(cells)==5: #número de colunas
        A.append(cells[0].find(text=True)) #iterando sobre cada linha
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find('a').text)
        E.append(cells[4].find(text=True))

    df = pd.DataFrame(index=A, columns=['Posição'])

    df['Posição']=A
    df['Estado']=B
    df['Código/IBGE']=C
    df['Capital']=D
    df['Área']=E

    df'''

    
# ================================================================================
# ================================================================================

# Referência https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco
