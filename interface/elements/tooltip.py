import pygame
from interface.elements.text_display import draw_text, Colors

class Tooltip:
    """
    Classe para exibir tooltips quando o mouse passa sobre elementos
    """
    def __init__(self, text, font, max_width=300, padding=8, bg_color=(40, 40, 40), 
                 text_color=Colors.WHITE, border_color=Colors.GREY):
        self.text = text
        self.font = font
        self.max_width = max_width
        self.padding = padding
        self.bg_color = bg_color
        self.text_color = text_color
        self.border_color = border_color
        self.visible = False
        self._calculate_size()
    
    def _calculate_size(self):
        """Calcula tamanho com base no texto, respeitando max_width e \n."""
        self.lines = []
        max_line_width = 0
        
        # First, split by explicit newlines
        segments = self.text.split('\n')
        
        for segment in segments:
            # Apply word wrapping to each segment
            words = segment.split(' ')
            if not words:
                self.lines.append("") # Handle empty lines from double newlines
                continue
                
            current_line = words[0]
            for word in words[1:]:
                # Handle potential empty words from multiple spaces
                if not word:
                    continue 
                test_line = current_line + " " + word
                test_width, _ = self.font.size(test_line)
                
                if test_width <= self.max_width:
                    current_line = test_line
                else:
                    self.lines.append(current_line)
                    line_width, _ = self.font.size(current_line)
                    max_line_width = max(max_line_width, line_width)
                    current_line = word
            
            # Add the last line of the segment
            self.lines.append(current_line)
            line_width, _ = self.font.size(current_line)
            max_line_width = max(max_line_width, line_width)

        # Determine the final width and height
        self.width = max_line_width + (self.padding * 2)
        self.height = (len(self.lines) * self.font.get_linesize()) + (self.padding * 2)
    
    def show(self, pos):
        """Marca o tooltip como visível e define sua posição"""
        self.pos = pos
        self.visible = True
    
    def hide(self):
        """Esconde o tooltip"""
        self.visible = False
    
    def update(self, mouse_pos):
        """Atualiza a posição do tooltip para seguir o mouse"""
        x, y = mouse_pos
        
        # Posiciona um pouco acima e à direita do cursor
        tooltip_x = x + 15
        tooltip_y = y - self.height - 5
        
        # Ajusta se estiver saindo da tela
        # (Nota: precisaríamos da dimensão da tela para isso ser completo)
        if tooltip_x + self.width > 1280:  # Assumindo largura máxima
            tooltip_x = x - self.width - 5
        if tooltip_y < 0:
            tooltip_y = y + 15
            
        self.pos = (tooltip_x, tooltip_y)
    
    def draw(self, surface):
        """Desenha o tooltip se estiver visível"""
        if not self.visible:
            return
        
        # Desenha o fundo
        rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(surface, self.bg_color, rect)
        pygame.draw.rect(surface, self.border_color.value, rect, 1)
        
        # Desenha o texto linha por linha
        x = self.pos[0] + self.padding
        y = self.pos[1] + self.padding
        
        for line in self.lines:
            draw_text(surface, line, (x, y), self.font, self.text_color)
            y += self.font.get_linesize()