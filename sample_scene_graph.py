import pygame
import os

# Define a Node class for the scene graph
class Node:
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent
        self.local_pos = (0, 0)
        if parent:
            parent.add_child(self)
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_global_pos(self):
        if self.parent:
            parent_pos = self.parent.get_global_pos()
            return (parent_pos[0] + self.local_pos[0], parent_pos[1] + self.local_pos[1])
        return self.local_pos

    def draw(self, screen):
        # Override this method in subclasses to draw the sprite or object
        pass

    def update(self):
        # Update this node and its children
        for child in self.children:
            child.update()

# Define a SpriteNode class that extends the Node class
class SpriteNode(Node):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        screen.blit(self.image, self.get_global_pos())
        for child in self.children:
            child.draw(screen)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load sprites and build the scene graph
character = SpriteNode(os.path.join('assets', 'character.png'))
sword = SpriteNode(os.path.join('assets', 'sword.png'), character)
character.local_pos = (200, 200)
sword.local_pos = (50, 0)  # Relative position to the character

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the scene graph
    character.update()

    # Draw the scene graph
    screen.fill((255, 255, 255))
    character.draw(screen)
    pygame.display.flip()

pygame.quit()
