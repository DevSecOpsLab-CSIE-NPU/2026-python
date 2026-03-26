"""
Phase 4: AI 策略 - 單元測試

測試 AIStrategy 類的評分函數、最佳出牌選擇和完整 AI 策略
使用貪心演算法最大化每一步的出牌分數
"""

import unittest
from enum import Enum
from typing import List, Optional, Tuple


# ==================== 枚舉定義 ====================

class Suit(Enum):
    """花色列舉"""
    CLUB = 0      # ♣ 梅花
    DIAMOND = 1   # ♦ 方塊
    HEART = 2     # ♥ 紅心
    SPADE = 3     # ♠ 黑桃


class CardType(Enum):
    """牌型列舉"""
    SINGLE = 1       # 單張
    PAIR = 2         # 對子
    TRIPLE = 3       # 三條
    STRAIGHT = 5     # 順子
    FLUSH = 6        # 同花
    FULL_HOUSE = 7   # 葫蘆（滿堂紅）
    FOUR_OF_A_KIND = 8  # 四條
    STRAIGHT_FLUSH = 9 # 順利同花


# ==================== 基礎類別 ====================

class Card:
    """撲克牌"""
    
    def __init__(self, rank: int, suit: int):
        """初始化撲克牌
        
        Args:
            rank: 牌點數 (3-14，其中 14=A, 2=最大)
            suit: 花色 (0=♣, 1=♦, 2=♥, 3=♠)
        """
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        """檢查兩張牌是否相等"""
        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        """牌的字符串表示"""
        rank_str = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 2: '2'}.get(self.rank, str(self.rank))
        suit_str = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}.get(self.suit, '?')
        return f"{suit_str}{rank_str}"
    
    def __hash__(self):
        """使卡牌可被雜湊"""
        return hash((self.rank, self.suit))


class Hand:
    """牌手"""
    
    def __init__(self, cards: List[Card]):
        """初始化牌手
        
        Args:
            cards: 牌的列表
        """
        self.cards = list(cards)
    
    def remove_cards(self, cards_to_remove: List[Card]) -> 'Hand':
        """從手牌中移除指定的牌
        
        Args:
            cards_to_remove: 要移除的牌列表
            
        Returns:
            新的 Hand 物件（去除指定的牌）
        """
        remaining = self.cards.copy()
        for card in cards_to_remove:
            remaining.remove(card)
        return Hand(remaining)
    
    def __repr__(self):
        """手牌的字符串表示"""
        return f"Hand({self.cards})"


# ==================== AI 策略類別 ====================

