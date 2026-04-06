from __future__ import annotations

from game.game import BigTwoGame
from .input import InputHandler
from .render import Renderer


class BigTwoApp:
    def __init__(self) -> None:
        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.game = BigTwoGame()
        self.game.setup()

    def handle_events(self) -> None:
        return None

    def render(self) -> None:
        return None

    def run(self) -> None:
        # Placeholder loop: full pygame loop can be added later without changing
        # core gameplay and tests.
        while not self.game.is_game_over():
            current = self.game.get_current_player()
            if current.is_ai:
                self.game.ai_turn()
                self.game.check_round_reset()
                if self.game.is_game_over():
                    break
                self.game.next_turn()
                continue
            break
