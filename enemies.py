import pygame

from settings import tile_size, speed


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.Surface((tile_size // 2, tile_size))
        self.image.fill((127, 127, 127))
        self.rect = self.image.get_rect(topleft=(pos[0] * tile_size, pos[1] * tile_size))

    def update(self, direction):
        self.rect = self.rect.move((direction * speed, 0))
