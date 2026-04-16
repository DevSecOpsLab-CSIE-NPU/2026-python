"""Phase 3: 牌型搜尋邏輯。"""

from __future__ import annotations

from itertools import combinations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class HandFinder:
    """根據手牌找出可用牌型組合。"""

    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        plays: list[list[Card]] = []
        for pair in combinations(hand, 2):
            cards = list(pair)
            info = HandClassifier.classify(cards)
            if info is not None and info[0] == CardType.PAIR:
                plays.append(cards)
        return plays

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        plays: list[list[Card]] = []
        for triple in combinations(hand, 3):
            cards = list(triple)
            info = HandClassifier.classify(cards)
            if info is not None and info[0] == CardType.TRIPLE:
                plays.append(cards)
        return plays

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        plays: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()

        for group in combinations(hand, 5):
            cards = list(group)
            info = HandClassifier.classify(cards)
            if info is None:
                continue

            if info[0] not in {
                CardType.STRAIGHT,
                CardType.FLUSH,
                CardType.FULL_HOUSE,
                CardType.FOUR_OF_A_KIND,
                CardType.STRAIGHT_FLUSH,
            }:
                continue

            key = tuple(sorted((c.rank, c.suit) for c in cards))
            if key in seen:
                continue
            seen.add(key)
            plays.append(cards)

        return plays

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: list[Card] | None) -> list[list[Card]]:
        if last_play is None:
            three_clubs = Card(3, 0)
            return [[three_clubs]] if three_clubs in hand else []

        last_info = HandClassifier.classify(last_play)
        if last_info is None:
            return []

        last_type = last_info[0]

        if last_type == CardType.SINGLE:
            candidates = HandFinder.find_singles(hand)
        elif last_type == CardType.PAIR:
            candidates = HandFinder.find_pairs(hand)
        elif last_type == CardType.TRIPLE:
            candidates = HandFinder.find_triples(hand)
        else:
            candidates = HandFinder.find_fives(hand)

        return [cards for cards in candidates if HandClassifier.can_play(last_play, cards)]
