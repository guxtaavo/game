import pygame as pg
import sys
from configjogo import ConfiJogo
from cenario import Cenario
from vida_jogador import Vida
from cronometro import Cronometro

class Tela_Jogo:
    
    def __init__(self, tela, imagem, vida, velocidade, tela2, imagem2, vida2, velocidade2):
        self.relogio = pg.time.Clock()
        self.esta_rodando = True
        self.font_timer = pg.font.SysFont("sigmar one", 54)

        #CRIANDO PRIMEIRO JOGADOR
        self.tela = tela
        self.imagem = pg.image.load(imagem)
        img = self.imagem
        self.vida = Vida(ConfiJogo.P1_POSICAO_X, ConfiJogo.P1_POSICAO_Y)
        self.velocidade = velocidade
        self.largura_imagem = img.get_rect().width
        self.altura_imagem = img.get_rect().height
        self.rect1 = img.get_rect()
       

        #CRIANDO O SEGUNDO JOGADOR
        self.tela2 = tela2
        self.imagem2 = pg.image.load(imagem2)
        img2 = self.imagem2
        self.vida2 = Vida(ConfiJogo.P2_POSICAO_X, ConfiJogo.P2_POSICAO_Y)
        self.velocidade2 = velocidade2
        self.largura_imagem2 = img2.get_rect().width
        self.altura_imagem2 = img2.get_rect().height
        self.rect2 = img2.get_rect()


        self.cenario = Cenario(ConfiJogo.TAMANHO_BLOCO, self.tela)

        self.cronometro = Cronometro()

    def rodar(self):
            while self.esta_rodando:    
                self.tela.fill(ConfiJogo.BRANCO)
                self.cenario.pintar(self.tela)
                self.desenha()
                self.tratamento_de_eventos()
                pg.display.flip()

    def desenha(self):
        self.coloca_imagem_tela(self.tela)
        self.vida.desenha_vida(self.tela)
        self.vida2.desenha_vida(self.tela)
        pg.display.flip()

    def jogo_terminou(self):
        if (self.cronometro.tempo_passado() > ConfiJogo.DURACAO_PARTIDA):
            return True
        else:
            return False

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
                sys.exit()

            # PARA MOVIMENTAR O JOGADOR 1
            if pg.key.get_pressed()[pg.K_w]:
                if not ((self.largura_imagem + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y - self.velocidade >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y - self.velocidade <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    ConfiJogo.P1_POSICAO_Y -= self.velocidade
                
            if pg.key.get_pressed()[pg.K_s]:     
                if not ((self.largura_imagem + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.velocidade + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y + self.velocidade <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    ConfiJogo.P1_POSICAO_Y += self.velocidade

            if pg.key.get_pressed()[pg.K_d]:
                if not ((self.largura_imagem + self.velocidade + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X + self.velocidade <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    ConfiJogo.P1_POSICAO_X += self.velocidade

            if pg.key.get_pressed()[pg.K_a]:
                if not ((self.largura_imagem - self.velocidade + ConfiJogo.P1_POSICAO_X >= ConfiJogo.P2_POSICAO_X and \
                ConfiJogo.P1_POSICAO_X - self.velocidade <= ConfiJogo.P2_POSICAO_X + self.largura_imagem2) and \
                (ConfiJogo.P1_POSICAO_Y + self.altura_imagem >= ConfiJogo.P2_POSICAO_Y and \
                ConfiJogo.P1_POSICAO_Y <= ConfiJogo.P2_POSICAO_Y + self.altura_imagem2)):
                    ConfiJogo.P1_POSICAO_X -= self.velocidade


            #PARA MOVIMENTAR O JOGADOR 2
            if pg.key.get_pressed()[pg.K_i]:
                if not ((self.largura_imagem2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y - self.velocidade2 + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y - self.velocidade2 <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    ConfiJogo.P2_POSICAO_Y -= self.velocidade2
                    
            if pg.key.get_pressed()[pg.K_k]:     
                if not ((self.largura_imagem2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.velocidade2 + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y + self.velocidade2 <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    ConfiJogo.P2_POSICAO_Y += self.velocidade2

            if pg.key.get_pressed()[pg.K_l]:
                if not ((self.largura_imagem2 + self.velocidade2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X + self.velocidade2 <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    ConfiJogo.P2_POSICAO_X += self.velocidade2

            if pg.key.get_pressed()[pg.K_j]:
                if not ((self.largura_imagem2 - self.velocidade2 + ConfiJogo.P2_POSICAO_X >= ConfiJogo.P1_POSICAO_X and \
                ConfiJogo.P2_POSICAO_X - self.velocidade2 <= ConfiJogo.P1_POSICAO_X + self.largura_imagem) and \
                (ConfiJogo.P2_POSICAO_Y + self.altura_imagem2 >= ConfiJogo.P1_POSICAO_Y and \
                ConfiJogo.P2_POSICAO_Y <= ConfiJogo.P1_POSICAO_Y + self.altura_imagem)):
                    ConfiJogo.P2_POSICAO_X -= self.velocidade2

            pg.display.flip()

        
    