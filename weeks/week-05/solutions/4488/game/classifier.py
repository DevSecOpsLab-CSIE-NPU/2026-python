"""Phase 2: Card type classification and comparison."""

from enum import Enum
from typing import Optional, Tuple, List
from collections import Counter
from game.models import Card


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
    """牌型分類與比較。"""

    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        """檢查是否為順子。
        
        Args:
            ranks: 牌的數字列表
            
        Returns:
            是否為順子
        """
        if len(ranks) != 5:
            return False

        sorted_ranks = sorted(set(ranks))

        # 檢查連續 5 張
        if len(sorted_ranks) == 5:
            if sorted_ranks[-1] - sorted_ranks[0] == 4:
                return True

        # 特殊情況：A-2-3-4-5
        if sorted(ranks) == [3, 4, 5, 14, 15]:
            return True

        return False

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """檢查是否為同花。
        
        Args:
            suits: 花色列表
            
        Returns:
            是否為同花
        """
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """分類牌型。
        
        Args:
            cards: 牌列表
            
        Returns:
            (牌型, 數字, 花色) 或 None
        """
        n = len(cards)

        if n == 1:
            return (CardType.SINGLE, cards[0].rank, cards[0].suit)

        if n == 2:
            if cards[0].rank == cards[1].rank:
                return (CardType.PAIR, cards[0].rank, 0)
            return None

        if n == 3:
            if cards[0].rank == cards[1].rank == cards[2].rank:
                return (CardType.TRIPLE, cards[0].rank, 0)
            return None

        if n == 5:
            ranks = [c.rank for c in cards]
            suits = [c.suit for c in cards]

            rank_counts = Counter(ranks)

            # 同花順
            if HandClassifier._is_flush(suits) and HandClassifier._is_straight(ranks):
                max_rank = max(ranks)
                if sorted(ranks) == [3, 4, 5, 14, 15]:
                    max_rank = 5
                return (CardType.STRAIGHT_FLUSH, max_rank, 0)

            # 四條
            if 4 in rank_counts.values():
                quad_rank = [r for r, c in rank_counts.items() if c == 4][0]
                return (CardType.FOUR_OF_A_KIND, quad_rank, 0)

            # 葫芦
            if 3 in rank_counts.values() and 2 in rank_counts.values():
                triple_rank = [r for r, c in rank_counts.items() if c == 3][0]
                return (CardType.FULL_HOUSE, triple_rank, 0)

            # 同花
            if HandClassifier._is_flush(suits):
                max_rank = max(ranks)
                return (CardType.FLUSH, max_rank, 0)

            # 順子
            if HandClassifier._is_straight(ranks):
                max_rank = max(ranks)
                if sorted(ranks) == [3, 4, 5, 14, 15]:
                    max_rank = 5
                return (CardType.STRAIGHT, max_rank, 0)

        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        """比較兩手牌大小。
        
        Args:
            play1: 第一手牌
            play2: 第二手牌
            
        Returns:
            1 = play1 大, -1 = play2 大, 0 = 平手
        """
        class1 = HandClassifier.classify(play1)
        class2 = HandClassifier.classify(play2)

        if class1 is None or class2 is None:
            return 0

        type1, rank1, suit1 = class1
        type2, rank2, suit2 = class2

        # 先比牌型
        if type1.value != type2.value:
            return 1 if type1.value > type2.value else -1

        # 再比數字
        if rank1 != rank2:
            return 1 if rank1 > rank2 else -1

        # 最後比花色（通常只有單張和對子）
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1

        return 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        """檢查是否可以出牌。
        
        Args:
            last_play: 上家出牌，None 表示第一回合
            cards: 要出的牌
            
        Returns:
            是否合法
        """
        if last_play is None:
            # 第一回合只能出3♣
            if len(cards) == 1 and cards[0].rank == 3 and cards[0].suit == 0:
                return True
            return False

        class_new = HandClassifier.classify(cards)
        class_old = HandClassifier.classify(last_play)

        if class_new is None or class_old is None:
            return False

        # 牌數要相同
        if len(cards) != len(last_play):
            return False

        # 牌型要相同
        if class_new[0] != class_old[0]:
            return False

        # 數字要大於或相同 (比較邏輯)
        return HandClassifier.compare(cards, last_play) >= 0
