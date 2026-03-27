"""
畫面繪製工具。
"""

from __future__ import annotations

from dataclasses import dataclass, field

from game.models import Card, Hand

try:
    import pygame
except ImportError:  # pragma: no cover - 是否安裝 pygame 取決於本機環境
    pygame = None


@dataclass
class SurfaceStub:
    """在沒有 pygame 的環境中，提供簡單的 surface 替身。"""

    width: int
    height: int
    commands: list[dict[str, object]] = field(default_factory=list)

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height


class Renderer:
    """負責把牌桌狀態轉成畫面。"""

    CARD_WIDTH = 60
    CARD_HEIGHT = 90
    CARD_SPACING = 70

    COLORS = {
        "background": (45, 45, 45),
        "card": (250, 250, 250),
        "selected": (241, 196, 15),
        "button": (52, 152, 219),
        "text": (20, 20, 20),
    }

    BUTTONS = {
        "play": (20, 20, 90, 36),
        "pass": (120, 20, 90, 36),
        "sort": (220, 20, 90, 36),
    }

    def __init__(self) -> None:
        self.font = None
        if pygame is not None:
            pygame.font.init()
            self.font = pygame.font.SysFont(None, 24)

    @staticmethod
    def card_label(card: Card) -> str:
        return repr(card)

    @classmethod
    def hand_layout(cls, count: int, x: int, y: int) -> list[tuple[int, int, int, int]]:
        return [
            (x + index * cls.CARD_SPACING, y, cls.CARD_WIDTH, cls.CARD_HEIGHT)
            for index in range(count)
        ]

    @staticmethod
    def _create_surface(width: int, height: int):
        if pygame is None:
            return SurfaceStub(width, height)
        return pygame.Surface((width, height))

    def draw_card(self, card: Card, x: int, y: int, selected: bool = False, surface=None):
        if surface is None:
            surface = self._create_surface(self.CARD_WIDTH, self.CARD_HEIGHT)

        if pygame is None or isinstance(surface, SurfaceStub):
            surface.commands.append(
                {
                    "type": "card",
                    "label": self.card_label(card),
                    "x": x,
                    "y": y,
                    "selected": selected,
                }
            )
            return surface

        color = self.COLORS["selected"] if selected else self.COLORS["card"]
        pygame.draw.rect(surface, color, pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT))
        pygame.draw.rect(surface, (30, 30, 30), pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT), 2)
        if self.font is not None:
            text = self.font.render(self.card_label(card), True, self.COLORS["text"])
            surface.blit(text, (x + 8, y + 8))
        return surface

    def draw_hand(
        self,
        hand: Hand,
        x: int,
        y: int,
        selected_indices: set[int] | None = None,
        surface=None,
    ):
        selected_indices = selected_indices or set()
        width = max(self.CARD_WIDTH, self.CARD_WIDTH + max(0, len(hand.cards) - 1) * self.CARD_SPACING)
        height = self.CARD_HEIGHT + 20
        if surface is None:
            surface = self._create_surface(width, height)

        for index, card in enumerate(hand.cards):
            card_x = index * self.CARD_SPACING
            card_y = 0 if index not in selected_indices else -10
            self.draw_card(card, card_x, card_y, index in selected_indices, surface)
        return surface
