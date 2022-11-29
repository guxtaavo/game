import pygame as pg
import sys
from configjogo import ConfiJogo
from cronometro import Cronometro


# CLASSE PARA A HISTÓRIA DO JOGO
class Tela_Vencedor:
    def __init__ (self, tela):
        self.tela = tela
        self.esta_rodando = True

        # CRIA O TEXTO DO FINAL DO JOGO
        font_texto_final_de_jogo = pg.font.SysFont("Candal", 70)
        self.texto_final_de_jogo = font_texto_final_de_jogo.render(
            f'Final de jogo', True, (255,255,255))


        # CRIA O TEXTO DE EMPATE
        font_texto_final_de_jogo = pg.font.SysFont("Candal", 70)
        self.texto_empate = font_texto_final_de_jogo.render(
            f'Empate!', True, (255,255,255))


        # CRIA O TEXTO DO PLAYER 1 VENCEDOR
        font_texto_final_de_jogo = pg.font.SysFont("Candal", 70)
        self.texto_vencedor_p1 = font_texto_final_de_jogo.render(
            f'O jogador 1 venceu!', True, (255,255,255))


        # CRIA O TEXTO DO PLAYER 2 VENCEDOR
        font_texto_final_de_jogo = pg.font.SysFont("Candal", 70)
        self.texto_vencedor_p2 = font_texto_final_de_jogo.render(
            f'O jogador 2 venceu!', True, (255,255,255))


        font_opcao_jogar_novamente =  pg.font.SysFont("monospace", 20)
        self.opcao_jogar_novamente = font_opcao_jogar_novamente.render(
            f'Pressione espaço para jogar novamente.', True, (255,255,255))
        

        self.imagem_background = pg.image.load("img/background.jpg")


        # VARIAVEIS PARA FAZER PISCAR O TEXTO 
        self.cronometro = Cronometro()
        self.mostrar_opcao = True

    # METODO RODAR DA TELA INICIAL
    def rodar(self):
            while self.esta_rodando:                
                self.desenha()
                # self.coloca_imagem_tela(self.tela)
                self.tratamento_de_eventos()    
                self.atualiza_estado()

    # FUNÇÃO PARA DESENHAR OS TEXTOS NA TELA DA HISTÓRIA
    def desenha(self):
        self.tela.fill((255,255,255))
        self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela) 
        pg.display.flip()
    
    # COLOCA A IMAGEM DE FUNDO DA TELA
    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem_background, (0, 0))

    # DESENHA OS TEXTOS NA TELA DE INICIO
    def desenha_textos(self, tela):
        tela.blit(self.texto_final_de_jogo, (250, 50))
        
        if ConfiJogo.VIDA_P1 == ConfiJogo.VIDA_P2:
            tela.blit(self.texto_empate, (300, 300))
        else:
            if ConfiJogo.VIDA_P1 > ConfiJogo.VIDA_P2:
                tela.blit(self.texto_vencedor_p1, (175, 300))
            else:
                tela.blit(self.texto_vencedor_p2, (175, 300))


        # IF PARA FAZER PISCAR
        if self.mostrar_opcao:
            tela.blit(self.opcao_jogar_novamente, (200,550)) 
    

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