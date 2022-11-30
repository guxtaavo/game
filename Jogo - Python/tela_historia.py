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
        font_historia = pg.font.SysFont("Candal", 30)
        self.linha1 = font_historia.render(
            f'O jogo se passa no reino de Cariacica, cujo o guerreiro Alfredo Chaves', True, (255,255,255))
        self.linha2 = font_historia.render(
            f'se apaixona pela princesa Vitória, do reino de Cariacica,', True, (255,255,255))
        self.linha3 = font_historia.render(
            f'e decide ajuda-la na batalha, com a ajuda do seu amigo elfo, o Serra,', True, (255,255,255))
        self.linha4 = font_historia.render(
            f'contra a invasão da gangue de ogros que estavam determinados', True, (255,255,255))
        self.linha5 = font_historia.render(
            f'a tomar a sua cidade, entretanto, eles não estarão sozinhos,', True, (255,255,255))
        self.linha6 = font_historia.render(
            f'irão contar com a ajuda da bruxa Marataizes que quer se vingar', True, (255,255,255))
        self.linha7 = font_historia.render(
            f'da sua irmã Vitória, por inveja de não ter conseguido a coroa.', True, (255,255,255))
        self.linha8 = font_historia.render(
            f'Entretanto, o Reino de Vila Velha, seu vizinho, está de olho na', True, (255,255,255))
        self.linha9 = font_historia.render(
            f'invasão e atento a ganhar terras.', True, (255,255,255))

        font_opcao_continuar =  pg.font.SysFont("monospace", 20)
        self.opcao_continuar = font_opcao_continuar.render(f'Pressione espaço para continuar.', True, (255,255,255))

        # VARIAVEIS PARA FAZER PISCAR O TEXTO 
        self.cronometro = Cronometro()
        self.mostrar_opcao = True

        self.imagem_background = pg.image.load("img/background.jpg")


    # METODO RODAR DA TELA INICIAL
    def rodar(self):
            while self.esta_rodando:                
                self.desenha()
                self.tratamento_de_eventos()    
                self.atualiza_estado()

    # FUNÇÃO PARA DESENHAR OS TEXTOS NA TELA DA HISTÓRIA
    def desenha(self):
        # self.tela.fill((154,154,154))
        self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela) 
        pg.display.flip()
    
    # # COLOCA A IMAGEM DE FUNDO DA TELA
    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem_background, (0, 0))

    # DESENHA OS TEXTOS NA TELA DE INICIO
    def desenha_textos(self, tela):
        tela.blit(self.linha1, (50, 60))
        tela.blit(self.linha2, (120, 115))
        tela.blit(self.linha3, (70, 170))
        tela.blit(self.linha4, (80, 225))
        tela.blit(self.linha5, (100, 280))
        tela.blit(self.linha6, (85, 335))
        tela.blit(self.linha7, (95, 390))
        tela.blit(self.linha8, (90, 445))
        tela.blit(self.linha9, (240, 500))


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
                prosseguir = pg.mixer.Sound("sons/click.wav")
                prosseguir.set_volume(0.1)
                prosseguir.play()    
                self.esta_rodando = False