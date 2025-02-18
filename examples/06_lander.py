import pygame
import math
from pathlib import Path

assets = Path(__file__).parent / "assets"

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Lunar Lander")

# Lander settings
lander_w = 75
lander_h = 75
lander_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 4)
lander_angle = 0
lander_velocity = pygame.Vector2(0, 0)
lander_acceleration = 0.2
lander_rotation_speed = 5
   
# Load and scale the lander image
lander_image = pygame.image.load(assets/'alien1.gif')

# Scale the image to make it a given height and width
lander_image = pygame.transform.scale(lander_image, (lander_w, lander_h))

gravity = pygame.Vector2(0, 0.1)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Function to draw the rotated lander
def draw_lander(screen, position, angle):

    # Rotate the lander image.     
    rotated_image = pygame.transform.rotate(lander_image, -angle)
    rotated_rect = rotated_image.get_rect(center=position)
    screen.blit(rotated_image, rotated_rect.topleft)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Stop the lander at the bottom of the screen
    if lander_pos.y >= HEIGHT - (lander_h/2):  # 37.5 is half the height of the scaled lander
        lander_pos.y = HEIGHT - (lander_h/2)
        lander_velocity = pygame.Vector2(0, 0)

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        lander_angle -= lander_rotation_speed
    if keys[pygame.K_RIGHT]:
        lander_angle += lander_rotation_speed
    if keys[pygame.K_SPACE]:
        # Apply thrust in the direction the lander is facing
        thrust_direction = pygame.Vector2(0, -1).rotate(lander_angle)
        lander_velocity += thrust_direction * lander_acceleration

    # Apply gravity
    lander_velocity += gravity

    # Update lander position
    lander_pos += lander_velocity

    # Drawing
    screen.fill((0, 0, 0))
    draw_lander(screen, lander_pos, lander_angle)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
