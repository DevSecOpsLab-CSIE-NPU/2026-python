from __future__ import annotations

from itertools import combinations
from typing import Optional

from .classifier import HandClassifier
from .models import Card, Hand


class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        result: list[list[Card]] = []
        for rank in range(3, 16):
            same_rank = [c for c in hand if c.rank == rank]
            for pair in combinations(same_rank, 2):
                result.append(list(pair))
        return result

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        result: list[list[Card]] = []
        for rank in range(3, 16):
            same_rank = [c for c in hand if c.rank == rank]
            for triple in combinations(same_rank, 3):
                result.append(list(triple))
        return result

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[list[Card]]:
        needed = [start_rank + i for i in range(5)]
        if start_rank == 3:
            needed = [3, 4, 5, 14, 15]

        chosen: list[Card] = []
        for rank in needed:
            candidates = sorted((c for c in hand if c.rank == rank), key=lambda c: c.suit)
            if not candidates:
                return None
            chosen.append(candidates[0])
        return chosen

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        result: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()
        for cards in combinations(hand, 5):
            combo = list(cards)
            if HandClassifier.classify(combo) is None:
                continue
            key = tuple(sorted((c.rank, c.suit) for c in combo))
            if key not in seen:
                seen.add(key)
                result.append(combo)
        return result

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[list[Card]]) -> list[list[Card]]:
        if last_play is None:
            starter = [c for c in hand if c.rank == 3 and c.suit == 0]
            return [[starter[0]]] if starter else []

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

        return [c for c in candidates if HandClassifier.can_play(last_play, c)]
