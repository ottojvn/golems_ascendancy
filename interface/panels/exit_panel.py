from interface.elements.text_display import draw_text
from interface.i18n import TRANSLATIONS

def draw_exit_panel(screen, cfg):
    locale = cfg["locale"]
    tr = TRANSLATIONS[locale]
    txt = tr['press_escape']
    pos = (cfg['width']//2, cfg['height'] - cfg['padding'])
    draw_text(screen, txt, pos, cfg['font_normal'], cfg['colors'].GREY, align="midbottom")