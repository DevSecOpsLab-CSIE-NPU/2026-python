from game.models import Deck, Player
from game.classifier import HandClassifier
from game.ai import AIStrategy
from game.finder import HandFinder


class BigTwoGame:
    def __init__(self):
        self.deck = None
        self.players = []
        self.current_player = 0
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 0

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [
            Player("玩家 1", is_ai=False),
            Player("AI 1", is_ai=True),
            Player("AI 2", is_ai=True),
            Player("AI 3", is_ai=True),
        ]
        for p in self.players:
            p.take_cards(self.deck.deal(13))
        for i, p in enumerate(self.players):
            if p.hand.find_3_clubs() is not None:
                self.current_player = i
                break
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 0

    def play(self, player, cards):
        if not self._is_valid_play(cards):
            return False
        if not HandClassifier.can_play(self.last_play and self.last_play[0], cards):
            return False
        player.play_cards(cards)
        self.last_play = (cards, player.name)
        self.pass_count = 0
        self.next_turn()
        if len(player.hand) == 0:
            self.winner = player
        return True

    def pass_(self, player):
        self.pass_count += 1
        self.check_round_reset()
        self.next_turn()
        return True

    def next_turn(self):
        self.current_player = (self.current_player + 1) % 4

    def _is_valid_play(self, cards):
        if len(cards) == 0:
            return False
        return HandClassifier.classify(cards) is not None

    def check_round_reset(self):
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    def check_winner(self):
        for p in self.players:
            if len(p.hand) == 0:
                self.winner = p
                return p
        return None

    def is_game_over(self):
        return self.winner is not None

    def get_current_player(self):
        return self.players[self.current_player]

    def ai_turn(self):
        player = self.get_current_player()
        last_cards = self.last_play and self.last_play[0]
        valid = HandFinder.get_all_valid_plays(player.hand, last_cards)
        if not valid:
            self.pass_(player)
            return False
        is_first = self.last_play is None
        chosen = AIStrategy.select_best(valid, player.hand, is_first)
        if chosen is None:
            self.pass_(player)
            return False
        self.play(player, chosen)
        return True
