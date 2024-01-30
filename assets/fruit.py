import pygame
import random


class Fruit:
    width = 25
    height = 25
    velocity = 5

    def __init__(self, x, y):
        self.obj = pygame.Rect(x, y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.obj.x, self.obj.y, self.obj.width, self.obj.height))

    def fall(self):
        self.obj.y += self.velocity

    def reset(self, x):
        self.obj.y = 0
        self.obj.x = random.randint(1, x)
