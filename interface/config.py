import pygame
from interface.elements.text_display import Colors

def get_config(screen):
    w, h = screen.get_size()
    scale = h / 720
    font_normal = pygame.font.Font(None, max(1, int(18 * scale)))
    font_large  = pygame.font.Font(None, max(1, int(36 * scale)))
    return {
        'screen':      screen,
        'width':       w,
        'height':      h,
        'padding':     max(1, int(20 * scale)),
        'line_spacing':max(1, int(5 * scale)),
        'indent':      max(1, int(15 * scale)),
        'font_normal':  font_normal,
        'font_large':   font_large,
        'colors':      Colors,
        'bg_color':    (40, 40, 40),
        'locale':      'en',  # default language
    }