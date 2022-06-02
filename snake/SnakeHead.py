from pygame import draw

from settings import RED
from settings import SNAKE_SEGMENT_SIZE
from SnakeSegment import SnakeSegment


class SnakeHead(SnakeSegment):
    def __init__(self, image_side_size_in_pixels=SNAKE_SEGMENT_SIZE):
        SnakeSegment.__init__(self, image_side_size_in_pixels)
        self.__draw_circle_on_surface()

    def __draw_circle_on_surface(self):
        half_size = self.image_side_size_in_pixels / 2
        draw.circle(self.image, RED, (half_size, half_size), half_size)
