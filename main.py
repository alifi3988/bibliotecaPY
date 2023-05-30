<<<<<<< HEAD
from objetosProjeto.db.conexaoDB import DadosWeb

=======
from objetosProjeto.layout.inicialLayout import inicialApresentacao
from objetosProjeto.layout.loginLayout import menuLogin
from objetosProjeto.layout.menuAdministrativo import importarJSON
>>>>>>> 3d73da57ebd5f442c59217673c1fc8b0163cc0fb

# função principal da aplicação
def main():
    #inicialApresentacao()
    #menuLogin()
    if DadosWeb() == True:
        print("ok")
    
if __name__ == "__main__":
    main()

