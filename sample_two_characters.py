import pygame


def extract_sprites(sprite_sheet, sprite_width, sprite_height, num_rows, num_columns, padding=0, spacing=0):
    """
    Extract individual sprites from a sprite sheet image.
    
    Args:
        sprite_sheet (pygame.Surface): The sprite sheet image.
        sprite_width (int): The width of each individual sprite.
        sprite_height (int): The height of each individual sprite.
        num_rows (int): The number of rows of sprites in the sprite sheet.
        num_columns (int): The number of columns of sprites in the sprite sheet.
        padding (int, optional): The padding around the sprite sheet. Defaults to 0.
        spacing (int, optional): The spacing between individual sprites. Defaults to 0.

    Returns:
        list[pygame.Surface]: A list of individual sprites extracted from the sprite sheet.
    """
    sprites = []
    for row in range(num_rows):
        for column in range(num_columns):
            # Calculate the position and dimensions of the current sprite
            x = padding + column * (sprite_width + spacing)
            y = padding + row * (sprite_height + spacing)
            sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
            # Extract the sprite from the sprite sheet
            sprite = sprite_sheet.subsurface(sprite_rect)
            # Add the sprite to the list
            sprites.append(sprite)
    return sprites


# Initialize Pygame
pygame.init()


# Set up screen dimensions and create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load and extract sprites for Leia (dancing)
leia_sprite_sheet = pygame.image.load("resources/leia-dancing-small.png").convert_alpha()
leia_sprite_width = 127.5
leia_sprite_height = 226
leia_sprites = extract_sprites(leia_sprite_sheet, leia_sprite_width, leia_sprite_height, num_rows=1, num_columns=4)

# Load and extract sprites for Luke (walking)
luke_sprite_sheet = pygame.image.load("resources/walking-left-small.png").convert_alpha()
luke_sprite_width = 127.75  # Update to match actual sprite width
luke_sprite_height = 237  # Update to match actual sprite height
luke_sprites = extract_sprites(luke_sprite_sheet, luke_sprite_width, luke_sprite_height, num_rows=1, num_columns=4)

# Define character positions and velocities
leia_x = 0
leia_y = HEIGHT // 2 - leia_sprite_height // 2
luke_x = WIDTH - luke_sprite_width  # Luke starts from the right edge
luke_y = HEIGHT // 2 - luke_sprite_height // 2
luke_velocity = -2  # Luke's walking speed (negative to move left)


# Define animation variables
current_frame = 0
frame_time = 0
frame_duration = 100

# Define conversation state and duration
in_conversation = False
conversation_duration = 0
conversation_max_duration = 3000  # Duration in milliseconds
TIMER_EVENT = pygame.USEREVENT + 1

# Set up clock
clock = pygame.time.Clock()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 20)
conversations = [
    "Greetings, Princess! I've heard that you're in trouble here in San Francisco.",
    "Indeed, I am. The situation has become dire, and I'm in need of help.",
    "Fear not, for I am a mighty dinosaur! How may I assist you in escaping this predicament?",
    "The Empire has set a trap for me, and they plan to capture me at any moment. I must leave this city quickly.",
    "I am fast and strong. Climb onto my back, and I will carry you to safety. We'll evade the Empire's grasp.",
    "Thank you, noble dinosaur. I trust in your abilities. Let's make haste!",
    "Hold on tight, Princess! We'll be out of San Francisco in no time."
]
# Define index variable to keep track of the current string
current_index = 0

# Define game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT:
            current_index += 1  # Move to the next string
            if current_index >= len(conversations):
                current_index = 0  # Loop back to the first string

    # Update animation
    if not in_conversation:
        frame_time += clock.tick(60)  # Limit frames per second and get time elapsed
        if frame_time > frame_duration:
            frame_time = 0
            current_frame = (current_frame + 1) % len(leia_sprites)

    # Render Leia (dancing on the left)
    screen.blit(leia_sprites[current_frame], (leia_x, leia_y))

    # Update Luke's position (walking towards the left)
    if not in_conversation:
        luke_x += luke_velocity

    # Render Luke (walking)
    screen.blit(luke_sprites[current_frame], (luke_x, luke_y))

    # Check for collision or meeting between Leia and Luke
    if luke_x <= leia_x + leia_sprite_width and not in_conversation:
        in_conversation = True
        # Define a timer event for updating strings
        pygame.time.set_timer(TIMER_EVENT, 2000)  # 2000 milliseconds (2 seconds)

        luke_velocity = 0  # Stop Luke's movement

    # Display conversation text
    if in_conversation:
        conversation_duration += clock.get_time()
        if current_index < len(conversations):
                # font = pygame.font.Font(None, 36)
                text = my_font.render(conversations[current_index], False, (255, 255, 255))
                # screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                screen.blit(text, (0, 0))

        else:
            # Reset conversation state and duration
            in_conversation = False
            current_index = 0
            conversation_duration = 0
            # Resume Luke's movement towards the left
            luke_velocity = -2
            pygame.time.set_timer(TIMER_EVENT, 0)  # Stop the timer


# font = pygame.font.Font(None, 36)
# text = my_font.render("Hello, Leia! How are you?", False, (255, 255, 255))
# # screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
# screen.blit(text, (0, 0))

    # Update display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
