import pygame as pg
import sys
import os
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_inicial import CenaHistoria
from tela_jogo import Tela_Jogo

bruxa = ["img/bruxa.png", 6, 0.3]

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
            tela_jogo = Tela_Jogo(self.tela, bruxa[0], bruxa[1], bruxa[2])
            tela_jogo.rodar()
            