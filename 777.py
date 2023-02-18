import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

# Set up game variables
GRAVITY = 0.5
JUMP_SPEED = 10
MOVE_SPEED = 5
MAX_Y_VELOCITY = 20

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.x_velocity = 0
        self.y_velocity = 0
        self.is_jumping = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Move the player horizontally
        if keys[K_LEFT]:
            self.x_velocity = -MOVE_SPEED
        elif keys[K_RIGHT]:
            self.x_velocity = MOVE_SPEED
        else:
            self.x_velocity = 0

        # Apply gravity to the player's y velocity
        self.y_velocity += GRAVITY

        # Cap the player's y velocity at the maximum value
        if self.y_velocity > MAX_Y_VELOCITY:
            self.y_velocity = MAX_Y_VELOCITY

        # Move the player vertically
        self.rect.y += self.y_velocity

        # Check for collisions with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.y_velocity > 0:
                    self.rect.bottom = platform.rect.top
                    self.y_velocity = 0
                    self.is_jumping = False
                elif self.y_velocity < 0:
                    self.rect.top = platform.rect.bottom
                    self.y_velocity = 0

        # Move the player horizontally
        self.rect.x += self.x_velocity

        # Keep the player on the screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

        # Jump if the player is on a platform and presses the jump key
        if not self.is_jumping and keys[K_SPACE]:
            self.y_velocity = -JUMP_SPEED
            self.is_jumping = True

# Define the Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Set up the platforms
platforms = pygame.sprite.Group()
platforms.add(Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
platforms.add(Platform(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, 20))

# Set up the player
player = Player()

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update game objects
    player
