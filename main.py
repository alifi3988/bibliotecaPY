from datetime import date, timedelta, datetime
from objetosProjeto.layout.inicialLayout import inicialApresentacao
from objetosProjeto.layout.loginLayout import menuLogin
from objetosProjeto.relatórios.relatorioLivros import gerar_relatorio

# função principal da aplicação
def main():
#    inicialApresentacao()
    #menuLogin()
    gerar_relatorio()
    
if __name__ == "__main__":
    main()
