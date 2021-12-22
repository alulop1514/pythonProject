import math

import pygame
import random
# Iniciamos pygame
pygame.init()
# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
puntuacion = 0
# Jugador
iconoJugador = pygame.image.load('iconoJugador.png')
jugX = 370
jugY = 480
jugXCambio = 0


def jugador(x, y):
    pantalla.blit(iconoJugador, (x, y))


# Enemigo
iconoEnemigo = pygame.image.load('alien.png')
eneX = random.randint(0, 800)
eneY = random.randint(50, 150)
eneXCambio = 0.3
eneYCambio = 10


def enemigo(x, y):
    pantalla.blit(iconoEnemigo, (x, y))


# Municion
iconoBala = pygame.image.load('bullet.png')
balaX = 0
balaY = 480
balaXCambio = 0
balaYCambio = 0.5
estadoBala = "preparada"

def disparoBala(x, y):
    global estadoBala
    estadoBala = "disparada"
    pantalla.blit(iconoBala, (x + 16, y + 16))


def colision(eneX, eneY, balaX, balaY):
    distancia = math.sqrt(math.pow(eneX - balaX, 2) + math.pow(eneY - balaY, 2))
    if distancia < 27:
        return True
    else:
        return False
ejecutando = True
while ejecutando:

    pantalla.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugXCambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugXCambio = 0.2
            if evento.key == pygame.K_SPACE:
                if estadoBala == "preparada":
                    balaX = jugX
                    balaY = jugY
                    disparoBala(balaX, balaY)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugXCambio = 0
            elif evento.key == pygame.K_RIGHT:
                 jugXCambio = 0

    jugX += jugXCambio
    if jugX <= 0:
        jugX = 0
    elif jugX >= 736:
        jugX = 736

    eneX += eneXCambio
    if eneX <= 0:
        eneXCambio = 0.3
        eneY += eneYCambio
    elif eneX >= 736:
        eneXCambio = -0.3
        eneY += eneYCambio
    if eneY >= jugY:
        pygame.quit()
    if balaY <= 0:
        balaY = 480
        estadoBala = "preparada"

    if estadoBala == "disparada":
        disparoBala(balaX, balaY)
        balaY -= balaYCambio
    colisionA = colision(eneX, eneY, balaX, balaY)
    if colisionA:
        balaY = 480
        estadoBala = "preparada"
        puntuacion += 1
        eneX = random.randint(0, 800)
        eneY = random.randint(50, 150)


    jugador(jugX, jugY)
    enemigo(eneX, eneY)
    pygame.display.update()
