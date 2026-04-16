"""Phase 5：Big Two 遊戲流程控制。"""

from __future__ import annotations

from typing import Optional

from game.ai import AIStrategy
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.models import Card, Deck, Player


class BigTwoGame:
    """管理牌局狀態與回合流程。"""

    def __init__(self) -> None:
        self.deck = Deck()
        self.players: list[Player] = []
        self.current_player = 0
        self.last_play: Optional[tuple[list[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1
        # 只有整局「第一手」才強制要出 3♣。
        self.opening_move_pending = True
        self.action_log: list[str] = []

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [
            Player("Player", is_ai=False),
            Player("AI_1", is_ai=True),
            Player("AI_2", is_ai=True),
            Player("AI_3", is_ai=True),
        ]

        # 每位玩家發 13 張。
        for p in self.players:
            p.hand = type(p.hand)(self.deck.deal(13))
            p.hand.sort_desc()

        # 找 3♣ 持有者決定先手。
        for i, p in enumerate(self.players):
            if p.hand.find_3_clubs() is not None:
                self.current_player = i
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.opening_move_pending = True
        starter = self.players[self.current_player].name
        self.action_log = [f"Game start. {starter} leads with ♣3."]

    def _is_valid_play(self, cards: list[Card]) -> bool:
        last_cards = None if self.last_play is None else self.last_play[0]

        # 只有整局第一手需要遵守「必須包含 3♣」。
        if self.opening_move_pending:
            return HandClassifier.can_play(None, cards)

        # 新一輪開始（上一手已被重置）時，領頭玩家可以出任何合法牌型。
        if last_cards is None:
            return HandClassifier.classify(cards) is not None

        return HandClassifier.can_play(last_cards, cards)

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def play(self, player: Player, cards: list[Card]) -> bool:
        if self.is_game_over():
            return False
        if player is not self.get_current_player():
            return False
        if not cards:
            return False
        if not all(c in player.hand for c in cards):
            return False
        if not self._is_valid_play(cards):
            return False

        player.play_cards(cards)
        self.last_play = (cards, player.name)
        self.pass_count = 0
        self.opening_move_pending = False
        played_text = " ".join(repr(card) for card in cards)
        self.action_log.append(f"{player.name} played: {played_text}")
        self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        if self.is_game_over():
            return False
        if player is not self.get_current_player():
            return False

        self.pass_count += 1
        self.action_log.append(f"{player.name} PASS")
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1
            self.action_log.append(f"Round {self.round_number} starts.")

    def check_winner(self) -> Optional[Player]:
        for p in self.players:
            if len(p.hand) == 0:
                self.winner = p
                return p
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai or self.is_game_over():
            return False

        last_cards = None if self.last_play is None else self.last_play[0]
        valid_plays = HandFinder.get_all_valid_plays(
            player.hand,
            last_cards,
            is_first_turn=self.opening_move_pending,
        )

        best = AIStrategy.select_best(valid_plays, player.hand, is_first=self.opening_move_pending)
        if best is None:
            return self.pass_(player)

        return self.play(player, best)
