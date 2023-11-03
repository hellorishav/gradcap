import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Define the colors using ASU's maroon and gold
MAROON = (140, 29, 64)
GOLD = (255, 198, 39)

# Screen settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set to fullscreen mode
window_width, window_height = screen.get_size()

pygame.display.set_caption('ASU Pride!')

message = "#ASUGrad"

base_font_size = window_width // 4
font = pygame.font.Font(None, base_font_size)

# Variables for pulsating effect
pulsate_speed = 0.05
pulsate_direction = 1
pulsate_max = 1.2  # max scale
pulsate_min = 0.8  # min scale
current_scale = 1

# Variables for color shift
color_shift_speed = 0.05
current_color = GOLD

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

    # Pulsating effect
    current_scale += pulsate_speed * pulsate_direction
    if current_scale > pulsate_max or current_scale < pulsate_min:
        pulsate_direction *= -1

    scaled_font_size = int(base_font_size * current_scale)
    scaled_font = pygame.font.Font(None, scaled_font_size)
    message_surface = scaled_font.render(message, True, current_color)
    message_rect = message_surface.get_rect(center=(window_width / 2, window_height / 2))

    # Color shift effect
    if current_color == GOLD:
        current_color = MAROON
    else:
        current_color = GOLD

    # Drawing
    screen.fill(MAROON)
    screen.blit(message_surface, message_rect)
    
    pygame.display.flip()

    clock.tick(60)
