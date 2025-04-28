import pygame
import sys
from interface.render import draw_ui
from game.state import init_state
from game.date import advance_date
from game.resources import update_resources
from game.population import update_population
from game.enums import GolemMaterials
from game.constants import SECONDS_PER_DAY

def run_game(screen, clock, cfg):
    """Runs the main game loop."""
    state = init_state(GolemMaterials.MUD)  # Example: Start with Mud Golems
    running = True

    logic_update_interval = SECONDS_PER_DAY * 1000  # Milliseconds per game day tick

    last_logic_update_time = pygame.time.get_ticks()

    tooltip_manager = cfg['tooltip_manager']

    while running:
        current_time = pygame.time.get_ticks()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            tooltip_manager.update(pygame.mouse.get_pos())

        # Game Logic Update
        time_since_last_update = current_time - last_logic_update_time
        days_to_advance = time_since_last_update / logic_update_interval

        if days_to_advance >= 1:
            num_days = int(days_to_advance)
            # Advance date, resources, and population
            state['date'] = advance_date(state['date'], num_days)
            state['resources'] = update_resources(state['resources'], num_days)
            state['population'] = update_population(state['population'], num_days)
            last_logic_update_time += num_days * logic_update_interval

        # Drawing
        screen.fill(cfg['bg_color'])
        draw_ui(state, cfg)

        # Display Update
        pygame.display.flip()

        # Frame Rate Cap
        clock.tick(60)

    pygame.quit()
    sys.exit()
