import pygame
import random

pygame.init()

# Define colors and window dimensions
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Set up the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Define constants for the snake's size and speed
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Define font style for displaying messages
font_style = pygame.font.SysFont(None, 50)

# Function to display messages on the screen
def display_message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initialize snake's starting position and movement
    snake_x = WINDOW_WIDTH / 2
    snake_y = WINDOW_HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Initialize the snake's body and length
    snake_list = []
    snake_length = 1

    # Initialize food position
    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:
        while game_close:
            window.fill(BLUE)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0

        # Update snake's position
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Draw the game window
        window.fill(BLUE)
        pygame.draw.rect(window, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake's body
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with food or itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake's body
        for segment in snake_list:
            pygame.draw.rect(window, BLACK, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        # Generate new food when snake eats the current one
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
