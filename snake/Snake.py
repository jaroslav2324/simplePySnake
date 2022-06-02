from SnakeHead import SnakeHead
from SnakeSegment import SnakeSegment
from SnakeTail import SnakeTail

from settings import SNAKE_SEGMENT_SIZE
from settings import UP, DOWN, RIGHT, LEFT


class Snake:
    def __init__(self):
        self.snake_head = SnakeHead()
        self.snake_tail = None
        self.list_segments = [self.snake_head]
        self.__calculate_len()
        self.error_status = 0

        self.prev_direction = RIGHT

    def add_segments_to_group(self, destination_group):
        for segment in self.list_segments:
            destination_group.add(segment)

    def __add_new_segment_to_group(self, destination_group, segment):
        destination_group.add(segment)

    def growth_snake(self, grid, sprite_group):
        if self.len == 1:
            self.snake_tail = SnakeTail()
            self.list_segments.append(self.snake_tail)
            # self.__calculate_tail_position(grid)
            self.__calculate_len()
            sprite_group.add(self.snake_tail)
            return
        if self.len > 1:
            snake_seg = SnakeSegment()
            self.snake_tail = self.list_segments.pop(self.len - 1)
            snake_seg.rect.center = self.snake_tail.rect.center
            self.list_segments.append(snake_seg)
            self.list_segments.append(self.snake_tail)
            self.__calculate_tail_position(grid)
            self.__calculate_len()
            sprite_group.add(snake_seg)

    def move_forward(self, direction):
        for seg_index in range(self.len - 1, 0, -1):
            self.list_segments[seg_index].rect.center = self.list_segments[seg_index - 1].rect.center

        if direction == UP:
            if self.prev_direction != DOWN:
                self.snake_head.rect.center = (self.snake_head.rect.center[0],
                                               self.snake_head.rect.center[1] - SNAKE_SEGMENT_SIZE)
                self.prev_direction = UP
            else:
                self.snake_head.rect.center = (self.snake_head.rect.center[0],
                                               self.snake_head.rect.center[1] + SNAKE_SEGMENT_SIZE)
            return
        if direction == DOWN:
            if self.prev_direction != UP:
                self.snake_head.rect.center = (self.snake_head.rect.center[0],
                                               self.snake_head.rect.center[1] + SNAKE_SEGMENT_SIZE)
                self.prev_direction = DOWN
            else:
                self.snake_head.rect.center = (self.snake_head.rect.center[0],
                                               self.snake_head.rect.center[1] - SNAKE_SEGMENT_SIZE)
            return
        if direction == RIGHT:
            if self.prev_direction != LEFT:
                self.snake_head.rect.center = (self.snake_head.rect.center[0] + SNAKE_SEGMENT_SIZE,
                                               self.snake_head.rect.center[1])
                self.prev_direction = RIGHT
            else:
                self.snake_head.rect.center = (self.snake_head.rect.center[0] - SNAKE_SEGMENT_SIZE,
                                               self.snake_head.rect.center[1])
            return
        if direction == LEFT:
            if self.prev_direction != RIGHT:
                self.snake_head.rect.center = (self.snake_head.rect.center[0] - SNAKE_SEGMENT_SIZE,
                                               self.snake_head.rect.center[1])
                self.prev_direction = LEFT
            else:
                self.snake_head.rect.center = (self.snake_head.rect.center[0] + SNAKE_SEGMENT_SIZE,
                                               self.snake_head.rect.center[1])
            return

    def __calculate_len(self):
        self.len = len(self.list_segments)

    # calculate tail position depending on the wall position
    def __calculate_tail_position(self, grid):
        if self.len > 2:
            coords_segment_before_tail = self.list_segments[-2].rect.center
            coords_segment_before_tail2 = self.list_segments[-3].rect.center

            tail_coords = (0, 0)
            # check direction of growth
            if coords_segment_before_tail2[0] - coords_segment_before_tail[0] == 0:
                if coords_segment_before_tail2[1] - coords_segment_before_tail[1] == SNAKE_SEGMENT_SIZE:
                   tail_coords = (coords_segment_before_tail[0], coords_segment_before_tail[1] - SNAKE_SEGMENT_SIZE)
                else:
                    tail_coords = (coords_segment_before_tail[0], coords_segment_before_tail[1] + SNAKE_SEGMENT_SIZE)
            if coords_segment_before_tail2[1] - coords_segment_before_tail[1] == 0:
               if coords_segment_before_tail2[0] - coords_segment_before_tail[0] == SNAKE_SEGMENT_SIZE:
                   tail_coords = (coords_segment_before_tail[0] - SNAKE_SEGMENT_SIZE, coords_segment_before_tail[1])
               else:
                   tail_coords = (coords_segment_before_tail[0] + SNAKE_SEGMENT_SIZE, coords_segment_before_tail[1])
        else:
            if self.prev_direction == UP:
                tail_coords = (self.snake_head.rect.center[0], self.snake_head.rect.center[1] + 2 * SNAKE_SEGMENT_SIZE)
            if self.prev_direction == DOWN:
                tail_coords = (self.snake_head.rect.center[0], self.snake_head.rect.center[1] - 2 * SNAKE_SEGMENT_SIZE)
            if self.prev_direction == RIGHT:
                tail_coords = (self.snake_head.rect.center[0] - 2 * SNAKE_SEGMENT_SIZE, self.snake_head.rect.center[1])
            if self.prev_direction == LEFT:
                tail_coords = (self.snake_head.rect.center[0] + 2 * SNAKE_SEGMENT_SIZE, self.snake_head.rect.center[1])

        # check walls

        if not grid.if_tile_wall(tail_coords[0], tail_coords[1]):
            self.snake_tail.rect.center = tail_coords
            return

        # if wall check tiles around pre-tail segment
        tail_coords = (self.list_segments[-2].rect.center[0] + SNAKE_SEGMENT_SIZE,
                       self.list_segments[-2].rect.center[1])

        if not grid.if_tile_wall(tail_coords[0], tail_coords[1]) and \
                not grid.if_tile_snake(tail_coords[0], tail_coords[1]):
            self.snake_tail.rect.center = tail_coords
            return

        tail_coords = (self.list_segments[-2].rect.center[0] - SNAKE_SEGMENT_SIZE,
                       self.list_segments[-2].rect.center[1])

        if not grid.if_tile_wall(tail_coords[0], tail_coords[1]) and \
                not grid.if_tile_snake(tail_coords[0], tail_coords[1]):
            self.snake_tail.rect.center = tail_coords
            return

        tail_coords = (self.list_segments[-2].rect.center[0],
                       self.list_segments[-2].rect.center[1] - SNAKE_SEGMENT_SIZE)

        if not grid.if_tile_wall(tail_coords[0], tail_coords[1]) and \
                not grid.if_tile_snake(tail_coords[0], tail_coords[1]):
            self.snake_tail.rect.center = tail_coords
            return

        tail_coords = (self.list_segments[-2].rect.center[0],
                       self.list_segments[-2].rect.center[1] + SNAKE_SEGMENT_SIZE)

        if not grid.if_tile_wall(tail_coords[0], tail_coords[1]) and \
                not grid.if_tile_snake(tail_coords[0], tail_coords[1]):
            self.snake_tail.rect.center = tail_coords
            return

        # if something goes wrong
        self.error_status = -1

    # check head != wall after moving
    def if_death_comes(self, grid):
        if grid.if_tile_wall(self.snake_head.rect.center[0], self.snake_head.rect.center[1]):
            return True
        if self.__snake_bumped_into_segment():
            return True
        else:
            return False

    def if_food_consumed(self, grid):
        if grid.if_tile_food(self.snake_head.rect.center[0], self.snake_head.rect.center[1]):
            return True
        else:
            return False

    def __snake_bumped_into_segment(self):
        if self.len < 4:
            return False
        for i in range(1, self.len):
            if self.list_segments[i].rect.center == self.snake_head.rect.center:
                return True
        return False
