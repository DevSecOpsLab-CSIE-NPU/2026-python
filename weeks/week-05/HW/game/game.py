"""P5: Game - Main game logic for Big Two"""

from typing import List, Optional, Tuple
from enum import Enum
from .models import Card, Deck, Hand, Player
from .classifier import CardType, HandClassifier
from .finder import HandFinder
from .ai import AIStrategy


class GameState(Enum):
    """Game state enumeration"""
    INITIALIZED = 0
    DEALING = 1
    PLAYING = 2
    ROUND_OVER = 3
    GAME_OVER = 4


class BigTwoGame:
    """Main Big Two game controller"""

    def __init__(self, player_names: Optional[List[str]] = None, ai_players: Optional[List[int]] = None):
        """
        Initialize a Big Two game.
        
        Args:
            player_names: List of 4 player names
            ai_players: List of player IDs (0-3) that are AI controlled
        """
        self.players = []
        self.state = GameState.INITIALIZED
        self.current_player_id = 0
        self.table: List[Card] = []  # Cards on table
        self.last_player_id: Optional[int] = None
        self.pass_count = 0
        self.round_num = 0
        self.history: List[Tuple] = []  # Game history
        
        self.classifier = HandClassifier()
        self.finder = HandFinder()
        self.ai_strategy = AIStrategy()
        
        self.ai_players = ai_players or []
        
        # Create 4 players
        names = player_names or ["Player 0", "Player 1", "Player 2", "Player 3"]
        for i in range(4):
            player = Player(i, names[i])
            self.players.append(player)

    def is_ai_player(self, player_id: int) -> bool:
        """Check if a player is AI controlled"""
        return player_id in self.ai_players

    def start_game(self):
        """Start a new game"""
        self.state = GameState.DEALING
        self.round_num = 0
        self._deal_initial_hand()

    def _deal_initial_hand(self):
        """Deal 13 cards to each player"""
        deck = Deck()
        deck.shuffle()
        
        for _ in range(13):
            for player in self.players:
                cards = deck.draw(1)
                if cards:
                    player.draw_cards(cards)
        
        # Sort each player's hand
        for player in self.players:
            player.hand.sort()
        
        # Find who has 3 of Spades and starts first
        for i, player in enumerate(self.players):
            three_spades = Card(3, player.hand.cards[0].suit)
            for card in player.hand.cards:
                if card.rank == 3 and str(card).startswith('3S'):
                    self.current_player_id = i
                    break

    def play_round(self):
        """Play one complete round"""
        self.state = GameState.PLAYING
        self.table = []
        self.last_player_id = None
        self.pass_count = 0
        
        # Reset pass counts
        for player in self.players:
            player.reset_pass_count()

        # Continue until only 1 player left
        while sum(1 for p in self.players if p.is_active) > 1:
            active_count = sum(1 for p in self.players if p.is_active)
            if active_count == 1:
                break
            
            self._play_turn()

    def _play_turn(self):
        """Play one turn (one player's turn)"""
        player = self.players[self.current_player_id]
        
        if not player.is_active:
            self.current_player_id = (self.current_player_id + 1) % 4
            return

        play = self._get_player_play(player)

        if play is None:
            # Player passes
            player.increment_pass_count()
            self.pass_count += 1
            
            if self.pass_count >= 3:
                # Round over, reset table for next player
                self.table = []
                self.last_player_id = None
                self.pass_count = 0
                
                for p in self.players:
                    p.reset_pass_count()
        else:
            # Player plays cards
            player.play_cards(play)
            self.table = play
            self.last_player_id = self.current_player_id
            self.pass_count = 0
            
            for p in self.players:
                p.reset_pass_count()

            # Check if player won
            if len(player.hand.cards) == 0:
                player.is_active = False

        # Move to next player
        self.current_player_id = (self.current_player_id + 1) % 4

    def _get_player_play(self, player: Player) -> Optional[List[Card]]:
        """Get the play for a player (AI or human)"""
        if self.is_ai_player(player.player_id):
            return self.ai_strategy.choose_play(
                player,
                self.table if self.table else None,
                self.last_player_id,
                self.pass_count
            )
        else:
            # For human players, return None (would be handled by UI)
            return None

    def is_valid_play(self, player_id: int, cards: List[Card]) -> bool:
        """Check if a play is valid"""
        player = self.players[player_id]
        
        # Check if player has the cards
        for card in cards:
            if card not in player.hand.cards:
                return False
        
        # Check if hand is valid
        if not self.classifier.is_valid_hand(cards):
            return False
        
        # If table is empty, any valid hand is OK
        if not self.table:
            return True
        
        # Check if it beats the last play
        last_result = self.classifier.classify(self.table)
        current_result = self.classifier.classify(cards)
        
        if last_result is None or current_result is None:
            return False
        
        last_type, last_strength = last_result
        current_type, current_strength = current_result
        
        # Must be same type and higher strength
        if current_type.value != last_type.value:
            return False
        
        if current_strength <= last_strength:
            return False
        
        return True

    def player_play(self, player_id: int, cards: Optional[List[Card]] = None) -> bool:
        """
        Process a player's play.
        
        Args:
            player_id: The player playing
            cards: The cards to play (None to pass)
            
        Returns:
            True if play was successful
        """
        if self.current_player_id != player_id:
            return False
        
        player = self.players[player_id]

        if cards is None:
            # Player passes
            player.increment_pass_count()
            self.pass_count += 1
            
            if self.pass_count >= 3:
                self.table = []
                self.last_player_id = None
                self.pass_count = 0
                
                for p in self.players:
                    p.reset_pass_count()
        else:
            if not self.is_valid_play(player_id, cards):
                return False
            
            # Play cards
            player.play_cards(cards)
            self.table = cards
            self.last_player_id = player_id
            self.pass_count = 0
            
            for p in self.players:
                p.reset_pass_count()

            # Check if player won
            if len(player.hand.cards) == 0:
                player.is_active = False

        # Move to next player
        self.current_player_id = (self.current_player_id + 1) % 4

        return True

    def get_game_status(self) -> dict:
        """Get current game status"""
        return {
            'state': self.state.name,
            'current_player': self.current_player_id,
            'round': self.round_num,
            'table': self.table,
            'last_player': self.last_player_id,
            'pass_count': self.pass_count,
            'players': [
                {
                    'id': p.player_id,
                    'name': p.name,
                    'cards': len(p.hand.cards),
                    'active': p.is_active,
                    'pass_count': p.pass_count
                }
                for p in self.players
            ]
        }

    def get_winner(self) -> Optional[Player]:
        """Get the game winner"""
        active_players = [p for p in self.players if p.is_active]
        if len(active_players) == 1:
            return active_players[0]
        return None

    def get_current_player(self) -> Player:
        """Get the current player"""
        return self.players[self.current_player_id]

    def get_valid_plays(self, player_id: int) -> List[List[Card]]:
        """Get all valid plays for a player"""
        player = self.players[player_id]
        return self.finder.find_all_plays(player.hand, self.table if self.table else None)
