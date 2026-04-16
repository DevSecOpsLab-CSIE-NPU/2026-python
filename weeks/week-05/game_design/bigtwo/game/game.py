"""Big Two Card Game - Main Game Logic"""

from typing import List, Optional
from .models import Deck, Player, Card, Hand
from .classifier import HandClassifier
from .finder import HandFinder
from .ai import AIStrategy


class BigTwoGame:
    def __init__(self):
        self.deck: Optional[Deck] = None
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[List[Card]] = None
        self.last_player: Optional[int] = None
        self.pass_count: int = 0
        self.winner: Optional[Player] = None
        self.round_number: int = 0
        self.is_first_turn: bool = True
        self.game_started: bool = False
        self.dealing_cards: bool = False
        self.deal_animation_done: bool = False

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        
        self.players = [
            Player("你", is_ai=False, position=0),
            Player("電腦一", is_ai=True, position=1),
            Player("電腦二", is_ai=True, position=2),
            Player("電腦三", is_ai=True, position=3),
        ]
        
        self.dealing_cards = True
        self.deal_animation_done = False

    def deal_one_round(self) -> bool:
        if not self.deck or len(self.deck.cards) == 0:
            self.dealing_cards = False
            self.deal_animation_done = True
            for player in self.players:
                player.hand.sort_desc()
            self._find_first_player()
            return False
        
        for player in self.players:
            if self.deck.cards:
                card = self.deck.deal(1)[0]
                player.take_cards([card])
        
        if len(self.players[0].hand) >= 13:
            self.dealing_cards = False
            self.deal_animation_done = True
            for player in self.players:
                player.hand.sort_desc()
            self._find_first_player()
            return False
        
        return True

    def _find_first_player(self) -> None:
        for i, player in enumerate(self.players):
            club_3 = player.hand.find_3_clubs()
            if club_3:
                self.current_player = i
                break
        
        self.last_play = None
        self.last_player = None
        self.pass_count = 0
        self.round_number = 0
        self.is_first_turn = True
        self.game_started = True

    def _is_valid_play(self, cards: List[Card]) -> bool:
        return HandClassifier.can_play(self.last_play, cards)

    def play(self, player: Player, cards: List[Card]) -> bool:
        if not self._is_valid_play(cards):
            return False
        
        player.play_cards(cards)
        player.cards_played.extend(cards)
        self.last_play = cards
        self.last_player = self.current_player
        self.pass_count = 0
        self.round_number += 1
        self.is_first_turn = False
        
        self.check_winner()
        return True

    def pass_turn(self, player: Player) -> bool:
        if self.last_play is None:
            return False
        
        self.pass_count += 1
        self.check_round_reset()
        return True

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.last_player = None
            self.pass_count = 0

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def check_winner(self) -> None:
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                break

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def ai_turn(self) -> Optional[List[Card]]:
        player = self.get_current_player()
        if not player.is_ai:
            return None
        
        valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play)
        
        if not valid_plays:
            return None
        
        best_play = AIStrategy.select_best(valid_plays, player.hand, self.is_first_turn)
        return best_play

    def get_valid_play_count(self) -> int:
        player = self.get_current_player()
        return len(HandFinder.get_all_valid_plays(player.hand, self.last_play))

    def get_player_hand_count(self, index: int) -> int:
        if 0 <= index < len(self.players):
            return len(self.players[index].hand)
        return 0
