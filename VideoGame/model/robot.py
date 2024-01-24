import pygame


class Robot(pygame.sprite.Sprite):
    def __init__(self,x,y,ventana_horizontal,ventana_vertical):
        super().__init__()
        self.imagen = pygame.image.load("imagenes/robot.png")
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))
        self.cuerpoRobot=self.imagen.get_rect()
        self.cuerpoRobot.x = x
        self.cuerpoRobot.y=y
        self.salud=10
        self.trajeAcuatico = False
        self.ventana_horizontal = ventana_horizontal
        self.ventana_vertical = ventana_vertical

    def move(self, dx, dy):
        if 0 <= self.cuerpoRobot.x + dx < self.ventana_horizontal - self.cuerpoRobot.width:
            self.cuerpoRobot.x += dx
        else:
            self.salud -= 1
        if 0 <= self.cuerpoRobot.y + dy < self.ventana_vertical - self.cuerpoRobot.height:
            self.cuerpoRobot.y += dy
        else:
            self.salud -= 1
