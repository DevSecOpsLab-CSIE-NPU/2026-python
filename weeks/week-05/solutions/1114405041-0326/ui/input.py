"""Phase 6：輸入處理。"""

from __future__ import annotations

from game.game import BigTwoGame


class InputHandler:
    HAND_X = 20
    HAND_Y = 400
    CARD_OFFSET = 24

    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices: list[int] = []
        self.last_message = "點選手牌後，再按 Play 出牌。"
        self.buttons = {
            "play": (20, 20, 100, 40),
            "pass": (140, 20, 100, 40),
        }

    def handle_event(self, event, game: BigTwoGame) -> bool:
        event_type = getattr(event, "type", None)

        # 測試時 event_type 可能是字串；實際 pygame 執行時則是整數常數。
        pygame = getattr(self.renderer, "pygame", None)
        mouse_down_values = {"MOUSEBUTTONDOWN"}
        key_down_values = {"KEYDOWN"}
        if pygame is not None:
            mouse_down_values.add(getattr(pygame, "MOUSEBUTTONDOWN", object()))
            key_down_values.add(getattr(pygame, "KEYDOWN", object()))

        if event_type in mouse_down_values:
            return self.handle_click(getattr(event, "pos", (0, 0)), game)
        if event_type in key_down_values:
            return self.handle_key(getattr(event, "key", ""), game)
        return False

    def _card_index_from_pos(self, pos: tuple[int, int], hand_size: int) -> int | None:
        x, y = pos
        if not (self.HAND_Y - 25 <= y <= self.HAND_Y + self.renderer.CARD_HEIGHT + 10):
            return None

        for i in range(hand_size - 1, -1, -1):
            card_x = self.HAND_X + i * self.CARD_OFFSET
            if card_x <= x <= card_x + self.renderer.CARD_WIDTH:
                return i
        return None

    def _advance_turn(self, game: BigTwoGame) -> None:
        """人類玩家完成動作後，只推進到下一位。

        AI 的動作交給主迴圈逐步執行，
        這樣畫面才看得到別人出的牌，不會一瞬間跳過。
        """
        game.check_round_reset()
        if not game.is_game_over():
            game.next_turn()

        if game.is_game_over() and game.winner is not None:
            self.last_message = f"{game.winner.name} 獲勝！"
        elif game.get_current_player().is_ai:
            self.last_message = f"輪到 {game.get_current_player().name}，請稍候。"
        else:
            self.last_message = f"輪到 {game.get_current_player().name}，請出牌。"

    def handle_click(self, pos: tuple[int, int], game: BigTwoGame) -> bool:
        player = game.get_current_player()
        x, y = pos

        if player.is_ai:
            self.last_message = "現在輪到 AI，請稍候。"
            return True

        # 按鈕命中測試
        for name, (bx, by, bw, bh) in self.buttons.items():
            if bx <= x <= bx + bw and by <= y <= by + bh:
                if name == "play":
                    return self.try_play(game)
                if game.opening_move_pending and game.last_play is None:
                    self.last_message = "第一手不能 PASS，請先出 ♣3。"
                    return False
                ok = game.pass_(player)
                if ok:
                    self.selected_indices.clear()
                    self.last_message = "你選擇過牌。"
                    self._advance_turn(game)
                else:
                    self.last_message = "目前不能過牌。"
                return ok

        # 手牌命中測試：根據點到的實際位置切換選牌。
        index = self._card_index_from_pos(pos, len(player.hand))
        if index is None:
            self.last_message = "請點手牌或按鈕。"
            return True

        if index in self.selected_indices:
            self.selected_indices.remove(index)
            self.last_message = f"取消選擇 {player.hand[index]}"
        else:
            self.selected_indices.append(index)
            self.selected_indices.sort()
            self.last_message = f"已選擇 {player.hand[index]}"
        return True

    def handle_key(self, key, game: BigTwoGame) -> bool:
        pygame = getattr(self.renderer, "pygame", None)
        enter_keys = {"ENTER", "KP_ENTER", 13}
        pass_keys = {"P", "p", 112}
        if pygame is not None:
            enter_keys.update({getattr(pygame, "K_RETURN", object()), getattr(pygame, "K_KP_ENTER", object())})
            pass_keys.add(getattr(pygame, "K_p", object()))

        if key in enter_keys:
            return self.try_play(game)
        if key in pass_keys:
            return self.handle_click((150, 30), game)
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if player.is_ai:
            self.last_message = "現在不是你的回合。"
            return False
        if not self.selected_indices:
            self.last_message = "請先選擇要出的牌。"
            return False

        selected_cards = [player.hand[i] for i in sorted(self.selected_indices) if i < len(player.hand)]

        if game.opening_move_pending and game.last_play is None:
            if not any(c.rank == 3 and c.suit == 0 for c in selected_cards):
                self.last_message = "第一手必須包含 ♣3。"
                return False

        ok = game.play(player, selected_cards)
        if ok:
            self.selected_indices.clear()
            self.last_message = "出牌成功。"
            self._advance_turn(game)
        else:
            self.last_message = "這組牌目前不能出。"
        return ok
