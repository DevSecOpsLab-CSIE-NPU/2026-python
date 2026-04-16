"""Phase 6：主應用（同時支援測試模式與實際互動）。"""

from __future__ import annotations

from game.game import BigTwoGame
from ui.input import InputHandler
from ui.render import Renderer


class BigTwoApp:
    WIDTH = 960
    HEIGHT = 560
    FPS = 30

    def __init__(self) -> None:
        self.renderer = Renderer()
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()
        self.game.setup()
        self.buttons = self.input_handler.buttons
        self.running = True
        self.status_message = "點選手牌，然後按 Play 出牌。"

        # 視窗在真正執行 run() 時才建立，避免測試時跳出 GUI。
        self.pygame = getattr(self.renderer, "pygame", None)
        self.screen = None
        self.clock = None
        self.ai_action_delay_ms = 700
        self.last_ai_action_at = 0

    def _ensure_window(self) -> bool:
        if self.pygame is None:
            self.status_message = "找不到 pygame，無法開啟遊戲視窗。"
            return False

        if self.screen is None:
            if not self.pygame.get_init():
                self.pygame.init()
            self.screen = self.pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.pygame.display.set_caption("Big Two 大老二")
            self.clock = self.pygame.time.Clock()
        return True

    def handle_events(self, events: list | None = None) -> None:
        if events is None and self.screen is not None and self.pygame is not None:
            events = self.pygame.event.get()

        for event in events or []:
            if self.pygame is not None and getattr(event, "type", None) == self.pygame.QUIT:
                self.running = False
                return

            handled = self.input_handler.handle_event(event, self.game)
            if handled:
                self.status_message = self.input_handler.last_message

    def render(self) -> dict:
        # 回傳目前畫面狀態資料，方便測試檢查。
        current = self.game.get_current_player()
        state = {
            "players": [
                self.renderer.draw_player(p, 0, i * 40, is_current=(p is current))
                for i, p in enumerate(self.game.players)
            ],
            "human_hand": self.renderer.draw_hand(
                self.game.players[0].hand, 20, 420, self.input_handler.selected_indices
            ),
            "buttons": self.renderer.draw_buttons(self.buttons, 0, 0),
            "winner": None if self.game.winner is None else self.game.winner.name,
            "history": self.game.action_log[-8:],
        }

        if self.game.last_play is not None:
            cards, player_name = self.game.last_play
            state["last_play"] = self.renderer.draw_last_play(cards, player_name, 20, 260)
        else:
            state["last_play"] = None

        if self.screen is not None:
            self.renderer.render_to_screen(self.screen, state, self.status_message)

        return state

    def _run_ai_if_needed(self) -> None:
        if self.running is False or self.game.is_game_over():
            return
        if not self.game.get_current_player().is_ai:
            return

        # 互動模式下加入短暫節奏，讓玩家看得到 AI 的出牌。
        if self.screen is not None and self.pygame is not None:
            now = self.pygame.time.get_ticks()
            if now - self.last_ai_action_at < self.ai_action_delay_ms:
                return
            self.last_ai_action_at = now

        ai_player = self.game.get_current_player()
        old_last_play = self.game.last_play
        self.game.ai_turn()
        self.game.check_round_reset()

        if self.game.is_game_over():
            self.status_message = f"{ai_player.name} 獲勝！"
            return

        if self.game.last_play is not None and self.game.last_play[1] == ai_player.name:
            played_text = " ".join(repr(card) for card in self.game.last_play[0])
            self.status_message = f"{ai_player.name} 出了：{played_text}"
        elif old_last_play is not None and self.game.last_play is None:
            self.status_message = f"{ai_player.name} PASS，這輪重新開始。"
        else:
            self.status_message = f"{ai_player.name} PASS"

        self.game.next_turn()
        if not self.game.is_game_over() and not self.game.get_current_player().is_ai:
            self.status_message += "｜輪到你了。"

    def run(self, max_steps: int | None = None) -> None:
        """執行遊戲。

        - max_steps=None: 真正開啟互動視窗
        - max_steps=數字: 測試模式，跑固定步數
        """
        interactive = max_steps is None
        if interactive and not self._ensure_window():
            return

        steps = 0
        while self.running:
            self.handle_events(None if interactive else [])
            if not self.running:
                break

            if not self.game.is_game_over():
                self._run_ai_if_needed()

            self.render()

            if interactive and self.pygame is not None:
                self.pygame.display.flip()
                self.clock.tick(self.FPS)

            steps += 1
            if max_steps is not None and steps >= max_steps:
                break
            if max_steps is not None and self.game.is_game_over():
                break

        if interactive and self.pygame is not None:
            self.pygame.quit()
