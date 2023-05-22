
class Retirada:
    def __init__(self, idLeitor, idLivro, dataRetirada, dataEntrega, estatusRetirada):
        self.idLeitor = idLeitor
        self.idLivro = idLivro
        self.dataRetirada = dataRetirada
        self.dataEntrega = dataEntrega
        self.statusRetirada = estatusRetirada
    
    def getIdLeitor(self):
        return self.idLeitor
    def setIdLeitor(self, x):
        self.idLeitor = x
    
    def getIdLivro(self):
        return self.idLivro
    def setIdLivro(self, x):
        self.idLivro = x
        
    def getDataRetirada(self):
        return self.dataRetirada
    def setDataRetirada(self, x):
        self.dataRetirada = x
        
    def getDataEntrega(self):
        return self.dataEntrega
    def setDataEntrega(self, x):
        self.dataEntrega = x
        
    def getStatusRetirada(self):
        return self.statusRetirada
    def setStatusRetirada(self, x):
        self.statusRetirada = x
    
    def __str__(self):
        return f'''{self.idLeitor}, {self.idLivro}, {self.dataRetirada}, {self.dataEntrega}, {self.statusRetirada}'''