"""
Phase 4: AI 策略
AIStrategy 類別實作
"""

from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class AIStrategy:
    """AI 策略"""
    
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
        """
        評分出牌，用於AI選擇最佳出牌
        :param cards: 要出的牌
        :param hand: 玩家的手牌
        :param is_first: 是否是第一回合
        :return: 評分
        """
        result = HandClassifier.classify(cards)
        if result is None:
            return -float('inf')
        
        card_type, rank, suit = result
        
        # 基礎牌型分數
        type_score = AIStrategy.TYPE_SCORES.get(card_type, 0)
        score = type_score * 100
        
        # 加上rank分數
        rank_score = rank * 10
        score += rank_score
        
        # 計算剩餘牌數（出牌後）
        remaining_count = len(hand) - len(cards)
        
        # 剩1張加分
        if remaining_count == 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        # 剩≤3張加分
        elif remaining_count <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS
        
        # ♠牌加分
        spade_count = sum(1 for c in cards if c.suit == 3)
        score += spade_count * AIStrategy.SPADE_BONUS
        
        return score
    
    @staticmethod
    def select_best(
        valid_plays: List[List[Card]],
        hand: Hand,
        is_first: bool = False
    ) -> Optional[List[Card]]:
        """
        選擇最佳出牌
        :param valid_plays: 所有合法出牌
        :param hand: 玩家的手牌
        :param is_first: 是否是第一回合
        :return: 選中的出牌或None
        """
        if not valid_plays:
            return None
        
        # 第一回合只能出3♣
        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play
            return valid_plays[0] if valid_plays else None
        
        # 其他回合選分數最高的
        best_play = None
        best_score = -float('inf')
        
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play
        
        return best_play
