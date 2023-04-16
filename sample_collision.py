import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 800, 600

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Define player and enemy rectangles
player = pygame.Rect(400, 300, 50, 50)
enemy = pygame.Rect(200, 200, 50, 50)

# Set up clock
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)

# Define conversation text
conversation_text = None

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player.move_ip(0, 5)

    # Enemy movement (random)
    enemy.move_ip(random.randint(-3, 3), random.randint(-3, 3))

    # Collision detection and conversation
    if player.colliderect(enemy):
        conversation_text = "Player: Hi! How are you? | Enemy: I'm good, thanks!"
        # Collision resolution: move player outside of enemy rectangle
        if player.centerx < enemy.centerx:
            player.right = enemy.left
        elif player.centerx > enemy.centerx:
            player.left = enemy.right
        if player.centery < enemy.centery:
            player.bottom = enemy.top
        elif player.centery > enemy.centery:
            player.top = enemy.bottom
    else:
        conversation_text = None

    # Rendering
    pygame.draw.rect(screen, BLUE, player)  # Draw player
    pygame.draw.rect(screen, RED, enemy)    # Draw enemy

    # Render conversation text if it exists
    if conversation_text:
        text_surface = font.render(conversation_text, True, WHITE)
        screen.blit(text_surface, (10, 10))

    # Update display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
