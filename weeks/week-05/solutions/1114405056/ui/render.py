try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from typing import List

from game.models import Card, Hand, Player

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
    'card_bg': (240, 240, 220),
}

CARD_WIDTH = 60
CARD_HEIGHT = 90


class Renderer:
    def __init__(self, screen=None):
        self.screen = screen

    def draw_card(self, card: Card, x: int, y: int, selected: bool = False, face_up: bool = True):
        if not PYGAME_AVAILABLE or self.screen is None:
            return
        color = COLORS['selected'] if selected else COLORS['card_bg']
        pygame.draw.rect(self.screen, color, (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=5)
        pygame.draw.rect(self.screen, (100, 100, 100), (x, y, CARD_WIDTH, CARD_HEIGHT), 2, border_radius=5)

        if not face_up:
            pygame.draw.rect(self.screen, COLORS['card_back'],
                             (x + 4, y + 4, CARD_WIDTH - 8, CARD_HEIGHT - 8), border_radius=3)
            return

        suit_color = COLORS['heart_diamond'] if card.suit in (1, 2) else COLORS['spade_club']
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render(repr(card), True, suit_color)
        self.screen.blit(text, (x + 4, y + 4))

    def draw_hand(self, hand: Hand, x: int, y: int, selected_indices: List[int],
                  face_up: bool = True):
        if not PYGAME_AVAILABLE or self.screen is None:
            return
        overlap = 35
        for i, card in enumerate(hand):
            cx = x + i * overlap
            cy = y - (15 if i in selected_indices else 0)
            self.draw_card(card, cx, cy, selected=(i in selected_indices), face_up=face_up)

    def draw_player(self, player: Player, x: int, y: int, is_current: bool):
        if not PYGAME_AVAILABLE or self.screen is None:
            return
        color = COLORS['player'] if not player.is_ai else COLORS['ai']
        if is_current:
            color = (255, 220, 50)
        font = pygame.font.SysFont('Arial', 16)
        label = f"{player.name} ({len(player.hand)} cards)"
        text = font.render(label, True, color)
        self.screen.blit(text, (x, y))

    def draw_last_play(self, cards: List[Card], player_name: str, x: int, y: int):
        if not PYGAME_AVAILABLE or self.screen is None:
            return
        font = pygame.font.SysFont('Arial', 14)
        label = f"Last: {player_name}"
        self.screen.blit(font.render(label, True, COLORS['text']), (x, y))
        for i, card in enumerate(cards):
            self.draw_card(card, x + i * (CARD_WIDTH + 5), y + 20)

    def draw_buttons(self, buttons: dict, x: int, y: int):
        if not PYGAME_AVAILABLE or self.screen is None:
            return
        font = pygame.font.SysFont('Arial', 16, bold=True)
        bx = x
        for name, rect in buttons.items():
            pygame.draw.rect(self.screen, COLORS['button'], rect, border_radius=6)
            text = font.render(name, True, COLORS['text'])
            self.screen.blit(text, (rect.x + 10, rect.y + 8))
