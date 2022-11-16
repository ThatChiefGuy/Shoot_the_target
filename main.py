import random
import pygame
from pygame import mixer
import cursor
import targets


class Game:
    def __init__(self, screen_height, screen_width):

        mixer.init()
        pygame.init()
        self.HEIGHT = screen_height
        self.WIDTH = screen_width

        self.background = pygame.image.load("back_ground.png")
        self.background = pygame.transform.scale(self.background, (self.HEIGHT, self.WIDTH))
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        pygame.display.set_caption("testing map")

        pygame.mouse.set_visible(False)
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.target_size_x = 100
        self.target_size_y = 100
        mixer.music.set_volume(0.2)
        self.current_time = 0
        self.target_spawn_time = 0
        self.current_time = 0
        self.target_spawn_time = 0

        self.cursor_group = pygame.sprite.Group()
        self.cursor = cursor.Cursor(self.WHITE, mixer)
        self.cursor_group.add(self.cursor)
        self.target_group = pygame.sprite.Group()

    def add_target(self):
        target = targets.Target(random.randrange(0, game.HEIGHT), random.randrange(0, game.WIDTH))
        self.target_group.add(target)
        self.target_spawn_time = self.current_time

    def draw(self):
        self.screen.fill(self.BLUE)
        self.screen.blit(self.background, (0, 0))
        self.target_group.draw(self.screen)
        self.cursor_group.draw(self.screen)
        pygame.display.update()


game = Game(800, 800)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                game.cursor.shoot(game.cursor, game.target_group)

        mouse_position = pygame.mouse.get_pos()
        game.cursor_group.update(mouse_position)

        game.current_time = pygame.time.get_ticks()

        if game.current_time - game.target_spawn_time > 1000:
            game.add_target()

        game.draw()


if __name__ == "__main__":
    main()
