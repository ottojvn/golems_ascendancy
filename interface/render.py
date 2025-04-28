from interface.config import get_config
from interface.panels.hud_panel import draw_top_hud
from interface.panels.exit_panel import draw_exit_panel
from interface.panels.jobs_panel import draw_jobs_panel

def init_ui(screen):
    cfg = get_config(screen)
    from interface.elements.tooltip_manager import TooltipManager
    cfg['tooltip_manager'] = TooltipManager(cfg['font_normal'])
    return cfg

def draw_ui(state, cfg, clickable_elements):
    screen = cfg['screen']
    screen.fill(cfg['bg_color'])
    
    # Draw the top HUD bar
    hud_height = draw_top_hud(screen, state, cfg)
    
    # Draw the jobs panel
    draw_jobs_panel(screen, state, cfg, clickable_elements)
    
    # Exit information at the bottom
    draw_exit_panel(screen, cfg)
    
    # Update and draw tooltips
    from pygame import mouse
    tm = cfg.get('tooltip_manager')
    if tm:
        tm.update(mouse.get_pos())
        tm.draw(screen)