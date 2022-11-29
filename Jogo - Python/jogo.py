import pygame as pg
import sys
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_selecao2 import TelaSelecao2
from tela_inicial import Menu
from tela_jogo import Tela_Jogo
from personagens import Personagens
from tela_historia import Tela_Historia
from tela_historia2 import Tela_Historia_2
from tela_vencedor import Tela_Vencedor

class Jogo:
    def __init__(self):
        #INICIALIZANDO O PYGAME
        pg.init()
        #INICIALIZANDO PARA COLOCAR SOM
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
        p1 = TelaSelecao.PLAYER1
        p2 = TelaSelecao2.PLAYER2

    def rodar(self):
        # DEFINE O VOLUME DA MÚSICA
        pg.mixer.music.set_volume(0.008)
        
        # PARA COLOCAR A MUSICA PARA RODAR
        musica = pg.mixer.music.load("sons/musica_fundo.mp3")
    
        # PARAMETRO (-1) PARA LOOP QUANDO ACABAR
        pg.mixer.music.play(-1)



        # MOSTRA A TELA INICIAL
        menu = Menu(self.tela)
        menu.rodar()

        # MOSTRA A TELA DE HISTORIA 1
        tela_historia = Tela_Historia(self.tela)
        tela_historia.rodar()

        # MOSTRA A TELA DE HISTORIA 2
        tela_historia2 = Tela_Historia_2(self.tela)
        tela_historia2.rodar()

        while True:
            pg.mixer.music.set_volume(0.008)
            # MOSTRA A TELA PRA ESCOLHER O P1
            tela_selecao = TelaSelecao(self.tela)
            tela_selecao.rodar()
            
            # MOSTRA A TELA PRA ESCOLHER O P2
            cena_selecao2 = TelaSelecao2(self.tela)
            cena_selecao2.rodar()

            # RECEBE OS PERSONAGENS ESCOLHIDOS PELOS JOGADORES
            p1 = TelaSelecao.PLAYER1
            p2 = TelaSelecao2.PLAYER2

            # RECEBE OS JOGADORES E PASSA PARA O JOGO OS ATRIBUTOS DO PERSONAGENS
            # EX.: IMG, VIDA, VELOCIDADE...
            jogo = Tela_Jogo(self.tela, p1[0], p1[1], p1[2], p1[3], p1[4], self.tela, p2[0], p2[1], p2[2], p2[3], p2[4])
            jogo.rodar()
            
            pg.mixer.music.set_volume(0)

            tela_vencedor = Tela_Vencedor(self.tela)
            tela_vencedor.rodar()
            
    