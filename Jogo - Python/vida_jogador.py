
import pygame as pg
import sys
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_selecao2 import TelaSelecao2

# CLASSE DA VIDA DO PERSONAGEM
class Vida:
    def __init__ (self ,posicao_x, posicao_y):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    # FUNÇÃO PARA DESENHAR A VIDA EM CIMA DO PERSONAGEM, BEM COMO FAZER DIMINUIR CASO SOFRA ALGUM DANO
    def desenha_vida(self, tela):

                                    #tela, cor, posicao, largura e altura.
        pg.draw.rect(tela, ((255, 0, 0)), (ConfiJogo.P1_POSICAO_X-9 , (ConfiJogo.P1_POSICAO_Y-15), ConfiJogo.VIDA_P1, 10))
        pg.draw.rect(tela, ((0, 0, 0)), (ConfiJogo.P1_POSICAO_X-9 , (ConfiJogo.P1_POSICAO_Y-15), 61 , 11), 2)

        # VARIAVEL VIDA E VIDA2 TEM QUE COMEÇAR SENDO == A 60 E DESCRESCER DE ACORDO COM O DANO
        pg.draw.rect(tela, ((255, 0, 0)), (ConfiJogo.P2_POSICAO_X-9 , (ConfiJogo.P2_POSICAO_Y-15), ConfiJogo.VIDA_P2, 10))
        pg.draw.rect(tela, ((0, 0, 0)), (ConfiJogo.P2_POSICAO_X-9 , (ConfiJogo.P2_POSICAO_Y-15), 61 , 11), 2)

        pg.display.flip()