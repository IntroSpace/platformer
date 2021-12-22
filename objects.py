import pygame

from enemies import Player
from settings import tile_size, FG


class Ground:
    def __init__(self, x, y, w, h, color):
        self.pos = x, y
        self.size = w, h
        self.color = color

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, *self.size))


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super(Tile, self).__init__(*groups)
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(FG)
        self.rect = self.image.get_rect(topleft=(pos[0] * tile_size, pos[1] * tile_size))


class Level:
    def __init__(self, data, *groups):
        self.groups = groups
        self.player = None
        self.new_level(data)

    def new_level(self, data):
        self.level = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for y, arr in enumerate(data):
            for x, tile in enumerate(arr):
                if tile == 'X':
                    Tile((x, y), self.level, *self.groups)
                if tile == 'P':
                    Player((x, y), self.player, *self.groups)

    def get_player(self):
        return self.player

    def draw(self, screen):
        self.level.draw(screen)