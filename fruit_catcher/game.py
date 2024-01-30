import random

import pygame
import bowl
import fruit

pygame.init()
pygame.font.init()


class Game:
    # com
    font = pygame.font.SysFont("comicsans", 18)

    def __init__(self, window, width, height):
        self.width = width
        self.height = height

        self.bowl = bowl.Bowl(200, 550)

        randomize = random.Random.randint(1, width)

        self.fruit = fruit.Fruit(randomize, 0)

        self.score = 0

        self.window = window

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.window.blit(score_text, (545, 20))
