from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
from typing import List, Optional

from .cards import Card, Hand
from .classifier import CardType, HandClassifier


class HandFinder:
    @staticmethod
    def _sort_cards(cards: List[Card]) -> List[Card]:
        return sorted(cards, key=lambda c: (c.rank, c.suit))

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[card] for card in HandFinder._sort_cards(hand.cards)]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        pairs: List[List[Card]] = []
        for rank in sorted(by_rank):
            same_rank = HandFinder._sort_cards(by_rank[rank])
            for combo in combinations(same_rank, 2):
                pairs.append(list(combo))
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        triples: List[List[Card]] = []
        for rank in sorted(by_rank):
            same_rank = HandFinder._sort_cards(by_rank[rank])
            for combo in combinations(same_rank, 3):
                triples.append(list(combo))
        return triples

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        if start_rank == 14:
            needed = [14, 15, 3, 4, 5]
        else:
            needed = [start_rank + i for i in range(5)]

        rank_buckets: List[List[Card]] = []
        for rank in needed:
            if not by_rank[rank]:
                return None
            rank_buckets.append(HandFinder._sort_cards(by_rank[rank]))

        candidate = list(product(*rank_buckets))[0]
        return HandFinder._sort_cards(list(candidate))

    @staticmethod
    def _all_straights(hand: Hand) -> List[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        starts = [3, 4, 5, 6, 7, 8, 9, 10, 11, 14]
        straights: List[List[Card]] = []
        seen = set()

        for start in starts:
            needed = [14, 15, 3, 4, 5] if start == 14 else [start + i for i in range(5)]
            if any(len(by_rank[r]) == 0 for r in needed):
                continue

            buckets = [HandFinder._sort_cards(by_rank[r]) for r in needed]
            for combo in product(*buckets):
                cards = HandFinder._sort_cards(list(combo))
                key = tuple((c.suit, c.rank) for c in cards)
                if key not in seen:
                    seen.add(key)
                    straights.append(cards)

        return straights

    @staticmethod
    def _all_flushes(hand: Hand) -> List[List[Card]]:
        by_suit: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_suit[card.suit].append(card)

        flushes: List[List[Card]] = []
        for suit in sorted(by_suit):
            suited_cards = HandFinder._sort_cards(by_suit[suit])
            if len(suited_cards) < 5:
                continue
            for combo in combinations(suited_cards, 5):
                c = list(combo)
                if HandClassifier.classify(c) == (CardType.FLUSH, max(x.rank for x in c), 0):
                    flushes.append(c)
        return flushes

    @staticmethod
    def _all_full_houses(hand: Hand) -> List[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        triples = []
        pairs = []
        for rank, cards in by_rank.items():
            cards = HandFinder._sort_cards(cards)
            if len(cards) >= 3:
                triples.extend((rank, list(c)) for c in combinations(cards, 3))
            if len(cards) >= 2:
                pairs.extend((rank, list(c)) for c in combinations(cards, 2))

        full_houses: List[List[Card]] = []
        for tr_rank, tr_cards in triples:
            for pa_rank, pa_cards in pairs:
                if tr_rank == pa_rank:
                    continue
                full_houses.append(HandFinder._sort_cards(tr_cards + pa_cards))

        return full_houses

    @staticmethod
    def _all_four_of_a_kind(hand: Hand) -> List[List[Card]]:
        by_rank: dict[int, List[Card]] = defaultdict(list)
        for card in hand.cards:
            by_rank[card.rank].append(card)

        quads: List[List[Card]] = []
        all_cards = HandFinder._sort_cards(hand.cards)
        for rank, cards in by_rank.items():
            if len(cards) < 4:
                continue
            for quad in combinations(HandFinder._sort_cards(cards), 4):
                quad_set = set(quad)
                for kicker in all_cards:
                    if kicker in quad_set:
                        continue
                    quads.append(HandFinder._sort_cards(list(quad) + [kicker]))
        return quads

    @staticmethod
    def _all_straight_flushes(hand: Hand) -> List[List[Card]]:
        straights = HandFinder._all_straights(hand)
        return [s for s in straights if HandClassifier.classify(s) and HandClassifier.classify(s)[0] == CardType.STRAIGHT_FLUSH]

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        fives = []
        fives.extend(HandFinder._all_straights(hand))
        fives.extend(HandFinder._all_flushes(hand))
        fives.extend(HandFinder._all_full_houses(hand))
        fives.extend(HandFinder._all_four_of_a_kind(hand))
        fives.extend(HandFinder._all_straight_flushes(hand))

        valid = []
        seen = set()
        for combo in fives:
            if HandClassifier.classify(combo) is None:
                continue
            key = tuple((c.suit, c.rank) for c in HandFinder._sort_cards(combo))
            if key not in seen:
                seen.add(key)
                valid.append(HandFinder._sort_cards(combo))
        return valid

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        candidates: List[List[Card]] = []
        candidates.extend(HandFinder.find_singles(hand))
        candidates.extend(HandFinder.find_pairs(hand))
        candidates.extend(HandFinder.find_triples(hand))
        candidates.extend(HandFinder.find_fives(hand))

        if last_play is None:
            return [cards for cards in candidates if HandClassifier.can_play(None, cards)]

        return [cards for cards in candidates if HandClassifier.can_play(last_play, cards)]
