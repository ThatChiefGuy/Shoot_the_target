import random
import pygame
from pygame import mixer
import cursor
import targets


class Game:
    def __init__(self):
        pygame.init()
        self.HEIGHT = 800
        self.WIDTH = 800

        self.background = pygame.image.load("back_ground.png")
        self.background = pygame.transform.scale(self.background, (self.HEIGHT, self.WIDTH))
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        pygame.display.set_caption("testing map")

        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.target_size_x = 100
        self.target_size_y = 100
        pygame.mouse.set_visible(False)
        mixer.music.set_volume(0.2)
        self.target_spawn_time = 0

        self.cursor_group = pygame.sprite.Group()
        self.cursor = cursor.Cursor(self.WHITE, mixer)
        self.cursor_group.add(self.cursor)

        self.target_group = pygame.sprite.Group()

    def add_target(self):
        target = targets.Target(random.randrange(0, self.HEIGHT), random.randrange(0, self.WIDTH))
        self.target_group.add(target)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.target_group.draw(self.screen)
        self.cursor_group.draw(self.screen)
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.cursor.shoot()

        mouse_position = pygame.mouse.get_pos()
        self.cursor_group.update(mouse_position)

        self.add_target()
        self.draw()


if __name__ == "__main__":
    game = Game()
    game.main()
