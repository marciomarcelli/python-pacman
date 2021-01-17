import pygame

#CORES
AMARELO = (255,255, 0)
PRETO = (0,0,0)

VELOCIDADE = 1
RAIO = 30


pygame.init()

tela = pygame.display.set_mode((640,480),0)

x = 10
y = 10

velocidade_x = 1
velocidade_y = 1

while True:

    # Calcula as regras
    x += velocidade_x
    y += velocidade_y
    if x + RAIO > 640:
        velocidade_x = -VELOCIDADE
    if x - RAIO < 0:
        velocidade_x = VELOCIDADE
    if y + RAIO > 480:
        velocidade_y = -VELOCIDADE
    if y - RAIO < 0:
        velocidade_y = VELOCIDADE

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x),int(y)), 30, 0)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()