from assets.game import Game
import pygame


class FruitCatchGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.bowl = self.game.bowl
        self.fruit = self.game.fruit

    def test_ai(self):

        # width, height = 600, 600
        # window = pygame.display.set_mode((width, height))
        #
        # game = Game(window, width, height)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.game.move_bowl(True)
            if keys[pygame.K_d]:
                self.game.move_bowl(False)

            self.game.loop()
            self.game.draw()
            pygame.display.update()

        pygame.quit()


width, height = 600, 600
window = pygame.display.set_mode((width, height))
f = FruitCatchGame(window, width, height)
f.test_ai()
