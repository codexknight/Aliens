import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()

        self.image_rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left=False

    def update(self):
        if self.moving_right:
            self.image_rect.x += 1

        if self.moving_left:
            self.image_rect.x -=1

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
