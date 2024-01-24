import pygame

from main import game_running


class Robot():
    def __init__(self):
        self.position = [0, 0]
        self.speed= 10

    def move_right(self):
        self.position[1] += self.speed
    def move_left(self):
        self.position[1] -= self.speed

robot_one= Robot()


while game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                robot_one.move_right()
            if event.key == pygame.K_LEFT:
                robot_one.move_left()