from interface.elements.text_display import draw_text

def draw_resources_panel(screen, resources, y, cfg):
    x0 = cfg['padding']
    draw_text(screen, "Recursos:", (x0, y), cfg['font_normal'], cfg['colors'].YELLOW)
    y += cfg['font_normal'].get_linesize() + cfg['line_spacing']
    xi = x0 + cfg['indent']
    for res, data in resources.items():
        qtd = data['quantity'] if isinstance(data, dict) else data
        draw_text(screen, f"- {res.value}: {qtd}", (xi, y), cfg['font_normal'], cfg['colors'].WHITE)
        y += cfg['font_normal'].get_linesize() + cfg['line_spacing']
    return y + cfg['padding']