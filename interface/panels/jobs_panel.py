import pygame
from interface.elements.text_display import draw_text
from interface.elements.resource_icons import draw_job_icon
from interface.i18n import TRANSLATIONS
from game.enums import Jobs

def draw_jobs_panel(screen, state, cfg, clickable_elements):
    """
    Desenha o painel de gerenciamento de jobs.
    """
    locale = cfg['locale']
    tr = TRANSLATIONS[locale]
    jobs_state = state.get('jobs', {})
    
    # Posição inicial para o painel de jobs (exemplo: abaixo da HUD)
    x = cfg['padding']
    y = cfg['padding'] * 2 + cfg['font_normal'].get_linesize() * 2 # Abaixo da HUD
    icon_size = cfg.get('icon_size', 24)
    
    # --- Gatherer Job ---
    gatherer_job_data = jobs_state.get(Jobs.GATHERER)
    if gatherer_job_data:
        job_x = x
        job_y = y
        
        # Desenha o ícone do job
        gatherer_rect = draw_job_icon(screen, Jobs.GATHERER, (job_x, job_y), size=icon_size)
        clickable_elements['gatherer_job'] = gatherer_rect # Store rect for click detection
        
        # Desenha a contagem de golems alocados
        assigned_count = gatherer_job_data.get('assigned_golems', 0)
        count_text = str(assigned_count)
        text_x = job_x + icon_size + cfg['indent'] // 2
        text_y = job_y + (icon_size - cfg['font_normal'].get_linesize()) // 2 # Center vertically
        draw_text(screen, count_text, (text_x, text_y), cfg['font_normal'], cfg['colors'].WHITE)
        
        # Tooltip para o job
        job_info = tr['jobs'].get(Jobs.GATHERER, {})
        tooltip_lines = [
            f"{job_info.get('name', 'Gatherer')}",
            f"{job_info.get('desc', '')}",
            f"({tr['ui']['left_click_assign']})",
            f"({tr['ui']['right_click_unassign']})"
        ]
        tooltip_text = "\n".join(line for line in tooltip_lines if line) # Join non-empty lines
        
        # Combine icon and text area for tooltip hover
        text_width, _ = cfg['font_normal'].size(count_text)
        hover_width = icon_size + cfg['indent'] // 2 + text_width
        hover_rect = pygame.Rect(job_x, job_y, hover_width, icon_size)
        cfg['tooltip_manager'].register_tooltip('gatherer_job_tooltip', tooltip_text, hover_rect)

    # Add drawing for other jobs here later
