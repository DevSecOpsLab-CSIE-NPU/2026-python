from typing import List, Optional, Tuple

from game.models import Deck, Hand, Player, Card
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class BigTwoGame:

    def __init__(self):
        self.deck: Optional[Deck] = None
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count: int = 0
        self.winner: Optional[Player] = None
        self.round_number: int = 0
        self.is_first_turn: bool = True

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [
            Player("Player1", is_ai=False),
            Player("AI_1", is_ai=True),
            Player("AI_2", is_ai=True),
            Player("AI_3", is_ai=True),
        ]
        for i, player in enumerate(self.players):
            player.take_cards(self.deck.deal(13))

        # Find who has 3♣
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = i
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.is_first_turn = True

    def play(self, player: Player, cards: List[Card]) -> bool:
        if not HandClassifier.can_play(
            self.last_play[0] if self.last_play else None,
            cards
        ):
            return False

        player.play_cards(cards)
        self.last_play = (cards, player.name)
        self.pass_count = 0
        self.is_first_turn = False
        self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        if self.is_first_turn:
            return False
        self.pass_count += 1
        self.check_round_reset()
        return True

    def next_turn(self):
        self.current_player = (self.current_player + 1) % 4

    def _is_valid_play(self, cards: List[Card]) -> bool:
        last = self.last_play[0] if self.last_play else None
        return HandClassifier.can_play(last, cards)

    def check_round_reset(self):
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Optional[Player]:
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
        player = self.get_current_player()
        if not player.is_ai:
            return False

        last = self.last_play[0] if self.last_play else None
        valid_plays = HandFinder.get_all_valid_plays(player.hand, last)

        best = AIStrategy.select_best(valid_plays, player.hand, self.is_first_turn)

        if best is not None:
            return self.play(player, best)
        else:
            if self.is_first_turn:
                # AI must play 3♣ on first turn; force single 3♣
                three_clubs = player.hand.find_3_clubs()
                if three_clubs:
                    return self.play(player, [three_clubs])
            return self.pass_(player)
