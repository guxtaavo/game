import pygame as pg
import sys
import os
from configjogo import ConfiJogo


#CLASSE PARA A HISTÓRIA DO JOGO
class CenaHistoria:
    def __init__ (self, tela):
        self.tela = tela
        self.esta_rodando = True
        #CRIA O TEXTO DE HISTORIA QUE SERA MOSTRADA NA PRIMEIRA TELA E OPÇÃO CONTINUAR
        font_historia = pg.font.SysFont(None, 30)
        self.historia = font_historia.render(
            f'Historia Jogo Exemplo.', True, (255,255,255))
        font_opcao_continuar =  pg.font.SysFont("tahoma", 20)
        self.opcao_continuar = font_opcao_continuar.render(f'Pressione espaço para continuar.', True, (255,255,255))  
        self.carregar_arquivos() 

    #METODO RODAR DA TELA INICIAL
    def rodar(self):
            while self.esta_rodando:                
                self.desenha()
                self.tratamento_de_eventos()    

    #FUNÇÃO PARA DESENHAR OS TEXTOS NA TELA INICIAL
    def desenha(self):
    
        self.tela.fill((154,154,154))
        self.coloca_imagem_tela(self.tela)
        self.desenha_textos(self.tela) 
        pg.display.flip()
   
        
    #CARREGA OS ARQUIVOS
    def carregar_arquivos(self):
      
            diretorio_imagens = os.path.join(os.getcwd(), 'img')
            diretorio_fonte = os.path.join(os.getcwd(), 'fonte')
            self.diretorio_background = os.path.join(diretorio_imagens, 'background.jpg')
            self.imagem_background = pg.image.load(self.diretorio_background).convert()
    
    #COLOCA A IMAGEM DE FUNDO DA TELA
    def coloca_imagem_tela(self, tela):
        tela.blit(self.imagem_background, (0, 0))

    #DESENHA OS TEXTOS NA TELA DE INICIO
    def desenha_textos(self, tela):
        tela.blit(self.historia, (40, 40))
        tela.blit(self.opcao_continuar, (300,550)) 
    
    #EVENTOS DO JOGO
    def tratamento_de_eventos(self):
        
        pg.event.get()
        
        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # evento de prosseguimento
        if pg.key.get_pressed()[pg.K_SPACE]:            
            self.esta_rodando = False