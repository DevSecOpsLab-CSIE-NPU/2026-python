from __future__ import annotations

from typing import Dict

import pygame

from p3_finder import HandFinder
from p4_ai import AIStrategy
from p5_game import BigTwoGame
from ui.input import InputHandler
from ui.render import Renderer


class BigTwoApp:
    """大老二 GUI 主程式。"""

    def __init__(self) -> None:
        """初始化 pygame、遊戲物件、渲染器、輸入處理器與按鈕。"""
        pygame.init()

        self.screen: pygame.Surface = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Big Two - GUI")

        self.game: BigTwoGame = BigTwoGame()
        self.game.setup()

        self.renderer: Renderer = Renderer(self.screen)

        # 人類玩家手牌位置
        self.hand_x = 90
        self.hand_y = 520

        # AI 資訊與牌背位置
        self.ai_info_positions = {
            1: (30, 80),
            2: (350, 80),
            3: (670, 80),
        }
        self.ai_card_positions = {
            1: (30, 150),
            2: (350, 150),
            3: (670, 150),
        }

        # 上家出牌區
        self.last_play_x = 320
        self.last_play_y = 290

        # 人類資訊區
        self.human_info_x = 90
        self.human_info_y = 470

        # 回合資訊區
        self.turn_info_x = 610
        self.turn_info_y = 8

        # 狀態訊息區
        self.status_x = 40
        self.status_y = 650
        self.status_message = "遊戲開始"

        # 按鈕
        self.buttons: Dict[str, pygame.Rect] = {
            "play": pygame.Rect(820, 485, 150, 52),
            "pass": pygame.Rect(820, 555, 150, 52),
        }

        self.input_handler: InputHandler = InputHandler(
            hand_x=self.hand_x,
            hand_y=self.hand_y,
            buttons=self.buttons,
        )

        self.last_play_player_name: str = "-"

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        """執行主迴圈。"""
        while self.running:
            self.handle_events()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self) -> None:
        """處理事件與回合推進。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if self.game.is_game_over():
                continue

            # 只有輪到人類時才處理輸入
            if self.game.current_player == 0:
                prev_last_play = self.game.last_play
                current_name = self.game.get_current_player().name

                acted = self.input_handler.handle_event(event, self.game)
                if acted:
                    # 這次有成功出牌
                    if self.game.last_play is not prev_last_play and self.game.last_play is not None:
                        cards_str = " ".join(str(c) for c in self.game.last_play)
                        self.status_message = f"你出牌：{cards_str}"
                        self.last_play_player_name = current_name
                    else:
                        # 一般代表過牌
                        self.status_message = "你過牌"

                    self._finish_turn_after_action()

        # 若輪到 AI，就讓 AI 自動行動直到回到人類或遊戲結束
        while not self.game.is_game_over() and self.game.current_player != 0:
            self._run_ai_turn()

    def _run_ai_turn(self) -> None:
        """執行單一 AI 回合。"""
        ai_player = self.game.get_current_player()
        if not ai_player.is_ai:
            return

        valid_plays = HandFinder.get_all_valid_plays(ai_player.hand, self.game.last_play)
        is_first = self.game.is_first_turn
        best_play = AIStrategy.select_best(valid_plays, ai_player.hand, is_first=is_first)

        if best_play is not None:
            played = self.game.play(ai_player, best_play)
            if played:
                cards_str = " ".join(str(c) for c in best_play)
                self.status_message = f"{ai_player.name} 出牌：{cards_str}"
                self.last_play_player_name = ai_player.name
                self._finish_turn_after_action()
                return

        # AI 不能出牌時過牌
        self.status_message = f"{ai_player.name} 過牌"
        self.game.pass_(ai_player)
        self._finish_turn_after_action()

    def _finish_turn_after_action(self) -> None:
        """玩家完成有效動作後的統一收尾。"""
        winner = self.game.check_winner()
        if winner is not None:
            self.status_message = f"遊戲結束！勝者：{winner.name}"
            return

        old_last_play = self.game.last_play
        self.game.check_round_reset()

        # 若回合被重置，補提示
        if old_last_play is not None and self.game.last_play is None:
            self.status_message = "新回合開始，可自由出牌"

        self.game.next_turn()

    def render(self) -> None:
        """渲染完整遊戲畫面。"""
        self.screen.fill(self.renderer.COLORS["background"])

        # 標題
        title_surface = self.renderer.large_font.render(
            "大老二 Big Two",
            True,
            self.renderer.COLORS["text"],
        )
        self.screen.blit(title_surface, (30, 20))

        current_index = self.game.current_player
        next_index = (current_index + 1) % 4

        # 先畫 AI 玩家資訊
        for ai_index in (1, 2, 3):
            player = self.game.players[ai_index]
            px, py = self.ai_info_positions[ai_index]
            self.renderer.draw_player(
                player,
                px,
                py,
                is_current=(ai_index == current_index),
                is_next=(ai_index == next_index),
            )

        # 再畫 AI 手牌（牌背）
        for ai_index in (1, 2, 3):
            ai_player = self.game.players[ai_index]
            start_x, start_y = self.ai_card_positions[ai_index]
            spacing = 30

            visible_count = min(len(ai_player.hand), 6)
            for i in range(visible_count):
                self.renderer.draw_card(
                    card=ai_player.hand[i],
                    x=start_x + i * spacing,
                    y=start_y,
                    face_down=True,
                )

        # 畫人類玩家資訊
        human_player = self.game.players[0]
        self.renderer.draw_player(
            human_player,
            self.human_info_x,
            self.human_info_y,
            is_current=(0 == current_index),
            is_next=(0 == next_index),
        )

        # 畫人類手牌
        self.renderer.draw_hand(
            human_player.hand,
            self.hand_x,
            self.hand_y,
            self.input_handler.selected_indices,
        )

        # 畫上家出牌
        self.renderer.draw_last_play(
            cards=self.game.last_play,
            player_name=self.last_play_player_name,
            x=self.last_play_x,
            y=self.last_play_y,
        )

        # 畫目前回合 / 下一位
        current_name = self.game.players[current_index].name
        next_name = self.game.players[next_index].name
        self.renderer.draw_turn_info(
            current_name=current_name,
            next_name=next_name,
            x=self.turn_info_x,
            y=self.turn_info_y,
        )

        # 畫按鈕
        self.renderer.draw_buttons(self.buttons)

        # 畫狀態訊息
        self.renderer.draw_status_message(
            self.status_message,
            self.status_x,
            self.status_y,
        )

        # 遊戲結束提示
        if self.game.is_game_over() and self.game.winner is not None:
            win_text = f"遊戲結束！勝者：{self.game.winner.name}"
            win_surface = self.renderer.large_font.render(
                win_text,
                True,
                self.renderer.COLORS["selected"],
            )
            win_rect = win_surface.get_rect(center=(500, 360))

            overlay = pygame.Surface((700, 90), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (150, 315))
            self.screen.blit(win_surface, win_rect)


if __name__ == "__main__":
    app = BigTwoApp()
    app.run()