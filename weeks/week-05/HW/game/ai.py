"""P4: AI Strategy - AI decision making for Big Two"""

from typing import List, Optional, Dict, Tuple
from .models import Card, Hand, Player
from .classifier import CardType, HandClassifier
from .finder import HandFinder


class AIStrategy:
    """AI strategy for Big Two game"""

    def __init__(self):
        self.classifier = HandClassifier()
        self.finder = HandFinder()

    def choose_play(self, player: Player, last_play: Optional[List[Card]] = None,
                   last_player_id: Optional[int] = None, 
                   pass_count: int = 0) -> Optional[List[Card]]:
        """
        Choose the best play for AI player.
        
        Args:
            player: The AI player
            last_play: The last play on the table
            last_player_id: Who played last
            pass_count: How many players have passed
            
        Returns:
            The chosen play or None to pass
        """
        valid_plays = self.finder.find_all_plays(player.hand, last_play)
        
        if not valid_plays:
            return None

        # If no last play (start of round), play the lowest card
        if last_play is None:
            return self._lowest_play(valid_plays)

        # Choose play based on game state
        # Prefer plays that don't waste high cards
        if pass_count >= 2:
            # Most players passed, more likely to win this round
            return self._lowest_play(valid_plays)

        # Conservative play: use lowest possible card
        return self._conservative_play(valid_plays, player.hand)

    def _lowest_play(self, plays: List[List[Card]]) -> List[Card]:
        """Return the play with lowest total rank (to save high cards)"""
        if not plays:
            return []
        
        return min(plays, key=lambda p: (sum(c.rank for c in p), -len(p)))

    def _conservative_play(self, plays: List[List[Card]], hand: Hand) -> List[Card]:
        """
        Choose a conservative play that saves high cards.
        
        Scoring: lower score is better (save high cards for later)
        """
        if not plays:
            return []

        scores = []
        for play in plays:
            score = self._score_play(play, hand)
            scores.append((score, play))
        
        # Sort by score (ascending) - lower score is better
        scores.sort(key=lambda x: x[0])
        return scores[0][1]

    def _score_play(self, play: List[Card], hand: Hand) -> float:
        """
        Score a play. Lower score means better play.
        
        Scoring factors:
        1. Total rank points (lower is better - save high cards)
        2. Number of cards (prefer shorter plays)
        3. Card distribution (preserve diversity)
        """
        # Factor 1: Sum of ranks (save high cards)
        rank_score = sum(card.rank for card in play)
        
        # Factor 2: Prefer fewer cards (less waste)
        card_count_score = len(play) * 100
        
        # Factor 3: Check if this leaves a bad distribution
        remaining_cards = [c for c in hand.cards if c not in play]
        distribution_score = self._evaluate_distribution(remaining_cards)
        
        total_score = rank_score + card_count_score - distribution_score
        
        return total_score

    def _evaluate_distribution(self, cards: List[Card]) -> float:
        """
        Evaluate how good the remaining card distribution is.
        Higher score is better.
        """
        if not cards:
            return 0
        
        # Count rank distribution
        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
        
        # Prefer hands with pairs or groups (higher counts)
        score = sum(count ** 2 for count in rank_counts.values())
        
        # Prefer more diverse suits
        suit_counts = {}
        for card in cards:
            suit_counts[card.suit] = suit_counts.get(card.suit, 0) + 1
        
        diversity = len(suit_counts)
        score += diversity * 10
        
        return score

    def evaluate_hand_strength(self, hand: Hand, game_state: Optional[Dict] = None) -> float:
        """
        Evaluate the strength of a hand (0.0 to 1.0).
        
        Args:
            hand: Player's hand
            game_state: Optional additional game information
            
        Returns:
            Hand strength score (0.0 = weak, 1.0 = strong)
        """
        if not hand.cards:
            return 0.0

        score = 0.0
        card_count = len(hand.cards)

        # Bonus for having many high cards
        high_cards = sum(1 for card in hand.cards if card.rank >= 13)
        score += (high_cards / card_count) * 0.3

        # Bonus for having pairs
        rank_counts = {}
        for card in hand.cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        pairs = sum(1 for count in rank_counts.values() if count >= 2)
        score += (pairs / max(len(rank_counts), 1)) * 0.3

        # Bonus based on card count (fewer cards = winning)
        score += (1.0 - (card_count / 13)) * 0.4

        return min(score, 1.0)

    def should_play_aggressively(self, player: Player, other_players: List[Player]) -> bool:
        """
        Decide if AI should play aggressively (try to win tricks).
        
        Args:
            player: The AI player
            other_players: Other players at the table
            
        Returns:
            True if should play aggressively
        """
        my_strength = self.evaluate_hand_strength(player.hand)
        
        # Aggressive if our hand is strong
        if my_strength > 0.7:
            return True
        
        # Aggressive if we're low on cards
        if len(player.hand.cards) <= 5:
            return True
        
        # Aggressive if others have many cards
        for other in other_players:
            if other != player:
                avg_other_cards = sum(len(p.hand.cards) for p in other_players if p != player) / 3
                if len(player.hand.cards) < avg_other_cards * 0.7:
                    return True
        
        return False

    def get_play_explanation(self, play: Optional[List[Card]]) -> str:
        """Get a human-readable explanation of why this play was chosen"""
        if play is None:
            return "No valid play, passing"
        
        result = self.classifier.classify(play)
        if result:
            hand_type, strength = result
            return f"Playing {hand_type.name} with strength {strength}"
        
        return f"Playing {len(play)} card(s)"
