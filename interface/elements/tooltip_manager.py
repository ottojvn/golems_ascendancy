import pygame
from interface.elements.tooltip import Tooltip

class TooltipManager:
    """
    Gerencia os tooltips da interface, controlando quando devem aparecer ou sumir
    """
    def __init__(self, font):
        self.font = font
        self.tooltips = {}  # Mapeamento de IDs para tooltips
        self.hover_areas = {}  # Mapeamento de IDs para áreas de hover (retângulos)
        self.active_tooltip = None  # ID do tooltip ativo no momento
    
    def register_tooltip(self, tooltip_id, text, hover_rect):
        """
        Registra uma nova área que pode mostrar tooltip
        
        Args:
            tooltip_id: Identificador único para esse tooltip
            text: Texto a ser exibido no tooltip
            hover_rect: pygame.Rect que define a área onde o mouse ativa o tooltip
        """
        self.tooltips[tooltip_id] = Tooltip(text, self.font)
        self.hover_areas[tooltip_id] = hover_rect
    
    def update_hover_area(self, tooltip_id, hover_rect):
        """Atualiza a área de hover para um tooltip existente"""
        if tooltip_id in self.hover_areas:
            self.hover_areas[tooltip_id] = hover_rect
    
    def update(self, mouse_pos):
        """
        Atualiza o estado dos tooltips com base na posição do mouse
        
        Args:
            mouse_pos: Tuple (x, y) com a posição atual do mouse
        """
        # Verifica se o mouse está sobre alguma área de tooltip
        found_hover = False
        
        for tooltip_id, rect in self.hover_areas.items():
            if rect.collidepoint(mouse_pos):
                found_hover = True
                
                # Se já tem um tooltip ativo diferente, esconde ele
                if self.active_tooltip and self.active_tooltip != tooltip_id:
                    self.tooltips[self.active_tooltip].hide()
                
                # Ativa o tooltip atual
                self.active_tooltip = tooltip_id
                tooltip = self.tooltips[tooltip_id]
                tooltip.update(mouse_pos)
                
                if not tooltip.visible:
                    tooltip.show(mouse_pos)
                break
        
        # Se o mouse não está sobre nenhuma área, esconde o tooltip ativo
        if not found_hover and self.active_tooltip:
            self.tooltips[self.active_tooltip].hide()
            self.active_tooltip = None
    
    def draw(self, surface):
        """Desenha o tooltip ativo, se houver"""
        if self.active_tooltip:
            self.tooltips[self.active_tooltip].draw(surface)
    
    def clear(self):
        """Limpa todos os tooltips registrados"""
        self.tooltips.clear()
        self.hover_areas.clear()
        self.active_tooltip = None