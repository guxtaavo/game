import pygame as pg
import sys
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_selecao2 import TelaSelecao2
from tela_inicial import Menu
from tela_jogo import Tela_Jogo
from personagens import Personagens

# PASSA PARA O JOGO A VARIAVEL DOS PERSONAGENS ESCOLHIDOS PELO USUARIO
# p1 = TelaSelecao.PLAYER1
# p2 = TelaSelecao2.PLAYER2

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
        p1 = TelaSelecao.PLAYER1
        p2 = TelaSelecao2.PLAYER2

    def rodar(self):
        # MOSTRA A TELA INICIAL
        cena_historia = Menu(self.tela)
        cena_historia.rodar()

        # MOSTRA A TELA PRA ESCOLHER O P1
        tela_selecao = TelaSelecao(self.tela)
        tela_selecao.rodar()
        
        #MOSTRA A TELA PRA ESCOLHER O P2
        cena_selecao2 = TelaSelecao2(self.tela)
        cena_selecao2.rodar()

        #RECEBE OS PERSONAGENS ESCOLHIDOS PELOS JOGADORES
        p1 = TelaSelecao.PLAYER1
        p2 = TelaSelecao2.PLAYER2

        # RECEBE OS JOGADORES E PASSA PARA O JOGO OS ATRIBUTOS DO PERSONAGENS
        # EX.: IMG, VIDA, VELOCIDADE...
        while True:
            jogadores = Tela_Jogo(self.tela, p1[0], p1[1], p1[2], self.tela, p2[0], p2[1], p2[2])
            jogadores.rodar()
            
    