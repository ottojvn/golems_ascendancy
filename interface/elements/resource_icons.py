import pygame
from game.enums import Resources, GolemMaterials

def draw_resource_icon(screen, resource, position, size=16):
    """
    Desenha um placeholder colorido para o ícone do recurso
    Args:
        screen: A superfície onde desenhar
        resource: O enum Resources a desenhar
        position: (x, y) posição para desenhar
        size: tamanho do ícone (quadrado)
        
    Returns:
        pygame.Rect: O retângulo do ícone, útil para detecção de hover
    """
    # Mapeamento de cores para recursos (placeholders)
    colors = {
        Resources.WOOD: (139, 69, 19),      # Marrom
        Resources.MUD: (101, 67, 33),       # Marrom escuro
        Resources.STONE: (169, 169, 169),   # Cinza claro
        Resources.GRANITE: (105, 105, 105), # Cinza escuro
        Resources.LIMESTONE: (220, 220, 220), # Quase branco
        Resources.SANDSTONE: (194, 178, 128), # Bege
        Resources.WATER: (65, 105, 225),    # Azul
        Resources.MUSHROOM: (255, 182, 193), # Rosa claro
    }
    
    # Desenhar o ícone
    color = colors.get(resource, (200, 200, 200))  # Cinza default
    rect = pygame.Rect(position[0], position[1], size, size)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Borda preta

    return rect  # Retorna o retângulo para referência


def draw_golem_icon(screen, material, position, size=24):
    """
    Desenha um placeholder para o ícone do golem
    Args:
        screen: A superfície onde desenhar
        material: O enum GolemMaterials a desenhar
        position: (x, y) posição para desenhar
        size: tamanho do ícone (quadrado)
        
    Returns:
        pygame.Rect: O retângulo do ícone, útil para detecção de hover
    """
    # Mapeamento de cores para materiais (placeholders) - CORRIGIDO para usar enum values
    colors = {
        GolemMaterials.WATER.value: (65, 105, 225),     # Azul
        GolemMaterials.STONE.value: (169, 169, 169),   # Cinza claro
        GolemMaterials.GRANITE.value: (105, 105, 105), # Cinza escuro
        GolemMaterials.LIMESTONE.value: (220, 220, 220), # Quase branco
        GolemMaterials.SANDSTONE.value: (194, 178, 128), # Bege
        GolemMaterials.COPPER.value: (184, 115, 51),    # Cobre
        GolemMaterials.TIN.value: (180, 180, 180), # Prateado
        GolemMaterials.MUD.value: (101, 67, 33),      # Marrom escuro
    }
    
    # Desenhar o ícone circular do golem
    # Usa material.value para buscar a cor correta
    color = colors.get(material.value, (200, 200, 200))  # Cinza default
    rect = pygame.Rect(position[0], position[1], size, size)
    
    # Desenha um círculo para representar o golem
    center = rect.center
    radius = size // 2
    pygame.draw.circle(screen, color, center, radius)
    pygame.draw.circle(screen, (0, 0, 0), center, radius, 1)  # Borda preta
    
    # Adiciona "olhos" para parecer um golem
    eye_radius = size // 8
    eye_offset = size // 6
    pygame.draw.circle(screen, (0, 0, 0), 
                      (center[0] - eye_offset, center[1] - eye_offset), 
                      eye_radius)
    pygame.draw.circle(screen, (0, 0, 0), 
                      (center[0] + eye_offset, center[1] - eye_offset), 
                      eye_radius)

    return rect  # Retorna o retângulo para referência