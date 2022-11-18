import pygame as pg
import sys
from configjogo import ConfiJogo
from botoes import Botao
from personagens import Personagens

# TELA DA SELEÇÃO DOS PERSONAGENS
class TelaSelecao:

    p1 = Personagens.BRUXA
    p2 = Personagens.ELFO

    def __init__ (self, tela):
        self.tela = tela
        self.esta_rodando = True
        self.carregar_arquivos()
        font_titulo_selecao = pg.font.SysFont("monospace", 35)
        self.titulo_selecao = font_titulo_selecao.render(
            f'Selecione o seu personangem:', True, (255,255,255))
        

    #ESCREVE OS TEXTOS NA PARTE DA SELEÇÃO DE PERSONAGENS
    def desenha_textos(self, tela):
        tela.blit(self.titulo_selecao, (105, 40))

    #COLOCA AS IMAGENS DE FUNDO
    def desenha(self):
        self.tela.fill((154,154,154))
        self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela)
        pg.display.flip()

    #CARREGA AS IMAGENS DOS PERSONAGENS NA TELA DA SELEÇÃO
    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem_background, (0, 0))
        tela.blit(self.imagem_botao_personagem1, (25,450))
        tela.blit(self.imagem_botao_personagem2, (225,450))
        tela.blit(self.imagem_botao_personagem3, (425,450))
        tela.blit(self.imagem_botao_personagem4, (625,450))
        tela.blit(self.imagem_personagem1, (45,270))
        tela.blit(self.imagem_personagem2, (250,270))
        tela.blit(self.imagem_personagem3, (440,270))
        tela.blit(self.imagem_personagem4, (640,270))


    #CARREGA OS ARQUIVOS
    def carregar_arquivos(self):
            self.imagem_background = pg.image.load("img/background.jpg").convert()
            self.imagem_botao_personagem1 = pg.image.load("img/Botao 1.png").convert()
            self.imagem_botao_personagem2 = pg.image.load("img/Botao 2.png").convert()
            self.imagem_botao_personagem3 = pg.image.load("img/Botao 3.png").convert()
            self.imagem_botao_personagem4 = pg.image.load("img/Botao 4.png").convert()

            self.imagem_personagem1 = pg.image.load("img/bruxa.png")
            self.imagem_personagem1 = pg.transform.scale(self.imagem_personagem1, (128,168))

            self.imagem_personagem2 = pg.image.load("img/ogro.png")
            self.imagem_personagem2 = pg.transform.scale(self.imagem_personagem2, (128,168))

            self.imagem_personagem3 = pg.image.load("img/principe.png")
            self.imagem_personagem3 = pg.transform.scale(self.imagem_personagem3, (128,168))

            self.imagem_personagem4 = pg.image.load("img/elfo.png")
            self.imagem_personagem4 = pg.transform.scale(self.imagem_personagem4, (128,172))
    #CRIA OS BOTÕES
    def cria_instancia_botao(self):
        self.botao_personagem_1 = Botao(25,450, self.imagem_botao_personagem1 , 0.8)
        self.botao_personagem_2 = Botao(225,450, self.imagem_botao_personagem2 , 0.8)
        self.botao_personagem_3 = Botao(425,450, self.imagem_botao_personagem3 , 0.8)
        self.botao_personagem_4 = Botao(625,450, self.imagem_botao_personagem4 , 0.8)

    #CRIA OS EVENTOS COM OS BOTOES
    def escolher_p1(self):

        if self.botao_personagem_1.desenha(self.tela):
            self.p1 = Personagens.BRUXA
            print('J1 Selecionado personagem 1')
            self.esta_rodando = False
                   
        if self.botao_personagem_2.desenha(self.tela):
            self.p1 = Personagens.ELFO
            print('J1 Selecionado personagem 2')
            self.esta_rodando = False

        if self.botao_personagem_3.desenha(self.tela):
            self.p1 = Personagens.OGRO
            print('J1 Selecionado personagem 3')
            self.esta_rodando = False

        if self.botao_personagem_4.desenha(self.tela):
            self.p1 = Personagens.PRINCIPE
            print('J1 Selecionado personagem 4')
            self.esta_rodando = False


    def escolher_p2(self):

        if self.botao_personagem_1.desenha(self.tela):
            self.p2 = Personagens.BRUXA
            print('J2 Selecionado personagem 1')
            self.esta_rodando = False
                   
        if self.botao_personagem_2.desenha(self.tela):
            self.p2 = Personagens.ELFO
            print('J2 Selecionado personagem 2')
            self.esta_rodando = False

        if self.botao_personagem_3.desenha(self.tela):
            self.p2 = Personagens.OGRO
            print('J2 Selecionado personagem 3')
            self.esta_rodando = False

        if self.botao_personagem_4.desenha(self.tela):
            self.p2 = Personagens.PRINCIPE
            print('J2 Selecionado personagem 4')
            self.esta_rodando = False     


    #TRATAMENTO DE EVENTOS
    def tratamento_de_eventos(self):
        
        for event in pg.event.get():
        #PARA SAIR DO JOGO
            if pg.key.get_pressed()[pg.K_ESCAPE] or event.type == pg.QUIT:
                sys.exit()

        
    #RODA O JOGO
    def rodar(self):
            while self.esta_rodando:
                self.desenha()
                self.tratamento_de_eventos()
                self.cria_instancia_botao()
                self.escolher_p1()
                self.escolher_p2()