"""Phase 6：輸入處理。"""

from __future__ import annotations

from game.game import BigTwoGame


class InputHandler:
    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices: list[int] = []
        self.buttons = {
            "play": (20, 20, 100, 40),
            "pass": (140, 20, 100, 40),
        }

    def handle_event(self, event, game: BigTwoGame) -> bool:
        event_type = getattr(event, "type", None)
        if event_type == "MOUSEBUTTONDOWN":
            return self.handle_click(getattr(event, "pos", (0, 0)), game)
        if event_type == "KEYDOWN":
            return self.handle_key(getattr(event, "key", ""), game)
        return False

    def handle_click(self, pos: tuple[int, int], game: BigTwoGame) -> bool:
        x, y = pos
        # 按鈕命中測試
        for name, (bx, by, bw, bh) in self.buttons.items():
            if bx <= x <= bx + bw and by <= y <= by + bh:
                if name == "play":
                    return self.try_play(game)
                return game.pass_(game.get_current_player())

        # 牌區命中（簡化）：點一下就切換第 0 張的選取狀態。
        if 0 in self.selected_indices:
            self.selected_indices.remove(0)
        else:
            self.selected_indices.append(0)
        return True

    def handle_key(self, key, game: BigTwoGame) -> bool:
        if key in ("ENTER", "KP_ENTER", 13):
            return self.try_play(game)
        if key in ("P", "p", 112):
            return game.pass_(game.get_current_player())
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if not self.selected_indices:
            return False

        selected_cards = [player.hand[i] for i in sorted(self.selected_indices) if i < len(player.hand)]
        ok = game.play(player, selected_cards)
        if ok:
            self.selected_indices.clear()
        return ok
