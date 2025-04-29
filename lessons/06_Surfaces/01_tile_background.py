"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame
import math
import time

# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')

def make_tiled_bg(screen, bg_file,stripes=2):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    stripe_width = bg_tile.get_width()/stripes
    for i in range (stripes):
        bg_tile.fill((0, i*255/stripes, 18),(math.ceil(i*stripe_width),0,math.ceil(stripe_width),(bg_tile.get_height())))
    

    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image


stripes=2
# Main loop
running = True
while running:
    background = make_tiled_bg(screen, assets/'background_tile.gif',stripes)
    
    stripes=stripes*2
    if stripes>255:
        stripes=2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    # Update the display
    pygame.display.flip()
    time.sleep(3)

# Quit Pygame
pygame.quit()
