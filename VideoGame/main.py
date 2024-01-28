import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

from VideoGame.model.Mapa import Mapa
from model.robot import Robot

pygame.init()
ventana = pygame.display.set_mode((1050, 600))

mapa_instance = Mapa()
mi_robot = Robot(300, 240, mapa_instance)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))

font = pygame.font.Font(None, 36)  # Tamaño de la fuente
with open('mapa.txt', 'r') as f:
    next(f)
    mapa = f.readlines()

game_running = True
while game_running:

    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mi_robot.move(-10, 0,1050,600,mapa)  # Mover a la izquierda
            elif event.key == K_RIGHT:
                mi_robot.move(10, 0,1050,600,mapa)  # Mover a la derecha
            elif event.key == K_UP:
                mi_robot.move(0, -10,1050,600,mapa)  # Mover hacia arriba
            elif event.key == K_DOWN:
                mi_robot.move(0, 10 ,1050,600,mapa)  # Mover hacia abajo

    # Si el robot tiene 0 de vida se cierra el juego
    if mi_robot.salud == 0:
        game_running = False

    mapa_instance.colision_con_muro(mi_robot.cuerpoRobot, mapa)
    mapa_instance.dibujar(ventana, mapa)
    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    # Esto muestra el texto de la ventana donde se ve la vida del robot
    vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255, 255, 0))
    # Esto es donde está situado el marcador de la vida
    ventana.blit(vida_texto, (10, 10))

    pygame.display.flip()

pygame.quit()
