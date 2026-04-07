"""P6: Renderer - Game rendering engine using Pygame"""

import pygame
from typing import List, Tuple, Optional
from game.models import Card


class Renderer:
    """Handles rendering of Big Two game board"""

    # Colors
    COLOR_GREEN = (34, 139, 34)  # Dark green for table
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_GRAY = (128, 128, 128)
    COLOR_RED = (255, 0, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_YELLOW = (255, 255, 0)  # Yellow for highlights

    # Card dimensions
    CARD_WIDTH = 70
    CARD_HEIGHT = 100
    CARD_SPACING = 10

    def __init__(self, width: int = 1200, height: int = 800):
        """Initialize the renderer with window dimensions"""
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height))
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)

    def draw_game_board(self, game_state: dict):
        """Draw the complete game board"""
        # Clear screen
        self.surface.fill(self.COLOR_GREEN)

        # Draw table area (center)
        self._draw_table_area(game_state)

        # Draw player areas
        self._draw_player_areas(game_state)

        # Draw game status
        self._draw_game_status(game_state)

        # Update display
        pygame.display.flip()

    def _draw_table_area(self, game_state: dict):
        """Draw the center table area with current play"""
        table_cards = game_state.get('table', [])
        
        # Draw border around table
        table_rect = pygame.Rect(200, 250, 800, 150)
        pygame.draw.rect(self.surface, self.COLOR_WHITE, table_rect, 2)

        # Draw table cards
        if table_cards:
            start_x = 300
            for i, card in enumerate(table_cards):
                x = start_x + (i * (self.CARD_WIDTH + self.CARD_SPACING))
                y = 300
                self._draw_card(card, x, y)

            # Draw "Last play" label
            text = self.font_small.render("Last Play", True, self.COLOR_WHITE)
            self.surface.blit(text, (200, 200))

    def _draw_player_areas(self, game_state: dict):
        """Draw each player's area"""
        players = game_state.get('players', [])
        current_player = game_state.get('current_player', 0)

        # Player positions: bottom (0), left (1), top (2), right (3)
        player_positions = [
            {'x': 500, 'y': 650, 'align': 'center'},      # Bottom
            {'x': 50, 'y': 350, 'align': 'left'},         # Left
            {'x': 500, 'y': 50, 'align': 'center'},       # Top
            {'x': 1050, 'y': 350, 'align': 'left'},       # Right
        ]

        for i, player in enumerate(players):
            pos = player_positions[i]
            is_current = (i == current_player)
            self._draw_player_info(player, pos, is_current)

    def _draw_player_info(self, player: dict, pos: dict, is_current: bool):
        """Draw information for one player"""
        x, y = pos['x'], pos['y']
        
        # Draw player name and info
        name = player.get('name', 'Player')
        cards_count = player.get('cards', 0)
        
        color = self.COLOR_RED if is_current else self.COLOR_WHITE
        
        name_text = self.font_medium.render(name, True, color)
        self.surface.blit(name_text, (x, y))

        cards_text = self.font_small.render(f"Cards: {cards_count}", True, self.COLOR_WHITE)
        self.surface.blit(cards_text, (x, y + 30))

        # Draw player's playing area indicator
        if is_current:
            border_rect = pygame.Rect(x - 10, y - 10, 200, 60)
            pygame.draw.rect(self.surface, self.COLOR_YELLOW, border_rect, 2)

    def _draw_game_status(self, game_state: dict):
        """Draw game status information"""
        state = game_state.get('state', 'UNKNOWN')
        round_num = game_state.get('round', 0)
        pass_count = game_state.get('pass_count', 0)

        # Draw status at top
        status_text = f"State: {state} | Round: {round_num} | Pass Count: {pass_count}"
        text = self.font_medium.render(status_text, True, self.COLOR_WHITE)
        self.surface.blit(text, (20, 20))

    def _draw_card(self, card: Card, x: int, y: int, selected: bool = False):
        """Draw a single card"""
        # Draw card rectangle
        card_rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        
        if selected:
            pygame.draw.rect(self.surface, self.COLOR_YELLOW, card_rect)
        else:
            pygame.draw.rect(self.surface, self.COLOR_WHITE, card_rect)
        
        pygame.draw.rect(self.surface, self.COLOR_BLACK, card_rect, 2)

        # Draw card text
        card_str = str(card)
        text = self.font_small.render(card_str, True, self.COLOR_BLACK)
        text_rect = text.get_rect(center=card_rect.center)
        self.surface.blit(text, text_rect)

    def draw_player_hand(self, cards: List[Card], selected_indices: List[int] = None):
        """Draw player's hand (for human player)"""
        selected_indices = selected_indices or []
        
        # Calculate starting x position for centered hand
        total_width = len(cards) * (self.CARD_WIDTH + self.CARD_SPACING) - self.CARD_SPACING
        start_x = (self.width - total_width) // 2
        y = self.height - self.CARD_HEIGHT - 20

        for i, card in enumerate(cards):
            x = start_x + (i * (self.CARD_WIDTH + self.CARD_SPACING))
            is_selected = i in selected_indices
            self._draw_card(card, x, y, is_selected)

    def get_card_at_position(self, pos: Tuple[int, int], cards: List[Card]) -> Optional[int]:
        """Get card index at given position"""
        x, y = pos
        
        total_width = len(cards) * (self.CARD_WIDTH + self.CARD_SPACING) - self.CARD_SPACING
        start_x = (self.width - total_width) // 2
        hand_y = self.height - self.CARD_HEIGHT - 20

        for i, card in enumerate(cards):
            card_x = start_x + (i * (self.CARD_WIDTH + self.CARD_SPACING))
            card_rect = pygame.Rect(card_x, hand_y, self.CARD_WIDTH, self.CARD_HEIGHT)
            if card_rect.collidepoint(x, y):
                return i

        return None
