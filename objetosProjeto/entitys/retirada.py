
class Retirada:
    def __init__(self, idLeitor, idLivro, dataRetirada, dataEntrega, estatusRetirada):
        self.idLeitor = idLeitor
        self.idLivro = idLivro
        self.dataRetirada = dataRetirada
        self.dataEntrega = dataEntrega
        self.statusRetirada = estatusRetirada
    
    def getIdLeitor(self):
        self.idLeitor
    def setIdLeitor(self, x):
        self.idLeitor = x
    
    def getIdLivro(self):
        self.idLivro
    def setIdLivro(self, x):
        self.idLivro = x
        
    def getDataRetirada(self):
        self.dataRetirada
    def setDataRetirada(self, x):
        self.dataRetirada = x
        
    def getDataEntrega(self):
        self.dataEntrega
    def setDataEntrega(self, x):
        self.dataEntrega = x
        
    def getStatusRetirada(self):
        self.statusRetirada
    def setStatusRetirada(self, x):
        self.statusRetirada = x
    
    def modificarStatus(self):
        self.statusRetirada = False
    
    def __str__(self):
        return f"{self.idLeitor}, {self.idLivro}, {self.dataRetirada}, {self.dataEntrega}, {self.estatusRetirada}"