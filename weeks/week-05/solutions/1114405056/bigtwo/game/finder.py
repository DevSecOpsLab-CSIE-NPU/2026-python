from itertools import combinations
from typing import List, Optional
from collections import defaultdict

from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class HandFinder:

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        by_rank = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)
        result = []
        for cards in by_rank.values():
            if len(cards) >= 2:
                for combo in combinations(cards, 2):
                    result.append(list(combo))
        return result

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        by_rank = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)
        result = []
        for cards in by_rank.values():
            if len(cards) >= 3:
                for combo in combinations(cards, 3):
                    result.append(list(combo))
        return result

    @staticmethod
    def _find_straight_combos(hand: Hand) -> List[List[Card]]:
        by_rank = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)

        result = []
        ranks = sorted(by_rank.keys())

        # Normal straights
        for i, start in enumerate(ranks):
            needed = [start + j for j in range(5)]
            if all(r in by_rank for r in needed):
                card_options = [by_rank[r] for r in needed]
                for combo in combinations_product(card_options):
                    result.append(list(combo))

        # A-2-3-4-5 straight: ranks 3,4,5,14,15
        a_low = [3, 4, 5, 14, 15]
        if all(r in by_rank for r in a_low):
            card_options = [by_rank[r] for r in a_low]
            for combo in combinations_product(card_options):
                result.append(list(combo))

        return result

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        result = []
        seen = set()

        def add(play):
            key = tuple(sorted((c.rank, c.suit) for c in play))
            if key not in seen:
                seen.add(key)
                result.append(play)

        by_rank = defaultdict(list)
        by_suit = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)
            by_suit[c.suit].append(c)

        # Straight flushes and straights
        for play in HandFinder._find_straight_combos(hand):
            suits = [c.suit for c in play]
            if len(set(suits)) == 1:
                add(play)  # straight flush
            else:
                add(play)  # straight

        # Flushes (same suit, 5 cards, non-straight)
        for suit_cards in by_suit.values():
            if len(suit_cards) >= 5:
                for combo in combinations(suit_cards, 5):
                    add(list(combo))

        # Full house: triple + pair from different ranks
        ranks = list(by_rank.keys())
        for r1 in ranks:
            if len(by_rank[r1]) >= 3:
                for triple in combinations(by_rank[r1], 3):
                    for r2 in ranks:
                        if r2 != r1 and len(by_rank[r2]) >= 2:
                            for pair in combinations(by_rank[r2], 2):
                                add(list(triple) + list(pair))

        # Four of a kind
        for r, cards in by_rank.items():
            if len(cards) >= 4:
                for four in combinations(cards, 4):
                    kickers = [c for c in hand if c.rank != r]
                    for kicker in kickers:
                        add(list(four) + [kicker])

        return result

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        if last_play is None:
            # First turn: return all plays containing 3♣
            all_plays = (
                HandFinder.find_singles(hand) +
                HandFinder.find_pairs(hand) +
                HandFinder.find_triples(hand) +
                HandFinder.find_fives(hand)
            )
            return [p for p in all_plays if HandClassifier.can_play(None, p)]

        n = len(last_play)
        if n == 1:
            candidates = HandFinder.find_singles(hand)
        elif n == 2:
            candidates = HandFinder.find_pairs(hand)
        elif n == 3:
            candidates = HandFinder.find_triples(hand)
        elif n == 5:
            candidates = HandFinder.find_fives(hand)
        else:
            return []

        return [p for p in candidates if HandClassifier.can_play(last_play, p)]


def combinations_product(lists):
    if not lists:
        yield []
        return
    for item in lists[0]:
        for rest in combinations_product(lists[1:]):
            yield [item] + rest
