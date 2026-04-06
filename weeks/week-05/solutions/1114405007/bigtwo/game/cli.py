from __future__ import annotations

from .game import BigTwoGame
from .models import Card


class BigTwoCLI:
    def __init__(self) -> None:
        self.game = BigTwoGame()
        self.game.setup()

    @staticmethod
    def _format_cards(cards: list[Card]) -> str:
        return " ".join(repr(c) for c in cards)

    @staticmethod
    def _show_hand(player_hand: list[Card]) -> None:
        parts = [f"[{i}] {repr(card)}" for i, card in enumerate(player_hand)]
        print("你的手牌:", "  ".join(parts))

    def _human_turn(self) -> None:
        player = self.game.get_current_player()
        while True:
            print("\n你的回合")
            if self.game.last_play is not None:
                last_cards, last_name = self.game.last_play
                print(f"上家出牌: {last_name} -> {self._format_cards(last_cards)}")
            else:
                if self.game.opening_required:
                    print("開局第一手必須包含 ♣3")
                else:
                    print("你是新一輪首家，可自由領牌")

            self._show_hand(player.hand)
            raw = input("輸入牌索引(空白分隔)，或輸入 p 過牌: ").strip()
            if not raw:
                print("請輸入指令")
                continue

            if raw.lower() == "p":
                if self.game.pass_(player):
                    print("你選擇過牌")
                    return
                print("目前不能過牌，請出牌")
                continue

            try:
                idxs = [int(x) for x in raw.split()]
            except ValueError:
                print("索引格式錯誤，請重新輸入")
                continue

            if len(set(idxs)) != len(idxs):
                print("索引不可重複")
                continue

            if any(i < 0 or i >= len(player.hand) for i in idxs):
                print("索引超出範圍")
                continue

            cards = [player.hand[i] for i in sorted(idxs)]
            if self.game.play(player, cards):
                print(f"你出牌: {self._format_cards(cards)}")
                return

            print("不合法的出牌，請重試")

    def _ai_turn(self) -> None:
        player = self.game.get_current_player()
        previous_last = self.game.last_play
        ok = self.game.ai_turn()
        if not ok:
            print(f"{player.name} 不能出牌，回合異常")
            return

        if self.game.last_play is not None and self.game.last_play != previous_last and self.game.last_play[1] == player.name:
            cards, _ = self.game.last_play
            print(f"{player.name} 出牌: {self._format_cards(cards)}")
        else:
            print(f"{player.name} 過牌")

    def run(self) -> None:
        print("=== Big Two CLI ===")
        print("規則: 輸入牌索引出牌，或輸入 p 過牌")

        while not self.game.is_game_over():
            current = self.game.get_current_player()
            if current.is_ai:
                self._ai_turn()
            else:
                self._human_turn()

            self.game.check_round_reset()
            if self.game.last_play is None and not self.game.opening_required:
                print("本輪結束，重新領牌")

            if self.game.is_game_over():
                break
            self.game.next_turn()

        if self.game.winner is not None:
            print(f"\n遊戲結束，勝者: {self.game.winner.name}")
