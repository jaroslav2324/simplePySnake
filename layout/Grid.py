import random

from settings import HEIGHT, WIDTH
from settings import SNAKE_SEGMENT_SIZE
from settings import EMPTY_TILE, WALL_TILE, FOOD_TILE, SNAKE_TILE
from GridTile import GridTile


class Grid:
    def __init__(self, food):
        self.grid = []
        self.__make_empty_grid()
        self.food = food
        row_food_position = self.__pixels_to_grid_coord(WIDTH / 2 + SNAKE_SEGMENT_SIZE / 2)
        column_food_position = self.__pixels_to_grid_coord(HEIGHT / 2 + SNAKE_SEGMENT_SIZE / 2)
        self.food_position = (row_food_position, column_food_position)
        food.rect.center = self.food_position

    def place_snake_on_tiles(self, snake):
        for segment in snake.list_segments:
            seg_coord_grid_x = self.__pixels_to_grid_coord(segment.rect.center[0])
            seg_coord_grid_y = self.__pixels_to_grid_coord(segment.rect.center[1])
            self.grid[seg_coord_grid_x][seg_coord_grid_y].type_tile = SNAKE_TILE

    def generate_food(self):
        # choose tile where food will be placed
        width_field = len(self.grid[0])
        height_field = len(self.grid)
        num_free_tiles = width_field * height_field

        random_pos = random.randint(0, num_free_tiles - 1)

        row = random_pos / width_field
        column = random_pos % width_field

        while self.grid[row][column].type_tile != EMPTY_TILE:
            random_pos = random.randint(0, num_free_tiles - 1)
            row = random_pos / width_field
            column = random_pos % width_field

        self.food_position = (row, column)
        self.food.rect.center = (self.__grid_coord_to_pixels(row), self.__grid_coord_to_pixels(column))

        self.grid[row][column].type_tile = FOOD_TILE
        return row, column

    # coords in pixels
    def if_tile_wall(self, coord_x_in_pixels, coord_y_in_pixels):
        grid_coord_x = self.__pixels_to_grid_coord(coord_x_in_pixels)
        grid_coord_y = self.__pixels_to_grid_coord(coord_y_in_pixels)
        if self.grid[grid_coord_x][grid_coord_y].type_tile == WALL_TILE:
            return True
        else:
            return False

    # coords in pixels
    def if_tile_snake(self, coord_x_in_pixels, coord_y_in_pixels):
        grid_coord_x = self.__pixels_to_grid_coord(coord_x_in_pixels)
        grid_coord_y = self.__pixels_to_grid_coord(coord_y_in_pixels)
        if self.grid[grid_coord_x][grid_coord_y].type_tile == SNAKE_TILE:
            return True
        else:
            return False

    # coords in pixels
    def if_tile_food(self, coord_x_in_pixels, coord_y_in_pixels):
        grid_coord_x = self.__pixels_to_grid_coord(coord_x_in_pixels)
        grid_coord_y = self.__pixels_to_grid_coord(coord_y_in_pixels)
        if self.grid[grid_coord_x][grid_coord_y].type_tile == FOOD_TILE:
            return True
        else:
            return False

    def if_tile_empty(self, coord_x_in_pixels, coord_y_in_pixels):
        grid_coord_x = self.__pixels_to_grid_coord(coord_x_in_pixels)
        grid_coord_y = self.__pixels_to_grid_coord(coord_y_in_pixels)
        if self.grid[grid_coord_x][grid_coord_y].type_tile == EMPTY_TILE:
            return True
        else:
            return False

    def __pixels_to_grid_coord(self, pixels):
        return (pixels - SNAKE_SEGMENT_SIZE / 2) / SNAKE_SEGMENT_SIZE

    def __grid_coord_to_pixels(self, coord):
        return coord * SNAKE_SEGMENT_SIZE + SNAKE_SEGMENT_SIZE / 2

    def update_grid(self, snake):
        self.__make_empty_grid()
        self.grid[self.food_position[0]][self.food_position[1]].type_tile = FOOD_TILE
        self.place_snake_on_tiles(snake)

    # only walls and empty tiles
    def __make_empty_grid(self):
        self.grid = []
        num_row = -1
        for pos_y in range(SNAKE_SEGMENT_SIZE / 2, HEIGHT, SNAKE_SEGMENT_SIZE):
            num_row += 1
            row = []
            for pos_x in range(SNAKE_SEGMENT_SIZE / 2, WIDTH, SNAKE_SEGMENT_SIZE):
                if pos_y == SNAKE_SEGMENT_SIZE / 2 or pos_y == HEIGHT - SNAKE_SEGMENT_SIZE / 2 \
                        or pos_x == SNAKE_SEGMENT_SIZE / 2 or pos_x == WIDTH - SNAKE_SEGMENT_SIZE / 2:
                    # may cause some troubles if WIDTH or HEIGHT changed
                    tile = GridTile(pos_x, pos_y, type_tile=WALL_TILE)
                else:
                    tile = GridTile(pos_x, pos_y)
                row.append(tile)
            self.grid.append(row)

    def print_grid_types(self):
        for row in self.grid:
            l = []
            for tile in row:
                l.append(tile.type_tile)
            print(l)
        print ('\n')

