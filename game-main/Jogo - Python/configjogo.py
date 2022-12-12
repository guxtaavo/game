# CLASSE PARA AS CONDIGURAÇÕES PRINCIPAIS DO JOGO
import pygame as pg
from tela_selecao import TelaSelecao
from tela_selecao2 import TelaSelecao2
import random
from personagens import Personagens

class ConfiJogo:
    ALTURA = 608
    LARGURA = 800
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    VERDE = (42, 130, 72)
    TITULO_JOGO = "The Kingdom"
    FPS = 60
    FONTE_HISTORIA = 30
    P1_POSICAO_X = 100
    P1_POSICAO_Y = 100
    P2_POSICAO_X = 400
    P2_POSICAO_Y = 400
    MINION_POSICAO_X = 560
    MINION_POSICAO_Y = 50
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

    # PARA FAZER COM QUE A BARRA DE VIDA DO MINION FIQUE PROPORCIONAL
    z = int(60 / Personagens.GUERREIRO[1])
    VIDA_MINION = int(Personagens.GUERREIRO[1] * z) 

    # SE ATUALIZARA COM 1 - NORTE, 2 - LESTE, 3 - SUL, 4 - OESTE
    ULTIMO_PASSO_P1 = 0
    ULTIMO_PASSO_P2 = 0

    LARGURA_P1 = 0
    ALTURA_P1 = 0
    LARGURA_P2 = 0
    ALTURA_P2 = 0
    LARGURA_P3 = 0
    ALTURA_P3 = 0
    
    VIDA_BLOCO_MADEIRA = 10

    VELOCIDADE_P1 = 0
    VELOCIDADE_P2 = 0
    VELOCIDADE_NPC = 0

    TAMANHO_LISTA = 0


    P1_DISPAROU = False
    P1_DISPARO_COLIDINDO = False
    DISPARO_P1_TELA = False
    X0_BALA_P1 = 100
    Y0_BALA_P1 = 100

    P2_DISPAROU = False
    P2_DISPARO_COLIDINDO = False
    DISPARO_P2_TELA = False
    X0_BALA_P2 = 400
    Y0_BALA_P2 = 400