import sys
import pygame


def run_game():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Aliens Invasion")


if __name__ == '__main__':
    ai = AlienInvasion()
    run_game()
