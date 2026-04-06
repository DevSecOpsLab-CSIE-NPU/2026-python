from __future__ import annotations

from typing import Iterable, Sequence

from game.models import Card


class Renderer:
    COLORS = {
        "background": (45, 45, 45),
        "card_back": (74, 144, 217),
        "spade_club": (255, 255, 255),
        "heart_diamond": (231, 76, 60),
        "player": (46, 204, 113),
        "ai": (149, 165, 166),
        "selected": (241, 196, 15),
        "button": (52, 152, 219),
    }

    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def __init__(self) -> None:
        self.enabled = True

    # GUI implementation is intentionally lightweight so game logic can be tested
    # in environments where pygame is not installed.
    def draw_card(self, card: Card, x: int, y: int, selected: bool = False) -> tuple[int, int, bool]:
        return x, y, selected

    def draw_hand(self, hand: Sequence[Card], x: int, y: int, selected_indices: Iterable[int]) -> int:
        return len(hand)

    def draw_player(self, player_name: str, x: int, y: int, is_current: bool) -> tuple[str, bool]:
        return player_name, is_current

    def draw_last_play(self, cards: Sequence[Card], player_name: str, x: int, y: int) -> tuple[str, int]:
        return player_name, len(cards)

    def draw_buttons(self, buttons: dict[str, tuple[int, int, int, int]], x: int, y: int) -> int:
        return len(buttons)
