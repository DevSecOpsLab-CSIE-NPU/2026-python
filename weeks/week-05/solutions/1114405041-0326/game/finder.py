"""Phase 3：牌型搜尋工具。

提供：
- 搜尋單張、對子、三條、五張牌型
- 依上一手牌回傳所有合法可出的牌組
"""

from __future__ import annotations

from itertools import combinations
from typing import Optional

from game.classifier import CardType, HandClassifier
from game.models import Card, Hand


class HandFinder:
    """從手牌中找出可出的各種牌型。"""

    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        pairs: list[list[Card]] = []
        # 依 rank 分組，再從同 rank 中選 2 張組合。
        for rank in range(3, 16):
            same_rank = [c for c in hand if c.rank == rank]
            for c1, c2 in combinations(same_rank, 2):
                pairs.append([c1, c2])
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        triples: list[list[Card]] = []
        for rank in range(3, 16):
            same_rank = [c for c in hand if c.rank == rank]
            for c1, c2, c3 in combinations(same_rank, 3):
                triples.append([c1, c2, c3])
        return triples

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[list[Card]]:
        """從指定起點找一組可組成順子的牌。

        這裡採「每個點數挑最小花色一張」的簡化策略，
        主要用於測試與示範。
        """
        target = [start_rank + i for i in range(5)]
        selected: list[Card] = []
        for rank in target:
            candidates = sorted([c for c in hand if c.rank == rank], key=lambda c: c.suit)
            if not candidates:
                return None
            selected.append(candidates[0])
        return selected

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        fives: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()

        # 用 C(n,5) 枚舉後交給 classify 判斷最穩定。
        for combo in combinations(hand, 5):
            cards = list(combo)
            result = HandClassifier.classify(cards)
            if result is None:
                continue
            if result[0] not in {
                CardType.STRAIGHT,
                CardType.FLUSH,
                CardType.FULL_HOUSE,
                CardType.FOUR_OF_A_KIND,
                CardType.STRAIGHT_FLUSH,
            }:
                continue

            key = tuple(sorted((c.rank, c.suit) for c in cards))
            if key not in seen:
                seen.add(key)
                fives.append(cards)

        return fives

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[list[Card]]) -> list[list[Card]]:
        """根據目前手牌與上一手，找出所有合法出牌。"""
        if last_play is None:
            # 第一手依規則只能出 3♣。
            for card in hand:
                if card.rank == 3 and card.suit == 0:
                    return [[card]]
            return []

        n = len(last_play)
        candidates: list[list[Card]] = []

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
