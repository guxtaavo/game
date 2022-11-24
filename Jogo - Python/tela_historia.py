import pygame as pg
import sys
from configjogo import ConfiJogo
from cronometro import Cronometro


# CLASSE PARA A HISTÓRIA DO JOGO
class Tela_Historia:
    def __init__ (self, tela):
        self.tela = tela
        self.esta_rodando = True

        # CRIA O TEXTO DE HISTORIA QUE SERA MOSTRADA NA PRIMEIRA TELA E OPÇÃO CONTINUAR
        font_historia = pg.font.SysFont("Candal", 70)
        self.historia = font_historia.render(
            f'The Kingdom', True, (255,255,255))
        font_opcao_continuar =  pg.font.SysFont("monospace", 20)
        self.opcao_continuar = font_opcao_continuar.render(f'Pressione espaço para continuar.', True, (255,255,255))

        # VARIAVEIS PARA FAZER PISCAR O TEXTO 
        self.cronometro = Cronometro()
        self.mostrar_opcao = True

    # METODO RODAR DA TELA INICIAL
    def rodar(self):
            while self.esta_rodando:                
                self.desenha()
                self.tratamento_de_eventos()    
                self.atualiza_estado()

    # FUNÇÃO PARA DESENHAR OS TEXTOS NA TELA DA HISTÓRIA
    def desenha(self):
        self.tela.fill((154,154,154))
        # self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela) 
        pg.display.flip()
    
    # # COLOCA A IMAGEM DE FUNDO DA TELA
    # def coloca_imagem_tela(self, tela):
    #     tela.blit(self.imagem_background, (0, 0))

    # DESENHA OS TEXTOS NA TELA DE INICIO
    def desenha_textos(self, tela):
        tela.blit(self.historia, (20, 20))

        # IF PARA FAZER PISCAR
        if self.mostrar_opcao:
            tela.blit(self.opcao_continuar, (220,550)) 
    
    # FUNÇÃO QUE FAZ PISCAR
    def atualiza_estado(self):
        if self.cronometro.tempo_passado() > 0.4:
            self.mostrar_opcao = not self.mostrar_opcao
            self.cronometro.reset()

    # EVENTOS DO JOGO
    def tratamento_de_eventos(self):
        
        for event in pg.event.get():
        # PARA SAIR DO JOGO
            if pg.key.get_pressed()[pg.K_ESCAPE] or event.type == pg.QUIT:
                sys.exit()

        # EVENTO DE PROSSEGUIMENTO
            if pg.key.get_pressed()[pg.K_SPACE]:            
                self.esta_rodando = False