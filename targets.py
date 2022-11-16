import pygame.sprite


class Target(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.size_x = 150
        self.size_y = 150
        self.image = pygame.image.load("target.png")
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position_x, position_y
        self.target_spawn_time = 0
        self.current_time = 0



