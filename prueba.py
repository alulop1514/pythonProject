import math

import pygame
import random

# Iniciamos pygame
pygame.init()
# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("background.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
puntuacion = 0
fuente = pygame.font.Font("freesansbold.ttf", 20)
textX = 10
textY = 10

def mostrar_puntuacion(x, y):
    puntuacion_escrita = fuente.render("Puntuacion: " + str(puntuacion), True, (255, 255, 255))
    pantalla.blit(puntuacion_escrita, (x, y))

def mostrar_game_over():
    fuente = pygame.font.Font("freesansbold.ttf", 64)
    game_over = fuente.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(game_over, (200, 200))

# Jugador
iconoJugador = pygame.image.load('iconoJugador.png')
jugX = 370
jugY = 480
jugXCambio = 0

def jugador(x, y):
    pantalla.blit(iconoJugador, (x, y))

# Power Up
estado_power_up = "no_lanzado"
icono_power_up = pygame.image.load("bullets.png")
powerX = random.randint(0, 700)
powerY = 0
powerYCambio = 2
def mostrar_power_up(x, y):
    pantalla.blit(icono_power_up, (x, y))

# Enemigo
iconoEnemigo = []
eneX = []
eneY = []
eneXCambio = []
eneYCambio = []
num_ene = 6
for i in range(num_ene):
    iconoEnemigo.append(pygame.image.load('alien.png'))
    eneX.append(random.randint(0, 700))
    eneY.append(random.randint(10, 50))
    eneXCambio.append(1.5)
    eneYCambio.append(20)


def enemigo(x, y, i):
    pantalla.blit(iconoEnemigo[i], (x, y))


# Municion
iconoBala = pygame.image.load('bullet.png')
balaX = 0
balaY = 480
balaXCambio = 0
balaYCambio = 5
estadoBala = "preparada"
dobleBala = False

def disparoBala(x, y):
    global estadoBala
    estadoBala = "disparada"
    if estado_power_up == "cogido":
        pantalla.blit(iconoBala, (x + 8, y + 16))
        pantalla.blit(iconoBala, (x + 32, y + 16))
    else:
        pantalla.blit(iconoBala, (x + 16, y + 16))



def colision(eneX, eneY, balaX, balaY):
    distancia = math.sqrt(math.pow(eneX - balaX, 2) + math.pow(eneY - balaY, 2))
    if estado_power_up == "cogido":
        if distancia < 36 and estadoBala == "disparada":
            return True
    else:
        if distancia < 27 and estadoBala == "disparada":
            return True
        else:
            return False
ejecutando = True
num_power_up = random.randint(0, 5)
while ejecutando:

    pantalla.fill((0, 0, 0))
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugXCambio = -2
            if evento.key == pygame.K_RIGHT:
                jugXCambio = 2
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

    for i in range(num_ene):
        eneX[i] += eneXCambio[i]
        if eneX[i] <= 0:
            eneXCambio[i] *= -1
            eneY[i] += eneYCambio[i]
        elif eneX[i] >= 736:
            eneXCambio[i] *= -1
            eneY[i] += eneYCambio[i]
        colisionA = colision(eneX[i], eneY[i], balaX, balaY)
        if colisionA:
            balaY = 480
            estadoBala = "preparada"
            puntuacion += 1
            eneX[i] = random.randint(0, 700)
            eneY[i] = random.randint(10, 50)
            if eneXCambio[i] > 0:
                eneXCambio[i] += 0.5
            else:
                eneXCambio[i] -= 0.5
            eneYCambio[i] += 1
            if estado_power_up == "no_lanzado":
                if num_power_up == random.randint(0, 5):
                    estado_power_up = "lanzado"
                    powerX = eneX[i]
                    powerY = eneY[i]
        enemigo(eneX[i], eneY[i], i)

        if eneY[i] >= jugY + 5:
            for j in range(num_ene):
                eneY[j] = 2000
            mostrar_game_over()
            break

    if balaY <= 0:
        balaY = 480
        estadoBala = "preparada"

    if estadoBala == "disparada":
        disparoBala(balaX, balaY)
        balaY -= balaYCambio
    colisionB = colision(jugX, jugY, powerX, powerY)
    if colisionB:
        estado_power_up = "cogido"
    if estado_power_up == "lanzado":
        powerY += powerYCambio
        mostrar_power_up(powerX, powerY)

        if powerY > jugY:
            estado_power_up = "no_lanzado"

    mostrar_puntuacion(textX, textY)
    jugador(jugX, jugY)
    pygame.display.update()
