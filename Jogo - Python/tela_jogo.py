import pygame as pg
import sys
from configjogo import ConfiJogo
from cenario import Cenario


class Tela_Jogo:
    def __init__(self, tela, imagem, vida, velocidade, tela2, imagem2, vida2, velocidade2):
        self.relogio = pg.time.Clock()
        self.esta_rodando = True
        
        #CRIANDO PRIMEIRO JOGADOR
        self.tela = tela
        self.imagem = pg.image.load(imagem)
        img = self.imagem
        self.vida = vida
        self.velocidade = velocidade
        self.largura_imagem = img.get_rect().width
        self.altura_imagem = img.get_rect().height

        #CRIANDO O SEGUNDO JOGADOR
        self.tela2 = tela2
        self.imagem2 = pg.image.load(imagem2)
        img2 = self.imagem2
        self.vida2 = vida2
        self.velocidade2 = velocidade2
        self.largura_imagem2 = img2.get_rect().width
        self.altura_imagem2 = img2.get_rect().height
        self.cenario = Cenario(ConfiJogo.TAMANHO_BLOCO, self.tela)

    def rodar(self):
            while self.esta_rodando:    
                self.tela.fill(ConfiJogo.BRANCO)
                self.cenario.pintar(self.tela)
                self.desenha()
                self.tratamento_de_eventos()
                pg.display.flip()

    def desenha(self):
        self.coloca_imagem_tela(self.tela)
        pg.display.flip()

    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem, (ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y))
        tela.blit(self.imagem2, (ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y))

    # FUNÇÃO QUE TRATA OS EVENTOS DO JOGO, COMO A MOVIMENTAÇÃO DOS PERSONAGENS
    def tratamento_de_eventos(self):
        self.relogio.tick(60)

        for event in pg.event.get():
        
            #PARA SAIR DO JOGO
            if pg.key.get_pressed()[pg.K_ESCAPE] or event.type == pg.QUIT:
                sys.exit()

            #PARA MOVIMENTAR O JOGADOR 1
            if pg.key.get_pressed()[pg.K_w]:            
                ConfiJogo.P1_POSICAO_Y -= self.velocidade

            if pg.key.get_pressed()[pg.K_s]:            
                ConfiJogo.P1_POSICAO_Y += self.velocidade

            if pg.key.get_pressed()[pg.K_d]:            
                ConfiJogo.P1_POSICAO_X += self.velocidade

            if pg.key.get_pressed()[pg.K_a]:            
                ConfiJogo.P1_POSICAO_X -= self.velocidade


            #PARA MOVIMENTAR O JOGADOR 2
            if pg.key.get_pressed()[pg.K_i]:            
                ConfiJogo.P2_POSICAO_Y -= self.velocidade2

            if pg.key.get_pressed()[pg.K_k]:            
                ConfiJogo.P2_POSICAO_Y += self.velocidade2

            if pg.key.get_pressed()[pg.K_l]:            
                ConfiJogo.P2_POSICAO_X += self.velocidade2

            if pg.key.get_pressed()[pg.K_j]:            
                ConfiJogo.P2_POSICAO_X -= self.velocidade2

          

            pg.display.flip()

        
    