class AIStrategy:
    """AI 出牌策略 - 使用貪心演算法
    
    評分規則：
    1. 基礎分數：牌型階級分 + 點數加權分
    2. 手牌剩餘獎勵：剩牌少時分數高（鼓勵儘快出完）
    3. 花色獎勵：出黑桃加5分（用於平局破解）
    """
    
    # 牌型分數權重
    CARD_TYPE_WEIGHTS = {
        CardType.SINGLE: 100,
        CardType.PAIR: 200,
        CardType.TRIPLE: 300,
        CardType.STRAIGHT: 400,
        CardType.FLUSH: 500,
        CardType.FULL_HOUSE: 600,
        CardType.FOUR_OF_A_KIND: 700,
        CardType.STRAIGHT_FLUSH: 800
    }
    
    # 點數權重
    RANK_WEIGHT = 10
    
    # 剩牌獎勵閾值
    NEAR_EMPTY_THRESHOLD = 1  # 只剩1張
    NEAR_EMPTY_BONUS = 10000  # 加10000分
    
    LOW_CARDS_THRESHOLD = 2   # 只剩2張
    LOW_CARDS_BONUS = 500     # 加500分
    
    # 花色獎勵
    SPADE_BONUS = 5
    
    @staticmethod
    def score_play(play: List[Card], hand: Hand, card_type: CardType) -> int:
        """計算一個出牌的分數
        
        分數 = 牌型基礎分 + 點數加權分 + 剩牌獎勵 + 花色獎勵
        
        Args:
            play: 要出的牌列表
            hand: 當前手牌
            card_type: 牌的類型
            
        Returns:
            計算後的分數
        """
        # 1. 牌型基礎分
        score = AIStrategy.CARD_TYPE_WEIGHTS.get(card_type, 0)
        
        # 2. 點數加權分（選出分數最高的牌進行加權）
        if play:
            max_card = max(play, key=lambda c: c.rank)
            score += max_card.rank * AIStrategy.RANK_WEIGHT
        
        # 3. 剩牌獎勵（鼓勵儘快出完手牌）
        remaining_count = len(hand.cards) - len(play)
        
        if remaining_count == AIStrategy.NEAR_EMPTY_THRESHOLD:
            # 剩1張時，獎勵很高
            score += AIStrategy.NEAR_EMPTY_BONUS
        elif remaining_count == AIStrategy.LOW_CARDS_THRESHOLD:
            # 剩2張時，獎勵適中
            score += AIStrategy.LOW_CARDS_BONUS
        
        # 4. 花色獎勵（出黑桃加5分，用於當分數相同時作為決策依據）
        if any(card.suit == Suit.SPADE.value for card in play):
            score += AIStrategy.SPADE_BONUS
        
        return score
    
    @staticmethod
    def select_best_play(valid_plays: List[List[Card]], 
                        hand: Hand,
                        classifications: Optional[List[Tuple[CardType, int, int]]] = None) -> Optional[List[Card]]:
        """從合法出牌列表中選擇最佳出牌
        
        使用貪心演算法：選擇分數最高的出牌
        
        Args:
            valid_plays: 所有合法的出牌列表
            hand: 當前手牌
            classifications: 出牌對應的牌型列表 (card_type, rank, suit_count)
                            若不提供，則假設全為 SINGLE
            
        Returns:
            分數最高的出牌 (List[Card])，若無合法出牌則回傳 None
        """
        if not valid_plays:
            return None
        
        # 若未提供分類，假設全為 SINGLE
        if classifications is None:
            classifications = [CardType.SINGLE for _ in valid_plays]
        
        # 計算每個出牌的分數
        best_play = None
        best_score = -1
        
        for play, card_type in zip(valid_plays, classifications):
            current_score = AIStrategy.score_play(play, hand, card_type)
            
            if current_score > best_score:
                best_score = current_score
                best_play = play
        
        return best_play
    
    @staticmethod
    def decide_play(hand: Hand,
                   valid_plays: List[List[Card]],
                   classifications: Optional[List[Tuple[CardType, int, int]]] = None) -> Optional[List[Card]]:
        """AI 決策：選擇最佳出牌或不出牌
        
        這是 AIStrategy 的主入口點，包含完整的決策邏輯
        
        Args:
            hand: 當前手牌
            valid_plays: 所有合法的出牌列表
            classifications: 出牌對應的牌型分類
            
        Returns:
            選定的出牌 (List[Card])，若無法或不應出牌則回傳 None
        """
        # 若無合法出牌，回傳 None（必須跳過）
        if not valid_plays:
            return None
        
        # 若提供分類，使用 select_best_play
        if classifications is not None:
            return AIStrategy.select_best_play(valid_plays, hand, classifications)
        
        # 否則，假設全為 SINGLE
        classifications = [CardType.SINGLE for _ in valid_plays]
        return AIStrategy.select_best_play(valid_plays, hand, classifications)


# ==================== 單元測試 ====================

