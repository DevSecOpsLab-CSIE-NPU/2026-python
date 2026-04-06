from __future__ import annotations

from typing import Optional

from .ai import AIStrategy
from .classifier import HandClassifier
from .finder import HandFinder
from .models import Card, Deck, Player


class BigTwoGame:
    def __init__(self) -> None:
        self.deck = Deck()
        self.players = [
            Player("Player", is_ai=False),
            Player("AI_1", is_ai=True),
            Player("AI_2", is_ai=True),
            Player("AI_3", is_ai=True),
        ]
        self.current_player = 0
        self.last_play: Optional[tuple[list[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1
        self.opening_required = True

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        for player in self.players:
            player.hand.clear()
            player.take_cards(self.deck.deal(13))
            player.hand.sort_desc()

        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = i
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.opening_required = True

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def _is_valid_play(self, cards: list[Card]) -> bool:
        if self.last_play is None:
            if self.opening_required:
                return HandClassifier.can_play(None, cards)
            return HandClassifier.classify(cards) is not None
        return HandClassifier.can_play(self.last_play[0], cards)

    def _all_lead_plays(self, player: Player) -> list[list[Card]]:
        return (
            HandFinder.find_singles(player.hand)
            + HandFinder.find_pairs(player.hand)
            + HandFinder.find_triples(player.hand)
            + HandFinder.find_fives(player.hand)
        )

    def play(self, player: Player, cards: list[Card]) -> bool:
        if player is not self.get_current_player():
            return False

        hand_copy = list(player.hand)
        for c in cards:
            if c not in hand_copy:
                return False
            hand_copy.remove(c)

        if not self._is_valid_play(cards):
            return False

        player.play_cards(cards)
        self.last_play = (list(cards), player.name)
        self.pass_count = 0
        self.opening_required = False
        self.winner = self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        if player is not self.get_current_player():
            return False
        if self.last_play is None:
            return False

        self.pass_count += 1
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Optional[Player]:
        for player in self.players:
            if len(player.hand) == 0:
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai:
            return False

        if self.last_play is None:
            if self.opening_required:
                valid_plays = HandFinder.get_all_valid_plays(player.hand, None)
            else:
                valid_plays = self._all_lead_plays(player)
        else:
            valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play[0])

        best_play = AIStrategy.select_best(
            valid_plays,
            player.hand,
            is_first=(self.opening_required and self.last_play is None),
        )

        if best_play is None:
            return self.pass_(player)
        return self.play(player, best_play)
