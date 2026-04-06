from __future__ import annotations

from game.game import BigTwoGame


class InputHandler:
    def __init__(self) -> None:
        self.selected_indices: list[int] = []
        self.buttons: dict[str, tuple[int, int, int, int]] = {
            "play": (20, 20, 120, 40),
            "pass": (160, 20, 120, 40),
        }

    def handle_event(self, event, game: BigTwoGame) -> bool:
        return False

    def handle_click(self, pos: tuple[int, int], game: BigTwoGame) -> bool:
        return False

    def handle_key(self, key: str, game: BigTwoGame) -> bool:
        if key.lower() == "p":
            return game.pass_(game.get_current_player())
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if not self.selected_indices:
            return False

        cards = [player.hand[i] for i in sorted(self.selected_indices) if i < len(player.hand)]
        ok = game.play(player, cards)
        if ok:
            self.selected_indices.clear()
        return ok
