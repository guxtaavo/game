import pygame as pg
import sys
import os
from configjogo import ConfiJogo
from tela_selecao import TelaSelecao
from tela_inicial import CenaHistoria
from jogo import Jogo
from cenario import Cenario
 
def main():
    game = Jogo()
    game.rodar()

if __name__ == "__main__":
    main()