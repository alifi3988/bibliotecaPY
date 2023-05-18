import bcrypt

 # Classe Usuário, com os atributos bascios
class Usuario:
    # contrutor da classe usuario
    def __init__(self, nome, login, senha, dataCriacao, statusAssociativo):
        self.nome = nome
        self.login = login
        self.senha = senha # não será armazenado a senha real, somente a criptografada
        self.dataCriacao = dataCriacao
        self.statusAssociativo = statusAssociativo

    # métodos g e s
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getDataCriacao(self):
        return self.dataCriacao

    def setDataCriacao(self, dataCriacao):
        self.dataCriacao = dataCriacao

    def getStatusAssociativo(self):
        return self.statusAssociativo

    def setStatusAssociativo(self, statusAssociativo):
        self.statusAssociativo = statusAssociativo

    def criptografarSenha(self):
        hashed = bcrypt.hashpw(self.getSenha().encode('utf8'), bcrypt.gensalt())
        print(f"Senha Criptografada: {hashed}")
        self.setSenha(hashed)

    # toString
    def __str__(self):
        return f"Usuario [nome: '{self.nome}', login: '{self.login}', senha: '{self.senha}', dataCricao: '{self.dataCriacao}', status: '{self.statusAssociativo}']"

