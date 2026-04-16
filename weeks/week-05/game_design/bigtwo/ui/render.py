"""Big Two Card Game - Game Renderer"""

import pygame
from typing import List, Optional, Dict
from game.models import Card, Player
from game.classifier import CardType, HandClassifier


class Renderer:
    COLORS: Dict[str, tuple] = {
        "background": (34, 85, 51),
        "card_bg": (245, 245, 245),
        "card_back": (20, 60, 120),
        "spade_club": (30, 30, 30),
        "heart_diamond": (180, 30, 30),
        "player": (46, 204, 113),
        "ai": (149, 165, 166),
        "selected": (255, 215, 0),
        "button": (52, 152, 219),
        "button_hover": (41, 128, 185),
        "button_disabled": (100, 100, 100),
        "text": (255, 255, 255),
        "text_dark": (50, 50, 50),
        "panel": (0, 80, 40),
        "gold": (255, 193, 7),
    }

    CARD_WIDTH = 55
    CARD_HEIGHT = 80
    CARD_SPACING = 25

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        pygame.font.init()
        self.font_small = pygame.font.Font(None, 20)
        self.font_normal = pygame.font.Font(None, 28)
        self.font_large = pygame.font.Font(None, 40)
        self.font_title = pygame.font.Font(None, 60)

    def draw_card(
        self, card: Card, x: int, y: int, selected: bool = False, face_up: bool = True
    ) -> None:
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)

        if face_up:
            pygame.draw.rect(self.screen, self.COLORS["card_bg"], rect, border_radius=8)
        else:
            pygame.draw.rect(
                self.screen, self.COLORS["card_back"], rect, border_radius=8
            )
            pattern_color = (40, 80, 160)
            for i in range(3):
                for j in range(4):
                    px = x + 10 + i * 15
                    py = y + 10 + j * 18
                    pygame.draw.circle(self.screen, pattern_color, (px, py), 3)

        pygame.draw.rect(self.screen, (200, 200, 200), rect, 1, border_radius=8)

        if selected:
            pygame.draw.rect(
                self.screen, self.COLORS["selected"], rect, 4, border_radius=8
            )
            shadow_rect = pygame.Rect(x + 3, y + 3, self.CARD_WIDTH, self.CARD_HEIGHT)
            pygame.draw.rect(
                self.screen, (255, 200, 0), shadow_rect, 2, border_radius=8
            )

        if face_up:
            color = (
                self.COLORS["heart_diamond"]
                if card.suit in [1, 2]
                else self.COLORS["spade_club"]
            )
            rank_text = Card.RANK_NAMES[card.rank]
            suit_text = Card.SUIT_SYMBOLS[card.suit]

            rank_surf = self.font_normal.render(rank_text, True, color)
            self.screen.blit(rank_surf, (x + 6, y + 5))

            suit_surf = self.font_small.render(suit_text, True, color)
            self.screen.blit(suit_surf, (x + 6, y + 28))

            center_suit = self.font_large.render(suit_text, True, color)
            suit_rect = center_suit.get_rect(
                center=(x + self.CARD_WIDTH // 2, y + self.CARD_HEIGHT // 2 + 5)
            )
            self.screen.blit(center_suit, suit_rect)

            rank_surf2 = self.font_normal.render(rank_text, True, color)
            rank_rect = rank_surf2.get_rect(
                center=(x + self.CARD_WIDTH - 15, y + self.CARD_HEIGHT - 20)
            )
            rotated = pygame.transform.rotate(rank_surf2, 180)
            self.screen.blit(
                rotated, (x + self.CARD_WIDTH - 30, y + self.CARD_HEIGHT - 35)
            )

    def draw_card_back(self, x: int, y: int) -> None:
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        pygame.draw.rect(self.screen, self.COLORS["card_back"], rect, border_radius=8)
        pattern_color = (40, 80, 160)
        for i in range(3):
            for j in range(4):
                px = x + 10 + i * 15
                py = y + 10 + j * 18
                pygame.draw.circle(self.screen, pattern_color, (px, py), 3)

    def draw_hand(
        self,
        hand,
        x: int,
        y: int,
        selected_indices: List[int] = None,
        start_offset: int = 0,
        visible_count: int = -1,
    ) -> None:
        if selected_indices is None:
            selected_indices = []

        if visible_count == -1:
            visible_count = len(hand)

        total_width = visible_count * self.CARD_SPACING + self.CARD_WIDTH
        start_x = x - total_width // 2

        for i in range(visible_count):
            if i < len(hand):
                card = hand[i]
                card_x = start_x + i * self.CARD_SPACING
                card_y = y - 15 if i in selected_indices else y
                self.draw_card(
                    card, card_x, card_y, i in selected_indices, face_up=True
                )

    def draw_player_cards_back(
        self, x: int, y: int, card_count: int, horizontal: bool = True
    ) -> None:
        if horizontal:
            for i in range(min(card_count, 13)):
                self.draw_card_back(x + i * 20, y)
        else:
            for i in range(min(card_count, 13)):
                self.draw_card_back(x, y + i * 25)

    def draw_player_info(
        self,
        player: Player,
        x: int,
        y: int,
        is_current: bool,
        card_count: int,
        horizontal: bool = True,
    ) -> None:
        color = self.COLORS["player"] if not player.is_ai else self.COLORS["ai"]

        if is_current:
            glow_surf = self.font_normal.render(
                f"▶ {player.name}", True, self.COLORS["gold"]
            )
            glow_rect = glow_surf.get_rect(center=(x + 60, y - 10))
            self.screen.blit(glow_surf, glow_rect)
            pygame.draw.circle(self.screen, self.COLORS["gold"], (x - 20, y - 10), 8)
        else:
            name_surf = self.font_normal.render(player.name, True, color)
            self.screen.blit(name_surf, (x, y - 10))

        count_surf = self.font_small.render(
            f"({card_count}張)", True, self.COLORS["text"]
        )
        self.screen.blit(count_surf, (x, y + 12))

        if card_count > 0:
            if horizontal:
                self.draw_player_cards_back(x, y + 30, min(card_count, 8), True)
            else:
                self.draw_player_cards_back(x - 30, y + 5, min(card_count, 5), False)

    def draw_last_play(
        self, cards: Optional[List[Card]], player_name: str, x: int, y: int
    ) -> None:
        panel_rect = pygame.Rect(x - 10, y - 10, 320, 120)
        pygame.draw.rect(self.screen, (0, 50, 30), panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0, 100, 60), panel_rect, 2, border_radius=10)

        label = self.font_normal.render(
            f"上一手: {player_name}", True, self.COLORS["text"]
        )
        self.screen.blit(label, (x, y))

        if cards:
            for i, card in enumerate(cards):
                self.draw_card(card, x + 20 + i * 60, y + 30, face_up=True)

            classification = HandClassifier.classify(cards)
            if classification:
                type_name = HandClassifier.get_type_name(classification[0])
                type_surf = self.font_small.render(
                    f"牌型: {type_name}", True, self.COLORS["gold"]
                )
                self.screen.blit(type_surf, (x + 20, y + 105))
        else:
            pass_text = self.font_normal.render("沒有人出牌", True, self.COLORS["ai"])
            self.screen.blit(pass_text, (x + 50, y + 60))

    def draw_buttons(self, buttons: Dict, mouse_pos: tuple) -> None:
        for name, (rect, enabled) in buttons.items():
            color = (
                self.COLORS["button_hover"]
                if rect.collidepoint(mouse_pos) and enabled
                else self.COLORS["button"]
                if enabled
                else self.COLORS["button_disabled"]
            )

            pygame.draw.rect(self.screen, color, rect, border_radius=8)
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 1, border_radius=8)

            text_surf = self.font_normal.render(name, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=rect.center)
            self.screen.blit(text_surf, text_rect)

    def draw_game_over(self, winner: Player) -> None:
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        title = "遊戲結束!"
        title_surf = self.font_title.render(title, True, self.COLORS["gold"])
        title_rect = title_surf.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(title_surf, title_rect)

        winner_text = f"{winner.name} 勝利!"
        if winner.is_ai:
            winner_text = "很遺憾，電腦獲勝了!"
        winner_surf = self.font_large.render(winner_text, True, self.COLORS["player"])
        winner_rect = winner_surf.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(winner_surf, winner_rect)

        restart_surf = self.font_normal.render(
            "按 R 鍵重新開始", True, self.COLORS["text"]
        )
        restart_rect = restart_surf.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(restart_surf, restart_rect)

    def draw_rules(self) -> None:
        rules_text = [
            "【大老二規則】",
            "• 持有梅花3的玩家先出牌",
            "• 必須出比上家大的牌（同類型）",
            "• 連續3人過牌可重新開始",
            "• 牌型大小: 同花順 > 四條 > 葫蘆 > 同花 > 順子 > 三條 > 對子 > 單張",
            "• 數字大小: 2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3",
            "• 操控: 點擊選牌, Play/Enter出牌, Pass/P過牌",
        ]

        y = 50
        for i, line in enumerate(rules_text):
            color = self.COLORS["gold"] if i == 0 else self.COLORS["text"]
            size = 28 if i == 0 else 20
            font = pygame.font.Font(None, size)
            surf = font.render(line, True, color)
            self.screen.blit(surf, (10, y + i * 25))

    def draw_dealing_animation(self, players: List[Player], current_round: int) -> None:
        msg = f"發牌中... ({len(players[0].hand)}/13)"
        msg_surf = self.font_large.render(msg, True, self.COLORS["gold"])
        msg_rect = msg_surf.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        pygame.draw.rect(
            self.screen, (0, 50, 30), msg_rect.inflate(40, 20), border_radius=10
        )
        self.screen.blit(msg_surf, msg_rect)
