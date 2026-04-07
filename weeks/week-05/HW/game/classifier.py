"""P2: Classifier - Hand type classification for Big Two"""

from enum import Enum
from typing import List, Optional, Tuple
from .models import Card, Hand, Suit


class CardType(Enum):
    """Enumeration of poker hand types in Big Two"""
    SINGLE = 1          # Single card
    PAIR = 2            # Two cards of same rank
    TRIPLE = 3          # Three cards of same rank (not used in Big Two typically)
    STRAIGHT = 4        # Five cards in sequence
    FLUSH = 5           # Five cards of same suit
    FULL_HOUSE = 6      # Three of a kind + pair
    FOUR_OF_A_KIND = 7  # Four cards of same rank + 1
    STRAIGHT_FLUSH = 8  # Five cards in sequence and same suit


class HandClassifier:
    """Classifies and validates poker hands"""

    def __init__(self):
        pass

    def classify(self, cards: List[Card]) -> Optional[Tuple[CardType, int]]:
        """
        Classify a hand of cards.
        
        Args:
            cards: List of cards to classify
            
        Returns:
            Tuple of (CardType, strength_value) or None if invalid hand
        """
        if not cards:
            return None

        # Single card
        if len(cards) == 1:
            return (CardType.SINGLE, cards[0].rank)

        # Pair - 2 cards
        if len(cards) == 2:
            if self._is_pair(cards):
                return (CardType.PAIR, cards[0].rank)
            return None

        # 5-card hands
        if len(cards) == 5:
            cards_sorted = sorted(cards)
            
            # Check straight flush
            result = self._check_straight_flush(cards_sorted)
            if result:
                return (CardType.STRAIGHT_FLUSH, result)
            
            # Check four of a kind
            result = self._check_four_of_a_kind(cards_sorted)
            if result:
                return (CardType.FOUR_OF_A_KIND, result)
            
            # Check full house
            result = self._check_full_house(cards_sorted)
            if result:
                return (CardType.FULL_HOUSE, result)
            
            # Check flush
            result = self._check_flush(cards_sorted)
            if result:
                return (CardType.FLUSH, result)
            
            # Check straight
            result = self._check_straight(cards_sorted)
            if result:
                return (CardType.STRAIGHT, result)
            
            return None

        return None

    def _is_pair(self, cards: List[Card]) -> bool:
        """Check if two cards form a pair"""
        if len(cards) != 2:
            return False
        return cards[0].rank == cards[1].rank

    def _check_straight(self, cards: List[Card]) -> Optional[int]:
        """
        Check if 5 cards form a straight.
        
        Returns:
            Highest card rank if valid straight, None otherwise
        """
        if len(cards) != 5:
            return None

        ranks = [card.rank for card in cards]
        ranks_sorted = sorted(set(ranks))

        # Check if exactly 5 different ranks
        if len(ranks_sorted) != 5:
            return None

        # Check if consecutive (considering special case for A-2-3-4-5)
        if ranks_sorted == [3, 4, 5, 6, 7]:
            return 7  # 7 is highest
        if ranks_sorted == [14, 2, 3, 4, 5]:
            return 5  # In Big Two, A-2-3-4-5 has 5 as the high card
        if ranks_sorted[-1] - ranks_sorted[0] == 4:
            return ranks_sorted[-1]

        return None

    def _check_flush(self, cards: List[Card]) -> Optional[int]:
        """
        Check if 5 cards form a flush.
        
        Returns:
            Highest card rank if valid flush, None otherwise
        """
        if len(cards) != 5:
            return None

        suits = [card.suit for card in cards]
        if len(set(suits)) == 1:
            return max(card.rank for card in cards)

        return None

    def _check_full_house(self, cards: List[Card]) -> Optional[int]:
        """
        Check if 5 cards form a full house (3 of a kind + pair).
        
        Returns:
            Rank of three of a kind if valid, None otherwise
        """
        if len(cards) != 5:
            return None

        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        counts = sorted(rank_counts.values())
        if counts == [2, 3]:
            # Find the rank that appears 3 times
            for rank, count in rank_counts.items():
                if count == 3:
                    return rank
        return None

    def _check_four_of_a_kind(self, cards: List[Card]) -> Optional[int]:
        """
        Check if 5 cards form four of a kind.
        
        Returns:
            Rank of the four cards if valid, None otherwise
        """
        if len(cards) != 5:
            return None

        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        for rank, count in rank_counts.items():
            if count == 4:
                return rank
        return None

    def _check_straight_flush(self, cards: List[Card]) -> Optional[int]:
        """
        Check if 5 cards form a straight flush.
        
        Returns:
            Highest card rank if valid straight flush, None otherwise
        """
        if len(cards) != 5:
            return None

        # Must be flush first
        suits = [card.suit for card in cards]
        if len(set(suits)) != 1:
            return None

        # Then check straight
        return self._check_straight(cards)

    def compare_hands(self, hand1: List[Card], hand2: List[Card]) -> int:
        """
        Compare two hands.
        
        Args:
            hand1: First hand
            hand2: Second hand
            
        Returns:
            1 if hand1 > hand2
            -1 if hand1 < hand2
            0 if equal
        """
        result1 = self.classify(hand1)
        result2 = self.classify(hand2)

        if result1 is None and result2 is None:
            return 0
        if result1 is None:
            return -1
        if result2 is None:
            return 1

        type1, strength1 = result1
        type2, strength2 = result2

        # Compare hand types
        if type1.value != type2.value:
            return 1 if type1.value > type2.value else -1

        # Same type, compare strength
        if strength1 != strength2:
            return 1 if strength1 > strength2 else -1

        # Same strength, compare suit of highest card
        highest1 = max(hand1, key=lambda c: (c.rank, c.suit))
        highest2 = max(hand2, key=lambda c: (c.rank, c.suit))

        if highest1.suit != highest2.suit:
            return 1 if highest1.suit > highest2.suit else -1

        return 0

    def is_valid_hand(self, cards: List[Card]) -> bool:
        """Check if cards form a valid hand"""
        return self.classify(cards) is not None
