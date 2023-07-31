import pygame
import random

# Set up Pygame
pygame.init()

# Game screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake dimensions
BLOCK_SIZE = 20

# Snake speed
SNAKE_SPEED = 15

# Initialize the game window
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Function to draw the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(game_screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to run the game loop
def run_game():
    # Initial position of the snake
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]

    # Initial position of the food
    food_position = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                     random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

    # Initial score
    score = 0

    # Initial direction of the snake
    change_direction = 'RIGHT'
    change = change_direction

    # Game over flag
    game_over = False

    # Clock to control game speed
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_direction = 'RIGHT'
                elif event.key == pygame.K_UP:
                    change_direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_direction = 'DOWN'

        # Change the direction only if it's not opposite to the current direction
        if change_direction == 'LEFT' and not change == 'RIGHT':
            change = 'LEFT'
        elif change_direction == 'RIGHT' and not change == 'LEFT':
            change = 'RIGHT'
        elif change_direction == 'UP' and not change == 'DOWN':
            change = 'UP'
        elif change_direction == 'DOWN' and not change == 'UP':
            change = 'DOWN'

        # Update the position of the snake
        if change == 'LEFT':
            snake_position[0] -= BLOCK_SIZE
        elif change == 'RIGHT':
            snake_position[0] += BLOCK_SIZE
        elif change == 'UP':
            snake_position[1] -= BLOCK_SIZE
        elif change == 'DOWN':
            snake_position[1] += BLOCK_SIZE

        # Snake body growth
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_position = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                             random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        else:
            snake_body.pop()

        # Draw everything on the game screen
        game_screen.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(game_screen, RED, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])

        # Game over conditions
        if snake_position[0] >= SCREEN_WIDTH or snake_position[0] < 0 or snake_position[1] >= SCREEN_HEIGHT or snake_position[1] < 0:
            game_over = True
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over = True

        # Update the display
        pygame.display.update()

        # Control game speed
        clock.tick(SNAKE_SPEED)

    # Display final score
    font = pygame.font.SysFont(None, 25)
    text = font.render("Your score: " + str(score), True, WHITE)
    game_screen.blit(text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.display.update()

    # Wait for a short moment before closing the game
    pygame.time.wait(1000)

# Run the game
run_game()

# Quit Pygame
pygame.quit()