# ATAQUE CORPO A CORPO
import pygame as pg
import sys
from configjogo import ConfiJogo
from vida_jogador import Vida
from cronometro import Cronometro
import math


class Curta_Distancia:
        def __init__ (self, dano, x, y): #player entre dano e x;
            self.dano = dano
           # self.player = player
            self.tempo_recarga = 0
            self.x = x
            self.y = y


        def ataque_p1(self, tela): #alvo  #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            self.tela = tela
            if pg.key.get_pressed()[pg.K_e]:
                self.distanciap1p2 = math.sqrt(math.pow((ConfiJogo.P1_POSICAO_X - ConfiJogo.P2_POSICAO_X), 2)+math.pow((ConfiJogo.P1_POSICAO_Y - ConfiJogo.P2_POSICAO_Y), 2))
                self.distanciap1minion = math.sqrt(math.pow((ConfiJogo.P1_POSICAO_X - ConfiJogo.MINION_POSICAO_X), 2)+math.pow((ConfiJogo.P1_POSICAO_Y - ConfiJogo.MINION_POSICAO_Y), 2))
                if self.distanciap1p2 < 60:
                    ConfiJogo.VIDA_P2 -= self.dano
                    if ConfiJogo.ULTIMO_PASSO_P1 == "NORTE" or ConfiJogo.ULTIMO_PASSO_P1 == "SUL" or ConfiJogo.ULTIMO_PASSO_P1 == "LESTE" or ConfiJogo.ULTIMO_PASSO_P1 == "OESTE":
                        pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, ConfiJogo.LARGURA_P1, ConfiJogo.ALTURA_P1))
                elif self.distanciap1minion < 60:
                    ConfiJogo.VIDA_MINION -= self.dano
                    pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, ConfiJogo.LARGURA_P1, ConfiJogo.ALTURA_P1))


        def ataque_p2(self, tela):  #alvo #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            self.tela = tela
            if pg.key.get_pressed()[pg.K_p]:
                self.distanciap2p1 = math.sqrt(math.pow((ConfiJogo.P2_POSICAO_X - ConfiJogo.P1_POSICAO_X), 2)+math.pow((ConfiJogo.P2_POSICAO_Y - ConfiJogo.P1_POSICAO_Y), 2))
                self.distanciap2minion = math.sqrt(math.pow((ConfiJogo.P2_POSICAO_X - ConfiJogo.MINION_POSICAO_X), 2)+math.pow((ConfiJogo.P2_POSICAO_Y - ConfiJogo.MINION_POSICAO_Y), 2))
                if self.distanciap2p1 < 60:
                    ConfiJogo.VIDA_P1 -= self.dano
                    if ConfiJogo.ULTIMO_PASSO_P2 == "NORTE" or ConfiJogo.ULTIMO_PASSO_P2 == "SUL" or ConfiJogo.ULTIMO_PASSO_P2 == "LESTE" or ConfiJogo.ULTIMO_PASSO_P2 == "OESTE":
                        pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y, ConfiJogo.LARGURA_P2, ConfiJogo.ALTURA_P2))
                elif self.distanciap2minion < 60:
                    ConfiJogo.VIDA_MINION -= self.dano
                    pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y, ConfiJogo.LARGURA_P2, ConfiJogo.ALTURA_P2))