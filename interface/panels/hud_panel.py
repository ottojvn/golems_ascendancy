import pygame
from interface.elements.text_display import draw_text
from interface.elements.resource_icons import draw_resource_icon, draw_golem_icon
from interface.i18n import TRANSLATIONS
from game.enums import Resources

def draw_top_hud(screen, state, cfg):
    """
    Desenha a barra horizontal superior (HUD) contendo data, população e recursos
    """
    # Dados que serão exibidos
    date = state.get('date', {})
    population = state.get('population', {})
    resources = state.get('resources', {})
    
    # Desenha o fundo da HUD
    hud_height = cfg['font_normal'].get_linesize() * 2 + cfg['padding'] * 2
    hud_rect = pygame.Rect(0, 0, cfg['width'], hud_height)
    pygame.draw.rect(screen, cfg['colors'].DARK_GREY.value, hud_rect)
    pygame.draw.line(screen, cfg['colors'].GREY.value, 
                    (0, hud_height), (cfg['width'], hud_height), 1)
    
    # Posição inicial para desenhar
    x = cfg['padding']
    y = cfg['padding']
    
    # i18n and date
    locale = cfg['locale']
    tr = TRANSLATIONS[locale]
    day = int(date['day'])
    year = int(date['year'])
    date_text = f"{tr['day']} {day} / {tr['year']} {year}"
    draw_text(screen, date_text, (x, y), cfg['font_normal'], cfg['colors'].WHITE)
    
    # Golem icon and count
    x += 250  # space after date
    icon_size = cfg.get('icon_size', 24)
    rect_g = draw_golem_icon(screen, population['material'], (x, y), size=icon_size)
    
    # Updated Golem Count Text
    available_golems = population.get('available', 0)
    total_golems = population.get('total', 0)
    golem_count_text = f"{available_golems} / {total_golems}"
    text_x = x + icon_size + cfg['indent']
    draw_text(screen, golem_count_text,
              (text_x, y),
              cfg['font_normal'], cfg['colors'].CYAN)

    # Tooltip for golem count (combining icon and text area)
    text_width, text_height = cfg['font_normal'].size(golem_count_text)
    tooltip_hover_rect = pygame.Rect(x, y, icon_size + cfg['indent'] + text_width, max(icon_size, text_height))
    tooltip_text = tr['ui']['golem_count_tooltip'].format(available=available_golems, total=total_golems)
    cfg['tooltip_manager'].register_tooltip('golem_count', tooltip_text, tooltip_hover_rect)
    
    # Resources row
    x = cfg['padding']
    y += cfg['font_normal'].get_linesize() + cfg['padding'] // 2
    
    # show all current resources
    all_resources = list(resources.keys())
    spacing = (cfg['width'] - cfg['padding']*2) // (len(all_resources) or 1)
    # draw each resource icon, quantity, tooltip
    for idx, res in enumerate(all_resources):
        qty = resources[res]['quantity']
        res_x = x + (idx * spacing)
        # draw icon
        rect_r = draw_resource_icon(screen, res, (res_x, y), size=cfg.get('icon_res_size', 16))
        # register tooltip
        cfg['tooltip_manager'].register_tooltip(f"res_{res.name}",
                                               tr['resources'][res], rect_r)
        # draw quantity next to icon
        draw_text(screen, str(qty),
                  (res_x + cfg.get('icon_res_size', 16) + 2, y),
                  cfg['font_normal'], cfg['colors'].WHITE)
    
    return hud_height  # Retorna a altura da HUD para ajustar o resto do layout