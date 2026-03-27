"""
應用程式入口。
"""

from __future__ import annotations

import sys

from game.ai import AIStrategy
from game.game import BigTwoGame
from ui.input import InputHandler
from ui.render import Renderer, pygame


class BigTwoApp:
    """整合遊戲邏輯與介面。"""

    def __init__(self, seed: int | None = None, use_gui: bool | None = None) -> None:
        self.game = BigTwoGame(seed=seed)
        self.game.setup()
        self.renderer = Renderer()
        self.input_handler = InputHandler(self.renderer)
        self.use_gui = pygame is not None if use_gui is None else use_gui and pygame is not None

        self.screen = None
        self.clock = None
        if self.use_gui and pygame is not None:
            pygame.init()
            self.screen = pygame.display.set_mode((960, 720))
            self.clock = pygame.time.Clock()
            pygame.display.set_caption("Big Two")

    def run(self, max_rounds: int = 200):
        if self.use_gui and pygame is not None:
            return self._run_gui()
        return self.run_cli(max_rounds=max_rounds)

    def _run_gui(self):  # pragma: no cover - 需要本機圖形環境
        assert pygame is not None
        assert self.screen is not None
        assert self.clock is not None

        running = True
        while running and not self.game.is_game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.game.get_current_player().is_ai:
                self.game.ai_turn()

            self.screen.fill(Renderer.COLORS["background"])
            hand_surface = self.renderer.draw_hand(
                self.game.players[0].hand,
                0,
                0,
                selected_indices=self.input_handler.selected_indices,
            )
            self.screen.blit(hand_surface, (20, 580))
            pygame.display.flip()
            self.clock.tick(30)

        return self.game.winner

    def run_cli(self, max_rounds: int = 200):
        rounds = 0
        while not self.game.is_game_over() and rounds < max_rounds:
            player = self.game.get_current_player()
            valid_plays = self.game.get_valid_plays_for_current_player()

            if player.is_ai or not sys.stdin.isatty():
                choice = AIStrategy.select_best(
                    valid_plays,
                    player.hand,
                    is_first_turn=self.game.first_turn,
                )
                if choice is None:
                    self.game.pass_turn(player)
                else:
                    self.game.play(player, choice)
            else:  # pragma: no cover - 互動流程不在自動測試範圍
                self._run_human_turn(player, valid_plays)

            rounds += 1

        return self.game.winner

    def _run_human_turn(self, player, valid_plays):  # pragma: no cover - 互動流程
        print(f"\n目前輪到: {player.name}")
        print("你的手牌:")
        for index, card in enumerate(player.hand.cards):
            print(f"  {index}: {card}")
        if self.game.last_play is not None:
            print(f"上一手: {' '.join(map(str, self.game.last_play))}")
        else:
            print("上一手: 無")

        command = input("輸入牌索引（逗號分隔），或輸入 p 表示 pass: ").strip()
        if command.lower() == "p":
            self.game.pass_turn(player)
            return

        try:
            indices = [int(part.strip()) for part in command.split(",") if part.strip()]
        except ValueError:
            print("輸入格式錯誤。")
            return

        cards = [player.hand.cards[index] for index in indices if 0 <= index < len(player.hand.cards)]
        if cards not in valid_plays:
            print("這手牌目前不能出。")
            return

        self.game.play(player, cards)
