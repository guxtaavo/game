# CLASSE PARA AS CONDIGURAÇÕES PRINCIPAIS DO JOGO
import pygame as pg

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