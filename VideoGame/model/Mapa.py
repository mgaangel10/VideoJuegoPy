import pygame

class Mapa:
    def __init__(self):
        # Carga las imágenes
        self.muro = pygame.transform.scale(pygame.image.load("imagenes/lava.png"), (50, 50))
        self.agua = pygame.transform.scale(pygame.image.load("imagenes/agua.jpg"), (50, 50))
        self.bomba = pygame.transform.scale(pygame.image.load("imagenes/tnt.png"), (50, 50))
        self.diamante = pygame.transform.scale(pygame.image.load("imagenes/diamante.png"), (50, 50))
        self.traje_agua = pygame.transform.scale(pygame.image.load("imagenes/enderman.png"), (50, 50))
        self.camino = pygame.transform.scale(pygame.image.load("imagenes/camino.png"), (50, 50))
        self.vida = pygame.transform.scale(pygame.image.load("imagenes/vida.png"), (50, 50))


        self.imagenes = {'M': self.muro, 'A': self.agua, 'B': self.bomba, 'D': self.diamante, 'T': self.traje_agua, ' ': self.camino,'V': self.vida}

    def dibujar(self, pantalla, mapa):

        for y, linea in enumerate(mapa):
            for x, caracter in enumerate(linea.strip()):
                if caracter in self.imagenes:
                    pantalla.blit(self.imagenes[caracter], (x*50, y*50))

    def colision_con_muro(self, jugador_rect, mapa,traje_acuatico):

        for y, linea in enumerate(mapa):
            for x, caracter in enumerate(linea.strip()):
                if caracter == 'M' or caracter == 'A' and not traje_acuatico:
                    muro_rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    agua_rect = pygame.Rect(x*50, y*50, 50, 50)
                    if jugador_rect.colliderect(muro_rect) or jugador_rect.colliderect(agua_rect):

                        return True
        return False

    def obtener_objeto(self, rect, mapa):
        x, y = rect.x // 50, rect.y // 50
        objeto = mapa[y][x]
        if objeto in 'BTDV':

            mapa[y] = mapa[y][:x] + ' ' + mapa[y][x + 1:]
            return objeto
        return None
