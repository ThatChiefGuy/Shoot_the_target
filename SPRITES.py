import pygame
import basics


class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__()
        self.x = x * basics.TILE_SIZE
        self.y = y * basics.TILE_SIZE
        self.width = basics.TILE_SIZE
        self.height = basics.TILE_SIZE
        self.group = group

        self.image = pygame.image.load("enmy.png")
        self.image_resized = pygame.transform.scale(self.image, (basics.TILE_SIZE, basics.TILE_SIZE))
        self.image.fill(basics.RED)

        self.rect = self.image_resized.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
