"""Big Two Card Game - Main Application"""

import pygame
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.game import BigTwoGame
from game.classifier import HandClassifier, CardType


class BigTwoApp:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 700
    FPS = 60

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("大老二 - Big Two")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.font_small = pygame.font.Font(None, 20)
        self.font_normal = pygame.font.Font(None, 28)
        self.font_large = pygame.font.Font(None, 42)
        self.font_title = pygame.font.Font(None, 56)
        self.font_big = pygame.font.Font(None, 72)

        self.CARD_WIDTH = 55
        self.CARD_HEIGHT = 80
        self.CARD_SPACING = 25

        self.game = BigTwoGame()
        self.input_handler = InputHandler(self)

        self.buttons = {
            "出牌": pygame.Rect(550, 610, 90, 45),
            "過牌": pygame.Rect(650, 610, 90, 45),
        }

        self.deal_timer = 0
        self.last_update_time = 0
        self.animation_cards = []
        self.selected_indices = []

        self.run()

    def run(self) -> None:
        running = True
        while running:
            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.game.is_game_over():
                            running = False
                        else:
                            self.selected_indices = []
                    elif event.key == pygame.K_r and self.game.is_game_over():
                        self.restart_game()
                    elif event.key == pygame.K_a:
                        self.selected_indices = list(
                            range(len(self.game.players[0].hand))
                        )
                    elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                        self.try_play()
                    elif event.key == pygame.K_p:
                        self.try_pass()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

    def handle_click(self, pos: tuple) -> None:
        if self.game.is_game_over():
            return

        if self.game.dealing_cards:
            return

        player = self.game.get_current_player()
        if player.is_ai or not self.game.deal_animation_done:
            return

        hand = player.hand
        total_width = len(hand) * self.CARD_SPACING + self.CARD_WIDTH
        start_x = 400 - total_width // 2
        start_y = 520

        for i in range(len(hand)):
            card_x = start_x + i * self.CARD_SPACING
            card_y = start_y - 15 if i in self.selected_indices else start_y

            if (
                card_x <= pos[0] <= card_x + self.CARD_WIDTH
                and card_y <= pos[1] <= card_y + self.CARD_HEIGHT
            ):
                if i in self.selected_indices:
                    self.selected_indices.remove(i)
                else:
                    self.selected_indices.append(i)
                return

        if self.buttons["出牌"].collidepoint(pos):
            self.try_play()
        elif self.buttons["過牌"].collidepoint(pos):
            self.try_pass()

    def try_play(self) -> None:
        player = self.game.get_current_player()
        if (
            player.is_ai
            or self.game.is_game_over()
            or not self.game.deal_animation_done
        ):
            return

        if not self.selected_indices:
            return

        selected_cards = [player.hand[i] for i in sorted(self.selected_indices)]

        if self.game.play(player, selected_cards):
            self.selected_indices = []
            self.game.next_turn()

    def try_pass(self) -> None:
        player = self.game.get_current_player()
        if (
            player.is_ai
            or self.game.is_game_over()
            or not self.game.deal_animation_done
        ):
            return

        if self.game.last_play is None:
            return

        if self.game.pass_turn(player):
            self.selected_indices = []
            self.game.next_turn()

    def update(self) -> None:
        if self.game.dealing_cards:
            if self.current_time - self.deal_timer > 100:
                self.deal_timer = self.current_time
                self.game.deal_one_round()
            return

        current = self.game.get_current_player()

        if current.is_ai and not self.game.is_game_over():
            if self.current_time - self.last_update_time > 700:
                self.last_update_time = self.current_time
                ai_play = self.game.ai_turn()
                if ai_play:
                    self.game.play(current, ai_play)
                else:
                    self.game.pass_turn(current)
                self.game.next_turn()

    def restart_game(self) -> None:
        self.game = BigTwoGame()
        self.game.setup()
        self.selected_indices = []
        self.buttons = {
            "出牌": pygame.Rect(550, 610, 90, 45),
            "過牌": pygame.Rect(650, 610, 90, 45),
        }

    def get_card_color(self, card) -> tuple:
        return (180, 30, 30) if card.suit in [1, 2] else (30, 30, 30)

    def draw_card(
        self, card, x: int, y: int, selected: bool = False, face_up: bool = True
    ) -> None:
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)

        if face_up:
            pygame.draw.rect(self.screen, (250, 250, 250), rect, border_radius=8)
        else:
            pygame.draw.rect(self.screen, (30, 80, 160), rect, border_radius=8)
            for i in range(3):
                for j in range(4):
                    px = x + 12 + i * 14
                    py = y + 12 + j * 16
                    pygame.draw.circle(self.screen, (50, 100, 180), (px, py), 3)

        pygame.draw.rect(self.screen, (180, 180, 180), rect, 1, border_radius=8)

        if selected:
            pygame.draw.rect(self.screen, (255, 215, 0), rect, 4, border_radius=8)

        if face_up:
            color = self.get_card_color(card)
            rank_text = card.RANK_NAMES[card.rank]
            suit_text = card.SUIT_SYMBOLS[card.suit]

            rank_surf = self.font_normal.render(rank_text, True, color)
            self.screen.blit(rank_surf, (x + 6, y + 5))

            suit_surf = self.font_small.render(suit_text, True, color)
            self.screen.blit(suit_surf, (x + 6, y + 28))

            center_suit = self.font_large.render(suit_text, True, color)
            suit_rect = center_suit.get_rect(
                center=(x + self.CARD_WIDTH // 2, y + self.CARD_HEIGHT // 2 + 3)
            )
            self.screen.blit(center_suit, suit_rect)

    def draw_card_back(self, x: int, y: int) -> None:
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        pygame.draw.rect(self.screen, (30, 80, 160), rect, border_radius=8)
        for i in range(3):
            for j in range(4):
                px = x + 12 + i * 14
                py = y + 12 + j * 16
                pygame.draw.circle(self.screen, (50, 100, 180), (px, py), 3)

    def draw_hand(self, hand, x: int, y: int) -> None:
        total_width = len(hand) * self.CARD_SPACING + self.CARD_WIDTH
        start_x = x - total_width // 2

        for i, card in enumerate(hand):
            card_x = start_x + i * self.CARD_SPACING
            card_y = y - 15 if i in self.selected_indices else y
            self.draw_card(card, card_x, card_y, i in self.selected_indices, True)

    def draw_player_cards(
        self, x: int, y: int, card_count: int, horizontal: bool = True
    ) -> None:
        for i in range(min(card_count, 8)):
            if horizontal:
                self.draw_card_back(x + i * 18, y)
            else:
                self.draw_card_back(x, y + i * 22)

    def draw_player_info(
        self,
        player,
        x: int,
        y: int,
        is_current: bool,
        card_count: int,
        horizontal: bool = True,
    ) -> None:
        color = (70, 200, 120) if not player.is_ai else (140, 150, 155)

        if is_current:
            pygame.draw.circle(self.screen, (255, 200, 0), (x - 15, y - 8), 8)
            name_surf = self.font_normal.render(f"▶ {player.name}", True, (255, 200, 0))
        else:
            name_surf = self.font_normal.render(player.name, True, color)
        self.screen.blit(name_surf, (x, y - 10))

        count_surf = self.font_small.render(f"({card_count}張)", True, (200, 200, 200))
        self.screen.blit(count_surf, (x, y + 15))

        if card_count > 0:
            if horizontal:
                self.draw_player_cards(x, y + 35, card_count, True)
            else:
                self.draw_player_cards(x - 25, y + 5, card_count, False)

    def draw_last_play(self, cards, player_name: str, x: int, y: int) -> None:
        panel_rect = pygame.Rect(x - 10, y - 10, 320, 115)
        pygame.draw.rect(self.screen, (15, 60, 35), panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, (40, 100, 70), panel_rect, 2, border_radius=10)

        label = self.font_normal.render(f"上一手: {player_name}", True, (255, 255, 255))
        self.screen.blit(label, (x, y))

        if cards:
            for i, card in enumerate(cards):
                self.draw_card(card, x + 20 + i * 58, y + 28, False, True)

            classification = HandClassifier.classify(cards)
            if classification:
                type_names = {
                    CardType.SINGLE: "單張",
                    CardType.PAIR: "對子",
                    CardType.TRIPLE: "三條",
                    CardType.STRAIGHT: "順子",
                    CardType.FLUSH: "同花",
                    CardType.FULL_HOUSE: "葫蘆",
                    CardType.FOUR_OF_A_KIND: "四條",
                    CardType.STRAIGHT_FLUSH: "同花順",
                }
                type_name = type_names.get(classification[0], "未知")
                type_surf = self.font_small.render(
                    f"牌型: {type_name}", True, (255, 200, 100)
                )
                self.screen.blit(type_surf, (x + 20, y + 100))
        else:
            pass_text = self.font_normal.render("等待首回合...", True, (140, 150, 155))
            self.screen.blit(pass_text, (x + 40, y + 55))

    def draw_buttons(self) -> None:
        mouse_pos = pygame.mouse.get_pos()

        can_play = False
        can_pass = self.game.last_play is not None

        player = self.game.get_current_player()
        if not player.is_ai and self.game.deal_animation_done and self.selected_indices:
            selected_cards = [player.hand[i] for i in sorted(self.selected_indices)]
            can_play = self.game._is_valid_play(selected_cards)

        play_rect = self.buttons["出牌"]
        pass_rect = self.buttons["過牌"]

        play_color = (
            (50, 150, 210)
            if play_rect.collidepoint(mouse_pos) and can_play
            else (100, 100, 100)
            if not can_play
            else (60, 140, 200)
        )
        pass_color = (
            (50, 150, 210)
            if pass_rect.collidepoint(mouse_pos) and can_pass
            else (100, 100, 100)
            if not can_pass
            else (60, 140, 200)
        )

        pygame.draw.rect(self.screen, play_color, play_rect, border_radius=8)
        pygame.draw.rect(self.screen, pass_color, pass_rect, border_radius=8)

        play_text = self.font_normal.render("出牌", True, (255, 255, 255))
        pass_text = self.font_normal.render("過牌", True, (255, 255, 255))

        play_rect2 = play_text.get_rect(center=play_rect.center)
        pass_rect2 = pass_text.get_rect(center=pass_rect.center)

        self.screen.blit(play_text, play_rect2)
        self.screen.blit(pass_text, pass_rect2)

    def draw_rules(self) -> None:
        rules = [
            "【大老二】點擊選牌 | Enter出牌 | P過牌 | A全選 | ESC取消",
        ]
        for i, rule in enumerate(rules):
            surf = self.font_small.render(rule, True, (180, 180, 180))
            self.screen.blit(surf, (10, 15 + i * 22))

    def draw_dealing_animation(self) -> None:
        msg = f"發牌中... ({len(self.game.players[0].hand)}/13)"
        msg_surf = self.font_large.render(msg, True, (255, 200, 0))
        msg_rect = msg_surf.get_rect(center=(400, 350))
        bg_rect = msg_rect.inflate(60, 30)
        pygame.draw.rect(self.screen, (0, 60, 40), bg_rect, border_radius=12)
        pygame.draw.rect(self.screen, (0, 150, 80), bg_rect, 3, border_radius=12)
        self.screen.blit(msg_surf, msg_rect)

    def draw_game_over(self) -> None:
        overlay = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        title = "遊戲結束"
        title_surf = self.font_big.render(title, True, (255, 200, 0))
        title_rect = title_surf.get_rect(center=(400, 200))
        self.screen.blit(title_surf, title_rect)

        winner = self.game.winner
        if winner:
            if winner.is_ai:
                winner_text = "電腦獲勝了!"
                winner_color = (200, 80, 80)
            else:
                winner_text = "恭喜你獲勝了!"
                winner_color = (70, 200, 120)

            winner_surf = self.font_large.render(winner_text, True, winner_color)
            winner_rect = winner_surf.get_rect(center=(400, 300))
            self.screen.blit(winner_surf, winner_rect)

        hint_surf = self.font_normal.render(
            "按 R 鍵重新開始 | ESC 離開", True, (180, 180, 180)
        )
        hint_rect = hint_surf.get_rect(center=(400, 400))
        self.screen.blit(hint_surf, hint_rect)

    def render(self) -> None:
        self.screen.fill((34, 85, 51))

        table_rect = pygame.Rect(50, 60, 700, 530)
        pygame.draw.rect(self.screen, (25, 85, 45), table_rect, border_radius=20)
        pygame.draw.rect(self.screen, (60, 130, 80), table_rect, 3, border_radius=20)

        self.draw_rules()

        if self.game.dealing_cards or not self.game.deal_animation_done:
            self.draw_dealing_animation()
            for i, player in enumerate(self.game.players):
                if i == 0:
                    self.draw_player_info(
                        player, 400, 600, False, len(player.hand), True
                    )
                else:
                    angle = (i - 1) * 90
                    if i == 1:
                        self.draw_player_info(
                            player, 720, 300, False, len(player.hand), False
                        )
                    elif i == 2:
                        self.draw_player_info(
                            player, 100, 300, False, len(player.hand), False
                        )
                    elif i == 3:
                        self.draw_player_info(
                            player, 100, 100, False, len(player.hand), True
                        )
            return

        p1 = self.game.players[0]
        p2 = self.game.players[1]
        p3 = self.game.players[2]
        p4 = self.game.players[3]

        self.draw_player_info(
            p2, 720, 320, self.game.current_player == 1, len(p2.hand), False
        )
        self.draw_player_info(
            p3, 80, 320, self.game.current_player == 2, len(p3.hand), False
        )
        self.draw_player_info(
            p4, 80, 100, self.game.current_player == 3, len(p4.hand), True
        )

        last_player_name = ""
        if self.game.last_player is not None:
            last_player_name = self.game.players[self.game.last_player].name
        self.draw_last_play(self.game.last_play, last_player_name, 240, 280)

        current = self.game.get_current_player()
        if not current.is_ai:
            self.draw_hand(p1.hand, 400, 550)
        else:
            label = self.font_normal.render(
                f"{current.name} 思考中...", True, (255, 200, 0)
            )
            label_rect = label.get_rect(center=(400, 550))
            self.screen.blit(label, label_rect)

        self.draw_buttons()

        if not current.is_ai and self.game.last_play is not None:
            valid_count = self.game.get_valid_play_count()
            if valid_count == 0:
                hint_surf = self.font_small.render(
                    "沒有能出的牌，請點擊過牌", True, (255, 100, 100)
                )
                self.screen.blit(hint_surf, (300, 495))

        info = f"回合: {self.game.round_number}"
        if self.game.pass_count > 0:
            info += f" | 連續過牌: {self.game.pass_count}/3"
        info_surf = self.font_small.render(info, True, (160, 160, 160))
        self.screen.blit(info_surf, (350, 670))

        if self.game.is_game_over():
            self.draw_game_over()


class InputHandler:
    def __init__(self, app: BigTwoApp):
        self.app = app
        self.selected_indices = []
