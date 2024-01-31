from assets.game import Game
import pygame
import neat
import os
import pickle

WIDTH, HEIGHT = 600, 600
TICK_RATE = 1000


class FruitCatchGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.bowl = self.game.bowl
        self.fruit = self.game.fruit

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(TICK_RATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.game.move_bowl(True)
            if keys[pygame.K_d]:
                self.game.move_bowl(False)

            output = net.activate(
                (self.bowl.obj.x, self.fruit.obj.y, abs(self.bowl.obj.center[0] - self.fruit.obj.center[0])))

            # print(output)

            decision = output.index(max(output))

            if decision == 0:
                self.game.move_bowl(True)
            else:
                self.game.move_bowl(False)

            self.game.loop()
            self.game.draw()

            if self.game.miss > 0:
                self.game.draw_game_over()
                pygame.time.wait(1000)
                self.game.reset()

            pygame.display.update()

        pygame.quit()

    def train_ai(self, genome, config):
        network = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output = network.activate(
                (self.bowl.obj.x, self.fruit.obj.y, abs(self.bowl.obj.center[0] - self.fruit.obj.center[0])))

            # print(output)

            decision = output.index(max(output))

            if decision == 0:
                self.game.move_bowl(True)
            else:
                self.game.move_bowl(False)

            game_score = self.game.score
            game_miss = self.game.miss

            self.game.loop()
            self.game.draw()
            self.game.draw_score()
            pygame.display.update()

            if game_miss >= 3 or game_score > 50:
                self.calculate_fitness(genome, game_score)
                break

    @staticmethod
    def calculate_fitness(genome, game_score):
        genome.fitness += game_score


def run_game_as_ai(config):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = FruitCatchGame(window, WIDTH, HEIGHT)

    game.test_ai(winner, config)


def eval_genomes(genomes, config):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        game = FruitCatchGame(window, WIDTH, HEIGHT)
        game.train_ai(genome, config)


def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-35')  # run from checkpoint
    # p = neat.Population(config)  # run anew
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 1)

    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.ini")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    # to train ai
    # run_neat(config)

    # to test ai
    run_game_as_ai(config)
