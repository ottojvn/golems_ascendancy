import sys

import pygame

from game.state import init_state, update_state
from interface.render import init_ui, draw_ui
from game.enums import GolemMaterials
from game.constants import SECONDS_PER_DAY  # import time scale

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
WINDOW_TITLE = "Golems Ascendancy"


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    cfg = init_ui(screen)
    # Escolha do tipo de golem para a partida
    selected = GolemMaterials.MUD # ajuste para entrada real
    state = init_state(selected)

    running = True
    while running:
        dt_seconds = clock.tick(FPS) / 1000.0
        dt = dt_seconds / SECONDS_PER_DAY  # real seconds to in-game days

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        state = update_state(state, dt)
        draw_ui(state, cfg)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
