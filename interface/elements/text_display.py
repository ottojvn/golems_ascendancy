from enum import Enum

import pygame


class Colors(Enum):
    BLACK = (0, 0, 0)
    CYAN = (0, 200, 200)
    GREY = (128, 128, 128)
    WHITE = (255, 255, 255)
    DARK_GREY = (60, 60, 60)


def draw_text(surface, text, position, font, color=Colors.WHITE, align="topleft"):
    """
    Desenha texto na superfície Pygame.

    Args:
        surface: A superfície Pygame onde desenhar (geralmente a tela).
        text: A string de texto a ser desenhada.
        position: Uma tupla (x, y) para a posição do texto.
        font: O objeto pygame.font.Font carregado.
        color: A cor do texto (padrão: branco).
        align: Como alinhar o retângulo do texto à posição (ex: "topleft", "center", "midtop").
    """
    try:
        text_surface = font.render(str(text), True, color.value)
        text_rect = text_surface.get_rect()
        if hasattr(text_rect, align):
            setattr(text_rect, align, position)
        else:
            print(f"Alinhamento inválido: {align}. Usando topleft.")
            text_rect.topleft = position
        surface.blit(text_surface, text_rect)
    except Exception as e:
        print(f"Erro ao renderizar texto '{text}': {e}")
        fallback_font = pygame.font.Font(None, 15)
        error_surface = fallback_font.render(f"Erro fonte: {text}", True, (255, 0, 0))
        error_rect = error_surface.get_rect(topleft=position)
        surface.blit(error_surface, error_rect)
