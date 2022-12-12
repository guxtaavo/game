import pygame as pg
import sys
from configjogo import ConfiJogo
from vida_jogador import Vida
from cronometro import Cronometro
from ataque_curta import Curta_Distancia
import math

from ataque_em_area import Ataque_em_area
from auto_ação import Auto_acao

class Tela_Jogo:
    def __init__(self, tela, imagem, vida, velocidade, ataque_dist, ataque_melee, tela2, imagem2, vida2, velocidade2, ataque_dist2, \
        ataque_melee2, tela3, imagem3, vida3, velocidade3, ataque_dist3, ataque_melee3):
        self.relogio = pg.time.Clock()
        self.esta_rodando = True
        self.font_timer = pg.font.SysFont("sigmar one", 54)

        lista_rect = []

        #CRIANDO PRIMEIRO JOGADOR
        self.tela = tela
        self.imagem = pg.image.load(imagem)
        img = self.imagem
        
        self.vida = Vida(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        self.velocidade = velocidade
        ConfiJogo.VELOCIDADE_P1 = velocidade
        self.ataque_dist = ataque_dist
        self.ataque_melee = ataque_melee
        self.largura_imagem = img.get_rect().width
        ConfiJogo.LARGURA_P1 = self.largura_imagem
        self.altura_imagem = img.get_rect().height
        ConfiJogo.ALTURA_P1 = self.altura_imagem
        self.rect1 = img.get_rect()
        lista_rect.append(self.rect1)
        self.pos_atual_xp1 = 0
        self.pos_atual_yp1 = 0
        self.balas_p1 = []
        self.ultimo_disparo_p1 = None
        self.ataque_melee = ataque_melee
        self.ataque_area = Ataque_em_area(self.tela, self.rect1)
        self.auto_acao = Auto_acao()

        self.disparop1 = pg.draw.rect(self.tela, ((0,0,0)), (ConfiJogo.X0_BALA_P1, ConfiJogo.Y0_BALA_P1, 10, 10))
        self.contador_p1 = 0
        


        #CRIANDO O SEGUNDO JOGADOR
        self.tela2 = tela2
        self.imagem2 = pg.image.load(imagem2)
        img2 = self.imagem2
        self.vida2 = Vida(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        self.velocidade2 = velocidade2
        ConfiJogo.VELOCIDADE_P2 = velocidade2
        self.ataque_dist2 = ataque_dist2
        self.ataque_melee2 = ataque_melee2
        self.largura_imagem2 = img2.get_rect().width
        ConfiJogo.LARGURA_P2 = self.largura_imagem2
        self.altura_imagem2 = img2.get_rect().height
        ConfiJogo.ALTURA_P2 = self.altura_imagem2
        self.rect2 = img2.get_rect()
        lista_rect.append(self.rect2)

        self.disparop2 = pg.draw.rect(self.tela, ((0,0,0)), (ConfiJogo.X0_BALA_P2, ConfiJogo.Y0_BALA_P2, 10, 10))
        self.contador_p2 = 0
        
  
        #CRIANDO O MINION 
        self.tela3 = tela3
        self.imagem3 = pg.image.load(imagem3)
        img3 = self.imagem3
        self.vida3 = Vida(ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
        self.velocidade3 = velocidade3
        self.ataque_dist3 = ataque_dist3
        self.ataque_melee3 = ataque_melee3
        self.largura_imagem3 = img3.get_rect().width
        ConfiJogo.LARGURA_P3 = self.largura_imagem3
        self.altura_imagem3 = img3.get_rect().height
        ConfiJogo.ALTURA_P3 = self.altura_imagem3
        self.rect3 = img3.get_rect()
        lista_rect.append(self.rect3)
        ConfiJogo.VELOCIDADE_NPC = self.velocidade3


        # VARIAVEIS UTILIZADAS PARA FAZER O IF DE COLISÃO
        self.lista_rect = lista_rect
        tamanho_lista = len(lista_rect)
        ConfiJogo.TAMANHO_LISTA = tamanho_lista
        

        #CONFIG PARA O ATAQUE CORPO A CORPO
        self.ataque_p1 = Curta_Distancia(ataque_melee, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        self.ataque_p2 = Curta_Distancia(ataque_melee2, ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        if ConfiJogo.VIDA_MINION >= 0:
            self.ataque_p3 = Curta_Distancia(ataque_melee3, ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y)
        

        # UTILIZADO PARA FAZER O CRONOMETRO DO JOGO
        self.cronometro = Cronometro()

        #UTILIZADO PARA FAZER O MAPA DO JOGO
        self.tamanho_bloco = ConfiJogo.TAMANHO_BLOCO
        self.cenario = (ConfiJogo.TAMANHO_BLOCO, self.tela)
        self.matriz = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]

    #FUNÇÃO PARA PINTAR O FUNDO DA TELA DO JOGO DE ACORDO COM A MATRIZ
    def pintar_cenario(self, tela):
        for linha in range (len(self.matriz)):
            for coluna in range (len(self.matriz[linha])):
                px = coluna * self.tamanho_bloco
                py = linha * self.tamanho_bloco

                if self.matriz[linha][coluna] == 0:
                    img = ConfiJogo.IMAGEM_GRAMA
                elif self.matriz[linha][coluna] == 1:
                    img = ConfiJogo.IMAGEM_PEDRA
                elif self.matriz[linha][coluna] == 2:
                    img = ConfiJogo.IMAGEM_MADEIRA
                elif self.matriz[linha][coluna] == 3:
                    img = ConfiJogo.IMAGEM_AGUA


                tela.blit(img, (px, py, self.tamanho_bloco, self.tamanho_bloco))

    # FUNÇÃO PARA RODAR O JOGO
    def rodar(self):
            while self.esta_rodando:
                self.pintar_cenario(self.tela)
                self.desenha()
                self.tratamento_de_eventos()
                if ConfiJogo.P1_DISPAROU == True and not ConfiJogo.P1_DISPARO_COLIDINDO == True:
                    Tiro.movimenta_disparo_p1(self)
                self.colisao_disparo_p1()
                self.colisao_disparo_p1_npc()

                if ConfiJogo.P2_DISPAROU == True and not ConfiJogo.P2_DISPARO_COLIDINDO == True:
                    Tiro.movimenta_disparo_p2(self)
                self.colisao_disparo_p2()
                self.colisao_disparo_p2_npc()
                pg.display.flip()
                if ConfiJogo.VIDA_P1 <= 0 or ConfiJogo.VIDA_P2 <= 0:
                    self.esta_rodando = False

    # FUNÇÃO PARA DESENHAR AS IMAGENS NA TELA
    def desenha(self):
        self.coloca_imagem_tela(self.tela)
        self.vida.desenha_vida(self.tela)
        self.vida2.desenha_vida(self.tela)
        if ConfiJogo.VIDA_MINION > 0:
            self.vida3.desenha_vida(self.tela)

        if ConfiJogo.P1_DISPAROU == True:
            self.desenha_balas_p1(self.tela)
            ConfiJogo.DISPARO_P1_TELA = True
        if ConfiJogo.P2_DISPAROU == True:
            self.desenha_balas_p2(self.tela)
            ConfiJogo.DISPARO_P2_TELA = True
        
        pg.display.flip()
        


    def desenha_balas_p1(self, tela):
        self.disparop1 = pg.draw.rect(self.tela, ((0,0,0)), (ConfiJogo.X0_BALA_P1, ConfiJogo.Y0_BALA_P1, 10, 10))
        pg.display.flip()


    def disparo_p1(self, x, y, dano):
        
        (Tiro(x, y, dano))

    def colisao_disparo_p1(self):
        if self.disparop1.colliderect(self.rect2) == True:
            
            
            if self.contador_p1 < 2:
                ConfiJogo.VIDA_P2 -= 2*self.ataque_dist
            ConfiJogo.P1_DISPARO_COLIDINDO = True
            #ConfiJogo.DISPARO_P1_TELA = False
            self.contador_p1 = self.contador_p1 + 1
            #self.disparo_p1_tela = False
            # 
       
    def colisao_disparo_p1_npc(self):
        if self.disparop1.colliderect(self.rect3) == True:
            
            
            if self.contador_p1 < 2:
                ConfiJogo.VIDA_MINION -= 2*self.ataque_dist
            ConfiJogo.P1_DISPARO_COLIDINDO = True
            #ConfiJogo.DISPARO_P1_TELA = False
            self.contador_p1 = self.contador_p1 + 1
            #self.disparo_p1_tela = False
            # 

    def desenha_balas_p2(self, tela):
        self.disparop2 = pg.draw.rect(self.tela, ((0,0,0)), (ConfiJogo.X0_BALA_P2, ConfiJogo.Y0_BALA_P2, 10, 10))
        pg.display.flip()


    def disparo_p2(self, x, y, dano):
        
        (Tiro(x, y, dano))



    def colisao_disparo_p2_npc(self):
        if self.disparop2.colliderect(self.rect3) == True:
            
            
            if self.contador_p2 < 2:
                ConfiJogo.VIDA_MINION -= 2*self.ataque_dist2
            ConfiJogo.P2_DISPARO_COLIDINDO = True
            #ConfiJogo.DISPARO_P1_TELA = False
            self.contador_p2 = self.contador_p2 + 1
            #self.disparo_p1_tela = False
            # 





    def colisao_disparo_p2(self):
        if self.disparop2.colliderect(self.rect1) == True:
            
            
            if self.contador_p2 < 2:
                ConfiJogo.VIDA_P1 -= 2*self.ataque_dist2
            ConfiJogo.P2_DISPARO_COLIDINDO = True
            #ConfiJogo.DISPARO_P1_TELA = False
            self.contador_p2 = self.contador_p2 + 1
            #self.disparo_p1_tela = False   
    


    
    
    
    
    
    
    
    
    
    
    
    
    # FUNÇÃO PARA VERIFICAR O TEMPO DO JOGO
    def jogo_terminou(self):
        if (self.cronometro.tempo_passado() > ConfiJogo.DURACAO_PARTIDA):
            return True
        else:
            return False

    # FUNÇÃO PARA DESENHAR OS PERSONAGENS NA TELA
    def coloca_imagem_tela(self, tela):
        self.rect1 = tela.blit(self.imagem, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y))
        self.rect2 = tela.blit(self.imagem2, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y))
        if ConfiJogo.VIDA_MINION > 0:
            self.rect3 = tela.blit(self.imagem3, (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y))
        else:
            self.rect3 = None
        

        # CONFG PASSADAS PARA O CRONOMETRO IR ABAIXANDO E DEFINIÇÕES DE POSICIONAMENTO
        tempo = ConfiJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        timer = self.font_timer.render(f"{tempo:.0f}", True, ConfiJogo.PRETO)
        tela.blit(timer, (ConfiJogo.ALTURA//2 + 72, 20))


    # FUNÇÃO QUE TRATA OS EVENTOS DO JOGO, COMO A MOVIMENTAÇÃO DOS PERSONAGENS
    def tratamento_de_eventos(self):
        self.relogio.tick(60)

        for event in pg.event.get():
            
            #PARA SAIR DO JOGO
            if pg.key.get_pressed()[pg.K_ESCAPE] or event.type == pg.QUIT:
                sys.exit()

            
            # EVENTO PARA GARANTIR O TÉRMINO DO JOGO AO FIM DO TEMPO DO CRONOMETRO
            if self.jogo_terminou() == True:
                self.esta_rodando = False
            
            # CONDICIONAL PARA REMOVER DA LISTA O MINION CASO FOSSE MORTO
            if ConfiJogo.VIDA_MINION <= 0 and ConfiJogo.TAMANHO_LISTA == 3:
                self.lista_rect.pop()
                ConfiJogo.TAMANHO_LISTA = 2
                
        
            # CALCULA A DISTANCIA DE CADA PERSOANGEM PARA O NPC
            d1 = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P1_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P1_POSICAO_Y)**2))
            d2 = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P2_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P2_POSICAO_Y)**2))

            # CONDICIONAIS PARA FAZER O MINION SE MOVER EM DIREÇÃO AO PERSONAGEM MAIS PERTO
            if ConfiJogo.VIDA_MINION > 0:
                if d2 > d1:
                    if ConfiJogo.P1_POSICAO_Y < ConfiJogo.MINION_POSICAO_Y:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y - self.velocidade3, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        altura = self.altura_imagem3
                        largura = self.largura_imagem3
                        if ((self.matriz[(y - self.velocidade3)//16][x//16] == 3) or \
                            (self.matriz[(y - self.velocidade3)//16][(x + largura)//16] == 3) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][x//16] == 3) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][(x + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[(y - self.velocidade3)//16][x//16] == 1) or \
                            (self.matriz[(y - self.velocidade3)//16][(x + largura)//16] == 1) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][x//16] == 1) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][(x + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_Y -= self.velocidade3


                    if ConfiJogo.P1_POSICAO_Y > ConfiJogo.MINION_POSICAO_Y:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y + self.velocidade3, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        altura = self.altura_imagem3
                        largura = self.largura_imagem3
                        if ((self.matriz[(y + self.velocidade3)//16][x//16] == 3) or \
                            (self.matriz[(y + self.velocidade3)//16][(x + largura)//16] == 3) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][x//16] == 3) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][(x + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[(y + self.velocidade3)//16][x//16] == 1) or \
                            (self.matriz[(y + self.velocidade3)//16][(x + largura)//16] == 1) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][x//16] == 1) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][(x + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_Y += self.velocidade3

                    if ConfiJogo.MINION_POSICAO_X < ConfiJogo.P1_POSICAO_X:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X + self.velocidade3, ConfiJogo.MINION_POSICAO_Y, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        largura = self.largura_imagem3
                        altura = self.altura_imagem3
                        if ((self.matriz[y//16][(x + self.velocidade3)//16] == 3) or \
                            (self.matriz[(y + largura)//16][(x + self.velocidade3)//16] == 3) or \
                            (self.matriz[y//16][(x + self.velocidade3 + largura)//16] == 3) or \
                            (self.matriz[(y + altura)//16][(x + self.velocidade3 + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[y//16][(x + self.velocidade3)//16] == 1) or \
                            (self.matriz[(y + largura)//16][(x + self.velocidade3)//16] == 1) or \
                            (self.matriz[y//16][(x + self.velocidade3 + largura)//16] == 1) or \
                            (self.matriz[(y + altura)//16][(x + self.velocidade3 + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_X += self.velocidade3
                    
                    if ConfiJogo.MINION_POSICAO_X > ConfiJogo.P1_POSICAO_X:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X - self.velocidade3, ConfiJogo.MINION_POSICAO_Y, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        largura = self.largura_imagem3
                        altura = self.altura_imagem3
                        if ((self.matriz[y//16][(x - self.velocidade3)//16] == 3) or \
                            (self.matriz[(y + largura)//16][(x - self.velocidade3)//16] == 3) or \
                            (self.matriz[y//16][(x - self.velocidade3 + largura)//16] == 3) or \
                            (self.matriz[(y + altura)//16][(x - self.velocidade3 + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[y//16][(x - self.velocidade3)//16] == 1) or \
                            (self.matriz[(y + largura)//16][(x - self.velocidade3)//16] == 1) or \
                            (self.matriz[y//16][(x - self.velocidade3 + largura)//16] == 1) or \
                            (self.matriz[(y + altura)//16][(x - self.velocidade3 + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_X -= self.velocidade3

                else:
                    if ConfiJogo.P2_POSICAO_Y < ConfiJogo.MINION_POSICAO_Y:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y - self.velocidade3, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        altura = self.altura_imagem3
                        largura = self.largura_imagem3
                        if ((self.matriz[(y - self.velocidade3)//16][x//16] == 3) or \
                            (self.matriz[(y - self.velocidade3)//16][(x + largura)//16] == 3) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][x//16] == 3) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][(x + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[(y - self.velocidade3)//16][x//16] == 1) or \
                            (self.matriz[(y - self.velocidade3)//16][(x + largura)//16] == 1) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][x//16] == 1) or \
                            (self.matriz[(y - self.velocidade3 + altura)//16][(x + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_Y -= self.velocidade3


                    if ConfiJogo.P2_POSICAO_Y > ConfiJogo.MINION_POSICAO_Y:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y + self.velocidade3, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        altura = self.altura_imagem3
                        largura = self.largura_imagem3
                        if ((self.matriz[(y + self.velocidade3)//16][x//16] == 3) or \
                            (self.matriz[(y + self.velocidade3)//16][(x + largura)//16] == 3) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][x//16] == 3) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][(x + largura)//16] == 3)):
                                self.velocidade = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[(y + self.velocidade3)//16][x//16] == 1) or \
                            (self.matriz[(y + self.velocidade3)//16][(x + largura)//16] == 1) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][x//16] == 1) or \
                            (self.matriz[(y + self.velocidade3 + altura)//16][(x + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_Y += self.velocidade3

                    if ConfiJogo.MINION_POSICAO_X < ConfiJogo.P2_POSICAO_X:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X + self.velocidade3, ConfiJogo.MINION_POSICAO_Y, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        largura = self.largura_imagem3
                        altura = self.altura_imagem3
                        if ((self.matriz[y//16][(x + self.velocidade3)//16] == 3) or \
                            (self.matriz[(y + largura)//16][(x + self.velocidade3)//16] == 3) or \
                            (self.matriz[y//16][(x + self.velocidade3 + largura)//16] == 3) or \
                            (self.matriz[(y + altura)//16][(x + self.velocidade3 + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[y//16][(x + self.velocidade3)//16] == 1) or \
                            (self.matriz[(y + largura)//16][(x + self.velocidade3)//16] == 1) or \
                            (self.matriz[y//16][(x + self.velocidade3 + largura)//16] == 1) or \
                            (self.matriz[(y + altura)//16][(x + self.velocidade3 + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_X += self.velocidade3
                    
                    if ConfiJogo.MINION_POSICAO_X > ConfiJogo.P2_POSICAO_X:
                        self.rect3_teste = pg.Rect(ConfiJogo.MINION_POSICAO_X - self.velocidade3, ConfiJogo.MINION_POSICAO_Y, self.largura_imagem3, self.altura_imagem3)
                        x = ConfiJogo.MINION_POSICAO_X
                        y = ConfiJogo.MINION_POSICAO_Y
                        largura = self.largura_imagem3
                        altura = self.altura_imagem3
                        if ((self.matriz[y//16][(x - self.velocidade3)//16] == 3) or \
                            (self.matriz[(y + largura)//16][(x - self.velocidade3)//16] == 3) or \
                            (self.matriz[y//16][(x - self.velocidade3 + largura)//16] == 3) or \
                            (self.matriz[(y + altura)//16][(x - self.velocidade3 + largura)//16] == 3)):
                                self.velocidade3 = 1
                        if self.rect3_teste.colliderect(self.rect1) == False and self.rect3_teste.colliderect(self.rect2) == False\
                            and not ((self.matriz[y//16][(x - self.velocidade3)//16] == 1) or \
                            (self.matriz[(y + largura)//16][(x - self.velocidade3)//16] == 1) or \
                            (self.matriz[y//16][(x - self.velocidade3 + largura)//16] == 1) or \
                            (self.matriz[(y + altura)//16][(x - self.velocidade3 + largura)//16] == 1)):
                                ConfiJogo.MINION_POSICAO_X -= self.velocidade3

           
            # CHAMANDANDO OS ATAQUES PARA TELA
            self.ataque_p1.ataque_p1(self.tela)
            self.ataque_p2.ataque_p2(self.tela2)
            if ConfiJogo.VIDA_MINION > 0:
                self.ataque_p3.ataque_p3(self.tela3)
            

            # PARA REDEFINIR A VELOCIDA QUANDO SAIR DO BLOCO DE LENTIDAO (ÁGUA)
            self.velocidade = ConfiJogo.VELOCIDADE_P1
            self.velocidade2 = ConfiJogo.VELOCIDADE_P2
            self.velocidade3 = ConfiJogo.VELOCIDADE_NPC

            # PARA MOVIMENTAR O JOGADOR 1
            if pg.key.get_pressed()[pg.K_w]:
                x = ConfiJogo.P1_POSICAO_X
                y = ConfiJogo.P1_POSICAO_Y
                largura = self.largura_imagem
                altura = self.altura_imagem
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y-self.velocidade, self.largura_imagem, self.altura_imagem)
                if ((self.matriz[(y - self.velocidade)//16][x//16] == 3) or \
                    (self.matriz[(y - self.velocidade)//16][(x + largura)//16] == 3) or \
                    (self.matriz[(y - self.velocidade + altura)//16][x//16] == 3) or \
                    (self.matriz[(y - self.velocidade + altura)//16][(x + largura)//16] == 3)):
                    self.velocidade = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect1_teste.colliderect(self.rect2) == False and self.rect1_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[(y - self.velocidade)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y - self.velocidade + altura)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade + altura)//16][(x + largura)//16] == 1)):
                            ConfiJogo.P1_POSICAO_Y -= self.velocidade
                            
                            if ConfiJogo.P1_DISPAROU == False:
                                ConfiJogo.Y0_BALA_P1 = ConfiJogo.Y0_BALA_P1 - self.velocidade
                else:
                    if self.rect1_teste.colliderect(self.rect2) == False\
                        and not ((self.matriz[(y - self.velocidade)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y - self.velocidade + altura)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade + altura)//16][(x + largura)//16] == 1)):
                            ConfiJogo.P1_POSICAO_Y -= self.velocidade
                            ConfiJogo.ULTIMO_PASSO_P1 = "NORTE"
                                
            if pg.key.get_pressed()[pg.K_s]:
                x = ConfiJogo.P1_POSICAO_X
                y = ConfiJogo.P1_POSICAO_Y
                largura = self.largura_imagem
                altura = self.altura_imagem
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y + self.velocidade, self.largura_imagem, self.altura_imagem)
                if ((self.matriz[(y + self.velocidade)//16][x//16] == 3) or \
                    (self.matriz[(y + self.velocidade)//16][(x + largura)//16] == 3) or \
                    (self.matriz[(y + self.velocidade + altura)//16][x//16] == 3) or \
                    (self.matriz[(y + self.velocidade + altura)//16][(x + largura)//16] == 3)):
                    self.velocidade = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect1_teste.colliderect(self.rect2) == False and self.rect1_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[(y + self.velocidade)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y + self.velocidade + altura)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_Y += self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "SUL"

                        if ConfiJogo.P1_DISPAROU == False:
                            ConfiJogo.Y0_BALA_P1 = ConfiJogo.Y0_BALA_P1 + self.velocidade

                else:
                    if self.rect1_teste.colliderect(self.rect2) == False\
                        and not ((self.matriz[(y + self.velocidade)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y + self.velocidade + altura)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_Y += self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "SUL"
                        

            if pg.key.get_pressed()[pg.K_d]:
                x = ConfiJogo.P1_POSICAO_X
                y = ConfiJogo.P1_POSICAO_Y
                largura = self.largura_imagem
                altura = self.altura_imagem
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X+self.velocidade, ConfiJogo.P1_POSICAO_Y, self.largura_imagem, self.altura_imagem)
                if ((self.matriz[y//16][(x + self.velocidade)//16] == 3) or \
                    (self.matriz[(y + largura)//16][(x + self.velocidade)//16] == 3) or \
                    (self.matriz[y//16][(x + self.velocidade + largura)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x + self.velocidade + largura)//16] == 3)):
                    self.velocidade = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect1_teste.colliderect(self.rect2) == False and self.rect1_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[y//16][(x + self.velocidade)//16] == 1) or \
                        (self.matriz[(y + largura)//16][(x + self.velocidade)//16] == 1) or \
                        (self.matriz[y//16][(x + self.velocidade + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_X += self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "LESTE"

                        if ConfiJogo.P1_DISPAROU == False:
                            ConfiJogo.X0_BALA_P1 = ConfiJogo.X0_BALA_P1 + self.velocidade
                else:
                    if self.rect1_teste.colliderect(self.rect2) == False\
                        and not ((self.matriz[y//16][(x + self.velocidade)//16] == 1) or \
                        (self.matriz[(y + largura)//16][(x + self.velocidade)//16] == 1) or \
                        (self.matriz[y//16][(x + self.velocidade + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_X += self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "LESTE"
                    
            if pg.key.get_pressed()[pg.K_a]:
                x = ConfiJogo.P1_POSICAO_X
                y = ConfiJogo.P1_POSICAO_Y
                largura = self.largura_imagem
                altura = self.altura_imagem
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X-self.velocidade, ConfiJogo.P1_POSICAO_Y, self.largura_imagem, self.altura_imagem)
                if ((self.matriz[y//16][(x- self.velocidade)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade)//16] == 3) or \
                    (self.matriz[y//16][(x - self.velocidade + largura)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade + largura)//16] == 3)):
                    self.velocidade = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect1_teste.colliderect(self.rect2) == False and self.rect1_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[y//16][(x- self.velocidade)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade)//16] == 1) or \
                        (self.matriz[y//16][(x - self.velocidade + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_X -= self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "OESTE"
                       
                        if ConfiJogo.P1_DISPAROU == False:
                            ConfiJogo.X0_BALA_P1 = ConfiJogo.X0_BALA_P1 - self.velocidade
                else:
                    if self.rect1_teste.colliderect(self.rect2) == False\
                        and not ((self.matriz[y//16][(x- self.velocidade)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade)//16] == 1) or \
                        (self.matriz[y//16][(x - self.velocidade + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade + largura)//16] == 1)):
                        ConfiJogo.P1_POSICAO_X -= self.velocidade
                        ConfiJogo.ULTIMO_PASSO_P1 = "OESTE"

            if pg.key.get_pressed()[pg.K_f] and not ConfiJogo.P1_DISPAROU == True:   #necessário checar  o tempo.
                Tela_Jogo.disparo_p1(self, ConfiJogo.X0_BALA_P1, ConfiJogo.Y0_BALA_P1, 5)
                ConfiJogo.P1_DISPAROU = True
                          
            


            # PARA MOVIMENTAR O JOGADOR 2
            if pg.key.get_pressed()[pg.K_i]:
                x = ConfiJogo.P2_POSICAO_X
                y = ConfiJogo.P2_POSICAO_Y
                largura = self.largura_imagem2
                altura = self.altura_imagem2
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y - self.velocidade2, self.largura_imagem2, self.altura_imagem2)
                if ((self.matriz[(y - self.velocidade2)//16][x//16] == 3) or \
                    (self.matriz[(y - self.velocidade2)//16][(x + largura)//16] == 3) or \
                    (self.matriz[(y - self.velocidade2 + altura)//16][x//16] == 3) or \
                    (self.matriz[(y - self.velocidade2 + altura)//16][(x + largura)//16] == 3)):
                    self.velocidade2 = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect2_teste.colliderect(self.rect1) == False and self.rect2_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[(y - self.velocidade2)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade2)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y - self.velocidade2 + altura)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade2 + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_Y -= self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "NORTE"

                        if ConfiJogo.P2_DISPAROU == False:
                                ConfiJogo.Y0_BALA_P2 = ConfiJogo.Y0_BALA_P2 - self.velocidade
                else:
                    if self.rect2_teste.colliderect(self.rect1) == False\
                        and not ((self.matriz[(y - self.velocidade2)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade2)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y - self.velocidade2 + altura)//16][x//16] == 1) or \
                        (self.matriz[(y - self.velocidade2 + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_Y -= self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "NORTE"
                    
            if pg.key.get_pressed()[pg.K_k]:
                x = ConfiJogo.P2_POSICAO_X
                y = ConfiJogo.P2_POSICAO_Y
                largura = self.largura_imagem2
                altura = self.altura_imagem2
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y+self.velocidade2, self.largura_imagem2, self.altura_imagem2)
                if ((self.matriz[(y + self.velocidade2)//16][x//16] == 3) or \
                    (self.matriz[(y + self.velocidade2)//16][(x + largura)//16] == 3) or \
                    (self.matriz[(y + self.velocidade2 + altura)//16][x//16] == 3) or \
                    (self.matriz[(y + self.velocidade2 + altura)//16][(x + largura)//16] == 3)):
                    self.velocidade2 = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect2_teste.colliderect(self.rect1) == False and self.rect2_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[(y + self.velocidade2)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade2)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y + self.velocidade2 + altura)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade2 + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_Y += self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "SUL"

                        if ConfiJogo.P2_DISPAROU == False:
                                ConfiJogo.Y0_BALA_P2 = ConfiJogo.Y0_BALA_P2 + self.velocidade
                else:
                    if self.rect2_teste.colliderect(self.rect1) == False\
                        and not ((self.matriz[(y + self.velocidade2)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade2)//16][(x + largura)//16] == 1) or \
                        (self.matriz[(y + self.velocidade2 + altura)//16][x//16] == 1) or \
                        (self.matriz[(y + self.velocidade2 + altura)//16][(x + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_Y += self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "SUL"

            if pg.key.get_pressed()[pg.K_l]:
                x = ConfiJogo.P2_POSICAO_X
                y = ConfiJogo.P2_POSICAO_Y
                largura = self.largura_imagem2
                altura = self.altura_imagem2
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X+self.velocidade2, ConfiJogo.P2_POSICAO_Y, self.largura_imagem2, self.altura_imagem2)
                if ((self.matriz[y//16][(x + self.velocidade2)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x + self.velocidade2)//16] == 3) or \
                    (self.matriz[y//16][(x + self.velocidade2 + largura)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x + self.velocidade2 + largura)//16] == 3)):
                    self.velocidade2 = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect2_teste.colliderect(self.rect1) == False and self.rect2_teste.colliderect(self.rect3) == False\
                        and not((self.matriz[y//16][(x + self.velocidade2)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade2)//16] == 1) or \
                        (self.matriz[y//16][(x + self.velocidade2 + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade2 + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_X += self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "LESTE"

                        if ConfiJogo.P2_DISPAROU == False:
                            ConfiJogo.X0_BALA_P2 = ConfiJogo.X0_BALA_P2 + self.velocidade
                else:
                    if self.rect2_teste.colliderect(self.rect1) == False\
                        and not((self.matriz[y//16][(x + self.velocidade2)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade2)//16] == 1) or \
                        (self.matriz[y//16][(x + self.velocidade2 + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x + self.velocidade2 + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_X += self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "LESTE"

            if pg.key.get_pressed()[pg.K_j]:
                x = ConfiJogo.P2_POSICAO_X
                y = ConfiJogo.P2_POSICAO_Y
                largura = self.largura_imagem2
                altura = self.altura_imagem2
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X-self.velocidade2, ConfiJogo.P2_POSICAO_Y, self.largura_imagem2, self.altura_imagem2)
                if ((self.matriz[y//16][(x- self.velocidade2)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade2)//16] == 3) or \
                    (self.matriz[y//16][(x - self.velocidade2 + largura)//16] == 3) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade2 + largura)//16] == 3)):
                    self.velocidade2 = 1
                if ConfiJogo.TAMANHO_LISTA == 3:
                    if self.rect2_teste.colliderect(self.rect1) == False and self.rect2_teste.colliderect(self.rect3) == False\
                        and not ((self.matriz[y//16][(x- self.velocidade2)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade2)//16] == 1) or \
                        (self.matriz[y//16][(x - self.velocidade2 + largura)//16] == 1) or \
                        (self.matriz[(y + altura)//16][(x - self.velocidade2 + largura)//16] == 1)):
                        ConfiJogo.P2_POSICAO_X -= self.velocidade2
                        ConfiJogo.ULTIMO_PASSO_P2 = "OESTE"

                        if ConfiJogo.P2_DISPAROU == False:
                            ConfiJogo.X0_BALA_P2 = ConfiJogo.X0_BALA_P2 - self.velocidade
                else:
                    if self.rect2_teste.colliderect(self.rect1) == False\
                    and not ((self.matriz[y//16][(x- self.velocidade2)//16] == 1) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade2)//16] == 1) or \
                    (self.matriz[y//16][(x - self.velocidade2 + largura)//16] == 1) or \
                    (self.matriz[(y + altura)//16][(x - self.velocidade2 + largura)//16] == 1)):
                      ConfiJogo.P2_POSICAO_X -= self.velocidade2
                    ConfiJogo.ULTIMO_PASSO_P2 = "OESTE"


            if pg.key.get_pressed()[pg.K_p] and not ConfiJogo.P2_DISPAROU == True:   #necessário checar  o tempo.
                Tela_Jogo.disparo_p2(self, ConfiJogo.X0_BALA_P2, ConfiJogo.Y0_BALA_P2, 5)
                ConfiJogo.P2_DISPAROU = True       

            # ATAQUE EM AREA JOGADOR 1
            if pg.key.get_pressed()[pg.K_z]:
                self.ataque_area.ataque_area_p1()

            # ATAQUE EM AREA JOGADOR 2
            if pg.key.get_pressed()[pg.K_n]:
                self.ataque_area.ataque_area_p2()

            #AUTO-AÇÃO JOGADOR 1
            if pg.key.get_pressed()[pg.K_x]:
                self.auto_acao.cura_p1()

            #AUTO-AÇÃO JOGADOR 2
            if pg.key.get_pressed()[pg.K_m]:
                self.auto_acao.cura_p2()   

            pg.display.flip()

class Tiro:
        def __init__ (self, x0_bala, y0_bala, dano):  #com x sendo a px do personagem e y sendo a p2 do personagem

            self.x0_bala = x0_bala
            self.y0_bala = y0_bala

            #self.velocidade_bala = 2

        

 
        def movimenta_disparo_p1(self):
           
            
            ConfiJogo.X0_BALA_P1 = ConfiJogo.X0_BALA_P1 + 7   #10 sendo a velocidade 

        def movimenta_disparo_p2(self):
           
            
            ConfiJogo.X0_BALA_P2 = ConfiJogo.X0_BALA_P2 - 7   #10 sendo a velocidade                       