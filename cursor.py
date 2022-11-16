import pygame.sprite


class Cursor(pygame.sprite.Sprite):
    def __init__(self, color, mixer):
        super().__init__()
        self.mixer = mixer
        self.image = pygame.image.load("cursor.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.gun_shoot = pygame.mixer.Sound("GunShotSnglShotEx PE1097508.mp3")
        self.collision_cursor = pygame.sprite.Sprite()

    def update(self, mouse_position):
        # moving the pointer
        self.rect.center = mouse_position
        self.collision_cursor.center = mouse_position

    def shoot(self, cursor, target_group):
        self.gun_shoot.play()
        pygame.sprite.spritecollide(cursor, target_group, True)
