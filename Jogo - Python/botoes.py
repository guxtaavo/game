#classe de botões.

import pygame

class Button:
    def __init__ (self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pygame.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)
        self.clickou = False

    def desenha(self, tela):
        acao = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clickou == False:
                self.clickou = True
                acao = True

        if pygame.mouse.get_pressed()[0] == 0:
                self.clickou = False

        tela.blit(self.imagem, (self.rect.x, self.rect.y))

        return acao

                    
