from pygame import Surface
from pygame import draw
from pygame.sprite import Sprite

from settings import WIDTH, HEIGHT
from settings import GREEN
from settings import SNAKE_SEGMENT_SIZE


class SnakeSegment(Sprite):
    def __init__(self, image_side_size_in_pixels=SNAKE_SEGMENT_SIZE):
        Sprite.__init__(self)
        self.image_side_size_in_pixels = image_side_size_in_pixels
        self.image = Surface((self.image_side_size_in_pixels, self.image_side_size_in_pixels))
        self.__draw_circle_on_surface()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + SNAKE_SEGMENT_SIZE / 2, HEIGHT / 2 + SNAKE_SEGMENT_SIZE / 2)  # coords on the screen

    def __draw_circle_on_surface(self):
        half_size = self.image_side_size_in_pixels / 2
        draw.circle(self.image, GREEN, (half_size, half_size), half_size)
