import pygame

pygame.init()

screen = pygame.display.set_mode((800,600), 0)

AMARELO = (255,255,0)
PRETO = (0,0,0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 150
        self.raio = self.tamanho // 2


    def pintar(self, tela):
        # Desenha o corpo do Pacman
        pygame.draw.circle(tela, AMARELO,(self.centro_x, self.centro_y), self.raio)

        #Desenha a boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior =  (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, PRETO, pontos,0)

        # Desenha o olho do Pacman
        olho_x = int(self.centro_x + self.raio / 2)
        olho_y = int(self.centro_y - self.raio * 0.7)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # Pinta a tela
        pacman.pintar(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

