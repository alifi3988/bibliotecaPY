from objetosProjeto.db.conexaoDB import DadosWeb


# função principal da aplicação
def main():
    #inicialApresentacao()
    #menuLogin()
    if DadosWeb() == True:
        print("ok")
    
if __name__ == "__main__":
    main()

