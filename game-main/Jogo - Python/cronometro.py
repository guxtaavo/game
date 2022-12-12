from time import time

#CLASSE UTILIZADA NA TELA_INICIAL PARA FAZER PISCAR O TEXTO
class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tempo_referencia = time()

    def tempo_passado(self):
        tempo_atual = time()
        return tempo_atual - self.tempo_referencia