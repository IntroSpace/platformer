import sys

import pygame
from pygame.locals import *
from objects import Ground, Level
from settings import W, H, level, dt

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

level = Level(level(), all_sprites)
player = level.get_player()


def update(dt):
    direct = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                direct = -1
            if event.key == K_RIGHT:
                direct = 1

    player.update(direct * dt)


def draw(screen):
    screen.fill((0, 0, 0))

    # ground.draw(screen)
    # player.draw(screen)
    all_sprites.draw(screen)
    # player.draw(screen)

    pygame.display.flip()


def run_game():
    pygame.init()
    pygame.key.set_repeat(100, 100)

    fps = 60
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN, vsync=1)

    while True:
        update(dt)
        draw(screen)

        clock.tick(fps)


run_game()
