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
    TITULO_JOGO = "Game"
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
    DURACAO_PARTIDA = 120
    ALTURA_TEMPO = 20

    # SEQUÊNCIA DE IF PARA FAZER COM QUE A BARRA FIQUE COM A LARGURA CORRETA E PROPORCIONAL
    if TelaSelecao.PLAYER1[1] == 12:
        VIDA_P1 = TelaSelecao.PLAYER1[1] * 5
    if TelaSelecao.PLAYER1[1] == 15:
        VIDA_P1 = TelaSelecao.PLAYER1[1] * 4
    if TelaSelecao.PLAYER1[1] == 20:
        VIDA_P1 = TelaSelecao.PLAYER1[1] * 3
    if TelaSelecao2.PLAYER2[1] == 12:
        VIDA_P2 = TelaSelecao2.PLAYER2[1] * 5
    if TelaSelecao2.PLAYER2[1] == 15:
        VIDA_P2 = TelaSelecao2.PLAYER2[1] * 4
    if TelaSelecao2.PLAYER2[1] == 20:
        VIDA_P2 = TelaSelecao2.PLAYER2[1] * 3
