"""Phase 4: AI strategy for card selection."""

from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType
from game.finder import HandFinder


class AIStrategy:
    """AI 出牌策略。"""

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

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        """評分出牌。
        
        Args:
            cards: 出牌牌組
            hand: 當前手牌
            is_first: 是否為第一回合
            
        Returns:
            評分
        """
        class_result = HandClassifier.classify(cards)
        if class_result is None:
            return 0

        card_type, rank, _ = class_result

        # 基本牌型分
        type_score = AIStrategy.TYPE_SCORES.get(card_type, 0) * 100

        # 數字分
        rank_score = rank * 10

        # 剩餘牌數加分
        remaining = len(hand) - len(cards)
        bonus = 0

        if remaining == 1:
            bonus = AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            bonus = AIStrategy.NEAR_EMPTY_BONUS

        # ♠牌加分 (suit == 3)
        spade_bonus = sum(AIStrategy.SPADE_BONUS for card in cards if card.suit == 3)

        total = type_score + rank_score + bonus + spade_bonus

        return total

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        """選擇最佳出牌。
        
        Args:
            valid_plays: 合法出牌清單
            hand: 當前手牌
            is_first: 是否為第一回合
            
        Returns:
            最佳出牌或 None
        """
        if not valid_plays:
            return None

        # 第一回合：只能選3♣
        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play
            return None

        # 其他：選分數最高者
        best_play = None
        best_score = -1

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play
