import pygame
import random


class Fruit:
    # com
    width = 25
    height = 25
    velocity = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obj = pygame.Rect(x, y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.obj.x, self.obj.y, self.obj.width, self.obj.height))

    def fall(self):
        self.y -= self.velocity

    def reset(self, y, x):
        self.y = y
        self.x = random.randint(1, x)
