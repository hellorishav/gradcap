import pygame
import sys

# Initialize pygame
pygame.init()

# Define the colors using hexadecimal values
MAROON = pygame.Color("#8C1D40")
GOLD = pygame.Color("#FFC627")

# Screen settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set to fullscreen mode
window_width, window_height = screen.get_size()

pygame.display.set_caption('ASU Pride!')

message = "Forks Up ASUUUUUUUU!!!!!"
slide_speed = 30

def get_optimal_font_size(message):
    font_size = window_height
    font = pygame.font.Font(None, font_size)
    text_width, text_height = font.size(message)
    
    while text_height > window_height:
        font_size -= 10
        font = pygame.font.Font(None, font_size)
        _, text_height = font.size(message)

    return font_size

font_size = get_optimal_font_size(message)
font = pygame.font.Font(None, font_size)
text = font.render(message, True, GOLD)
text_rect = text.get_rect()
text_rect.y = (window_height - text_rect.height) // 2
text_rect.right = window_width

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Escape mechanism to close the fullscreen window
                pygame.quit()
                sys.exit()

    # Move the text from right to left for sliding effect
    text_rect.x -= slide_speed
    if text_rect.right < 0:
        text_rect.left = window_width

    # Drawing
    screen.fill(MAROON)
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    clock.tick(60)
