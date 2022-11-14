import pygame as pg
import sys
from configjogo import ConfiJogo

#CRIANDO CLASSE CENARIO
class Cenario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        #MATRIZ PARA REPRESENTAR O MAPA
        self.matriz = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]
    
    #PARA PINTAR O MAPA DE ACORDO COM O VALOR DEFINIDO NA MATRIZ COMO BLOCO
    #EX.: 1 SERIA A PAREDE E 0 O VAZIO AONDE O PERSONAGEM PODERIA SE MOVER
    def pintar_linha(self, tela, n_i, i):
        for n_j, j in enumerate(i):
            x = n_j * self.tamanho
            y = n_i * self.tamanho
            
            cor = ConfiJogo.PRETO

            if j == 1:
                cor = ConfiJogo.AZUL

            pg.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
    
    
    def pintar(self, tela):
        #ENUMERATE PEGA O INDICE DA MATRIZ
        for n_i, i in enumerate(self.matriz):
            self.pintar_linha(tela, n_i, i)
