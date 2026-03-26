"""Phase 6：渲染工具。

為了方便在沒有圖形環境的測試執行，
本檔採用「資料驅動描述」方式回傳繪製資訊。
"""

from __future__ import annotations

from game.models import Card, Hand, Player


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

    def draw_card(self, card: Card | None, x: int, y: int, selected: bool = False) -> dict:
        """回傳一張牌的繪製描述。"""
        if card is None:
            text = "BACK"
            color = self.COLORS["card_back"]
        else:
            text = repr(card)
            color = self.COLORS["heart_diamond"] if card.suit in (1, 2) else self.COLORS["spade_club"]

        return {
            "x": x,
            "y": y,
            "w": self.CARD_WIDTH,
            "h": self.CARD_HEIGHT,
            "text": text,
            "color": color,
            "selected": selected,
        }

    def draw_hand(self, hand: Hand, x: int, y: int, selected_indices: list[int]) -> list[dict]:
        cards: list[dict] = []
        offset = 24
        for i, card in enumerate(hand):
            cards.append(self.draw_card(card, x + i * offset, y, selected=(i in selected_indices)))
        return cards

    def draw_player(self, player: Player, x: int, y: int, is_current: bool) -> dict:
        return {
            "name": player.name,
            "x": x,
            "y": y,
            "is_current": is_current,
            "is_ai": player.is_ai,
            "cards": len(player.hand),
        }

    def draw_last_play(self, cards: list[Card], player_name: str, x: int, y: int) -> dict:
        return {
            "player_name": player_name,
            "cards": [self.draw_card(c, x + i * 26, y) for i, c in enumerate(cards)],
        }

    def draw_buttons(self, buttons: dict[str, tuple[int, int, int, int]], x: int, y: int) -> list[dict]:
        # buttons: {name: (bx, by, bw, bh)}
        out: list[dict] = []
        for name, rect in buttons.items():
            bx, by, bw, bh = rect
            out.append({"name": name, "rect": (x + bx, y + by, bw, bh), "color": self.COLORS["button"]})
        return out
