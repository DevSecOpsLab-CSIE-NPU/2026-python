"""Phase 6：主應用（可在無 pygame 環境下執行最小回圈）。"""

from __future__ import annotations

from game.game import BigTwoGame
from ui.input import InputHandler
from ui.render import Renderer


class BigTwoApp:
    def __init__(self) -> None:
        self.renderer = Renderer()
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()
        self.game.setup()
        self.buttons = self.input_handler.buttons
        self.running = True

    def handle_events(self, events: list | None = None) -> None:
        if self.game.is_game_over():
            return
        for event in events or []:
            self.input_handler.handle_event(event, self.game)

    def render(self) -> dict:
        # 回傳目前畫面狀態資料，方便測試檢查。
        current = self.game.get_current_player()
        state = {
            "players": [
                self.renderer.draw_player(p, 0, i * 40, is_current=(p is current))
                for i, p in enumerate(self.game.players)
            ],
            "human_hand": self.renderer.draw_hand(self.game.players[0].hand, 20, 400, self.input_handler.selected_indices),
            "buttons": self.renderer.draw_buttons(self.buttons, 0, 0),
            "winner": None if self.game.winner is None else self.game.winner.name,
        }

        if self.game.last_play is not None:
            cards, player_name = self.game.last_play
            state["last_play"] = self.renderer.draw_last_play(cards, player_name, 20, 260)
        else:
            state["last_play"] = None

        return state

    def run(self, max_steps: int = 1) -> None:
        # 測試用途：跑有限步數，避免無限迴圈。
        steps = 0
        while self.running and steps < max_steps and not self.game.is_game_over():
            if self.game.get_current_player().is_ai:
                self.game.ai_turn()
                self.game.check_round_reset()
                self.game.next_turn()
            steps += 1
