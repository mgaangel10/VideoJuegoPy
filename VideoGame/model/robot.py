import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, x, y, mapas_instance):
        super().__init__()
        self.imagen = pygame.image.load("imagenes/steven.png")
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))
        self.cuerpoRobot = self.imagen.get_rect()
        self.cuerpoRobot.x = x
        self.cuerpoRobot.y = y
        self.salud = 10
        self.trajeAcuatico = False
        self.mapas_instance = mapas_instance

    def move(self, dx, dy, ventana_horizontal, ventana_vertical, mapa):
        new_rect = self.cuerpoRobot.move(dx, dy)

        # Verifica si hay colisión con muros
        if not self.mapas_instance.colision_con_muro(new_rect, mapa):
            # Solo actualiza la posición si no hay colisión
            self.cuerpoRobot = new_rect
        else:
            self.salud -= 1

    def update_rect(self):
        self.cuerpoRobot = self.imagen.get_rect(topleft=(self.cuerpoRobot.x, self.cuerpoRobot.y))


    def update_rect(self):
        self.cuerpoRobot = self.imagen.get_rect(topleft=(self.cuerpoRobot.x, self.cuerpoRobot.y))