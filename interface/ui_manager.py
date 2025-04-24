import pygame

from interface.elements.text_display import Colors, draw_text


class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()

        font_path = "interface/assets/fonts/Pixeloid/OpenType (.otf)/PixeloidSans.otf"
        font_size_normal = 18
        font_size_large = font_size_normal * 2

        try:
            self.font_normal = pygame.font.Font(font_path, font_size_normal)
            self.font_large = pygame.font.Font(font_path, font_size_large)
            print(f"Fonte '{font_path}' carregada com sucesso.")
        except pygame.error as e:
            print(
                f"ERRO: Não foi possível carregar a fonte em '{font_path}'. Verifique o caminho e o arquivo."
            )
            print(f"Pygame error: {e}")
            print("Usando fonte padrão do sistema.")
            pygame.font.init()  # Garante que o módulo de fontes está inicializado
            self.font_normal = pygame.font.Font(None, font_size_normal)
            self.font_large = pygame.font.Font(None, font_size_large)

        # --- Dados Mock ---
        self.mock_era = "Idade da Pedra - Início"

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass  # Lógica de clique (se necessário no futuro)

    def draw(self, gamestate):
        self.screen.fill((40, 40, 40))

        # Configurações de layout
        padding = 20  # Espaçamento geral das bordas e entre seções
        line_spacing = 5  # Espaçamento extra entre linhas de texto
        line_height = self.font_normal.get_linesize() + line_spacing
        panel_x = padding  # Posição X inicial para o painel esquerdo

        # --- Título (Opcional, descomente se quiser) ---
        # draw_text(
        #     self.screen,
        #     "Golems Ascendancy",
        #     (self.screen_width // 2, padding), # Posição no topo central
        #     self.font_large,
        #     COLOR_WHITE,
        #     align="midtop",
        # )
        # current_y = padding + self.font_large.get_linesize() + padding # Ajusta y se o título estiver ativo
        current_y = padding * 2  # Posição Y inicial abaixo do topo (ou título)

        # --- Era Atual (Topo Direito) ---
        draw_text(
            self.screen,
            f"Era: {self.mock_era}",
            (self.screen_width - padding, current_y),  # Canto superior direito
            self.font_normal,
            Colors.WHITE,
            align="topright",  # Alinha pela direita
        )

        # --- Painel de Recursos (Esquerda) ---
        resource_label_pos = (panel_x, current_y)
        draw_text(
            self.screen,
            "Recursos:",
            resource_label_pos,
            self.font_normal,
            Colors.YELLOW,
            align="topleft",  # Alinha pela esquerda
        )
        current_y += line_height  # Move para baixo para a lista

        resource_item_x = panel_x + 15  # Indenta os itens da lista
        for resource, amount in gamestate.get_resources().items():
            draw_text(
                self.screen,
                f"- {resource.value}: {amount}",
                (resource_item_x, current_y),  # Posição do item
                self.font_normal,
                Colors.WHITE,
                align="topleft",
            )
            current_y += line_height  # Move para baixo para o próximo item

        # Espaçamento antes da próxima seção
        current_y += padding

        # --- Painel de Golems (Abaixo dos Recursos) ---
        golem_label_pos = (panel_x, current_y)
        draw_text(
            self.screen,
            "Golems:",
            golem_label_pos,
            self.font_normal,
            Colors.CYAN,
            align="topleft",
        )
        current_y += line_height  # Move para baixo para a lista

        golem_item_x = panel_x + 15  # Indenta os itens da lista
        total_golems = 0  # Para calcular o total
        golem_population = gamestate.get_population()  # Chama só uma vez
        for material, amount in golem_population.items():
            draw_text(
                self.screen,
                f"- {material.value}: {amount}",
                (golem_item_x, current_y),
                self.font_normal,
                Colors.WHITE,
                align="topleft",
            )
            total_golems += amount  # Soma ao total
            current_y += line_height  # Move para baixo para o próximo item

        # Desenha o total de Golems (se houver algum)
        if golem_population:  # Só desenha o total se a lista não estiver vazia
            current_y += line_spacing  # Pequeno espaço antes do total
            draw_text(
                self.screen,
                f"- Total: {total_golems}",
                (golem_item_x, current_y),
                self.font_normal,
                Colors.WHITE,
                align="topleft",
            )
            current_y += line_height  # Move para baixo após o total

        # --- Mensagem de Saída (Inferior Central) ---
        draw_text(
            self.screen,
            "Pressione ESC para sair",
            (
                self.screen_width // 2,
                self.screen_height - padding,
            ),  # Base da tela, centralizado
            self.font_normal,
            Colors.GREY,
            align="midbottom",  # Alinha pelo centro inferior
        )
