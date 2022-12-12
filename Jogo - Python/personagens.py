# CLASSE QUE RECEBE OS PERSONAGENS DO JOGO COM SUAS RESPECTIVAS CARACTERISTICAS

# IMAGEM DO PERSONAGEM / VIDA / VELOCIDADE / FORÇA ATAQUE A DIST / FORÇA ATAQUE MELEE
class Personagens:
    BRUXA = ["img/bruxa.png", 10, 4, 3, 1]
    ELFO = ["img/elfo.png", 12, 5, 2, 1]
    OGRO = ["img/ogro.png", 20, 3, 1, 3]
    PRINCIPE = ["img/principe.png", 15, 5, 1, 2]
    GUERREIRO = ["img/guerreiro.png", 5, 2, 0, 1]
    # VIDA VARIANDO DE 1-20
    # ATAQUES VARIANDO DE 1-3
    # VELOCIDADE VARIANDO DE 1-5

    def apagar(self):
        del self
