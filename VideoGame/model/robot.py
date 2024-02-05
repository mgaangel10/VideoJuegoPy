import time

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
        self.vida = False
        self.trajeAcuatico = False
        self.trajeAcuaticoActivo = False
        self.mapas_instance = mapas_instance
        self.imagenTrajeAcuatico = pygame.image.load("imagenes/endermanFront.png")
        self.imagenTrajeAcuatico = pygame.transform.scale(self.imagenTrajeAcuatico, (50, 50))
        self.ultimo_choque = 0
        self.inventario = {'B': 0, 'T': 0, 'D': 0, 'V': 0}

    def move(self, dx, dy, ventana_horizontal, ventana_vertical, mapa):
        new_rect = self.cuerpoRobot.move(dx, dy)

        if not self.mapas_instance.colision_con_muro(new_rect, mapa, self.trajeAcuaticoActivo):
            self.cuerpoRobot = new_rect
            objeto = self.mapas_instance.obtener_objeto(new_rect, mapa)
            if objeto:
                self.recoger_objeto(objeto)
        else:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.ultimo_choque >= 500:
                self.salud -= 1
                self.ultimo_choque = tiempo_actual

    def update_rect(self):
        self.cuerpoRobot = self.imagen.get_rect(topleft=(self.cuerpoRobot.x, self.cuerpoRobot.y))

    def recoger_objeto(self, objeto):
        if objeto in self.inventario:
            self.inventario[objeto] += 1
            if objeto == 'V':
                self.vida = True

    def consumir_vida(self):
        if self.vida and self.inventario['V'] > 0:
            self.salud += 5
            self.inventario['V'] -= 1
            self.vida = False



    def usar_bomba(self, mapa):
        if self.inventario['B'] > 0:
            self.inventario['B'] -= 1
            x, y = self.cuerpoRobot.x // 50, self.cuerpoRobot.y // 50
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if mapa[y + dy][x + dx] == 'M':
                        mapa[y + dy] = mapa[y + dy][:x + dx] + ' ' + mapa[y + dy][x + dx + 1:]


