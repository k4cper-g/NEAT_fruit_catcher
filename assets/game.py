from assets.bowl import Bowl
from assets.fruit import Fruit
import random
import pygame

pygame.init()
pygame.font.init()


class Game:
    font = pygame.font.SysFont("comicsans", 18)

    def __init__(self, window, width, height):
        self.width = width
        self.height = height

        self.bowl = Bowl(200, 550)

        randomize = random.randint(1, width)

        self.fruit = Fruit(randomize, 0)

        self.score = 0

        self.miss = 0

        self.window = window

    def draw(self):
        self.window.fill((0, 0, 0))

        self.draw_score()

        self.bowl.draw(self.window)

        self.fruit.draw(self.window)

    def reset(self):
        self.miss = 0
        self.score = 0

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

    def draw_game_over(self):
        over_text = self.font.render('Game over!', True, (255, 255, 255))
        self.window.blit(over_text, (250, 250))

    def move_bowl(self, left):
        if left and self.bowl.obj.x > 0:
            self.bowl.obj.x -= self.bowl.velocity
        if not left and self.bowl.obj.x < self.width-self.bowl.width:
            self.bowl.obj.x += self.bowl.velocity

    def handle_collision(self):
        if self.fruit.obj.colliderect(self.bowl.obj):
            self.score += 1
            self.fruit.reset(self.width-self.fruit.width*2)

    def loop(self):
        self.fruit.fall()
        self.handle_collision()

        if self.fruit.obj.y >= self.height:
            self.fruit.reset(self.width-(self.fruit.width*2))
            self.miss += 1

        return self.score
