"""Core BigTwo game implementation."""

from .models import Deck, Player
from .classifier import HandClassifier

class BigTwoGame:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(i) for i in range(4)]
        self.current_player = 0
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 0

    def setup(self):
        self.deck.shuffle()
        self.deck.deal(self.players)
        self.current_player = self._find_first_player()
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1

    def _find_first_player(self):
        for index, player in enumerate(self.players):
            if player.has_three_of_clubs():
                return index
        return 0

    def play(self, player, cards):
        if not self._is_valid_play(cards):
            return False
        player.remove_cards(cards)
        self.last_play = (cards, 'play')
        self.pass_count = 0
        self.check_winner()
        return True

    def pass_(self, player):
        self.pass_count += 1
        self.last_play = None if self.pass_count >= 3 else self.last_play
        return True

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def _is_valid_play(self, cards):
        return HandClassifier.can_play(cards, self.last_play)

    def check_round_reset(self):
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    def check_winner(self):
        for player in self.players:
            if not player.hand:
                self.winner = player
                return player
        return None

    def is_game_over(self):
        return self.winner is not None

    def get_current_player(self):
        return self.players[self.current_player]

    def ai_turn(self):
        player = self.get_current_player()
        return None
