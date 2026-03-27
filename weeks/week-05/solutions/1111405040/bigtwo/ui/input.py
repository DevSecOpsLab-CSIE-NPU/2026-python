"""
使用者輸入處理。
"""

from __future__ import annotations

from game.game import BigTwoGame
from ui.render import Renderer, pygame


class InputHandler:
    """處理選牌、按鈕與鍵盤操作。"""

    HAND_X = 20
    HAND_Y = 620

    def __init__(self, renderer: Renderer | None = None) -> None:
        self.renderer = renderer or Renderer()
        self.selected_indices: set[int] = set()
        self.buttons = dict(Renderer.BUTTONS)

    def button_at(self, pos: tuple[int, int]) -> str | None:
        x, y = pos
        for name, (bx, by, width, height) in self.buttons.items():
            if bx <= x <= bx + width and by <= y <= by + height:
                return name
        return None

    def toggle_selection(self, index: int, hand_size: int) -> None:
        if index < 0 or index >= hand_size:
            return
        if index in self.selected_indices:
            self.selected_indices.remove(index)
        else:
            self.selected_indices.add(index)

    def card_index_at(self, pos: tuple[int, int], hand_size: int) -> int | None:
        px, py = pos
        layout = self.renderer.hand_layout(hand_size, self.HAND_X, self.HAND_Y)
        for index in range(hand_size - 1, -1, -1):
            x, y, width, height = layout[index]
            if index in self.selected_indices:
                y -= 10
            if x <= px <= x + width and y <= py <= y + height:
                return index
        return None

    def handle_click(self, pos: tuple[int, int], game: BigTwoGame) -> bool:
        player = game.get_current_player()

        button = self.button_at(pos)
        if button == "play":
            return self.try_play(game)
        if button == "pass":
            if game.pass_turn(player):
                self.selected_indices.clear()
                return True
            return False
        if button == "sort":
            player.hand.sort_desc()
            return True

        if player.is_ai:
            return False

        card_index = self.card_index_at(pos, len(player.hand.cards))
        if card_index is None:
            return False

        self.toggle_selection(card_index, len(player.hand.cards))
        return True

    def handle_key(self, key, game: BigTwoGame) -> bool:
        if pygame is not None:
            if key == pygame.K_RETURN:
                return self.try_play(game)
            if key == pygame.K_p:
                player = game.get_current_player()
                if game.pass_turn(player):
                    self.selected_indices.clear()
                    return True
                return False
            if key == pygame.K_s:
                game.get_current_player().hand.sort_desc()
                return True

        if key in ("\r", "\n", "enter"):
            return self.try_play(game)
        if key in ("p", "P"):
            player = game.get_current_player()
            if game.pass_turn(player):
                self.selected_indices.clear()
                return True
            return False
        if key in ("s", "S"):
            game.get_current_player().hand.sort_desc()
            return True
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if not self.selected_indices:
            return False

        cards = [player.hand.cards[index] for index in sorted(self.selected_indices)]
        if game.play(player, cards):
            self.selected_indices.clear()
            return True
        return False
