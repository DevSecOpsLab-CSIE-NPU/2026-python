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
    """負責把遊戲狀態畫到畫面上。"""

    CARD_WIDTH = 60
    CARD_HEIGHT = 90
    CARD_SPACING = 70
    FONT_CANDIDATES = [
        "Microsoft JhengHei",
        "Microsoft YaHei",
        "Noto Sans CJK TC",
        "Noto Sans CJK SC",
        "PingFang TC",
        "Heiti TC",
        "Arial Unicode MS",
        "Arial",
    ]

    COLORS = {
        "background": (45, 45, 45),
        "card": (250, 250, 250),
        "selected": (241, 196, 15),
        "button": (52, 152, 219),
        "text": (20, 20, 20),
        "panel": (65, 65, 65),
        "border": (220, 220, 220),
    }

    BUTTONS = {
        "play": (20, 20, 90, 36),
        "pass": (120, 20, 90, 36),
        "sort": (220, 20, 90, 36),
    }

    def __init__(self) -> None:
        self.font = None
        self.small_font = None
        if pygame is not None:
            pygame.font.init()
            self.font = self._load_font(24)
            self.small_font = self._load_font(20)

    @classmethod
    def _load_font(cls, size: int):
        """優先選擇可顯示中文的字型。"""

        if pygame is None:
            return None

        for name in cls.FONT_CANDIDATES:
            font_path = pygame.font.match_font(name)
            if font_path:
                return pygame.font.Font(font_path, size)

        return pygame.font.SysFont(None, size)

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
        return pygame.Surface((width, height), pygame.SRCALPHA)

    def draw_text(
        self,
        surface,
        text: str,
        x: int,
        y: int,
        small: bool = False,
        color=(240, 240, 240),
    ) -> None:
        if pygame is None or isinstance(surface, SurfaceStub):
            if isinstance(surface, SurfaceStub):
                surface.commands.append({"type": "text", "text": text, "x": x, "y": y})
            return

        font = self.small_font if small else self.font
        if font is None:
            return

        rendered = font.render(text, True, color)
        surface.blit(rendered, (x, y))

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
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (30, 30, 30), rect, 2)
        self.draw_text(surface, self.card_label(card), x + 8, y + 8, color=self.COLORS["text"])
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
            surface = self._create_surface(width + x, height + max(0, y))

        for index, card in enumerate(hand.cards):
            card_x = x + index * self.CARD_SPACING
            card_y = y if index not in selected_indices else y - 10
            self.draw_card(card, card_x, card_y, index in selected_indices, surface)
        return surface

    def draw_buttons(self, surface) -> None:
        if pygame is None or isinstance(surface, SurfaceStub):
            return

        labels = {"play": "出牌", "pass": "Pass", "sort": "排序"}
        for name, (x, y, width, height) in self.BUTTONS.items():
            rect = pygame.Rect(x, y, width, height)
            pygame.draw.rect(surface, self.COLORS["button"], rect, border_radius=6)
            pygame.draw.rect(surface, self.COLORS["border"], rect, 2, border_radius=6)
            self.draw_text(surface, labels[name], x + 18, y + 8, small=True)

    def draw_player_summary(self, surface, label: str, card_count: int, x: int, y: int, is_current: bool) -> None:
        if pygame is None or isinstance(surface, SurfaceStub):
            return

        rect = pygame.Rect(x, y, 180, 64)
        border = self.COLORS["selected"] if is_current else self.COLORS["border"]
        pygame.draw.rect(surface, self.COLORS["panel"], rect, border_radius=8)
        pygame.draw.rect(surface, border, rect, 2, border_radius=8)
        self.draw_text(surface, label, x + 12, y + 10)
        self.draw_text(surface, f"手牌: {card_count}", x + 12, y + 34, small=True)

    def draw_last_play(self, surface, cards: list[Card] | None, player_name: str | None, x: int, y: int) -> None:
        if pygame is None or isinstance(surface, SurfaceStub):
            return

        self.draw_text(surface, "上一手", x, y)
        if player_name:
            self.draw_text(surface, f"玩家: {player_name}", x, y + 24, small=True)
        if not cards:
            self.draw_text(surface, "目前尚未出牌", x, y + 52, small=True)
            return

        for index, card in enumerate(cards):
            self.draw_card(card, x + index * self.CARD_SPACING, y + 60, False, surface)

    def draw_table(self, surface, game, selected_indices: set[int], status_message: str = "") -> None:
        if pygame is None or isinstance(surface, SurfaceStub):
            return

        human = game.players[0]
        self.draw_player_summary(surface, game.players[1].name, len(game.players[1].hand), 20, 100, game.current_player_index == 1)
        self.draw_player_summary(surface, game.players[2].name, len(game.players[2].hand), 390, 40, game.current_player_index == 2)
        self.draw_player_summary(surface, game.players[3].name, len(game.players[3].hand), 760, 100, game.current_player_index == 3)

        self.draw_last_play(surface, game.last_play, game.last_play_player_name, 280, 220)
        self.draw_buttons(surface)
        self.draw_text(surface, f"目前輪到: {game.get_current_player().name}", 20, 540)
        self.draw_text(surface, f"你的手牌 ({len(human.hand)} 張)", 20, 590)
        if status_message:
            self.draw_text(surface, status_message, 340, 30, small=True)

        self.draw_hand(human.hand, 20, 620, selected_indices, surface)
