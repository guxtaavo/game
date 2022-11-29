import pygame as pg
import sys
from configjogo import ConfiJogo
from vida_jogador import Vida
from cronometro import Cronometro
from cenario import Cenario
import math

class Tela_Jogo:
    Mapa =  [
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

    def __init__(self, tela, imagem, vida, velocidade, ataque_dist, ataque_melee, tela2, imagem2, vida2, velocidade2, ataque_dist2, \
        ataque_melee2):
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
        self.altura_imagem = img.get_rect().height
        self.rect1 = img.get_rect()
        self.pos_atual_xp1 = 0
        self.pos_atual_yp1 = 0
        self.balas_p1 = []
        self.ultimo_disparo_p1 = None
        #def __init__ (self, dano, player, x, y)
        self.ataque_p1 = self.Curta_Distancia(3, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
       

        #CRIANDO O SEGUNDO JOGADOR
        self.tela2 = tela2
        self.imagem2 = pg.image.load(imagem2)
        img2 = self.imagem2
        self.vida2 = Vida(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        self.velocidade2 = velocidade2
        self.ataque_dist2 = ataque_dist2
        self.ataque_melee2 = ataque_melee2
        self.largura_imagem2 = img2.get_rect().width
        self.altura_imagem2 = img2.get_rect().height
        self.rect2 = img2.get_rect()
        self.pos_atual_xp2 = 0
        self.pos_atual_yp2 = 0


        self.balas_p2 = []
        self.ultimo_disparo_p2 = None

        self.ataque_p2 = self.Curta_Distancia(3, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        
    
        self.cenario = Cenario(ConfiJogo.TAMANHO_BLOCO, self.tela)


        self.cronometro = Cronometro()
    


    def rodar(self):
            while self.esta_rodando:
                self.tela.fill(ConfiJogo.BRANCO)
                self.cenario.pintar(self.tela)
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

        # CONFG PASSADAS PARA O CRONOMETRO IR ABAIXANDO E DEFINIÇÕES DE POSICIONAMENTO
        tempo = ConfiJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        timer = self.font_timer.render(f"{tempo:.0f}", True, ConfiJogo.PRETO)
        tela.blit(timer, (ConfiJogo.LARGURA//2 + 72, 20))




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


            self.ataque_p1.ataque_p1()
            # PARA MOVIMENTAR O JOGADOR 1
            if pg.key.get_pressed()[pg.K_w]:
                # VERFICA SE O JOGADOR 1 NAO VAI SOBREPOR O JOGADOR 2
                if not ((self.largura_imagem + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y - self.velocidade >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y - self.velocidade <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                    if not ((Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y - self.velocidade)//38][ConfiJogo.P1_POSICAO_X//50] == 1) or \
                        (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y - self.velocidade)//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem)//50] == 1) or \
                        (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y - self.velocidade + self.altura_imagem)//38][ConfiJogo.P1_POSICAO_X//50] == 1) or \
                        (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y - self.velocidade + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem)//50] == 1)):
                            ConfiJogo.P1_POSICAO_Y -= self.velocidade
                             
                            
                
            if pg.key.get_pressed()[pg.K_s]:     
                if not ((self.largura_imagem + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.velocidade + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y + self.velocidade <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                    if not ((Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.velocidade)//38][ConfiJogo.P1_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.velocidade)//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.velocidade + self.altura_imagem)//38][ConfiJogo.P1_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.velocidade + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem)//50] == 1)):
                        ConfiJogo.P1_POSICAO_Y += self.velocidade
                        

            if pg.key.get_pressed()[pg.K_d]:
                if not ((self.largura_imagem + self.velocidade + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X + self.velocidade <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                     if not ((Tela_Jogo.Mapa[ConfiJogo.P1_POSICAO_Y//38][(ConfiJogo.P1_POSICAO_X + self.velocidade)//50] == 1) or \
                    (Tela_Jogo.Mapa[ConfiJogo.P1_POSICAO_Y//38][(ConfiJogo.P1_POSICAO_X + self.velocidade + self.largura_imagem)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X + self.velocidade)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X + self.velocidade + self.largura_imagem)//50] == 1)):
                        ConfiJogo.P1_POSICAO_X += self.velocidade
                        

            if pg.key.get_pressed()[pg.K_a]:
                if not ((self.largura_imagem - self.velocidade + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X - self.velocidade <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                     if not ((Tela_Jogo.Mapa[ConfiJogo.P1_POSICAO_Y//38][(ConfiJogo.P1_POSICAO_X - self.velocidade)//50] == 1) or \
                    (Tela_Jogo.Mapa[ConfiJogo.P1_POSICAO_Y//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem - self.velocidade)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X - self.velocidade)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P1_POSICAO_Y + self.altura_imagem)//38][(ConfiJogo.P1_POSICAO_X + self.largura_imagem - self.velocidade)//50] == 1)):
                        ConfiJogo.P1_POSICAO_X -= self.velocidade
                         

            if pg.key.get_pressed()[pg.K_f]:   #necessário checar  o tempo.
                Tela_Jogo.disparo_p1(self, ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y, 5)           



            self.ataque_p2.ataque_p2()
           
            # PARA MOVIMENTAR O JOGADOR 2
            if pg.key.get_pressed()[pg.K_i]:
                # VERIFICA SE O PERSONAGEM 2 NAO VAI SOBREPOR O PERSONAGEM 1
                if not ((self.largura_imagem2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y - self.velocidade2 <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    #  VERIFICA SE O PERSONAGEM 2 NAO VAI SE COLIDIR COM ALGUM BLOCO DELIMITANTE
                    if not ((Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y - self.velocidade2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y - self.velocidade2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1)):
                        ConfiJogo.P2_POSICAO_Y -= self.velocidade2
                    
            if pg.key.get_pressed()[pg.K_k]:     
                if not ((self.largura_imagem2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.velocidade2 + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y + self.velocidade2 <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                    if not ((Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.velocidade2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.velocidade2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.velocidade2 + self.altura_imagem2)//38][ConfiJogo.P2_POSICAO_X//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.velocidade2 + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X + self.largura_imagem2)//50] == 1)):
                        ConfiJogo.P2_POSICAO_Y += self.velocidade2

            if pg.key.get_pressed()[pg.K_l]:
                if not ((self.largura_imagem2 + self.velocidade2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X + self.velocidade2 <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                    if not ((Tela_Jogo.Mapa[ConfiJogo.P2_POSICAO_Y//38][(ConfiJogo.P2_POSICAO_X + self.velocidade2)//50] == 1) or \
                    (Tela_Jogo.Mapa[ConfiJogo.P2_POSICAO_Y//38][(ConfiJogo.P2_POSICAO_X + self.velocidade2 + self.largura_imagem2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X + self.velocidade2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X + self.velocidade2 + self.largura_imagem2)//50] == 1)):
                        ConfiJogo.P2_POSICAO_X += self.velocidade2

            if pg.key.get_pressed()[pg.K_j]:
                if not ((self.largura_imagem2 - self.velocidade2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X - self.velocidade2 <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    # DELIMITAR A MOVIMENTAÇÃO DO PERSONAGEM ATÉ O BLOCO PEDRA
                    if not ((Tela_Jogo.Mapa[ConfiJogo.P2_POSICAO_Y//38][(ConfiJogo.P2_POSICAO_X - self.velocidade2)//50] == 1) or \
                    (Tela_Jogo.Mapa[ConfiJogo.P2_POSICAO_Y//38][(ConfiJogo.P2_POSICAO_X - self.velocidade2 + self.largura_imagem2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X - self.velocidade2)//50] == 1) or \
                    (Tela_Jogo.Mapa[(ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)//38][(ConfiJogo.P2_POSICAO_X - self.velocidade2 + self.largura_imagem2)//50] == 1)):
                        ConfiJogo.P2_POSICAO_X -= self.velocidade2

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


        def ataque_p1(self): #alvo  #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            if pg.key.get_pressed()[pg.K_e]:
                self.distanciap1p2 = math.sqrt(math.pow((ConfiJogo.P1_POSICAO_X - ConfiJogo.P2_POSICAO_X), 2)+math.pow((ConfiJogo.P1_POSICAO_Y - ConfiJogo.P2_POSICAO_Y), 2))
                if self.distanciap1p2 < 60:
                    ConfiJogo.VIDA_P2 -= 2


        def ataque_p2(self):  #alvo #distancia 2p = sqrt((x-xo)^2+(y-yo)^2)
            if pg.key.get_pressed()[pg.K_p]:
                self.distanciap2p1 = math.sqrt(math.pow((ConfiJogo.P2_POSICAO_X - ConfiJogo.P1_POSICAO_X), 2)+math.pow((ConfiJogo.P2_POSICAO_Y - ConfiJogo.P1_POSICAO_Y), 2))
                if self.distanciap2p1 < 60:
                    ConfiJogo.VIDA_P1 -= 2
                        
                

        
    