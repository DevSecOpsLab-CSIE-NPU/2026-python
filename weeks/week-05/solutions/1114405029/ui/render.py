from __future__ import annotations

from typing import Dict, List, Optional

import pygame

from p1_models import Card, Hand


class Renderer:
    """負責所有畫面渲染（卡牌、玩家、文字、按鈕等）。"""

    COLORS = {
        "background": (45, 45, 45),
        "card_front": (245, 245, 245),
        "card_back": (74, 144, 217),
        "border": (20, 20, 20),
        "text": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (220, 50, 50),
        "selected": (255, 215, 0),
        "button": (52, 152, 219),
        "panel": (60, 60, 60),
        "current_turn": (255, 215, 0),
        "next_turn": (100, 180, 255),
        "status_bg": (30, 30, 30),
    }

    CARD_WIDTH = 80
    CARD_HEIGHT = 120

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        # 使用支援中文的字型，避免按鈕/玩家名稱/提示文字顯示成方框
        self.font = self._create_font(20, bold=False)
        self.small_font = self._create_font(16, bold=False)
        self.large_font = self._create_font(32, bold=True)

    # -------------------------------------------------------
    # 字型處理
    # -------------------------------------------------------

    def _create_font(self, size: int, bold: bool = False) -> pygame.font.Font:
        """建立支援中文的字型。"""
        candidate_names = [
            "Microsoft JhengHei",
            "微軟正黑體",
            "Microsoft YaHei",
            "SimHei",
            "PMingLiU",
            "MingLiU",
            "Noto Sans CJK TC",
            "Noto Sans CJK SC",
            "Arial Unicode MS",
        ]

        for name in candidate_names:
            try:
                font = pygame.font.SysFont(name, size, bold=bold)
                test_surface = font.render("中文測試A♠", True, (255, 255, 255))
                if test_surface is not None:
                    return font
            except Exception:
                continue

        return pygame.font.SysFont(None, size, bold=bold)

    # -------------------------------------------------------
    # 卡牌繪製
    # -------------------------------------------------------

    def _rank_to_str(self, rank: int) -> str:
        if rank == 11:
            return "J"
        if rank == 12:
            return "Q"
        if rank == 13:
            return "K"
        if rank == 14:
            return "A"
        if rank == 15:
            return "2"
        return str(rank)

    def _suit_to_symbol(self, suit: int) -> str:
        return ["♣", "♦", "♥", "♠"][suit]

    def draw_card(
        self,
        card: Card,
        x: int,
        y: int,
        selected: bool = False,
        face_down: bool = False,
    ) -> None:
        """繪製單張牌。"""
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)

        # 牌背
        if face_down:
            pygame.draw.rect(
                self.screen,
                self.COLORS["card_back"],
                rect,
                border_radius=10,
            )
            pygame.draw.rect(
                self.screen,
                self.COLORS["text"],
                rect,
                2,
                border_radius=10,
            )
            return

        # 牌面
        pygame.draw.rect(
            self.screen,
            self.COLORS["card_front"],
            rect,
            border_radius=10,
        )

        border_color = self.COLORS["selected"] if selected else self.COLORS["border"]
        pygame.draw.rect(
            self.screen,
            border_color,
            rect,
            2,
            border_radius=10,
        )

        rank_str = self._rank_to_str(card.rank)
        suit_str = self._suit_to_symbol(card.suit)
        color = self.COLORS["red"] if card.suit in (1, 2) else self.COLORS["black"]

        # 左上角資訊
        text_rank = self.font.render(rank_str, True, color)
        text_suit = self.font.render(suit_str, True, color)
        self.screen.blit(text_rank, (x + 6, y + 4))
        self.screen.blit(text_suit, (x + 6, y + 26))

        # 中央大花色：放大一點，讓花色更清楚
        center = self.large_font.render(suit_str, True, color)
        center_rect = center.get_rect(center=(x + self.CARD_WIDTH // 2, y + 65))
        self.screen.blit(center, center_rect)

    def draw_hand(self, hand: Hand, x: int, y: int, selected_indices: List[int]) -> None:
        """繪製玩家手牌。"""
        spacing = 52
        for i, card in enumerate(hand):
            is_selected = i in selected_indices
            offset_y = -15 if is_selected else 0
            self.draw_card(
                card,
                x + i * spacing,
                y + offset_y,
                selected=is_selected,
            )

    # -------------------------------------------------------
    # 玩家資訊
    # -------------------------------------------------------

    def draw_player(
        self,
        player,
        x: int,
        y: int,
        is_current: bool = False,
        is_next: bool = False,
    ) -> None:
        """繪製玩家名稱與剩餘手牌數。"""
        name = player.name

        if is_current:
            name += " [目前回合]"
        elif is_next:
            name += " [下一位]"

        color = (
            self.COLORS["current_turn"]
            if is_current
            else self.COLORS["next_turn"]
            if is_next
            else self.COLORS["text"]
        )

        name_surf = self.font.render(name, True, color)
        count_surf = self.small_font.render(
            f"手牌：{len(player.hand)} 張",
            True,
            self.COLORS["text"],
        )

        self.screen.blit(name_surf, (x, y))
        self.screen.blit(count_surf, (x, y + 24))

    # -------------------------------------------------------
    # 上家出牌
    # -------------------------------------------------------

    def draw_last_play(
        self,
        cards: Optional[List[Card]],
        player_name: str,
        x: int,
        y: int,
    ) -> None:
        """繪製上家出的牌。"""
        if not cards:
            text = self.font.render("目前沒有上家牌型", True, self.COLORS["text"])
            self.screen.blit(text, (x, y))
            return

        title = self.font.render(f"上家出牌：{player_name}", True, self.COLORS["text"])
        self.screen.blit(title, (x, y - 30))

        spacing = 60
        for i, card in enumerate(cards):
            self.draw_card(card, x + i * spacing, y)

    # -------------------------------------------------------
    # 按鈕
    # -------------------------------------------------------

    def draw_buttons(self, buttons: Dict[str, pygame.Rect]) -> None:
        """繪製按鈕。"""
        for name, rect in buttons.items():
            pygame.draw.rect(
                self.screen,
                self.COLORS["button"],
                rect,
                border_radius=10,
            )
            pygame.draw.rect(
                self.screen,
                self.COLORS["text"],
                rect,
                2,
                border_radius=10,
            )

            label = "出牌" if name == "play" else "過牌"
            text = self.font.render(label, True, self.COLORS["text"])
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    # -------------------------------------------------------
    # 回合資訊
    # -------------------------------------------------------

    def draw_turn_info(self, current_name: str, next_name: str, x: int, y: int) -> None:
        """顯示目前輪到誰與下一位玩家。"""
        panel_rect = pygame.Rect(x, y, 260, 72)

        pygame.draw.rect(
            self.screen,
            self.COLORS["panel"],
            panel_rect,
            border_radius=10,
        )
        pygame.draw.rect(
            self.screen,
            self.COLORS["text"],
            panel_rect,
            2,
            border_radius=10,
        )

        current_surf = self.font.render(
            f"目前輪到：{current_name}",
            True,
            self.COLORS["current_turn"],
        )
        next_surf = self.font.render(
            f"下一位：{next_name}",
            True,
            self.COLORS["next_turn"],
        )

        self.screen.blit(current_surf, (x + 10, y + 8))
        self.screen.blit(next_surf, (x + 10, y + 38))

    # -------------------------------------------------------
    # 狀態訊息
    # -------------------------------------------------------

    def draw_status_message(self, message: str, x: int, y: int) -> None:
        """顯示底部狀態訊息。"""
        panel_rect = pygame.Rect(x - 10, y - 6, 920, 36)

        pygame.draw.rect(
            self.screen,
            self.COLORS["status_bg"],
            panel_rect,
            border_radius=8,
        )
        pygame.draw.rect(
            self.screen,
            self.COLORS["text"],
            panel_rect,
            1,
            border_radius=8,
        )

        msg_surface = self.font.render(message, True, self.COLORS["selected"])
        self.screen.blit(msg_surface, (x, y))