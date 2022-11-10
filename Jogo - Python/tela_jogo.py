import pygame as pg
import sys
import os
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_inicial import CenaHistoria

class Tela_Jogo:
    def __init__(self, tela, imagem, vida, velocidade):
        self.tela = tela
        self.imagem = pg.image.load(imagem)
        img = self.imagem
        self.vida = vida
        self.velocidade = velocidade
        self.esta_rodando = True
        self.largura_imagem = img.get_rect().width
        self.altura_imagem = img.get_rect().height

    def rodar(self):
            while self.esta_rodando:                
                self.desenha()
                self.tratamento_de_eventos()
                pg.display.flip()

    def desenha(self):
        self.tela.fill(ConfiJogo.BRANCO)
        self.coloca_imagem_tela(self.tela)
        pg.display.flip()

    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y))

    def tratamento_de_eventos(self):
        pg.event.get()
        
        #PARA SAIR DO JOGO
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        #PARA MOVIMENTAR O JOGADOR 1
        if pg.key.get_pressed()[pg.K_w]:            
            ConfiJogo.P1_POSICAO_Y -= self.velocidade

        if pg.key.get_pressed()[pg.K_s]:            
            ConfiJogo.P1_POSICAO_Y += self.velocidade

        if pg.key.get_pressed()[pg.K_d]:            
            ConfiJogo.P1_POSICAO_X += self.velocidade

        if pg.key.get_pressed()[pg.K_a]:            
            ConfiJogo.P1_POSICAO_X -= self.velocidade

        #CONDICIONAIS PARA LIMITAR A TELA JOGADOR 1
        if ConfiJogo.P1_POSICAO_Y - self.altura_imagem > ConfiJogo.ALTURA:
            ConfiJogo.P1_POSICAO_Y = ConfiJogo.ALTURA + self.altura_imagem

        if ConfiJogo.P1_POSICAO_Y < 0:
            ConfiJogo.P1_POSICAO_Y = 0

        if ConfiJogo.P1_POSICAO_X > ConfiJogo.LARGURA - self.largura_imagem:
            ConfiJogo.P1_POSICAO_X = ConfiJogo.LARGURA - self.largura_imagem

        if ConfiJogo.P1_POSICAO_X < 0:
            ConfiJogo.P1_POSICAO_X = 0

    

        
    