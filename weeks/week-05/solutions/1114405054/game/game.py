"""Phase 5: Big Two 遊戲流程控制。"""

from __future__ import annotations

from .ai import AIStrategy
from .classifier import HandClassifier
from .finder import HandFinder
from .models import Card, Deck, Hand, Player


class BigTwoGame:
    """管理牌局初始化、回合推進、出牌合法性與勝負判定。"""

    def __init__(self) -> None:
        self.deck = Deck()
        self.players: list[Player] = []
        self.current_player = 0
        self.last_play: tuple[list[Card], str] | None = None
        self.pass_count = 0
        self.winner: Player | None = None
        self.round_number = 1

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [
            Player("Player1", is_ai=False),
            Player("AI_1", is_ai=True),
            Player("AI_2", is_ai=True),
            Player("AI_3", is_ai=True),
        ]

        for player in self.players:
            player.hand = Hand(self.deck.deal(13))
            player.hand.sort_desc()

        self.current_player = 0
        for idx, player in enumerate(self.players):
            if Card(3, 0) in player.hand:
                self.current_player = idx
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1

    def _is_valid_play(self, cards: list[Card]) -> bool:
        if not cards:
            return False

        if self.last_play is None:
            return HandClassifier.can_play(None, cards)

        return HandClassifier.can_play(self.last_play[0], cards)

    def play(self, player: Player, cards: list[Card]) -> bool:
        if self.winner is not None:
            return False
        if not self.players:
            return False
        if player != self.get_current_player():
            return False
        if any(card not in player.hand for card in cards):
            return False
        if not self._is_valid_play(cards):
            return False

        player.play_cards(cards)
        self.last_play = (list(cards), player.name)
        self.pass_count = 0
        self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        if self.winner is not None:
            return False
        if not self.players:
            return False
        if player != self.get_current_player():
            return False
        if self.last_play is None:
            return False

        self.pass_count += 1
        return True

    def next_turn(self) -> None:
        if not self.players:
            return

        self.current_player = (self.current_player + 1) % len(self.players)

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Player | None:
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def ai_turn(self) -> bool:
        if self.winner is not None:
            return False

        player = self.get_current_player()
        if not player.is_ai:
            return False

        last_cards = None if self.last_play is None else self.last_play[0]
        valid_plays = HandFinder.get_all_valid_plays(player.hand, last_cards)
        best = AIStrategy.select_best(valid_plays, player.hand, is_first=(self.last_play is None))

        if best is None:
            return self.pass_(player)

        return self.play(player, best)
