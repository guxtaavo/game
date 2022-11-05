#JOGO EM PYTHON
import pygame as pg
import sys
from configjogo import ConfiJogo

class Jogo:
    def __init__(self):
        #INICIALIZANDO O PYGAME
        pg.init()
        #INICIALIZANDO PARA COLOCAR SOM DEPOIS
        pg.mixer.init()
        #INICIALIZANDO A TELA
        self.tela = pg.display.set_mode((ConfiJogo.ALTURA, ConfiJogo.LARGURA))
        #DEFININDO O NOME QUE VAI NA ABA QUE VAI SER ABERTA
        pg.display.set_caption(ConfiJogo.TITULO_JOGO)
        #INICIALIZA ONDE VAI SER DEFINIDO A TAXA DE FPS DO JOGO
        self.relogio = pg.time.Clock()
        #ENQUANTO O JOGO ESTIVER RODANDO = TRUE :::::: PARA O WHILE LOOP
        self.esta_rodando = True

game = Jogo()

while game.esta_rodando:

        #DEFININDO O FPS DO JOGO 
        game.relogio.tick(ConfiJogo.FPS)
        
        #KEYS = PARA ABREVIAR
        keys = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                keys[pg.K_ESCAPE]:
                    print("Encerrando o programa.")
                    sys.exit()

      
