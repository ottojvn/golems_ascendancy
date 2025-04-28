import pygame
import sys
from interface.render import draw_ui
from game.state import init_state
from game.date import advance_date
from game.resources import update_resources
from game.population import update_population
from game.jobs import allocate_golem_to_job, deallocate_golem_from_job, Jobs
from game.enums import GolemMaterials
from game.constants import SECONDS_PER_DAY

def run_game(screen, clock, cfg):
    """Runs the main game loop."""
    state = init_state(GolemMaterials.MUD)  # Example: Start with Mud Golems
    running = True

    # --- REMOVED Initial Allocation Example ---
    # Golems now start idle by default
    # -----------------------------------------

    logic_update_interval = SECONDS_PER_DAY * 1000  # Milliseconds per game day tick
    last_logic_update_time = pygame.time.get_ticks()
    tooltip_manager = cfg['tooltip_manager']
    clickable_elements = {} # Store rects of clickable UI elements

    while running:
        current_time = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check clicks on job icons
                gatherer_rect = clickable_elements.get('gatherer_job')
                if gatherer_rect and gatherer_rect.collidepoint(mouse_pos):
                    if event.button == 1: # Left click
                        allocate_golem_to_job(state, Jobs.GATHERER, 1)
                    elif event.button == 3: # Right click
                        deallocate_golem_from_job(state, Jobs.GATHERER, 1)

            tooltip_manager.update(mouse_pos)

        # Game Logic Update
        time_since_last_update = current_time - last_logic_update_time
        days_to_advance = time_since_last_update / logic_update_interval

        if days_to_advance >= 1:
            num_days = int(days_to_advance)
            # Advance date
            state['date'] = advance_date(state['date'], num_days)
            # Update resources based on job output over num_days
            state['resources'] = update_resources(state, num_days)
            # Update population (currently just a placeholder)
            state['population'] = update_population(state['population'], num_days)
            last_logic_update_time += num_days * logic_update_interval

        # Drawing
        screen.fill(cfg['bg_color'])
        # Pass clickable_elements dict to draw_ui to be populated
        draw_ui(state, cfg, clickable_elements)

        # Display Update
        pygame.display.flip()

        # Frame Rate Cap
        clock.tick(60)

    pygame.quit()
    sys.exit()
