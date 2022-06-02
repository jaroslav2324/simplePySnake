from pygame.sprite import Sprite
from pygame import Surface

from settings import EMPTY_TILE, WALL_TILE, FOOD_TILE, SNAKE_TILE
from settings import SNAKE_SEGMENT_SIZE
from settings import BLACK, GREY


class GridTile(Sprite):
    def __init__(self, x_coord, y_coord, type_tile=EMPTY_TILE):
        Sprite.__init__(self)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type_tile = type_tile

        self.image = Surface((SNAKE_SEGMENT_SIZE, SNAKE_SEGMENT_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

        if self.type_tile == WALL_TILE:
            self.image.fill(GREY)

