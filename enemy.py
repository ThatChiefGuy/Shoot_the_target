import pygame.sprite
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, screen):
        super().__init__()
        self.enemy_color = (63, 72, 204)
        self.image = pygame.image.load("enmy.png").convert_alpha(screen)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.set_colorkey(self.enemy_color)
        self.rect = self.image.get_rect()
        self.rect.center = [position_x, position_y]

    def update(self):
        print("j")

