from __future__ import annotations

from itertools import combinations
from typing import Optional

from classifier import CardType, HandClassifier
from models import Card, Hand


class HandFinder:
    """從手牌中搜尋可出的牌型組合。"""

    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        cards = list(hand)
        pairs: list[list[Card]] = []
        for combo in combinations(cards, 2):
            play = list(combo)
            classified = HandClassifier.classify(play)
            if classified is not None and classified[0] == CardType.PAIR:
                pairs.append(play)
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        cards = list(hand)
        triples: list[list[Card]] = []
        for combo in combinations(cards, 3):
            play = list(combo)
            classified = HandClassifier.classify(play)
            if classified is not None and classified[0] == CardType.TRIPLE:
                triples.append(play)
        return triples

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[list[Card]]:
        """從指定起點 rank 嘗試找一組 5 張順子（含 A-2-3-4-5 特例）。"""
        cards = list(hand)
        by_rank: dict[int, list[Card]] = {}
        for card in cards:
            by_rank.setdefault(card.rank, []).append(card)

        if start_rank == 14:
            needed = [14, 15, 3, 4, 5]
        else:
            needed = [start_rank + i for i in range(5)]

        picked: list[Card] = []
        for rank in needed:
            if rank not in by_rank:
                return None
            # 取該點數花色最大的牌，讓結果更穩定。
            picked.append(max(by_rank[rank], key=lambda c: c.suit))

        if HandClassifier.classify(picked) is None:
            return None
        return picked

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        cards = list(hand)
        fives: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()

        for combo in combinations(cards, 5):
            play = list(combo)
            classified = HandClassifier.classify(play)
            if classified is None:
                continue

            ctype = classified[0]
            if ctype not in {
                CardType.STRAIGHT,
                CardType.FLUSH,
                CardType.FULL_HOUSE,
                CardType.FOUR_OF_A_KIND,
                CardType.STRAIGHT_FLUSH,
            }:
                continue

            key = tuple(sorted((card.rank, card.suit) for card in play))
            if key in seen:
                continue
            seen.add(key)
            fives.append(play)

        return fives

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[list[Card]]) -> list[list[Card]]:
        cards = list(hand)

        # 首回合規則：只能出包含 3♣ 的牌。
        if last_play is None:
            first = Card(3, 0)
            return [[first]] if first in cards else []

        last_type = HandClassifier.classify(last_play)
        if last_type is None:
            return []

        if len(last_play) == 1:
            candidates = HandFinder.find_singles(hand)
        elif len(last_play) == 2:
            candidates = HandFinder.find_pairs(hand)
        elif len(last_play) == 3:
            candidates = HandFinder.find_triples(hand)
        elif len(last_play) == 5:
            candidates = HandFinder.find_fives(hand)
        else:
            return []

        return [play for play in candidates if HandClassifier.can_play(last_play, play)]
