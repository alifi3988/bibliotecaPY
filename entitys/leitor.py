class Leitor:
    def __init__(self, nome, idade, cpf, email, telefone, cidade, uf, data) :
     self.nome = nome
     self.idade = idade 
     self.cpf = cpf  
     self.email = email 
     self.telefone = telefone
     self.cidade = cidade
     self.uf = uf
     self.data = data

    def getNome(self):
       return self.nome
    def setNome(self, nome):
       self.nome = nome
    
    def getIdade(self):
       return self.idade
    def setIdade (self, idade):
       self.idade = idade

    def getCpf(self):
       return self.cpf
    def setCpf(self, cpf):
       self.cpf = cpf

    def getEmail(self):
       return self.email
    def setEmail(self, email):
       self.email = email

    def getTelefone(self):
       return self.telefone
    def setTelefone(self, telefone):
       self.telefone = telefone
    

    def getCidade(self):
       return self.cidade
    def setCidade(self, cidade):
       self.cidade = cidade

    def getUf(self):
       return self.uf
    def setUf (self, uf):
       self.uf = uf

    def getData(self):
       return self.data
    def setData(self, data):
       self.data = data

