import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from model.robot import Robot

pygame.init()
ventana = pygame.display.set_mode((690, 480))
fondo = pygame.image.load("imagenes/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (690, 480))
mi_robot = Robot(300, 240, 690, 480)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))

font = pygame.font.Font(None, 36)  # Tamaño de la fuente

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mi_robot.move(-10, 0)#mover a la izquierda
            elif event.key == K_RIGHT:
                mi_robot.move(10, 0)  #mover a la derecha
            elif event.key == K_UP:
                mi_robot.move(0, -10)  #mover hacia arriba
            elif event.key == K_DOWN:
                mi_robot.move(0, 10)  #mover hacia abajo


    #si el robot tiene 0 de vida se cierra el juego
    if mi_robot.salud == 0:
        game_running = False
    #esto ajusta el fondo de pantalla
    ventana.blit(fondo, (0, 0))


    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    #esto muestra el texto de la ventana donde se ve la vida del robot
    vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255, 0, 0))
    #esto es donde esta situado el marcador de la vida
    ventana.blit(vida_texto, (10, 10))

    pygame.display.flip()

pygame.quit()
