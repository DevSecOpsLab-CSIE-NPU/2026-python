"""Phase 2: 牌型分類與比較邏輯。"""

from __future__ import annotations

from collections import Counter
from enum import IntEnum

from .models import Card


class CardType(IntEnum):
    """牌型大小定義，數值越大牌型越強。"""

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """提供牌型分類、比較與出牌合法性判定。"""

    @staticmethod
    def _is_straight(ranks: list[int]) -> bool:
        unique = sorted(set(ranks))
        if len(unique) != 5:
            return False

        if unique == [3, 4, 5, 14, 15]:
            return True

        return all(unique[i] + 1 == unique[i + 1] for i in range(4))

    @staticmethod
    def _straight_high_rank(ranks: list[int]) -> int:
        unique = sorted(set(ranks))
        if unique == [3, 4, 5, 14, 15]:
            return 5
        return max(unique)

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: list[Card]) -> tuple[CardType, int, int] | None:
        n = len(cards)
        if n == 0:
            return None

        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counter = Counter(ranks)

        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2:
            if len(rank_counter) == 1:
                return (CardType.PAIR, ranks[0], 0)
            return None

        if n == 3:
            if len(rank_counter) == 1:
                return (CardType.TRIPLE, ranks[0], 0)
            return None

        if n != 5:
            return None

        is_straight = HandClassifier._is_straight(ranks)
        is_flush = HandClassifier._is_flush(suits)

        if is_straight and is_flush:
            return (CardType.STRAIGHT_FLUSH, HandClassifier._straight_high_rank(ranks), 0)

        counts = sorted(rank_counter.values(), reverse=True)
        if counts == [4, 1]:
            four_rank = max(rank for rank, cnt in rank_counter.items() if cnt == 4)
            return (CardType.FOUR_OF_A_KIND, four_rank, 0)

        if counts == [3, 2]:
            triple_rank = max(rank for rank, cnt in rank_counter.items() if cnt == 3)
            return (CardType.FULL_HOUSE, triple_rank, 0)

        if is_flush:
            return (CardType.FLUSH, max(ranks), min(suits))

        if is_straight:
            return (CardType.STRAIGHT, HandClassifier._straight_high_rank(ranks), 0)

        return None

    @staticmethod
    def _pair_top_suit(cards: list[Card]) -> int:
        return max(card.suit for card in cards)

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)

        if c1 is None and c2 is None:
            return 0
        if c1 is None:
            return -1
        if c2 is None:
            return 1

        t1, r1, s1 = c1
        t2, r2, s2 = c2

        if t1 != t2:
            return 1 if t1 > t2 else -1
        if r1 != r2:
            return 1 if r1 > r2 else -1

        if t1 == CardType.PAIR:
            p1_suit = HandClassifier._pair_top_suit(play1)
            p2_suit = HandClassifier._pair_top_suit(play2)
            if p1_suit != p2_suit:
                return 1 if p1_suit > p2_suit else -1

        if s1 != s2:
            return 1 if s1 > s2 else -1
        return 0

    @staticmethod
    def can_play(last_play: list[Card] | None, cards: list[Card]) -> bool:
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        if last_play is None:
            return Card(3, 0) in cards

        previous = HandClassifier.classify(last_play)
        if previous is None:
            return False

        if current[0] != previous[0]:
            return False

        return HandClassifier.compare(cards, last_play) == 1
