from configjogo import ConfiJogo

class Auto_acao:
    def __init__(self):
        self.aumento_de_vida = 2

    def cura_p1(self):
        ConfiJogo.VIDA_P1 += self.aumento_de_vida
        if ConfiJogo.VIDA_P1 > 60:
            ConfiJogo.VIDA_P1 = 60

    
    def cura_p2(self):
        ConfiJogo.VIDA_P2 += self.aumento_de_vida
        if ConfiJogo.VIDA_P2 > 60:
            ConfiJogo.VIDA_P2 = 60