import math
import pygame as pg
from configjogo import ConfiJogo

class Ataque_em_area:
    def __init__(self, tela, rect_p1):
        self.tela = tela
        self.dano_area = 0.3
        self.rect_area = rect_p1
        self.rect_area2 = rect_p1
        self.rect_area.center = (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        self.alcance = 200

    def ataque_area_p1(self):
        if ConfiJogo.TAMANHO_LISTA == 3:
            self.delta_p1_minion = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P1_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P1_POSICAO_Y)**2))
            self.delta_p1_p2 = int(math.sqrt((ConfiJogo.P1_POSICAO_X - ConfiJogo.P2_POSICAO_X)**2 + (ConfiJogo.P1_POSICAO_Y - ConfiJogo.P2_POSICAO_Y)**2))
            if (self.delta_p1_p2 < self.delta_p1_minion) and self.delta_p1_p2 <= self.alcance:
                self.rect_area.center = (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
                ConfiJogo.VIDA_P2 -= self.dano_area
                pg.draw.rect(self.tela, (0,0,0), self.rect_area)

            elif (self.delta_p1_minion < self.delta_p1_p2) and self.delta_p1_minion <= self.alcance:
                self.rect_area.center = (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
                ConfiJogo.VIDA_MINION -= self.dano_area
                pg.draw.rect(self.tela, (0,0,0), self.rect_area)

            elif (self.delta_p1_minion == self.delta_p1_p2) and (self.delta_p1_minion,self.delta_p1_p2 <= self.alcance):
                self.rect_area.center = (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
                self.rect_area2.center = (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
                ConfiJogo.VIDA_P2 -= self.dano_area
                ConfiJogo.VIDA_MINION -= self.dano_area
                pg.draw.rect(self.tela, (0,0,0), self.rect_area)
                pg.draw.rect(self.tela, (0,0,0), self.rect_area2)
        elif self.delta_p1_p2 <= self.alcance:
            self.rect_area.center = (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
            ConfiJogo.VIDA_P2 -= self.dano_area
            pg.draw.rect(self.tela, (0,0,0), self.rect_area)

            
    def ataque_area_p2(self):
        if ConfiJogo.TAMANHO_LISTA == 3:
            self.delta_p2_minion = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P2_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P2_POSICAO_Y)**2))
            self.delta_p1_p2 = int(math.sqrt((ConfiJogo.P1_POSICAO_X - ConfiJogo.P2_POSICAO_X)**2 + (ConfiJogo.P1_POSICAO_Y - ConfiJogo.P2_POSICAO_Y)**2))
            if (self.delta_p1_p2 < self.delta_p2_minion) and self.delta_p1_p2 <= self.alcance:
                self.rect_area.center = (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
                ConfiJogo.VIDA_P1 -= self.dano_area
                pg.draw.rect(self.tela, (255,255,255), self.rect_area)

            elif (self.delta_p2_minion < self.delta_p1_p2) and self.delta_p2_minion <= self.alcance:
                self.rect_area.center = (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
                ConfiJogo.VIDA_MINION -= self.dano_area
                pg.draw.rect(self.tela, (255,255,255), self.rect_area)

            elif (self.delta_p2_minion == self.delta_p1_p2) and (self.delta_p2_minion,self.delta_p1_p2 <= self.alcance):
                self.rect_area.center = (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
                self.rect_area2.center = (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
                ConfiJogo.VIDA_P1 -= self.dano_area
                ConfiJogo.VIDA_MINION -= self.dano_area
                pg.draw.rect(self.tela, (255,255,255), self.rect_area)
                pg.draw.rect(self.tela, (255,255,255), self.rect_area2)
        elif self.delta_p1_p2 <= self.alcance:
            self.rect_area.center = (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
            ConfiJogo.VIDA_P1 -= self.dano_area
            pg.draw.rect(self.tela, (255,255,255), self.rect_area)