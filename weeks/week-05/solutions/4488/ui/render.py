"""Phase 6: Pygame Renderer."""

try:
    import pygame
except ImportError:
    pygame = None

from typing import List, Optional, Tuple
from game.models import Card


class Renderer:
    """Pygame 牌面渲染器。"""

    # 色彩定義
    COLORS = {
        'background': (45, 45, 45),
        'card_back': (74, 144, 217),
        'spade_club': (255, 255, 255),
        'heart_diamond': (231, 76, 60),
        'player': (46, 204, 113),
        'ai': (149, 165, 166),
        'selected': (241, 196, 15),
        'button': (52, 152, 219),
        'text': (255, 255, 255),
    }

    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def __init__(self) -> None:
        """初始化渲染器。"""
        if pygame is None:
            raise ImportError("pygame not installed")

    def draw_card(self, surface: 'pygame.Surface', card: Card, x: int, y: int, 
                  selected: bool = False) -> None:
        """繪製單張牌。
        
        Args:
            surface: pygame surface
            card: 要繪製的牌
            x: x 座標
            y: y 座標
            selected: 是否被選中
        """
        # 繪製牌背景
        color = self.COLORS['selected'] if selected else (200, 200, 200)
        pygame.draw.rect(surface, color, (x, y, self.CARD_WIDTH, self.CARD_HEIGHT))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, self.CARD_WIDTH, self.CARD_HEIGHT), 2)

        # 繪製花色和數字
        if pygame.font:
            font = pygame.font.Font(None, 24)
            suit_symbol = Card.SUIT_SYMBOLS[card.suit]
            rank_name = Card.RANK_NAMES[card.rank]

            text_color = self.COLORS['spade_club'] if card.suit in (0, 3) else self.COLORS['heart_diamond']

            suit_text = font.render(suit_symbol, True, text_color)
            rank_text = font.render(rank_name, True, text_color)

            surface.blit(suit_text, (x + 5, y + 5))
            surface.blit(rank_text, (x + 5, y + 30))

    def draw_player_info(self, surface: 'pygame.Surface', name: str, card_count: int,
                         x: int, y: int, is_current: bool = False, is_ai: bool = False) -> None:
        """繪製玩家資訊。
        
        Args:
            surface: pygame surface
            name: 玩家名稱
            card_count: 手牌數
            x: x 座標
            y: y 座標
            is_current: 是否為當前玩家
            is_ai: 是否為 AI
        """
        color = self.COLORS['player'] if not is_ai else self.COLORS['ai']
        if is_current:
            color = self.COLORS['selected']

        if pygame.font:
            font = pygame.font.Font(None, 20)
            text = font.render(f"{name} ({card_count})", True, color)
            surface.blit(text, (x, y))
