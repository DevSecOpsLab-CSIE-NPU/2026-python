"""Phase 2: 牌型分類與比較。"""

from __future__ import annotations

from collections import Counter
from enum import Enum
from typing import List, Optional, Tuple

from .models import Card


class CardType(Enum):
    """牌型列舉。"""

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """大老二牌型分類工具。"""

    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        uniq = sorted(set(ranks))
        if len(uniq) != 5:
            return False

        # 特例：A-2-3-4-5（使用 14,15,3,4,5 表示）
        if uniq == [3, 4, 5, 14, 15]:
            return True

        return all(uniq[i] + 1 == uniq[i + 1] for i in range(4))

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        if not cards:
            return None

        n = len(cards)
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_count = Counter(ranks)

        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2:
            if len(rank_count) == 1:
                return (CardType.PAIR, ranks[0], 0)
            return None

        if n == 3:
            if len(rank_count) == 1:
                return (CardType.TRIPLE, ranks[0], 0)
            return None

        if n != 5:
            return None

        is_straight = HandClassifier._is_straight(ranks)
        is_flush = HandClassifier._is_flush(suits)
        count_values = sorted(rank_count.values(), reverse=True)

        # A-2-3-4-5 的順子高牌視為 5，其餘順子高牌為最大 rank
        straight_high = 5 if sorted(set(ranks)) == [3, 4, 5, 14, 15] else max(ranks)

        if is_straight and is_flush:
            return (CardType.STRAIGHT_FLUSH, straight_high, 0)

        if count_values == [4, 1]:
            four_rank = max(rank_count.items(), key=lambda x: x[1])[0]
            return (CardType.FOUR_OF_A_KIND, four_rank, 0)

        if count_values == [3, 2]:
            triple_rank = max(rank_count.items(), key=lambda x: x[1])[0]
            return (CardType.FULL_HOUSE, triple_rank, 0)

        if is_flush:
            return (CardType.FLUSH, max(ranks), 0)

        if is_straight:
            return (CardType.STRAIGHT, straight_high, 0)

        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
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

        # 不同牌型，直接比牌型等級
        if t1 != t2:
            return 1 if t1.value > t2.value else -1

        if r1 != r2:
            return 1 if r1 > r2 else -1

        # 同點數時，對單張與對子使用花色作最後比較
        if t1 == CardType.SINGLE:
            if s1 != s2:
                return 1 if s1 > s2 else -1
            return 0

        if t1 == CardType.PAIR:
            p1_high_suit = max(c.suit for c in play1)
            p2_high_suit = max(c.suit for c in play2)
            if p1_high_suit != p2_high_suit:
                return 1 if p1_high_suit > p2_high_suit else -1
            return 0

        return 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        # 第一手必須包含梅花 3
        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)

        last_cls = HandClassifier.classify(last_play)
        cur_cls = HandClassifier.classify(cards)
        if last_cls is None or cur_cls is None:
            return False

        # 既有出牌時，需同張數且同牌型才可跟牌
        if len(last_play) != len(cards):
            return False
        if last_cls[0] != cur_cls[0]:
            return False

        return HandClassifier.compare(cards, last_play) == 1
