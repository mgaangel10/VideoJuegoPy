import pygame


class Robot(pygame.sprite.Sprite):
    def __init__(self,x,y,ventana_horizontal,ventana_vertical):
        super().__init__()
        self.imagen = pygame.image.load("imagenes/robot.png")
        self.cuerpoRobot=self.imagen.get_rect()
        self.cuerpoRobot.x = x
        self.cuerpoRobot.y=y
        self.salud=10
        self.trajeAcuatico = False
        self.ventana_horzontal = ventana_horizontal
        self.ventana_vertical = ventana_vertical

    def move(self, dx, dy):
        self.cuerpoRobot.x += dx
        self.cuerpoRobot.y += dy
