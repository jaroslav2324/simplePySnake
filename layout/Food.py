import pygame
from pygame.sprite import Sprite
from pygame import Surface

from settings import WIDTH, HEIGHT
from settings import SNAKE_SEGMENT_SIZE


class Food(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        center_coord_x = WIDTH / 2
        center_coord_y = HEIGHT / 2
        self.image = Surface((SNAKE_SEGMENT_SIZE, SNAKE_SEGMENT_SIZE))
        pygame.draw.polygon(self.image, (255, 255, 0), [(18, 10), (23, 15), (25, 18), (27, 15), (32, 10), (40, 10),
                                                        (42, 15), (45, 25), (35, 50), (30, 50), (25, 45), (20, 50),
                                                        (15, 50), (5, 25), (8, 15), (10, 10)]
                            )
        self.rect = self.image.get_rect()
        self.rect.center = (center_coord_x, center_coord_y)
