"""P3: Finder - Find all valid plays from a hand"""

from typing import List, Set, Tuple, Optional
from .models import Card, Hand
from .classifier import CardType, HandClassifier


class HandFinder:
    """Finds all valid plays from a player's hand"""

    def __init__(self):
        self.classifier = HandClassifier()

    def find_all_plays(self, hand: Hand, last_play: Optional[List[Card]] = None) -> List[List[Card]]:
        """
        Find all valid plays from the hand.
        
        Args:
            hand: Player's hand
            last_play: The last play on the table (None if first play)
            
        Returns:
            List of all valid plays
        """
        if not hand.cards:
            return []

        all_plays = []

        # If no last play, find all valid hands
        if last_play is None:
            # All singles
            for card in hand.cards:
                all_plays.append([card])
            
            # All pairs
            all_plays.extend(self._find_pairs(hand.cards))
            
            # All 5-card hands
            all_plays.extend(self._find_five_card_hands(hand.cards))
        else:
            # Find plays that beat the last play
            last_type_result = self.classifier.classify(last_play)
            if last_type_result:
                last_type, last_strength = last_type_result
                
                # Same type, higher strength
                all_plays.extend(self._find_beats_same_type(hand.cards, last_type, last_strength))

        return all_plays

    def _find_pairs(self, cards: List[Card]) -> List[List[Card]]:
        """Find all pairs in the hand"""
        pairs = []
        rank_groups = {}
        
        for card in cards:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, group in rank_groups.items():
            if len(group) >= 2:
                # Create all possible pairs from cards of this rank
                for i in range(len(group)):
                    for j in range(i + 1, len(group)):
                        pairs.append([group[i], group[j]])
        
        return pairs

    def _find_five_card_hands(self, cards: List[Card]) -> List[List[Card]]:
        """Find all valid 5-card hands (straights, flushes, etc.)"""
        hands = []
        
        # Generate all 5-card combinations
        from itertools import combinations
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            if self.classifier.is_valid_hand(combo_list):
                hands.append(combo_list)
        
        return hands

    def _find_beats_same_type(self, cards: List[Card], hand_type: CardType, 
                            last_strength: int) -> List[List[Card]]:
        """Find all plays of the same type that beat the last play"""
        beats = []
        
        if hand_type == CardType.SINGLE:
            # Find all singles that beat the last single
            for card in cards:
                if card.rank > last_strength:
                    beats.append([card])
        
        elif hand_type == CardType.PAIR:
            # Find all pairs with rank > last strength
            rank_groups = {}
            for card in cards:
                if card.rank not in rank_groups:
                    rank_groups[card.rank] = []
                rank_groups[card.rank].append(card)
            
            for rank in sorted(rank_groups.keys(), reverse=True):
                if rank > last_strength and len(rank_groups[rank]) >= 2:
                    for i in range(len(rank_groups[rank])):
                        for j in range(i + 1, len(rank_groups[rank])):
                            beats.append([rank_groups[rank][i], rank_groups[rank][j]])
        
        elif hand_type == CardType.STRAIGHT:
            # Find straights with higher top card
            beats.extend(self._find_better_straights(cards, last_strength))
        
        elif hand_type == CardType.FLUSH:
            # Find flushes with higher top card
            beats.extend(self._find_better_flushes(cards, last_strength))
        
        elif hand_type == CardType.FULL_HOUSE:
            # Find full houses with higher three-of-a-kind
            beats.extend(self._find_better_full_houses(cards, last_strength))
        
        elif hand_type == CardType.FOUR_OF_A_KIND:
            # Find four of a kind with higher rank
            beats.extend(self._find_better_four_of_a_kind(cards, last_strength))
        
        elif hand_type == CardType.STRAIGHT_FLUSH:
            # Find straight flushes with higher top card
            beats.extend(self._find_better_straight_flushes(cards, last_strength))
        
        return beats

    def _find_better_straights(self, cards: List[Card], last_strength: int) -> List[List[Card]]:
        """Find straights with top card > last_strength"""
        straights = []
        from itertools import combinations
        
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            result = self.classifier.classify(combo_list)
            if result and result[0] == CardType.STRAIGHT and result[1] > last_strength:
                straights.append(combo_list)
        
        return straights

    def _find_better_flushes(self, cards: List[Card], last_strength: int) -> List[List[Card]]:
        """Find flushes with top card > last_strength"""
        flushes = []
        from itertools import combinations
        
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            result = self.classifier.classify(combo_list)
            if result and result[0] == CardType.FLUSH and result[1] > last_strength:
                flushes.append(combo_list)
        
        return flushes

    def _find_better_full_houses(self, cards: List[Card], last_strength: int) -> List[List[Card]]:
        """Find full houses with three-of-a-kind > last_strength"""
        full_houses = []
        from itertools import combinations
        
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            result = self.classifier.classify(combo_list)
            if result and result[0] == CardType.FULL_HOUSE and result[1] > last_strength:
                full_houses.append(combo_list)
        
        return full_houses

    def _find_better_four_of_a_kind(self, cards: List[Card], last_strength: int) -> List[List[Card]]:
        """Find four of a kind with rank > last_strength"""
        four_of_a_kind = []
        from itertools import combinations
        
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            result = self.classifier.classify(combo_list)
            if result and result[0] == CardType.FOUR_OF_A_KIND and result[1] > last_strength:
                four_of_a_kind.append(combo_list)
        
        return four_of_a_kind

    def _find_better_straight_flushes(self, cards: List[Card], last_strength: int) -> List[List[Card]]:
        """Find straight flushes with top card > last_strength"""
        straight_flushes = []
        from itertools import combinations
        
        for combo in combinations(cards, 5):
            combo_list = list(combo)
            result = self.classifier.classify(combo_list)
            if result and result[0] == CardType.STRAIGHT_FLUSH and result[1] > last_strength:
                straight_flushes.append(combo_list)
        
        return straight_flushes

    def get_best_play(self, hand: Hand, last_play: Optional[List[Card]] = None) -> Optional[List[Card]]:
        """
        Get the best play from hand (used as a simple strategy).
        
        Args:
            hand: Player's hand
            last_play: The last play on the table
            
        Returns:
            The best play or None if no valid play exists
        """
        plays = self.find_all_plays(hand, last_play)
        if not plays:
            return None
        
        # Prefer lower cards to save high cards
        return min(plays, key=lambda p: (sum(card.rank for card in p), len(p)))

    def has_valid_play(self, hand: Hand, last_play: Optional[List[Card]] = None) -> bool:
        """Check if player has any valid play"""
        return len(self.find_all_plays(hand, last_play)) > 0
