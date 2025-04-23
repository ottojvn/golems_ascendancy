import sys

import pygame

from game.game_state import GameState
from interface.ui_manager import UIManager

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
WINDOW_TITLE = "Golems Ascendancy"


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    ui_manager = UIManager(screen)
    game_state = GameState()

    running = True
    while running:
        # clock.tick()
        dt = clock.tick(FPS) / 1000.0
        clock.tick(FPS)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        ui_manager.update(events)
        game_state.update(dt)

        ui_manager.draw(game_state)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
