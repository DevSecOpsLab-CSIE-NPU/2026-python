"""Phase 3: Hand pattern finder."""

from typing import List, Optional
from itertools import combinations
from game.models import Card, Hand
from game.classifier import HandClassifier


class HandFinder:
    """搜尋所有可用的牌型組合。"""

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """找出所有單張。
        
        Args:
            hand: 手牌
            
        Returns:
            所有單張組合
        """
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """找出所有對子。
        
        Args:
            hand: 手牌
            
        Returns:
            所有對子組合
        """
        pairs = []
        rank_groups: dict[int, List[Card]] = {}

        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    pairs.append(list(pair))

        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """找出所有三條。
        
        Args:
            hand: 手牌
            
        Returns:
            所有三條組合
        """
        triples = []
        rank_groups: dict[int, List[Card]] = {}

        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    triples.append(list(triple))

        return triples

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        """從指定 rank 找順子。
        
        Args:
            hand: 手牌
            start_rank: 起始數字
            
        Returns:
            順子或 None
        """
        needed = list(range(start_rank, start_rank + 5))

        # 特殊情況：A-2-3-4-5
        if start_rank == 3:
            # 檢查 3-4-5-6-7
            try_needed = [3, 4, 5, 6, 7]
            found = []
            for rank in try_needed:
                selected = None
                for card in hand:
                    if card.rank == rank and card not in found:
                        selected = card
                        break
                if selected is None:
                    break
                found.append(selected)
            if len(found) == 5:
                return found

            # 檢查 A-2-3-4-5 (特殊情況)
            ace_needed = [14, 15, 3, 4, 5]  # A, 2, 3, 4, 5
            found = []
            for rank in ace_needed:
                selected = None
                for card in hand:
                    if card.rank == rank and card not in found:
                        selected = card
                        break
                if selected is None:
                    break
                found.append(selected)
            if len(found) == 5:
                return found

        else:
            found = []
            for rank in needed:
                selected = None
                for card in hand:
                    if card.rank == rank and card not in found:
                        selected = card
                        break
                if selected is None:
                    return None
                found.append(selected)
            return found

        return None

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """找出所有五張牌型。
        
        Args:
            hand: 手牌
            
        Returns:
            所有五張牌型組合
        """
        fives = []

        if len(hand) < 5:
            return fives

        # 嘗試所有 5 張組合
        for combo in combinations(hand, 5):
            combo_list = list(combo)
            if HandClassifier.classify(combo_list) is not None:
                fives.append(combo_list)

        return fives

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        """取得所有合法出牌。
        
        Args:
            hand: 手牌
            last_play: 上家出牌，None 表示第一回合
            
        Returns:
            所有合法出牌清單
        """
        valid_plays = []

        if last_play is None:
            # 第一回合：只能出3♣
            for card in hand:
                if card.rank == 3 and card.suit == 0:
                    valid_plays.append([card])
            return valid_plays

        last_class = HandClassifier.classify(last_play)
        if last_class is None:
            return valid_plays

        last_type = last_class[0]

        # 根據上家牌型尋找合法出牌
        if last_type.value == 1:  # 單張
            candidates = HandFinder.find_singles(hand)
        elif last_type.value == 2:  # 對子
            candidates = HandFinder.find_pairs(hand)
        elif last_type.value == 3:  # 三條
            candidates = HandFinder.find_triples(hand)
        elif last_type.value >= 4:  # 五張牌型
            candidates = HandFinder.find_fives(hand)
        else:
            candidates = []

        for candidate in candidates:
            if HandClassifier.can_play(last_play, candidate):
                valid_plays.append(candidate)

        return valid_plays
