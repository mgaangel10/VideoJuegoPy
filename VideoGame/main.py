import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

from VideoGame.model.Mapa import Mapa
from model.robot import Robot

# Constantes
ANCHO_VENTANA = 1050
ALTO_VENTANA = 600
VELOCIDAD_MOVIMIENTO = 2
DIAMANTES_NECESARIOS = 4
TIEMPO_ESPERA = 3000
s=True
numero=2
esPar=True
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

mapa_instance = Mapa()
mi_robot = Robot(300, 240, mapa_instance)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))

font = pygame.font.Font(None, 36)
with open('mapa.txt', 'r') as f:
    next(f)
    mapa = f.readlines()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        mi_robot.move(-VELOCIDAD_MOVIMIENTO, 0, ANCHO_VENTANA, ALTO_VENTANA, mapa)
        mi_robot.imagen = pygame.image.load("imagenes/steven_l.png")
        mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
    if keys[K_RIGHT]:
        mi_robot.move(VELOCIDAD_MOVIMIENTO, 0, ANCHO_VENTANA, ALTO_VENTANA, mapa)
        mi_robot.imagen = pygame.image.load("imagenes/steven_r.png")
        mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
    if keys[K_UP]:
        mi_robot.move(0, -VELOCIDAD_MOVIMIENTO, ANCHO_VENTANA, ALTO_VENTANA, mapa)
        mi_robot.imagen = pygame.image.load("imagenes/steven_espalda.png")
        mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
    if keys[K_DOWN]:
        mi_robot.move(0, VELOCIDAD_MOVIMIENTO, ANCHO_VENTANA, ALTO_VENTANA, mapa)
        mi_robot.imagen = pygame.image.load("imagenes/steven.png")
        mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
    if keys[pygame.K_t]:
        if mi_robot.inventario['T'] > 0:
            mi_robot.trajeAcuaticoActivo = not mi_robot.trajeAcuaticoActivo
            if mi_robot.trajeAcuaticoActivo:
                mi_robot.imagen = mi_robot.imagenTrajeAcuatico
            else:
                mi_robot.imagen = pygame.image.load("imagenes/steven.png")
                mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
    if keys[pygame.K_v]:
        mi_robot.consumir_vida()
    if keys[pygame.K_b]:
        mi_robot.usar_bomba(mapa)
    if mi_robot.inventario['D'] == DIAMANTES_NECESARIOS:

        ganar_texto = font.render('Has ganado', True, (255, 255, 0))

        ventana.blit(ganar_texto, (ventana.get_width() // 2 - ganar_texto.get_width() // 2,
                                   ventana.get_height() // 2 - ganar_texto.get_height() // 2))

        pygame.display.flip()

        pygame.time.wait(TIEMPO_ESPERA)

        game_running = False

    if mi_robot.salud == 0:
        game_running = False

    mapa_instance.colision_con_muro(mi_robot.cuerpoRobot, mapa,mi_robot.trajeAcuaticoActivo)
    mapa_instance.dibujar(ventana, mapa)
    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    if mi_robot.salud > 5:
        vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (0, 255, 0))
    elif mi_robot.salud > 3:
            vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255, 255, 0))
    else:
        vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255,0,0))

    ventana.blit(vida_texto, (10, 10))
    for i, (objeto, cantidad) in enumerate(mi_robot.inventario.items()):
        objeto_texto = font.render(f'{objeto}: {cantidad}', True, (255, 255, 0))
        ventana.blit(objeto_texto, (150 + i * 100, 10))

    pygame.display.flip()

pygame.quit()
