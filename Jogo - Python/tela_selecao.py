import pygame as pg
import sys
import os
from configjogo import ConfiJogo
from botoes import Button

class TelaSelecao:
    def __init__ (self, tela):
        self.tela = tela
        self.esta_rodando = True
        self.carregar_arquivos()
        font_titulo_selecao = pg.font.SysFont(None, 30)
        self.titulo_selecao = font_titulo_selecao.render(
            f'Seleção de Personagens', True, (255,255,255))

    #ESCREVE OS TEXTOS NA PARTE DA SELEÇÃO DE PERSONAGENS
    def desenha_textos(self, tela):
        tela.blit(self.titulo_selecao, (40, 40))

    #COLOCA AS IMAGENS DE FUNDO
    def desenha(self):
        self.tela.fill((154,154,154))
        self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela)
        pg.display.flip()

    #CARREGA AS IMAGENS DOS PERSONAGENS NA TELA DA SELEÇÃO
    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem_background, (0, 0))
        tela.blit(self.imagem_personagem1, (25,450))
        tela.blit(self.imagem_personagem2, (225,450))
        tela.blit(self.imagem_personagem3, (425,450))
        tela.blit(self.imagem_personagem4, (625,450))      

    #CARREGA OS ARQUIVOS
    def carregar_arquivos(self):
            diretorio_imagens = os.path.join(os.getcwd(), 'img')
            diretorio_fonte = os.path.join(os.getcwd(), 'fonte')
            self.diretorio_background = os.path.join(diretorio_imagens, 'background.jpg')
            self.imagem_background = pg.image.load(self.diretorio_background).convert()
            self.diretorio_imagens_botao_personagem1 = os.path.join(diretorio_imagens, 'botao 1.png')
            self.imagem_personagem1 = pg.image.load(self.diretorio_imagens_botao_personagem1).convert()

            self.diretorio_imagens_botao_personagem2 = os.path.join(diretorio_imagens, 'botao 2.png')
            self.imagem_personagem2 = pg.image.load(self.diretorio_imagens_botao_personagem2).convert()

            self.diretorio_imagens_botao_personagem3 = os.path.join(diretorio_imagens, 'botao 3.png')
            self.imagem_personagem3 = pg.image.load(self.diretorio_imagens_botao_personagem3).convert()

            self.diretorio_imagens_botao_personagem4 = os.path.join(diretorio_imagens, 'botao 4.png')
            self.imagem_personagem4 = pg.image.load(self.diretorio_imagens_botao_personagem4).convert()

    #CRIA OS BOTÕES
    def cria_instancia_botao(self):
        self.botao_personagem_1 = Button(25,450, self.imagem_personagem1 , 0.8)
        self.botao_personagem_2 = Button(225,450, self.imagem_personagem2 , 0.8)
        self.botao_personagem_3 = Button(425,450, self.imagem_personagem3 , 0.8)
        self.botao_personagem_4 = Button(625,450, self.imagem_personagem4 , 0.8)

    #CRIA OS EVENTOS COM OS BOTOES
    def tratamento_evento_botao(self):

        if self.botao_personagem_1.desenha(self.tela):
            print('Selecionado personagem 1')
                   
        if self.botao_personagem_2.desenha(self.tela):
            print('Selecionado personagem 2')

        if self.botao_personagem_3.desenha(self.tela):
            print('Selecionado personagem 3')

        if self.botao_personagem_4.desenha(self.tela):
            print('Selecionado personagem 4')          


    #TRATAMENTO DE EVENTOS
    def tratamento_de_eventos(self):
        pg.event.get()
        
        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        
    #RODA O JOGO
    def rodar(self):
            while self.esta_rodando:
                self.desenha()
                self.tratamento_de_eventos()
                self.cria_instancia_botao()
                self.tratamento_evento_botao()