"""Phase 2：牌型分類與比較。

這個模組專門處理「出牌是什麼牌型」以及「兩手牌誰比較大」：
1. classify: 把一組牌分類成單張/對子/三條/五張牌型
2. compare: 比較兩組合法牌
3. can_play: 判斷本次出牌是否合法且是否大於上一手
"""

from __future__ import annotations

from collections import Counter
from enum import IntEnum
from typing import Optional

from game.models import Card


class CardType(IntEnum):
    """牌型等級。

    數字越大代表牌型層級越高，便於直接比較。
    """

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """牌型分類器。"""

    @staticmethod
    def _is_straight(ranks: list[int]) -> tuple[bool, int]:
        """檢查是否為順子。

        回傳 (是否為順子, 順子最大點數)
        - 一般順子：點數連續且不重複
        - 特例順子：A-2-3-4-5（以 5 作為比較高點）
        """
        unique = sorted(set(ranks))
        if len(unique) != 5:
            return (False, 0)

        # A-2-3-4-5 特判（在本題點數系統中為 14,15,3,4,5）
        if set(unique) == {3, 4, 5, 14, 15}:
            return (True, 5)

        if unique[-1] - unique[0] == 4:
            return (True, unique[-1])

        return (False, 0)

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        # 同花：所有花色都一樣。
        return len(set(suits)) == 1

    @staticmethod
    def _count_ranks(ranks: list[int]) -> list[tuple[int, int]]:
        """統計點數出現次數，並依 (次數, 點數) 由大到小排序。"""
        counts = Counter(ranks)
        return sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        """分類牌型。

        回傳 (CardType, 主要比較點數, 主要比較花色)
        若不是合法牌型，回傳 None。
        """
        n = len(cards)
        if n == 0:
            return None

        ordered = sorted(cards, key=lambda c: (c.rank, c.suit))
        ranks = [c.rank for c in ordered]
        suits = [c.suit for c in ordered]

        if n == 1:
            c = ordered[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2:
            if ranks[0] == ranks[1]:
                return (CardType.PAIR, ranks[0], max(suits))
            return None

        if n == 3:
            if ranks[0] == ranks[1] == ranks[2]:
                return (CardType.TRIPLE, ranks[0], max(suits))
            return None

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        is_straight, straight_high = HandClassifier._is_straight(ranks)
        counts = HandClassifier._count_ranks(ranks)
        count_pattern = sorted((cnt for _, cnt in counts), reverse=True)

        if is_flush and is_straight:
            return (CardType.STRAIGHT_FLUSH, straight_high, max(suits))

        if count_pattern == [4, 1]:
            quad_rank = counts[0][0]
            return (CardType.FOUR_OF_A_KIND, quad_rank, max(suits))

        if count_pattern == [3, 2]:
            triple_rank = counts[0][0]
            return (CardType.FULL_HOUSE, triple_rank, max(suits))

        if is_flush:
            high = max(ordered, key=lambda c: (c.rank, c.suit))
            return (CardType.FLUSH, high.rank, high.suit)

        if is_straight:
            return (CardType.STRAIGHT, straight_high, max(suits))

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        """比較兩手牌。

        回傳：
        - 1 代表 play1 較大
        - -1 代表 play2 較大
        - 0 代表平手
        """
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if c1 is None or c2 is None:
            raise ValueError("compare 只接受合法牌型")

        # 比較順序：牌型 > 點數 > 花色
        if c1[0] != c2[0]:
            return 1 if c1[0] > c2[0] else -1
        if c1[1] != c2[1]:
            return 1 if c1[1] > c2[1] else -1
        if c1[2] != c2[2]:
            return 1 if c1[2] > c2[2] else -1
        return 0

    @staticmethod
    def can_play(last_play: Optional[list[Card]], cards: list[Card]) -> bool:
        """判斷本次出牌是否可出。"""
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        # 第一手必須包含 3♣。
        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)

        last = HandClassifier.classify(last_play)
        if last is None:
            return False

        # 這份規則要求跟上一手同張數，並且牌更大。
        if len(cards) != len(last_play):
            return False

        return HandClassifier.compare(cards, last_play) == 1
