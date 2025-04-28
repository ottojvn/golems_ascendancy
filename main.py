import sys
import pygame
# Import init_ui from render, not config
from interface.render import init_ui
from game.game_loop import run_game

WINDOW_TITLE = "Golems Ascendancy"
# Define default dimensions here for initial screen creation
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720

def main():
    """Initializes Pygame, sets up the screen and clock, loads UI config, and starts the game loop."""
    pygame.init()
    pygame.font.init()

    # Create screen first using default dimensions
    screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    # Initialize UI elements and configuration, passing the screen
    # init_ui now comes from interface.render
    cfg = init_ui(screen)

    # Start the game
    run_game(screen, clock, cfg)

if __name__ == "__main__":
    main()
