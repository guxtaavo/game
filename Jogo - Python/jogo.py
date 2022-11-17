import pygame as pg
import sys
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_inicial import Menu
from tela_jogo import Tela_Jogo
from personagens import Personagens

# #PASSA PARA O JOGO A VARIAVEL DOS PERSONAGENS ESCOLHIDOS PELO USUARIO
p1 = TelaSelecao.p1
p2 = TelaSelecao.p2

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
        cena_historia = Menu(self.tela)
        cena_historia.rodar()
        tela_selecao = TelaSelecao(self.tela)
        tela_selecao.rodar()

        cena_selecao = TelaSelecao(self.tela)
        cena_selecao.rodar()

        # RECEBE OS JOGADORES E PASSA PARA O JOGO OS ATRIBUTOS DO PERSONAGENS
        # EX.: IMG, VIDA, VELOCIDADE...
        while True:
            jogadores = Tela_Jogo(self.tela, p1[0], p1[1], p1[2], self.tela, p2[0], p2[1], p2[2])
            jogadores.rodar()
            
    