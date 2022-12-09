# ATAQUE A DISTÂNCIA
import pygame as pg
import sys
from configjogo import ConfiJogo
from vida_jogador import Vida
from cronometro import Cronometro
import math


class Tiro:
        def __init__ (self, x_bala, y_bala, dano):  #com x sendo a px do personagem e y sendo a p2 do personagem
            self.x_bala = x_bala
            self.y_bala = y_bala
            
        def movimenta_disparo_p1(self):
            self.x_bala = ConfiJogo.P1_POSICAO_X + 10