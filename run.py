import requests
import time
import subprocess
import pygame
import sys

API_URL = "https://rishavkumar.io/gradcap/get"
CHECK_INTERVAL = 3  # in seconds

# Initialize pygame for the loading screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Loading...')
font = pygame.font.Font(None, 60)
loading_text = font.render("Loading...", True, (255, 255, 255))
loading_text_rect = loading_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

def show_loading_screen():
    screen.fill((0, 0, 0))
    screen.blit(loading_text, loading_text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# This will hold the current process that's running
current_process = None
# This will store the last result from the API
last_result = None

while True:
    try:
        # Call the API
        response = requests.get(API_URL)
        if response.status_code == 200:
            result = response.text.strip()

            # Check if the result has changed
            if result != last_result:
                last_result = result

                # If there's a process running, terminate it
                if current_process:
                    current_process.terminate()
                    current_process.wait()

                show_loading_screen()

                # Based on the API response, run the appropriate script
                if result == "congrats":
                    current_process = subprocess.Popen(["python3", "congrats.py"])
                elif result == "forksup_sliding":
                    current_process = subprocess.Popen(["python3", "forksup_sliding.py"])
                elif result == "asugrad":
                    current_process = subprocess.Popen(["python3", "asugrad.py"])

        # Wait for the interval before checking again
        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(CHECK_INTERVAL)
