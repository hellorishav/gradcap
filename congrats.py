import pygame
import sys

# Initialize pygame
pygame.init()

# Define the colors
MAROON = (140, 29, 64)
GOLD = (255, 198, 39)

# Screen settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set to fullscreen mode
window_width, window_height = screen.get_size()

pygame.display.set_caption('ASU Pride!')

# Variables for color pulse
current_bg_color = MAROON
current_text_color = GOLD
color_change_timer = 0
color_change_interval = 2000  # 2 seconds in milliseconds

messages = ["Congrats!", "Class of '23", "Forks Up!"]
current_message_index = 0

def get_optimal_font_size(message):
    font_size = window_height
    font = pygame.font.Font(None, font_size)
    text_width, text_height = font.size(message)
    
    while text_width > window_width or text_height > window_height:
        font_size -= 10
        font = pygame.font.Font(None, font_size)
        text_width, text_height = font.size(message)

    return font_size

current_font_size = get_optimal_font_size(messages[current_message_index])
font = pygame.font.Font(None, current_font_size)

current_text = font.render(messages[current_message_index], True, current_text_color)
current_text_rect = current_text.get_rect()
current_text_rect.center = (window_width // 2, window_height // 2)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)  # Returns milliseconds since last frame
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Escape mechanism to close the fullscreen window
                pygame.quit()
                sys.exit()

    # Color pulse effect
    color_change_timer += dt
    if color_change_timer >= color_change_interval:
        color_change_timer = 0
        current_bg_color, current_text_color = current_text_color, current_bg_color
        
        # Update message to display
        current_message_index = (current_message_index + 1) % 3
        current_font_size = get_optimal_font_size(messages[current_message_index])
        font = pygame.font.Font(None, current_font_size)

        current_text = font.render(messages[current_message_index], True, current_text_color)
        current_text_rect = current_text.get_rect()
        current_text_rect.center = (window_width // 2, window_height // 2)

    # Drawing
    screen.fill(current_bg_color)
    screen.blit(current_text, current_text_rect)
    
    pygame.display.flip()
