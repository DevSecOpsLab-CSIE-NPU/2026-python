"""
使用者輸入處理。
"""

from __future__ import annotations

from game.game import BigTwoGame
from ui.render import Renderer


class InputHandler:
    """處理選牌與按鈕操作。"""

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

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if not self.selected_indices:
            return False

        cards = [player.hand.cards[index] for index in sorted(self.selected_indices)]
        if game.play(player, cards):
            self.selected_indices.clear()
            return True
        return False
