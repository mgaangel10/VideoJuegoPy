import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from model.robot import Robot

pygame.init()
ventana = pygame.display.set_mode((690, 480))

fondo = pygame.image.load("imagenes/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (690, 480))
mi_robot = Robot(300, 240,690,480)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mi_robot.move(-10, 0)
            elif event.key == K_RIGHT:
                mi_robot.move(10, 0)  # Mover a la derecha
            elif event.key == K_UP:
                mi_robot.move(0, -10)  # Mover hacia arriba
            elif event.key == K_DOWN:
                mi_robot.move(0, 10)  # Mover hacia abajo


    ventana.blit(fondo, (0, 0))


    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    pygame.display.flip()

pygame.quit()