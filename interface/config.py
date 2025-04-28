import pygame
import os
from interface.elements.text_display import Colors

# Font paths (assuming fonts are in interface/assets/fonts/)
FONT_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'fonts', 'Pixeloid')
FONT_PATH_REGULAR = os.path.join(FONT_DIR, 'PixeloidSans.ttf')
FONT_PATH_BOLD = os.path.join(FONT_DIR, 'PixeloidSans-Bold.ttf')

def get_config(screen):
    w, h = screen.get_size()
    scale = h / 720
    try:
        font_normal = pygame.font.Font(FONT_PATH_REGULAR, max(1, int(18 * scale)))
        font_large = pygame.font.Font(FONT_PATH_BOLD, max(1, int(36 * scale)))
    except pygame.error as e:
        print(f"Error loading font: {e}")
        print("Falling back to default system font.")
        font_normal = pygame.font.Font(None, max(1, int(18 * scale)))
        font_large = pygame.font.Font(None, max(1, int(36 * scale)))

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