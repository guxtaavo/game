import pygame as pg

# CLASSE PARA FAZER OS BOTOES DA TELA DE SELEÇÃO DOS PERSONAGENS
class Botao:
    def __init__ (self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pg.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)
        self.clickou = False

    # FUNÇÃO PARA DESENHAR OS BOTOES NA TELA
    def desenha(self, tela):
        acao = False

        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clickou == False:
                self.clickou = True
                acao = True

        if pg.mouse.get_pressed()[0] == 0:
                self.clickou = False

        tela.blit(self.imagem, (self.rect.x, self.rect.y))

        return acao

                    
