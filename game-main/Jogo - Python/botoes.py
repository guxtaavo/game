import pygame as pg

# CLASSE PARA FAZER OS BOTOES DA TELA DE SELEÇÃO DOS PERSONAGENS
class Botao:
    def __init__ (self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pg.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)