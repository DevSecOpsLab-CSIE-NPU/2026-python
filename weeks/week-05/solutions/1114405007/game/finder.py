"""Phase 3: 牌型搜尋。"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Optional

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class HandFinder:
    """從手牌中找出可用的牌型組合。"""

    @staticmethod
    def _sorted_hand(hand: Hand) -> List[Card]:
        # 固定排序可讓輸出穩定，利於測試
        return sorted(list(hand), key=lambda c: c.to_sort_key(), reverse=True)

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[card] for card in HandFinder._sorted_hand(hand)]

    @staticmethod
    def _group_by_rank(hand: Hand) -> Dict[int, List[Card]]:
        groups: Dict[int, List[Card]] = defaultdict(list)
        for card in hand:
            groups[card.rank].append(card)
        return groups

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        pairs: List[List[Card]] = []
        for cards in HandFinder._group_by_rank(hand).values():
            if len(cards) >= 2:
                for combo in combinations(cards, 2):
                    pairs.append(list(combo))

        pairs.sort(key=lambda p: (p[0].rank, max(c.suit for c in p)), reverse=True)
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        triples: List[List[Card]] = []
        for cards in HandFinder._group_by_rank(hand).values():
            if len(cards) >= 3:
                for combo in combinations(cards, 3):
                    triples.append(list(combo))

        triples.sort(key=lambda t: t[0].rank, reverse=True)
        return triples

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        # 由起始牌點往後取五個連續點數（含 A-2-3-4-5 特例）
        if start_rank == 14:
            target_ranks = [14, 15, 3, 4, 5]
        else:
            target_ranks = [start_rank + i for i in range(5)]

        rank_map: Dict[int, List[Card]] = defaultdict(list)
        for c in hand:
            rank_map[c.rank].append(c)

        picked: List[Card] = []
        for r in target_ranks:
            if r not in rank_map:
                return None
            # 固定挑同 rank 中最大的花色
            picked.append(max(rank_map[r], key=lambda x: x.suit))
        return picked

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        fives: List[List[Card]] = []
        seen = set()

        # 以所有 5 張組合過濾合法五張牌型
        for combo in combinations(list(hand), 5):
            play = list(combo)
            cls = HandClassifier.classify(play)
            if cls is None:
                continue
            if cls[0] not in {
                CardType.STRAIGHT,
                CardType.FLUSH,
                CardType.FULL_HOUSE,
                CardType.FOUR_OF_A_KIND,
                CardType.STRAIGHT_FLUSH,
            }:
                continue

            key = tuple(sorted((c.rank, c.suit) for c in play))
            if key not in seen:
                seen.add(key)
                fives.append(play)

        def _five_key(play: List[Card]):
            cls = HandClassifier.classify(play)
            if cls is None:
                return (0, 0, 0)
            t, r, s = cls
            return (t.value, r, s)

        fives.sort(key=_five_key, reverse=True)
        return fives

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        if last_play is None:
            # 第一手僅回傳 [3♣]
            for c in hand:
                if c.rank == 3 and c.suit == 0:
                    return [[c]]
            return []

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

        valid = [play for play in candidates if HandClassifier.can_play(last_play, play)]

        # 由大到小排序，方便後續出牌策略直接取第一手
        def _play_key(play: List[Card]):
            cls = HandClassifier.classify(play)
            if cls is None:
                return (0, 0, 0)
            t, r, s = cls
            if t == CardType.PAIR:
                s = max(c.suit for c in play)
            return (t.value, r, s)

        valid.sort(key=_play_key, reverse=True)
        return valid
