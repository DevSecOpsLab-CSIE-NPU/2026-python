"""Phase 6：渲染工具。

同時支援：
1. 測試時回傳資料描述
2. 實際執行時把畫面畫到 pygame 視窗
"""

from __future__ import annotations

from game.models import Card, Hand, Player

try:
    import pygame
except Exception:  # pragma: no cover - 無圖形環境時允許失敗
    pygame = None


class Renderer:
    COLORS = {
        "background": (45, 45, 45),
        "card_back": (74, 144, 217),
        # 黑桃、梅花應使用深色，否則在白底牌面上會看起來像空白。
        "spade_club": (20, 20, 20),
        "heart_diamond": (231, 76, 60),
        "player": (46, 204, 113),
        "ai": (149, 165, 166),
        "selected": (241, 196, 15),
        "button": (52, 152, 219),
        "panel": (70, 70, 70),
    }

    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def __init__(self) -> None:
        self.pygame = pygame
        self.font = None
        self.small_font = None

    def _ensure_fonts(self) -> None:
        if self.pygame is None:
            return
        if not self.pygame.get_init():
            self.pygame.init()
        if not self.pygame.font.get_init():
            self.pygame.font.init()
        if self.font is None:
            # 優先使用 Windows 常見中文字體，避免訊息變成方塊或亂碼。
            font_name = "microsoft jhenghei, microsoft yahei, simhei, arial"
            self.font = self.pygame.font.SysFont(font_name, 24)
            self.small_font = self.pygame.font.SysFont(font_name, 18)

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
            card_y = y - 20 if i in selected_indices else y
            cards.append(self.draw_card(card, x + i * offset, card_y, selected=(i in selected_indices)))
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
            "cards": [self.draw_card(c, x + i * 70, y) for i, c in enumerate(cards)],
        }

    def draw_buttons(self, buttons: dict[str, tuple[int, int, int, int]], x: int, y: int) -> list[dict]:
        out: list[dict] = []
        for name, rect in buttons.items():
            bx, by, bw, bh = rect
            out.append({"name": name, "rect": (x + bx, y + by, bw, bh), "color": self.COLORS["button"]})
        return out

    def render_to_screen(self, screen, state: dict, status_message: str = "") -> None:
        """若有 pygame 視窗，將 state 真正畫到畫面上。"""
        if self.pygame is None or screen is None:
            return

        self._ensure_fonts()
        pg = self.pygame
        screen.fill(self.COLORS["background"])

        # 標題
        title = self.font.render("Big Two 大老二", True, (255, 255, 255))
        screen.blit(title, (700, 20))

        # 狀態訊息
        msg = self.small_font.render(status_message, True, (255, 255, 200))
        screen.blit(msg, (20, 75))

        # 玩家資訊
        for info in state.get("players", []):
            rect = pg.Rect(20 + info["x"], 110 + info["y"], 180, 28)
            color = self.COLORS["player"] if not info["is_ai"] else self.COLORS["ai"]
            pg.draw.rect(screen, color, rect, border_radius=6)
            if info["is_current"]:
                pg.draw.rect(screen, self.COLORS["selected"], rect, width=3, border_radius=6)
            text = f"{info['name']} - {info['cards']} 張"
            label = self.small_font.render(text, True, (0, 0, 0))
            screen.blit(label, (rect.x + 8, rect.y + 5))

        # 上一手出牌
        last_play = state.get("last_play")
        if last_play is not None:
            label = self.small_font.render(f"上一手：{last_play['player_name']}", True, (255, 255, 255))
            screen.blit(label, (20, 230))
            for card in last_play["cards"]:
                self._draw_card_rect(screen, card)

        # 人類玩家手牌
        hand_panel = pg.Rect(10, 360, 930, 170)
        pg.draw.rect(screen, self.COLORS["panel"], hand_panel, border_radius=8)
        hand_label = self.small_font.render("你的手牌", True, (255, 255, 255))
        screen.blit(hand_label, (20, 370))
        for card in state.get("human_hand", []):
            self._draw_card_rect(screen, card)

        # 按鈕
        for button in state.get("buttons", []):
            bx, by, bw, bh = button["rect"]
            pg.draw.rect(screen, button["color"], (bx, by, bw, bh), border_radius=8)
            text = self.small_font.render(button["name"].upper(), True, (255, 255, 255))
            screen.blit(text, (bx + 20, by + 10))

        # 行動歷史：保留最近幾次誰出了什麼牌 / PASS
        history_rect = pg.Rect(610, 110, 320, 240)
        pg.draw.rect(screen, self.COLORS["panel"], history_rect, border_radius=8)
        history_title = self.small_font.render("History", True, (255, 255, 255))
        screen.blit(history_title, (620, 120))
        for idx, line in enumerate(state.get("history", [])):
            txt = self.small_font.render(line, True, (230, 230, 230))
            screen.blit(txt, (620, 145 + idx * 24))

        if state.get("winner"):
            win_text = self.font.render(f"勝利者：{state['winner']}", True, self.COLORS["selected"])
            screen.blit(win_text, (320, 300))

    def _draw_card_rect(self, screen, card_desc: dict) -> None:
        pg = self.pygame
        rect = pg.Rect(card_desc["x"], card_desc["y"], card_desc["w"], card_desc["h"])
        bg = (250, 250, 250) if card_desc["text"] != "BACK" else self.COLORS["card_back"]
        pg.draw.rect(screen, bg, rect, border_radius=8)
        border_color = self.COLORS["selected"] if card_desc.get("selected") else (30, 30, 30)
        pg.draw.rect(screen, border_color, rect, width=3, border_radius=8)
        text = self.small_font.render(card_desc["text"], True, card_desc["color"])
        screen.blit(text, (rect.x + 8, rect.y + 8))
