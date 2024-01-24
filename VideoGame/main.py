import pygame

from model.robot import Robot

pygame.init()
robot_player=Robot();


robots=pygame.image.load("imagenes/image.png")
ventana = pygame.display.set_mode((690,480))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            game_running = False

    ventana.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()