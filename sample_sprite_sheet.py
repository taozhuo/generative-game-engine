import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions and create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the sprite sheet image
sprite_sheet = pygame.image.load("spritesheet.png").convert_alpha()

# Define the size of each sprite (frame) in the sprite sheet
sprite_width = 64
sprite_height = 64

# Define the number of rows and columns in the sprite sheet
num_rows = 4
num_columns = 4

# Extract individual sprites (frames) from the sprite sheet
sprites = []
for row in range(num_rows):
    for column in range(num_columns):
        x = column * sprite_width
        y = row * sprite_height
        sprite = sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
        sprites.append(sprite)

# Set up clock
clock = pygame.time.Clock()

# Define the current frame index and time elapsed since last frame update
current_frame = 0
frame_time = 0

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation
    frame_time += clock.get_time()
    if frame_time > 100:  # Change frame every 100 milliseconds
        frame_time = 0
        current_frame = (current_frame + 1) % len(sprites)

    # Render the current frame
    screen.blit(sprites[current_frame], (WIDTH // 2, HEIGHT // 2))

    # Update display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
