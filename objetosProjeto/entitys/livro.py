class Livro:
    # declaração do construtor da classe
    def __init__(self, titulo, autor, editora, anoLancamento, registrado, statusAssociativo):
        self.titulo = titulo
        self.autor = autor
        self.editor = editora
        self.anoLancamento = anoLancamento
        self.registrado = registrado
        self.statusAssociativo = statusAssociativo

    # definindo os g e s
    def getTitulo(self):
        return self.titulo
    def setTitulo(self, x):
        self.titulo= x
    
    def getAutor(self):
        return self.autor
    def setAutor(self, x):
        self.autor = x

    def getEditor(self):
        return self.editor
    def setEditor(self, x):
        self.editor = x
    
    def getAnoLancamento(self):
        return self.anoLancamento
    def setAnoLancamento(self, x):
        self.anoLancamento = x
    
    def getRegistrado(self):
        return self.registrado
    def setRegistrado(self, x):
        self.registrado = x
    
    def getStatusAssociativo(self):
        return self.statusAssociativo
    def setStatusAssociativo(self, x):
        self.statusAssociativo = x
    
    # toString
    def __str__(self):
        return f'''titulo: '{self.titulo}', autor: '{self.autor}', editor: '{self.editor}', lncamento: '{self.anoLancamento}', registrado: '{self.registrado}', status: '{self.statusAssociativo}' '''