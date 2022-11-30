# CLASSE PARA AS CONDIGURAÇÕES PRINCIPAIS DO JOGO
import pygame as pg
from tela_selecao import TelaSelecao
from tela_selecao2 import TelaSelecao2

class ConfiJogo:
    ALTURA = 800
    LARGURA = 608
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    TITULO_JOGO = "The Kingdom"
    FPS = 60
    FONTE_HISTORIA = 30
    P1_POSICAO_X = 100
    P1_POSICAO_Y = 100
    P2_POSICAO_X = 400
    P2_POSICAO_Y = 400
    TAMANHO_BLOCO = 16
    IMAGEM_AGUA = pg.image.load("img/agua.png")
    IMAGEM_PEDRA = pg.image.load("img/pedra.png")
    IMAGEM_GRAMA = pg.image.load("img/grama.png")
    IMAGEM_MADEIRA = pg.image.load("img/madeira.png")
    DURACAO_PARTIDA = 90
    ALTURA_TEMPO = 20

    # PARA FAZER COM QUE A BARRA DE VIDA DO P1 FIQUE PROPORCIONAL
    x = int(60 / TelaSelecao.PLAYER1[1])
    VIDA_P1 = int(TelaSelecao.PLAYER1[1] * x)

    # PARA FAZER COM QUE A BARRA DE VIDA DO P2 FIQUE PROPORCIONAL
    y = int(60 / TelaSelecao2.PLAYER2[1])
    VIDA_P2 = int(TelaSelecao2.PLAYER2[1] * y)
