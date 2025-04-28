from interface.elements.text_display import draw_text

def draw_date_panel(screen, date, y, cfg):
    txt = f"Data: Dia: {int(date['day'])} / Ano: {int(date['year'])}"
    draw_text(screen, txt, (cfg['padding'], y), cfg['font_normal'], cfg['colors'].WHITE)
    return y + cfg['font_normal'].get_linesize() + cfg['line_spacing']