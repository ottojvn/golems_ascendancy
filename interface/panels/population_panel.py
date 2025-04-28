from interface.elements.text_display import draw_text

def draw_population_panel(screen, pop, y, cfg):
    x0 = cfg['padding']
    draw_text(screen, "Golems:", (x0, y), cfg['font_normal'], cfg['colors'].CYAN)
    y += cfg['font_normal'].get_linesize() + cfg['line_spacing']
    xi = x0 + cfg['indent']
    material = pop['material']
    count = pop['count']
    draw_text(screen, f"- {material.value}: {count}", (xi, y), cfg['font_normal'], cfg['colors'].WHITE)
    return y + cfg['font_normal'].get_linesize() + cfg['padding']