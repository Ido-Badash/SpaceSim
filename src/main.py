# ~~~ main.py ~~~ 

#* ----- NORMAL IMPORTS -----
import sys
import pygame
import traceback
import logging as log
from colorama import Fore

#* ----- LOCAL IMPORTS -----
from utils import timeit, highlight
from runners import SolarSystemRunner

#* ----- LOGGING SETUP -----
current_log_level = log.ERROR
logger = log.getLogger(__name__)
log.basicConfig(level=current_log_level)

#* ----- SETUP -----
# --- Initiation ---
pygame.init()

# --- Set the screen ---
user_screen = pygame.display.Info()
user_w, user_h = user_screen.current_w, user_screen.current_h
user_screen_ratio = user_w / user_h if user_w > user_h else user_h / user_w
user_screen_diff = abs(user_w - user_h)

# Define minimum screen width and height with a ratio of 1:1
min_screen_w = min_screen_h = min(user_w, user_h) / (1.5)
screen_w, screen_h = min_screen_w + 100, min_screen_h + 100
screen = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
fps = 60

#* ----- Create Objects -----
solar_system = SolarSystemRunner(
    surf=screen,
    surf_w=screen_w,
    surf_h=screen_h,
    min_surf_w=min_screen_w,
    min_surf_h=min_screen_h,
    clock=clock, ticks=fps
)

# --- Setup Objects ---
solar_system.setupSolar()

#* ----- FUNCTIONS -----
def main():
    solar_system.run()

@timeit
def entryPoint():
    try:
        running = True
        while running:
            main()
    except Exception as e:
        # Handle exceptions and print traceback
        error_message = f"An error occurred: {e}"
        traceback_message = "".join(traceback.format_exception(None, e, e.__traceback__))
        log.error(highlight(error_message, Fore.RED))
        log.error(highlight(traceback_message, Fore.RED))
    finally:
        log.info("Program has been closed.")
        pygame.quit()
        sys.exit()

#* ----- ENTRY POINT ----- 
if __name__ == "__main__":
    entryPoint()
