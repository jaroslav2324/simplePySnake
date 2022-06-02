import pygame

from snake.Snake import Snake
from layout.Grid import Grid
from layout.Food import Food

from settings import *


def make_game_turn(snake_, grid_, moving_direction, snake_sprite_group):
    grid_.print_grid_types()
    # check food consumption
    if snake_.if_food_consumed(grid):
        # growth
        snake_.growth_snake(grid, snake_sprite_group)
        # update grid
        grid_.update_grid(snake)
        # generate food
        grid_.generate_food()
    else:
        # update grid
        grid_.update_grid(snake)

    # move snake
    snake_.move_forward(moving_direction)

    # check death
    if snake_.if_death_comes(grid):
        # end game menu
        quit()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
snake_sprites = pygame.sprite.Group()
food_sprites = pygame.sprite.Group()
grid_sprites = pygame.sprite.Group()

snake = Snake()
snake.add_segments_to_group(snake_sprites)

food = Food()
food_sprites.add(food)

grid = Grid(food)
for row in grid.grid:
    for tile in row:
        grid_sprites.add(tile)

grid.update_grid(snake)
grid.generate_food()

running = True
while running:

    screen.fill(BLACK)

    grid_sprites.draw(screen)
    # grid_sprites.update()
    food_sprites.draw(screen)
    snake_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

    last_chosen_direction = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                last_chosen_direction = LEFT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                last_chosen_direction = RIGHT
            if event.key == pygame.K_DELETE or event.key == pygame.K_s:
                last_chosen_direction = DOWN
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                last_chosen_direction = UP

    if last_chosen_direction is None:
        make_game_turn(snake, grid, snake.prev_direction, snake_sprites)
    else:
        make_game_turn(snake, grid, last_chosen_direction, snake_sprites)

pygame.quit()
