import pygame
import random


class Bowl:
    # com
    velocity = 5
    width = 200
    height = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obj = pygame.Rect(x, y, self.width, self.height)

    def move(self, left):
        if left:
            self.x -= self.velocity
        else:
            self.x += self.velocity

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.obj.x, self.obj.y, self.obj.width, self.obj.height))