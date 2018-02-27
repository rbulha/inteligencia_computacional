class balde:
    def __init__(self,capacidade):
        self.agua = 0
        self.capacidade = capacidade
    def enche(self,quantidade):
        if quantidade > self.capacidade:
            resto = quantidade - self.capacidade
            self.agua = self.capacidade
        else:
            resto =0
            self.agua = quantidade
        return resto
    def esvazia(sefl):
        self.agua = 0

b=[balde(4),balde(3)]

def solucao(b):
    if b[0].agua == 2:
    
