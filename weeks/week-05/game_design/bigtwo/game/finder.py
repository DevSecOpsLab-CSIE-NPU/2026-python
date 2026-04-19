from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from .classifier import HandClassifier
from .models import Card, Hand


class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in sorted(hand.cards)]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        by_rank: dict[int, list[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        pairs: list[list[Card]] = []
        for same_rank_cards in by_rank.values():
            if len(same_rank_cards) >= 2:
                for pair in combinations(sorted(same_rank_cards), 2):
                    pairs.append(list(pair))
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        by_rank: dict[int, list[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        triples: list[list[Card]] = []
        for same_rank_cards in by_rank.values():
            if len(same_rank_cards) >= 3:
                for triple in combinations(sorted(same_rank_cards), 3):
                    triples.append(list(triple))
        return triples

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        found: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()

        for combo in combinations(hand.cards, 5):
            cards = sorted(combo)
            if HandClassifier.classify(cards) is None:
                continue
            key = tuple((c.rank, c.suit) for c in cards)
            if key not in seen:
                seen.add(key)
                found.append(cards)

        return found

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> list[Card] | None:
        candidates = sorted(hand.cards)
        target_ranks = [start_rank + i for i in range(5)]

        chosen: list[Card] = []
        for target_rank in target_ranks:
            card = next((c for c in candidates if c.rank == target_rank and c not in chosen), None)
            if card is None:
                return None
            chosen.append(card)
        return chosen

    @staticmethod
    def get_all_valid_plays(
        hand: Hand, last_play: list[Card] | None, first_turn: bool = True
    ) -> list[list[Card]]:
        if last_play is None:
            if first_turn:
                three_clubs = hand.find_3_clubs()
                return [[three_clubs]] if three_clubs is not None else []

            all_plays = (
                HandFinder.find_singles(hand)
                + HandFinder.find_pairs(hand)
                + HandFinder.find_triples(hand)
                + HandFinder.find_fives(hand)
            )
            return all_plays

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

        return [cards for cards in candidates if HandClassifier.can_play(last_play, cards)]
