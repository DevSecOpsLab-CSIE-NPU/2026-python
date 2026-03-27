"""
Big Two 遊戲流程。
"""

from __future__ import annotations

from game.ai import AIStrategy
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.models import Card, Deck, Hand, Player


class BigTwoGame:
    """管理一局 Big Two 遊戲。"""

    def __init__(self, seed: int | None = None, human_name: str = "Player") -> None:
        self.seed = seed
        self.human_name = human_name
        self.deck = Deck(seed=seed)
        self.players: list[Player] = []
        self.current_player_index = 0
        self.last_play: list[Card] | None = None
        self.last_play_player_name: str | None = None
        self.last_player_index: int | None = None
        self.pass_count = 0
        self.winner: Player | None = None
        self.round_number = 0
        self.first_turn = True

    def setup(self) -> None:
        self.deck = Deck(seed=self.seed)
        self.players = [
            Player(self.human_name, False),
            Player("AI_1", True),
            Player("AI_2", True),
            Player("AI_3", True),
        ]

        for _ in range(13):
            for player in self.players:
                player.take_cards(self.deck.deal(1))

        self.last_play = None
        self.last_play_player_name = None
        self.last_player_index = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.first_turn = True

        for index, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player_index = index
                break

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def next_turn(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self, player: Player, cards: list[Card]) -> bool:
        if self.winner is not None:
            return False
        if not self.players:
            return False
        if player is not self.get_current_player():
            return False
        if not cards or not player.hand.has_cards(cards):
            return False
        if not HandClassifier.can_play(self.last_play, cards, is_first_turn=self.first_turn):
            return False
        if not player.play_cards(cards):
            return False

        self.last_play = sorted(cards, key=lambda card: card.to_sort_key(), reverse=True)
        self.last_play_player_name = player.name
        self.last_player_index = self.current_player_index
        self.pass_count = 0
        self.first_turn = False
        self.winner = self.check_winner()
        if self.winner is None:
            self.next_turn()
        return True

    def pass_turn(self, player: Player) -> bool:
        if self.winner is not None:
            return False
        if player is not self.get_current_player():
            return False
        if self.last_play is None:
            return False

        self.pass_count += 1
        if self.pass_count >= len(self.players) - 1 and self.last_player_index is not None:
            self.last_play = None
            self.last_play_player_name = None
            self.pass_count = 0
            self.current_player_index = self.last_player_index
            self.last_player_index = None
            self.round_number += 1
        else:
            self.next_turn()
        return True

    def check_winner(self) -> Player | None:
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_valid_plays_for_current_player(self) -> list[list[Card]]:
        player = self.get_current_player()
        return HandFinder.get_all_valid_plays(
            player.hand,
            self.last_play,
            is_first_turn=self.first_turn,
        )

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai or self.winner is not None:
            return False

        valid_plays = self.get_valid_plays_for_current_player()
        choice = AIStrategy.select_best(
            valid_plays,
            player.hand,
            is_first_turn=self.first_turn,
        )
        if choice is None:
            return self.pass_turn(player)
        return self.play(player, choice)