class TestScoreFunction(unittest.TestCase):
    """測試評分函數 (AIStrategy.score_play)
    
    驗證：
    1. 基礎分數計算
    2. 點數加權
    3. 剩牌獎勵
    4. 花色獎勵
    """
    
    def test_score_single_basic(self):
        """【測試1】單張評分 - 基礎計算
        
        給定：單張 ♣A，手牌有5張（避免剩牌獎勵）
        預期：分數 = 100 (牌型) + 140 (14×10) = 240
        """
        # 【準備】牌和手牌
        card_a = Card(14, Suit.CLUB.value)  # ♣A，rank=14（非黑桃，無額外獎勵）
        play = [card_a]
        # 準備5張手牌，出牌後剩4張（不觸發剩牌獎勵）
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), card_a])
        
        # 【執行】計算分數
        score = AIStrategy.score_play(play, hand, CardType.SINGLE)
        
        # 【驗證】
        expected = 100 + (14 * 10)  # 牌型分 + 點數分
        self.assertEqual(score, expected, f"單張 ♣A 應得 {expected} 分，實得 {score} 分")
    
    def test_score_pair_higher_than_single(self):
        """【測試2】對子評分高於單張
        
        給定：對子 vs 單張（相同點數卡）
        預期：對子分數 > 單張分數
        """
        # 【準備】
        card_a1 = Card(14, 3)  # ♠A
        card_a2 = Card(14, 0)  # ♣A
        
        pair = [card_a1, card_a2]
        single = [card_a1]
        hand = Hand([Card(3, 0), card_a1, card_a2])
        
        # 【執行】
        pair_score = AIStrategy.score_play(pair, hand, CardType.PAIR)
        single_score = AIStrategy.score_play(single, hand, CardType.SINGLE)
        
        # 【驗證】
        self.assertGreater(pair_score, single_score, 
                          f"對子分數({pair_score}) 應大於單張分數({single_score})")
    
    def test_score_triple_higher_than_pair(self):
        """【測試3】三條評分高於對子
        
        給定：三條 vs 對子（相同點數卡）
        預期：三條分數 > 對子分數
        """
        # 【準備】
        card_a1 = Card(14, 3)  # ♠A
        card_a2 = Card(14, 0)  # ♣A
        card_a3 = Card(14, 1)  # ♦A
        
        triple = [card_a1, card_a2, card_a3]
        pair = [card_a1, card_a2]
        hand = Hand([card_a1, card_a2, card_a3, Card(3, 2)])
        
        # 【執行】
        triple_score = AIStrategy.score_play(triple, hand, CardType.TRIPLE)
        pair_score = AIStrategy.score_play(pair, hand, CardType.PAIR)
        
        # 【驗證】
        self.assertGreater(triple_score, pair_score,
                          f"三條分數({triple_score}) 應大於對子分數({pair_score})")
    
    def test_score_near_empty_bonus(self):
        """【測試4】只剩1張時有高額獎勵
        
        給定：出1張牌後手牌只剩1張
        預期：獎勵 > 10000
        """
        # 【準備】
        card1 = Card(3, 0)   # ♣3
        card2 = Card(14, 3)  # ♠A
        play = [card1]
        hand = Hand([card1, card2])  # 2張，移除1張後剩1張
        
        # 【執行】
        score = AIStrategy.score_play(play, hand, CardType.SINGLE)
        
        # 【驗證】
        self.assertGreater(score, 10000, 
                          f"剩1張時分數應 > 10000，實得 {score}")
    
    def test_score_low_cards_bonus(self):
        """【測試5】只剩2張時有中等獎勵
        
        給定：出1張牌後手牌剩2張
        預期：獎勵 > 500
        """
        # 【準備】
        cards = [Card(3, 0), Card(4, 1), Card(14, 3)]
        play = [cards[0]]  # 出♣3
        hand = Hand(cards)  # 3張，移除1張後剩2張
        
        # 【執行】
        score = AIStrategy.score_play(play, hand, CardType.SINGLE)
        
        # 【驗證】
        self.assertGreater(score, 500,
                          f"剩2張時分數應 > 500，實得 {score}")
    
    def test_score_spade_bonus(self):
        """【測試6】出黑桃牌額外獎勵
        
        給定：含黑桃的出牌
        預期：分數 = 基礎分 + 5
        """
        # 【準備】
        spade_card = Card(10, Suit.SPADE.value)  # ♠10
        club_card = Card(10, Suit.CLUB.value)    # ♣10
        
        spade_play = [spade_card]
        club_play = [club_card]
        hand = Hand([spade_card, club_card, Card(3, 0)])
        
        # 【執行】
        spade_score = AIStrategy.score_play(spade_play, hand, CardType.SINGLE)
        club_score = AIStrategy.score_play(club_play, hand, CardType.SINGLE)
        
        # 【驗證】
        difference = spade_score - club_score
        self.assertEqual(difference, 5,
                        f"黑桃牌應額外+5分，差值為 {difference}")


