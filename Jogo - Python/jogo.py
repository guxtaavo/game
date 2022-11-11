import pygame as pg
import sys
import os
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_inicial import CenaHistoria
from tela_jogo import Tela_Jogo


bruxa = ["img/bruxa.png", 6, 4]
elfo = ["img/elfo.png", 4, 5]
ogro = ["img/ogro.png", 10, 2]
principe = ["img/principe.png", 5, 5]

p1 = ogro
p2 = principe

class Jogo:
    def __init__(self):
        #INICIALIZANDO O PYGAME
        pg.init()
        #INICIALIZANDO PARA COLOCAR SOM DEPOIS
        pg.mixer.init()
        #INICIALIZANDO A TELA
        self.tela = pg.display.set_mode((ConfiJogo.ALTURA, ConfiJogo.LARGURA))
        #DEFININDO O NOME QUE VAI NA ABA QUE VAI SER ABERTA
        #self.carregar_arquivos()
        pg.display.set_caption(ConfiJogo.TITULO_JOGO)
        #INICIALIZA ONDE VAI SER DEFINIDO A TAXA DE FPS DO JOGO
        self.relogio = pg.time.Clock()
        #ENQUANTO O JOGO ESTIVER RODANDO = TRUE :::::: PARA O WHILE LOOP
        self.esta_rodando = True

    def rodar(self):
        #mostrando a cena inicial ((cena historia))
        cena_historia = CenaHistoria(self.tela)
        cena_historia.rodar()
    
        while True:
            jogadores = Tela_Jogo(self.tela, p1[0], p1[1], p1[2], self.tela, p2[0], p2[1], p2[2])
            jogadores.rodar()
            
    