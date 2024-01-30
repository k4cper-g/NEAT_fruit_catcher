import neat
import pygame
import random


def game_over():
    game_font = pygame.font.SysFont('comicsans', 32)
    game_text = game_font.render('Game over!', True, (255, 255, 255))
    # set the center of the rectangular object.
    game_text_rect = game_text.get_rect()
    game_text_rect.center = (width // 2, height // 2)
    screen.blit(game_text, game_text_rect)
    pygame.display.update()
    pygame.time.wait(1000)


pygame.init()
pygame.font.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))

velocity = 5

run = True

bowl = pygame.Rect(200, 550, 200, 25)

rand = random.randint(1, width)

fruit = pygame.Rect(rand, 0, 25, 25)

health = 3

score = 0

font = pygame.font.SysFont('comicsans', 18)

health_text = font.render(f'Health: {health}', True, (255, 255, 255))
health_text_rect = health_text.get_rect()
health_text_rect.center = (60, 20)

score_text = font.render(f'Score: {score}', True, (255, 255, 255))
score_text_rect = score_text.get_rect()
score_text_rect.center = (545, 20)

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and bowl.x > 0:
        bowl.x -= velocity

    if keys[pygame.K_d] and bowl.x < width - bowl.width:
        bowl.x += velocity

    if fruit.y >= height:
        fruit.x = random.randint(1, width-fruit.x)
        fruit.y = 0
        health -= 1
        health_text = font.render(f'Health: {health}', True, (255, 255, 255))

    if fruit.colliderect(bowl):
        score += 1
        fruit.x = random.randint(1, width-fruit.x)
        fruit.y = 0
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))

    if health <= 0:
        game_over()
        score = 0
        health = 3
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        health_text = font.render(f'Health: {health}', True, (255, 255, 255))

    fruit.y = fruit.y + 5

    screen.fill((0, 0, 0))

    screen.blit(health_text, health_text_rect)
    screen.blit(score_text, score_text_rect)
    pygame.draw.rect(screen, (255, 255, 255), (fruit.x, fruit.y, fruit.width, fruit.height))
    pygame.draw.rect(screen, (255, 255, 255), (bowl.x, bowl.y, bowl.width, bowl.height))
    pygame.display.update()

pygame.quit()
