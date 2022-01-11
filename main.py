import pygame
contador = 0
# Press the green button in the gutter to run the script.
pygame.init()
true = True
pantalla = pygame.display.set_mode((20, 20))
pygame.display.set_caption("Space Invaders")

while true:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                contador += 1
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                true = False
print(contador)