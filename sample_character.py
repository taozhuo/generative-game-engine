import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection")

# Load the background image
background_image = pygame.image.load("resources/disco_scene.png")
character_image = pygame.image.load("resources/inkscape.png")


# Get the dimensions of the character image
character_width, character_height = character_image.get_size()

# Define the character's initial position
character_x = screen_width // 2 - character_width // 2
character_y = screen_height // 2 - character_height // 2

# Define an obstacle as a rectangle (x, y, width, height)
obstacle = pygame.Rect(300, 200, 100, 200)

# Character speed
character_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Handle character movement
    dx = dy = 0
    if keys[pygame.K_LEFT]:
        dx -= character_speed
    if keys[pygame.K_RIGHT]:
        dx += character_speed
    if keys[pygame.K_UP]:
        dy -= character_speed
    if keys[pygame.K_DOWN]:
        dy += character_speed

    # Move the character
    new_character_x = character_x + dx
    new_character_y = character_y + dy

    # Define the character's new rectangle after the movement
    character_rect = pygame.Rect(new_character_x, new_character_y, character_width, character_height)

    # Check for collision with the obstacle
    if not character_rect.colliderect(obstacle):
        # No collision, update the character's position
        character_x = new_character_x
        character_y = new_character_y

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the obstacle
    pygame.draw.rect(screen, (255, 0, 0), obstacle)  # Draw the obstacle in red

    # Draw the character
    screen.blit(character_image, (character_x, character_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