class TestSelectBestPlay(unittest.TestCase):
    """測試最佳出牌選擇 (AIStrategy.select_best_play)
    
    驗證：
    1. 從合法出牌中選擇分數最高的
    2. 無合法出牌時回傳 None
    3. 首回合處理（梅花3）
    """
    
    def test_select_best_single_vs_pair(self):
        """【測試7】在單張vs對子中選擇對子
        
        給定：合法出牌 [單張, 對子]
        預期：選擇對子（分數更高）
        """
        # 【準備】
        card_a1 = Card(14, 3)  # ♠A
        card_a2 = Card(14, 0)  # ♣A
        
        single = [card_a1]
        pair = [card_a1, card_a2]
        valid_plays = [single, pair]
        classifications = [CardType.SINGLE, CardType.PAIR]
        
        hand = Hand([card_a1, card_a2, Card(3, 2)])
        
        # 【執行】
        best = AIStrategy.select_best_play(valid_plays, hand, classifications)
        
        # 【驗證】
        self.assertEqual(best, pair, "應選擇對子而非單張")
    
    def test_select_empty_returns_none(self):
        """【測試8】無合法出牌時回傳 None
        
        給定：空的合法出牌列表
        預期：回傳 None
        """
        # 【準備】
        hand = Hand([Card(3, 0)])
        valid_plays = []
        
        # 【執行】
        result = AIStrategy.select_best_play(valid_plays, hand)
        
        # 【驗證】
        self.assertIsNone(result, "無合法出牌應回傳 None")
    
    def test_select_first_turn_club_three(self):
        """【測試9】首回合只有梅花3可出
        
        給定：首回合手牌 [♣3, ♠A, ♣K]，只有 [♣3] 合法
        預期：選擇 ♣3
        """
        # 【準備】
        club_3 = Card(3, Suit.CLUB.value)  # ♣3（必須首回合出）
        spade_a = Card(14, Suit.SPADE.value)
        club_k = Card(13, Suit.CLUB.value)
        
        valid_plays = [[club_3]]  # 只有♣3可出
        classifications = [CardType.SINGLE]
        
        hand = Hand([club_3, spade_a, club_k])
        
        # 【執行】
        best = AIStrategy.select_best_play(valid_plays, hand, classifications)
        
        # 【驗證】
        self.assertEqual(best, [club_3], "首回合應選擇 ♣3")


class TestAIStrategy(unittest.TestCase):
    """測試完整 AI 策略 (AIStrategy.decide_play)
    
    驗證：
    1. 有牌可出時一定出牌
    2. 優先選高分牌（貪心演算法）
    3. 努力出完手牌（剩牌獎勵優先）
    """
    
    def test_ai_always_plays_when_possible(self):
        """【測試10】有牌可出時 AI 一定出牌
        
        給定：有合法出牌
        預期：不回傳 None
        """
        # 【準備】
        single = [Card(14, 3)]  # ♠A
        valid_plays = [single]
        classifications = [CardType.SINGLE]
        hand = Hand([Card(14, 3), Card(3, 0)])
        
        # 【執行】
        decision = AIStrategy.decide_play(hand, valid_plays, classifications)
        
        # 【驗證】
        self.assertIsNotNone(decision, "有合法出牌時應決策出牌")
    
    def test_ai_prefers_high_value_play(self):
        """【測試11】AI 優先選擇高分牌
        
        給定：合法出牌 [♣3, ♠A]（◆A分數更高）
        預期：選擇 ♠A
        """
        # 【準備】
        club_3 = Card(3, Suit.CLUB.value)     # ♣3
        spade_a = Card(14, Suit.SPADE.value)  # ♠A（較高）
        
        valid_plays = [[club_3], [spade_a]]
        classifications = [CardType.SINGLE, CardType.SINGLE]
        hand = Hand([club_3, spade_a])
        
        # 【執行】
        decision = AIStrategy.decide_play(hand, valid_plays, classifications)
        
        # 【驗證】
        self.assertEqual(decision, [spade_a], "應選擇 ♠A（高分牌）而非 ♣3")
    
    def test_ai_tries_to_empty_hand(self):
        """【測試12】AI 會優先嘗試出完手牌
        
        給定：剩最後一張牌，出牌會讓手牌空
        預期：優先選擇這個出牌
        """
        # 【準備】
        last_card = Card(14, 3)  # ♠A（最後一張）
        other_cards = [Card(3, 0), Card(4, 1)]
        
        # 情景：手牌 [♣3, ♦4, ♠A]
        # 可出牌：[♣3] 或 [♦4]（不能出♠A因為會剩餘）
        # 或者可出牌包括 [♠A]（剩0張）- 應優先選
        
        valid_plays = [
            [other_cards[0]],  # ♣3（剩2張）
            [other_cards[1]],  # ♦4（剩2張）
            [last_card]        # ♠A（剩0張） - 最高獎勵
        ]
        classifications = [CardType.SINGLE, CardType.SINGLE, CardType.SINGLE]
        hand = Hand(other_cards + [last_card])
        
        # 【執行】
        decision = AIStrategy.decide_play(hand, valid_plays, classifications)
        
        # 【驗證】
        self.assertEqual(decision, [last_card], 
                        "應優先選擇出完手牌的出牌（♠A）")


# ==================== 測試入口 ====================

if __name__ == '__main__':
    # 設定詳細的測試輸出格式
    unittest.main(verbosity=2)
