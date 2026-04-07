"""P1: Models - Core data structures for Big Two card game"""

from enum import Enum
from typing import List, Optional


class Suit(Enum):
    """Card suits in Big Two, ordered by strength"""
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SMALL_JOKER = 4
    BIG_JOKER = 5

    def __lt__(self, other):
        if not isinstance(other, Suit):
            return NotImplemented
        return self.value < other.value

    def __le__(self, other):
        if not isinstance(other, Suit):
            return NotImplemented
        return self.value <= other.value

    def __gt__(self, other):
        if not isinstance(other, Suit):
            return NotImplemented
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, Suit):
            return NotImplemented
        return self.value >= other.value


class Card:
    """Represents a single playing card"""

    # Rank constants
    SUIT_MAP = {
        'S': Suit.SPADES,
        'H': Suit.HEARTS,
        'D': Suit.DIAMONDS,
        'C': Suit.CLUBS,
        'sJ': Suit.SMALL_JOKER,
        'BJ': Suit.BIG_JOKER,
    }

    RANK_MAP = {
        '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 11,
        'Q': 12, 'K': 13, 'A': 14, '2': 15,
    }

    RANK_NAMES = {
        3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: '10', 11: 'J',
        12: 'Q', 13: 'K', 14: 'A', 15: '2',
    }

    SUIT_NAMES = {
        Suit.SPADES: 'S',
        Suit.HEARTS: 'H',
        Suit.DIAMONDS: 'D',
        Suit.CLUBS: 'C',
        Suit.SMALL_JOKER: 'sJ',
        Suit.BIG_JOKER: 'BJ',
    }

    def __init__(self, rank: int, suit: Suit):
        """
        Initialize a card.
        
        Args:
            rank: 3-15 (3-10, J=11, Q=12, K=13, A=14, 2=15)
            suit: Suit enum value
        """
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        """String representation of card"""
        rank_str = self.RANK_NAMES.get(self.rank, str(self.rank))
        suit_str = self.SUIT_NAMES.get(self.suit, str(self.suit))
        return f"{rank_str}{suit_str}"

    def __repr__(self) -> str:
        return f"Card({self.rank}, {self.suit.name})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other) -> bool:
        """Compare cards: first by rank, then by suit"""
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __le__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self == other or self < other

    def __gt__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank != other.rank:
            return self.rank > other.rank
        return self.suit > other.suit

    def __ge__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self == other or self > other

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))


class Deck:
    """Standard deck with 54 cards (52 + 2 jokers)"""

    def __init__(self):
        """Initialize a full deck"""
        self.cards: List[Card] = []
        self._create_deck()

    def _create_deck(self):
        """Create all 54 cards in the deck"""
        self.cards = []
        
        # Add regular cards (3-10, J-A-2) for each suit
        for suit in [Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS]:
            for rank in range(3, 16):  # 3 to 15 (includes 2)
                self.cards.append(Card(rank, suit))
        
        # Add jokers
        self.cards.append(Card(16, Suit.SMALL_JOKER))  # Small joker (special rank)
        self.cards.append(Card(17, Suit.BIG_JOKER))    # Big joker (special rank)

    def shuffle(self):
        """Shuffle the deck"""
        import random
        random.shuffle(self.cards)

    def draw(self, count: int = 1) -> List[Card]:
        """Draw cards from the deck"""
        drawn = []
        for _ in range(count):
            if self.cards:
                drawn.append(self.cards.pop())
        return drawn

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f"Deck({len(self.cards)} cards)"


class Hand:
    """A player's hand of cards"""

    def __init__(self, cards: Optional[List[Card]] = None):
        """
        Initialize a hand.
        
        Args:
            cards: List of cards in hand, defaults to empty list
        """
        self.cards: List[Card] = cards if cards is not None else []

    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)

    def add_cards(self, cards: List[Card]):
        """Add multiple cards to the hand"""
        self.cards.extend(cards)

    def remove_card(self, card: Card) -> bool:
        """Remove a card from the hand"""
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def remove_cards(self, cards: List[Card]) -> bool:
        """Remove multiple cards from the hand"""
        for card in cards:
            if not self.remove_card(card):
                return False
        return True

    def sort(self):
        """Sort cards in the hand by rank and suit"""
        self.cards.sort()

    def get_cards_by_rank(self, rank: int) -> List[Card]:
        """Get all cards of a specific rank"""
        return [card for card in self.cards if card.rank == rank]

    def get_cards_by_suit(self, suit: Suit) -> List[Card]:
        """Get all cards of a specific suit"""
        return [card for card in self.cards if card.suit == suit]

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self) -> str:
        return f"Hand({', '.join(str(card) for card in self.cards)})"

    def __repr__(self) -> str:
        return f"Hand({self.cards})"


class Player:
    """Represents a player in the Big Two game"""

    def __init__(self, player_id: int, name: str = ""):
        """
        Initialize a player.
        
        Args:
            player_id: 0-3, representing the player's position
            name: Player's name (optional)
        """
        self.player_id = player_id
        self.name = name or f"Player {player_id}"
        self.hand = Hand()
        self.pass_count = 0
        self.is_active = True

    def draw_cards(self, cards: List[Card]):
        """Draw cards into the player's hand"""
        self.hand.add_cards(cards)

    def play_cards(self, cards: List[Card]) -> bool:
        """
        Play cards from the hand.
        
        Args:
            cards: List of cards to play
            
        Returns:
            True if successfully played, False otherwise
        """
        if self.hand.remove_cards(cards):
            return True
        return False

    def can_play_cards(self, cards: List[Card]) -> bool:
        """Check if player has all the cards to play"""
        for card in cards:
            if card not in self.hand.cards:
                return False
        return True

    def reset_pass_count(self):
        """Reset the pass count"""
        self.pass_count = 0

    def increment_pass_count(self):
        """Increment the pass count"""
        self.pass_count += 1

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.player_id}, Hand: {len(self.hand)} cards)"

    def __repr__(self) -> str:
        return f"Player({self.player_id}, {self.name})"
