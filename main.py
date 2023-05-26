from objetosProjeto.db.conexaoDB import BKPBancoDeDados, recuperarDados
from objetosProjeto.layout.inicialLayout import inicialApresentacao
from objetosProjeto.layout.loginLayout import menuLogin
from objetosProjeto.layout.menuAdministrativo import criarDiretorioProjeto, importarJSON, requestAplicacao
from objetosProjeto.layout.sobre import sobreAplicacao

# função principal da aplicação
def main():
    inicialApresentacao()
    menuLogin()
if __name__ == "__main__":
    main()
