"""
Phase 4: AI 策略 - AIStrategy 類別
"""
from typing import List, Optional
from .models import Card, Hand
from .classifier import HandClassifier, CardType


class AIStrategy:
    """AI 出牌策略"""
    
    # 牌型分數
    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8
    }
    
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5
    
    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        """
        評估出牌的分數
        
        Args:
            cards: 要出的牌
            hand: 玩家手牌
            is_first: 是否為第一回合
            
        Returns:
            評分
        """
        classification = HandClassifier.classify(cards)
        if classification is None:
            return -1000
        
        card_type, num, suit = classification
        
        # 基礎分數 = 牌型分數 × 100 + 數字分數 × 10
        type_score = AIStrategy.TYPE_SCORES.get(card_type, 0)
        rank_order = Card.RANK_ORDER.get(num, 0)
        
        base_score = type_score * 100 + rank_order * 10
        
        # 計算剩餘牌張數
        remaining = len(hand) - len(cards)
        
        # 加上獎勵
        bonus = 0
        
        # 剩1張時獎勵最多
        if remaining == 1:
            bonus += AIStrategy.EMPTY_HAND_BONUS
        # 剩2-3張時有獎勵
        elif remaining <= 3:
            bonus += AIStrategy.NEAR_EMPTY_BONUS
        
        # 黑桃加分
        spade_count = sum(1 for card in cards if card.suit == 3)
        bonus += spade_count * AIStrategy.SPADE_BONUS
        
        return base_score + bonus
    
    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        """
        從合法出牌中選擇最佳出牌
        
        Args:
            valid_plays: 所有合法出牌
            hand: 玩家手牌
            is_first: 是否為第一回合
            
        Returns:
            最佳出牌或 None
        """
        if not valid_plays:
            return None
        
        # 第一回合直接選 3♣（已在 valid_plays 中）
        if is_first:
            for play in valid_plays:
                if (len(play) == 1 and play[0].rank == 3 and play[0].suit == 0):
                    return play
            return None
        
        # 貪心策略：選分數最高的
        best_play = None
        best_score = -float('inf')
        
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play
        
        return best_play
