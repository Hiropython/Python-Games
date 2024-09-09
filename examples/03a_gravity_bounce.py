"""
Gravity bounce with x motion

If we add X velocity, the player will bounce around the screen. We will need to
add a check to see if the player hits the left or right side of the screen.

"""
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED=(255,0,0)

# Game settings
PLAYER_SIZE = 20


GRAVITY = 1
JUMP_VELOCITY = 30

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define player
player = pygame.Rect(100, SCREEN_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_y_velocity = 0
player_x_velocity = 10

is_jumping = False


# Main game loop
running = True
clock = pygame.time.Clock()

while running:

    # Handle events, such as quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Continuously jump. If the player is not jumping, may it jump
    if is_jumping is False:
        # Jumping means that the player is going up. The top of the 
        # screen is y=0, and the bottom is y=SCREEN_HEIGHT. So, to go up,
        # we need to have a negative y velocity
        player_y_velocity = -JUMP_VELOCITY
        is_jumping = True

    # If the player hits one side of the screen or the other, bounce the player
    if player.x <= 0 or player.x >= SCREEN_WIDTH - PLAYER_SIZE:
        player_x_velocity = -player_x_velocity

    # If the player hits the top of the screen, bounce the player
    if player.y <= 0:
        player_y_velocity = -player_y_velocity


    # Update player position. Gravity is always pulling the player down,
    # which is the positive y direction, so we add GRAVITY to the y velocity
    # to make the player go up more slowly. Eventually, the player will have
    # a positive y velocity, and gravity will pull the player down.
    player_y_velocity += GRAVITY
    player.y += player_y_velocity
    player.x += player_x_velocity

    # If the player hits the ground, stop the player from falling.
    # The player's position is measured from the top left corner, so the
    # bottom of the player is player.y + PLAYER_SIZE. If the bottom of the
    # player is greater than the height of the screen, the player is on the
    # ground. So, set the player's y position to the bottom of the screen
    # and stop the player from falling
    if player.y >= SCREEN_HEIGHT - PLAYER_SIZE:
        player.y = SCREEN_HEIGHT - PLAYER_SIZE
        player_y_velocity = 0
        is_jumping = False


    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()