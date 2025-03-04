"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path

# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

# Screen dimensions
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")

# Colors

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FPS
FPS = 60

# Player attributes
class Settings:
    gravity=0.3
PLAYER_SIZE = 50

player_speed = 5

# Obstacle attributes
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 60
obstacle_speed = 5

# Font
font = pygame.font.SysFont(None, 36)


# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - OBSTACLE_HEIGHT 
        self.game=game
        self.cactus=pygame.image.load(images_dir/"cactus_9.png")
        self.explosion = pygame.image.load(images_dir / "explosion1.gif")
        self.image=self.cactus
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.x -= obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()
            self.game.obstacle_count=self.game.obstacle_count+1

    def explode(self):
        """Replace the image with an explosition image."""
        OBSTACLE_HEIGHT=20
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)
         
         


# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
        self.y_vel=0
        self.dino=pygame.image.load(images_dir / "dino_0.png")
        self.image=self.dino
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect(center=self.rect.center)
        

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.y= self.rect.y-self.y_vel
        self.y_vel=self.y_vel-Settings.gravity
        #if keys[pygame.K_UP]:
            #self.rect.y -= self.speed
        
       
                
            

        #if keys[pygame.K_DOWN]:
            #self.rect.y += self.speed

        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
            self.y_vel=0
            if keys[pygame.K_SPACE]:
                self.y_vel=8
class Game:
# Create a player object
    def __init__ (self):
        self.obstacles = pygame.sprite.Group()

        

        self.obstacle_count = 0
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)

    # Add obstacles periodically
    def add_obstacle(self):
        # random.random() returns a random float between 0 and 1, so a value
        # of 0.25 means that there is a 25% chance of adding an obstacle. Since
        # add_obstacle() is called every 100ms, this means that on average, an
        # obstacle will be added every 400ms.
        # The combination of the randomness and the time allows for random
        # obstacles, but not too close together. 
        
        if random.random() < 0.4:
            obstacle = Obstacle(self)
            self.obstacles.add(obstacle)
            return 1
        return 0


    # Main game loop
    def game_loop(self):
        clock = pygame.time.Clock()
        game_over = False
        last_obstacle_time = pygame.time.get_ticks()

        # Group for obstacles
        

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            # Update player
            self.player.update()

            # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 500:
                last_obstacle_time = pygame.time.get_ticks()
                #self.obstacle_count += 
                self.add_obstacle()
            
            self.obstacles.update()

            # Check for collisions
            collider = pygame.sprite.spritecollide(self.player, self.obstacles, dokill=False)
            if collider:
                collider[0].explode()
                game_over=True

        
            # Draw everything
            screen.fill(WHITE)
            #pygame.draw.rect(screen, BLUE, self.player)
            self.obstacles.draw(screen)
            self.player_group.draw(screen)

            # Display obstacle count
            obstacle_text = font.render(f"Score: {self.obstacle_count}", True, BLACK)
            screen.blit(obstacle_text, (10, 10))

            pygame.display.update()
            clock.tick(FPS)

        # Game over screen
        screen.fill(WHITE)

if __name__ == "__main__":
    Game ().game_loop()
    while True:
        obstacle_text = font.render("Game over", True, BLACK)
        screen.blit(obstacle_text, (WIDTH/2, HEIGHT/2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
