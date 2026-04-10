from typing import List
from .models import Deck, Player, Card
from .classifier import HandClassifier
from .ai import AIStrategy


class BigTwoGame:
    """遊戲狀態機"""

    def __init__(self):
        self.players = [
            Player("你"),
            Player("阿強", True),
            Player("小美", True),
            Player("賭神", True)
        ]

        self.deck = Deck()
        self.current_idx = 0
        self.last_play = None
        self.last_play_idx = 0
        self.pass_count = 0
        self.is_first_turn_of_game = True
        self.winner = None

        self._settled = False

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()

        for p in self.players:
            p.hand = self.deck.deal(13)

        club_3 = Card(3, 0)
        for i, p in enumerate(self.players):
            if club_3 in p.hand:
                self.current_idx = i
                self.last_play_idx = i
                break

        self.last_play = None
        self.pass_count = 0
        self.is_first_turn_of_game = True
        self.winner = None
        self._settled = False

    def get_current_player(self):
        return self.players[self.current_idx]

    def play_turn(self, cards: List[Card]) -> bool:
        p = self.get_current_player()

        if not cards:
            if self.last_play is None:
                return False
            self.pass_count += 1
            self._advance_turn()
            return True

        club_3 = Card(3, 0)
        if self.is_first_turn_of_game and club_3 not in cards:
            return False

        if self.last_play:
            if HandClassifier.compare(cards, self.last_play) <= 0:
                return False
        else:
            if not HandClassifier.classify(cards):
                return False

        p.remove_cards(cards)
        self.last_play = cards
        self.last_play_idx = self.current_idx
        self.pass_count = 0
        self.is_first_turn_of_game = False

        if len(p.hand) == 0:
            self.winner = p
            self._settle_economy()
            return True

        self._advance_turn()
        return True

    def _advance_turn(self):
        self.current_idx = (self.current_idx + 1) % 4

        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.current_idx = self.last_play_idx

    def _settle_economy(self):
        if self._settled:
            return
        self._settled = True

        base_bet = 50
        total_gain = 0

        for p in self.players:
            if p != self.winner:
                rem = len(p.hand)

                if rem == 13:
                    multiplier = 3
                elif rem >= 10:
                    multiplier = 2
                else:
                    multiplier = 1

                lost = rem * base_bet * multiplier

                p.gold -= lost
                total_gain += lost

                if p.gold <= 0:
                    p.is_bankrupt = True

        self.winner.gold += total_gain

    def run_ai_turn(self) -> List[Card]:
        p = self.get_current_player()

        if not p.is_ai:
            return []

        club_3 = Card(3, 0) if self.is_first_turn_of_game else None

        best_move = AIStrategy.select_best_move(
            p.hand,
            self.last_play,
            club_3
        )

        self.play_turn(best_move if best_move else [])
        return best_move if best_move else []