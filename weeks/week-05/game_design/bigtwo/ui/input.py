"""Big Two Card Game - Input Handler"""

import pygame
from typing import List, Tuple, Optional
from game.models import Card, Player
from game.game import BigTwoGame
from game.classifier import HandClassifier, CardType
from game.finder import HandFinder


class InputHandler:
    def __init__(self):
        self.selected_indices: List[int] = []
        self.last_click_time: int = 0
        self.hover_button: Optional[str] = None

    def handle_event(
        self,
        event: pygame.event.Event,
        game: BigTwoGame,
        buttons: dict,
        mouse_pos: Tuple[int, int],
    ) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game, buttons)
        elif event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        elif event.type == pygame.MOUSEMOTION:
            self.hover_button = self._get_hover_button(event.pos, buttons)
        return ""

    def _get_hover_button(self, pos: tuple, buttons: dict) -> Optional[str]:
        for name, (rect, enabled) in buttons.items():
            if rect.collidepoint(pos) and enabled:
                return name
        return None

    def handle_click(self, pos: tuple, game: BigTwoGame, buttons: dict) -> str:
        if game.is_game_over():
            return ""

        player = game.get_current_player()
        if player.is_ai or not game.deal_animation_done:
            return ""

        hand = player.hand
        card_spacing = 25
        total_width = len(hand) * card_spacing + 55
        start_x = 400 - total_width // 2
        start_y = 520

        for i in range(len(hand)):
            card_x = start_x + i * card_spacing
            card_y = start_y - 15 if i in self.selected_indices else start_y

            if card_x <= pos[0] <= card_x + 55 and card_y <= pos[1] <= card_y + 80:
                if i in self.selected_indices:
                    self.selected_indices.remove(i)
                else:
                    self.selected_indices.append(i)
                return ""

        for name, (rect, enabled) in buttons.items():
            if rect.collidepoint(pos) and enabled:
                if name in ["出牌", "Play"]:
                    if self.try_play(game):
                        return "play"
                elif name in ["過牌", "Pass"]:
                    if self.try_pass(game):
                        return "pass"

        return ""

    def handle_key(self, key: int, game: BigTwoGame) -> str:
        if key == pygame.K_RETURN or key == pygame.K_KP_ENTER:
            if self.try_play(game):
                return "play"
        elif key == pygame.K_p:
            if self.try_pass(game):
                return "pass"
        elif key == pygame.K_r and game.is_game_over():
            return "restart"
        elif key == pygame.K_s:
            for i in range(len(self.selected_indices)):
                pass
        elif key == pygame.K_a:
            if self.selected_indices:
                self.selected_indices = list(range(len(game.get_current_player().hand)))
        elif key == pygame.K_ESCAPE:
            self.selected_indices = []
        return ""

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if player.is_ai or game.is_game_over() or not game.deal_animation_done:
            return False

        if not self.selected_indices:
            return False

        selected_cards = [player.hand[i] for i in sorted(self.selected_indices)]

        if game.play(player, selected_cards):
            self.selected_indices = []
            return True

        return False

    def try_pass(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if player.is_ai or game.is_game_over() or not game.deal_animation_done:
            return False

        if game.last_play is None:
            return False

        if game.pass_turn(player):
            self.selected_indices = []
            return True

        return False

    def get_selected_cards(self, hand) -> List[Card]:
        return [hand[i] for i in sorted(self.selected_indices) if i < len(hand)]

    def reset(self) -> None:
        self.selected_indices = []

    def can_play_current_selection(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if not self.selected_indices:
            return False

        selected_cards = [player.hand[i] for i in sorted(self.selected_indices)]
        return game._is_valid_play(selected_cards)
