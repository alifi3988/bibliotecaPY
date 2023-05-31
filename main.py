import time
from objetosProjeto.layout.inicialLayout import inicialApresentacao
from objetosProjeto.layout.loginLayout import menuLogin


# função principal da aplicação
def main():
    
    inicialApresentacao()
    while True:
        if menuLogin() == False:
            break
    print("Sistema Finalizado!".center(52))
    time.sleep(3)
    
if __name__ == "__main__":
    main()



