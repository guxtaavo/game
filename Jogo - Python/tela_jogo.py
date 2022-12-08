import pygame as pg
import sys
from configjogo import ConfiJogo
from vida_jogador import Vida
from cronometro import Cronometro
# from cenario import Cenario
import math

class Tela_Jogo:
    def __init__(self, tela, imagem, vida, velocidade, ataque_dist, ataque_melee, tela2, imagem2, vida2, velocidade2, ataque_dist2, \
        ataque_melee2, tela3, imagem3, vida3, velocidade3, ataque_dist3, ataque_melee3):
        self.relogio = pg.time.Clock()
        self.esta_rodando = True
        self.font_timer = pg.font.SysFont("sigmar one", 54)


        #CRIANDO PRIMEIRO JOGADOR
        self.tela = tela
        self.imagem = pg.image.load(imagem)
        img = self.imagem
        
        self.vida = Vida(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        self.velocidade = velocidade
        self.ataque_dist = ataque_dist
        self.ataque_melee = ataque_melee
        self.largura_imagem = img.get_rect().width
        ConfiJogo.LARGURA_P1 = self.largura_imagem
        self.altura_imagem = img.get_rect().height
        ConfiJogo.ALTURA_P1 = self.altura_imagem
        self.rect1 = img.get_rect()
        self.pos_atual_xp1 = 0
        self.pos_atual_yp1 = 0
        self.balas_p1 = []
        self.ultimo_disparo_p1 = None
        self.ataque_melee = ataque_melee
        self.ataque_p1 = self.Curta_Distancia(ataque_melee, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
       

        #CRIANDO O SEGUNDO JOGADOR
        self.tela2 = tela2
        self.imagem2 = pg.image.load(imagem2)
        img2 = self.imagem2
        self.vida2 = Vida(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        self.velocidade2 = velocidade2
        self.ataque_dist2 = ataque_dist2
        self.ataque_melee2 = ataque_melee2
        self.largura_imagem2 = img2.get_rect().width
        ConfiJogo.LARGURA_P2 = self.largura_imagem2
        self.altura_imagem2 = img2.get_rect().height
        ConfiJogo.ALTURA_P2 = self.altura_imagem2
        self.rect2 = img2.get_rect()
  

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


        #CONFIG PARA O ATAQUE A DISTANCIA
        self.balas_p2 = []
        self.ultimo_disparo_p2 = None
        self.balas_p1 = []
        self.ultimo_disparo_p1 = None


        #CONFIG PARA O ATAQUE CORPO A CORPO
        self.ataque_melee2 = ataque_melee2
        self.ataque_p2 = self.Curta_Distancia(ataque_melee2, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        self.ataque_melee = ataque_melee
        self.ataque_p1 = self.Curta_Distancia(ataque_melee, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        

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
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
    


    def rodar(self):
            while self.esta_rodando:
                self.tela.fill(ConfiJogo.BRANCO)
                self.pintar_cenario(self.tela)
                self.desenha()
                self.tratamento_de_eventos()
                self.Tiro.movimenta_disparo_p1(self)
                pg.display.flip()
                if ConfiJogo.VIDA_P1 <= 0 or ConfiJogo.VIDA_P2 <= 0:
                    self.esta_rodando = False

    def desenha(self):
        self.coloca_imagem_tela(self.tela)
        self.vida.desenha_vida(self.tela)
        self.vida2.desenha_vida(self.tela)
        if ConfiJogo.VIDA_MINION > 0:
            self.vida3.desenha_vida(self.tela)
        self.desenha_balas_p1()
        pg.display.flip()


    def desenha_balas_p1(self):
        for disparos in self.balas_p1:
            pg.draw.rect(self.tela, ((0,0,0)), (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, 10, 10))    


    def jogo_terminou(self):
        if (self.cronometro.tempo_passado() > ConfiJogo.DURACAO_PARTIDA):
            return True
        else:
            return False
    

    def disparo_p1(self, x, y, dano):
        x = ConfiJogo.P1_POSICAO_X
       # y = ConfiJogo.P1_POSICAO_Y
        x = x + 30
        self.balas_p1.append(self.Tiro(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, 5))
        x = 10


    # FUNÇÃO PARA DESENHAR OS PERSONAGENS NA TELA
    def coloca_imagem_tela(self, tela):
        self.rect1 = tela.blit(self.imagem, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y))
        self.rect2 = tela.blit(self.imagem2, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y))
        if ConfiJogo.VIDA_MINION > 0:
            self.rect3 = tela.blit(self.imagem3, (ConfiJogo.MINION_POSICAO_X, ConfiJogo.MINION_POSICAO_Y))
        

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

        
            d1 = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P1_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P1_POSICAO_Y)**2))
            d2 = int(math.sqrt((ConfiJogo.MINION_POSICAO_X - ConfiJogo.P2_POSICAO_X)**2 + (ConfiJogo.MINION_POSICAO_Y - ConfiJogo.P2_POSICAO_Y)**2))
            if ConfiJogo.VIDA_MINION > 0:
                if d1 > d2:
                    if ConfiJogo.P1_POSICAO_X > ConfiJogo.MINION_POSICAO_X:
                        ConfiJogo.MINION_POSICAO_X += self.velocidade3
                    elif ConfiJogo.P1_POSICAO_X < ConfiJogo.MINION_POSICAO_X:
                        ConfiJogo.MINION_POSICAO_X -= self.velocidade3
                    if ConfiJogo.P1_POSICAO_Y > ConfiJogo.MINION_POSICAO_Y:
                        ConfiJogo.MINION_POSICAO_Y += self.velocidade3
                    elif ConfiJogo.P1_POSICAO_Y < ConfiJogo.MINION_POSICAO_Y:
                        ConfiJogo.MINION_POSICAO_Y -= self.velocidade3
                else:
                    if ConfiJogo.P2_POSICAO_X > ConfiJogo.MINION_POSICAO_X:
                        ConfiJogo.MINION_POSICAO_X += self.velocidade3
                    elif ConfiJogo.P2_POSICAO_X < ConfiJogo.MINION_POSICAO_X:
                        ConfiJogo.MINION_POSICAO_X -= self.velocidade3
                    if ConfiJogo.P2_POSICAO_Y > ConfiJogo.MINION_POSICAO_Y:
                        ConfiJogo.MINION_POSICAO_Y += self.velocidade3
                    elif ConfiJogo.P2_POSICAO_Y < ConfiJogo.MINION_POSICAO_Y:
                        ConfiJogo.MINION_POSICAO_Y -= self.velocidade3

            self.ataque_p1.ataque_p1(self.tela)
            # PARA MOVIMENTAR O JOGADOR 1
            if pg.key.get_pressed()[pg.K_w]:
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y-self.velocidade, self.largura_imagem, self.altura_imagem)
                if self.rect1_teste.colliderect(self.rect2) == False:
                    ConfiJogo.P1_POSICAO_Y -= self.velocidade
                    ConfiJogo.ULTIMO_PASSO_P1 = "NORTE"
                
            if pg.key.get_pressed()[pg.K_s]:
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y+self.velocidade, self.largura_imagem, self.altura_imagem)
                if self.rect1_teste.colliderect(self.rect2) == False:
                    ConfiJogo.P1_POSICAO_Y += self.velocidade
                    ConfiJogo.ULTIMO_PASSO_P1 = "SUL"
                        
            if pg.key.get_pressed()[pg.K_d]:
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X+self.velocidade, ConfiJogo.P1_POSICAO_Y, self.largura_imagem, self.altura_imagem)
                if self.rect1_teste.colliderect(self.rect2) == False:
                    ConfiJogo.P1_POSICAO_X += self.velocidade
                    ConfiJogo.ULTIMO_PASSO_P1 = "LESTE"
                        
            if pg.key.get_pressed()[pg.K_a]:
                self.rect1_teste = pg.Rect(ConfiJogo.P1_POSICAO_X-self.velocidade, ConfiJogo.P1_POSICAO_Y, self.largura_imagem, self.altura_imagem)
                if self.rect1_teste.colliderect(self.rect2) == False:
                    ConfiJogo.P1_POSICAO_X -= self.velocidade
                    ConfiJogo.ULTIMO_PASSO_P1 = "OESTE"



            if pg.key.get_pressed()[pg.K_f]:   #necessário checar  o tempo.
                Tela_Jogo.disparo_p1(self, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, 5)           

            self.ataque_p2.ataque_p2(self.tela2)

            # PARA MOVIMENTAR O JOGADOR 2
            if pg.key.get_pressed()[pg.K_i]:
                # VERIFICA SE O PERSONAGEM 2 NAO VAI SOBREPOR O PERSONAGEM 1
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y-self.velocidade2, self.largura_imagem2, self.altura_imagem2)
                if self.rect2_teste.colliderect(self.rect1) == False:
                    ConfiJogo.P2_POSICAO_Y -= self.velocidade2
                    ConfiJogo.ULTIMO_PASSO_P2 = "NORTE"
                    #  VERIFICA SE O PERSONAGEM 2 NAO VAI SE COLIDIR COM ALGUM BLOCO DELIMITANTE
                    # if not ((self.matriz[(ConfiJogo.P2_POSICAO_Y - self.velocidade2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    # (self.matriz[(ConfiJogo.P2_POSICAO_Y - self.velocidade2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1) or \
                    # (self.matriz[(ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    # (self.matriz[(ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1)):
                    
            if pg.key.get_pressed()[pg.K_k]:     
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y+self.velocidade2, self.largura_imagem2, self.altura_imagem2)
                if self.rect2_teste.colliderect(self.rect1) == False:
                    ConfiJogo.P2_POSICAO_Y += self.velocidade2
                    ConfiJogo.ULTIMO_PASSO_P2 = "SUL"

            if pg.key.get_pressed()[pg.K_l]:
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X+self.velocidade2, ConfiJogo.P2_POSICAO_Y, self.largura_imagem2, self.altura_imagem2)
                if self.rect2_teste.colliderect(self.rect1) == False:
                    ConfiJogo.P2_POSICAO_X += self.velocidade2
                    ConfiJogo.ULTIMO_PASSO_P2 = "LESTE"

            if pg.key.get_pressed()[pg.K_j]:
                self.rect2_teste = pg.Rect(ConfiJogo.P2_POSICAO_X-self.velocidade2, ConfiJogo.P2_POSICAO_Y, self.largura_imagem2, self.altura_imagem2)
                if self.rect2_teste.colliderect(self.rect1) == False:
                    ConfiJogo.P2_POSICAO_X -= self.velocidade2
                    ConfiJogo.ULTIMO_PASSO_P2 = "OESTE"

            pg.display.flip()



    class Tiro:
        def __init__ (self, x_bala, y_bala, dano):  #com x sendo a px do personagem e y sendo a p2 do personagem
            self.x_bala = x_bala
            self.y_bala = y_bala
            
        def movimenta_disparo_p1(self):
            self.x_bala = ConfiJogo.P1_POSICAO_X + 10



    class Curta_Distancia:
        def __init__ (self, dano, x, y): #player entre dano e x;
            self.dano = dano
           # self.player = player
            self.tempo_recarga = 0
            self.x = x
            self.y = y


        def ataque_p1(self, tela): #alvo  #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            self.tela = tela
            if pg.key.get_pressed()[pg.K_e]:
                self.distanciap1p2 = math.sqrt(math.pow((ConfiJogo.P1_POSICAO_X - ConfiJogo.P2_POSICAO_X), 2)+math.pow((ConfiJogo.P1_POSICAO_Y - ConfiJogo.P2_POSICAO_Y), 2))
                self.distanciap1minion = math.sqrt(math.pow((ConfiJogo.P1_POSICAO_X - ConfiJogo.MINION_POSICAO_X), 2)+math.pow((ConfiJogo.P1_POSICAO_Y - ConfiJogo.MINION_POSICAO_Y), 2))
                if self.distanciap1p2 < 60:
                    ConfiJogo.VIDA_P2 -= self.dano
                    if ConfiJogo.ULTIMO_PASSO_P1 == "NORTE" or ConfiJogo.ULTIMO_PASSO_P1 == "SUL" or ConfiJogo.ULTIMO_PASSO_P1 == "LESTE" or ConfiJogo.ULTIMO_PASSO_P1 == "OESTE":
                        pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, ConfiJogo.LARGURA_P1, ConfiJogo.ALTURA_P1))
                elif self.distanciap1minion < 60:
                    ConfiJogo.VIDA_MINION -= self.dano
                    pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, ConfiJogo.LARGURA_P1, ConfiJogo.ALTURA_P1))


        def ataque_p2(self, tela):  #alvo #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            self.tela = tela
            if pg.key.get_pressed()[pg.K_p]:
                self.distanciap2p1 = math.sqrt(math.pow((ConfiJogo.P2_POSICAO_X - ConfiJogo.P1_POSICAO_X), 2)+math.pow((ConfiJogo.P2_POSICAO_Y - ConfiJogo.P1_POSICAO_Y), 2))
                self.distanciap2minion = math.sqrt(math.pow((ConfiJogo.P2_POSICAO_X - ConfiJogo.MINION_POSICAO_X), 2)+math.pow((ConfiJogo.P2_POSICAO_Y - ConfiJogo.MINION_POSICAO_Y), 2))
                if self.distanciap2p1 < 60:
                    ConfiJogo.VIDA_P1 -= self.dano
                    if ConfiJogo.ULTIMO_PASSO_P2 == "NORTE" or ConfiJogo.ULTIMO_PASSO_P2 == "SUL" or ConfiJogo.ULTIMO_PASSO_P2 == "LESTE" or ConfiJogo.ULTIMO_PASSO_P2 == "OESTE":
                        pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y, ConfiJogo.LARGURA_P2, ConfiJogo.ALTURA_P2))
                elif self.distanciap2minion < 60:
                    ConfiJogo.VIDA_MINION -= self.dano
                    pg.draw.rect(self.tela, ConfiJogo.PRETO, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y, ConfiJogo.LARGURA_P2, ConfiJogo.ALTURA_P2))