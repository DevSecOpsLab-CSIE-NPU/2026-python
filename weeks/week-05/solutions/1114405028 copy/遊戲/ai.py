from typing import List, Optional
from .models import Card, Hand
from .分類器 import CardType, HandClassifier

class AIStrategy:
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
        # 評分出牌
        type_info = HandClassifier.classify(cards)
        if type_info is None:
            return 0
        
        card_type, rank, suit = type_info
        
        # 牌型分數 × 100
        score = AIStrategy.TYPE_SCORES[card_type] * 100
        
        # 數字分數 × 10
        score += rank * 10
        
        # 剩餘手牌加分
        remaining = len(hand) - len(cards)
        if remaining == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS
        
        # ♠牌加分
        spade_count = sum(1 for c in cards if c.suit == 3)
        score += spade_count * AIStrategy.SPADE_BONUS
        
        return score
    
    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        # 貪心選擇最佳出牌
        if not valid_plays:
            return None
        
        if is_first:
            # 第一回合，只能選3♣
            for play in valid_plays:
                if len(play) == 1 and play[0] == Card(3, 0):
                    return play
            return None
        
        # 選分數最高
        best_play = None
        best_score = -1
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand)
            if score > best_score:
                best_score = score
                best_play = play
        
        return best_play