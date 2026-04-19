from __future__ import annotations

from dataclasses import dataclass, field

from .ai import AIStrategy
from .classifier import HandClassifier
from .finder import HandFinder
from .models import Card, Deck, Player


@dataclass
class BigTwoGame:
    deck: Deck = field(default_factory=Deck)
    players: list[Player] = field(default_factory=list)
    current_player: int = 0
    last_play: tuple[list[Card], str] | None = None
    pass_count: int = 0
    winner: Player | None = None
    round_number: int = 1
    first_trick: bool = True

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [
            Player("You", is_ai=False),
            Player("AI-1", is_ai=True),
            Player("AI-2", is_ai=True),
            Player("AI-3", is_ai=True),
        ]

        for player in self.players:
            player.take_cards(self.deck.deal(13))

        self.current_player = 0
        for idx, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = idx
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.first_trick = True

    def play(self, player: Player, cards: list[Card]) -> bool:
        if self.players[self.current_player] is not player:
            return False

        if not all(card in player.hand.cards for card in cards):
            return False

        if not self._is_valid_play(cards):
            return False

        player.play_cards(cards)
        self.last_play = (sorted(cards), player.name)
        self.pass_count = 0
        self.first_trick = False
        self.winner = self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        if self.players[self.current_player] is not player:
            return False
        if self.last_play is None:
            return False

        self.pass_count += 1
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % len(self.players)

    def _is_valid_play(self, cards: list[Card]) -> bool:
        last_cards = self.last_play[0] if self.last_play is not None else None
        if last_cards is None and not self.first_trick:
            return HandClassifier.classify(cards) is not None
        return HandClassifier.can_play(last_cards, cards)

    def check_round_reset(self) -> None:
        if self.pass_count >= 3 and self.last_play is not None:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Player | None:
        for player in self.players:
            if len(player.hand) == 0:
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai:
            return False

        last_cards = self.last_play[0] if self.last_play is not None else None
        valid_plays = HandFinder.get_all_valid_plays(
            player.hand,
            last_cards,
            first_turn=self.first_trick,
        )
        selected = AIStrategy.select_best(
            valid_plays,
            player.hand,
            is_first=self.first_trick,
        )

        if selected is None:
            return self.pass_(player)

        return self.play(player, selected)
