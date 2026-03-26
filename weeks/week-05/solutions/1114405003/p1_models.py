# -*- coding: utf-8 -*-
"""
大二紙牌遊戲 - Phase 1 資料模型

實作 Card、Deck、Hand、Player 類別
"""

from typing import List, Optional, Tuple
import random


class Card:
    """
    紙牌類別
    
    屬性：
    - rank: 等級（2-14，其中14=A，2=2最高）
    - suit: 花色（0=♣、1=♦、2=♥、3=♠）
    """
    
    # 花色對應
    SUIT_SYMBOLS = {0: "♣", 1: "♦", 2: "♥", 3: "♠"}
    
    # 等級對應（2-14）
    RANK_SYMBOLS = {
        2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 
        10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"
    }
    
    def __init__(self, rank: int, suit: int) -> None:
        """
        初始化卡牌
        
        Args:
            rank: 等級（2-14）
            suit: 花色（0-3）
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        """
        形成「♠A」格式的字串表示
        
        Returns:
            花色+等級的字串，如 "♠A"、"♣3"
        """
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"
    
    def __eq__(self, other: "Card") -> bool:
        """判斷是否相同牌"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self) -> int:
        """回傳雜湊值（為了支持 set 去重）"""
        return hash((self.rank, self.suit))
    
    def __gt__(self, other: "Card") -> bool:
        """
        比較大小：先比等級，再比花色（♠>♥>♦>♣）
        
        等級順序：2(最高) > A > K > Q > J > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3
        
        Args:
            other: 另一張牌
            
        Returns:
            self > other 時為 True
        """
        # 等級排序值：2 映射為 15（最高），其他保持原值
        rank_priority_self = 15 if self.rank == 2 else self.rank
        rank_priority_other = 15 if other.rank == 2 else other.rank
        
        if rank_priority_self != rank_priority_other:
            return rank_priority_self > rank_priority_other
        return self.suit > other.suit
    
    def __lt__(self, other: "Card") -> bool:
        """小於比較"""
        rank_priority_self = 15 if self.rank == 2 else self.rank
        rank_priority_other = 15 if other.rank == 2 else other.rank
        
        if rank_priority_self != rank_priority_other:
            return rank_priority_self < rank_priority_other
        return self.suit < other.suit
    
    def __ge__(self, other: "Card") -> bool:
        """大於等於比較"""
        return self > other or self == other
    
    def __le__(self, other: "Card") -> bool:
        """小於等於比較"""
        return self < other or self == other
    
    def to_sort_key(self) -> Tuple[int, int]:
        """
        回傳排序鍵 tuple
        
        Returns:
            (rank, suit) 元組
        """
        return (self.rank, self.suit)


class Deck:
    """
    牌堆類別
    
    管理完整的 52 張牌組（等級 2-14 × 花色 0-3）
    """
    
    def __init__(self) -> None:
        """初始化牌堆，建立 52 張牌"""
        self.cards: List[Card] = []
        self._create_cards()
    
    def _create_cards(self) -> None:
        """
        建立牌組
        
        生成範圍：等級 2-14 × 花色 0-3 = 52 張牌
        """
        for rank in range(2, 15):
            for suit in range(4):
                self.cards.append(Card(rank, suit))
    
    def shuffle(self) -> None:
        """打亂牌序"""
        random.shuffle(self.cards)
    
    def deal(self, num: int) -> List[Card]:
        """
        發牌
        
        Args:
            num: 發出的張數
            
        Returns:
            發出的牌清單（可能少於 num 張，如果剩餘牌不足）
        """
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt
    
    def __len__(self) -> int:
        """回傳剩餘牌數"""
        return len(self.cards)


class Hand(list):
    """
    手牌類別
    
    繼承自 list，代表玩家手中的牌
    支持排序、查詢、移除等操作
    """
    
    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        """
        初始化手牌
        
        Args:
            cards: 初始牌清單，預設為空
        """
        super().__init__()
        if cards:
            self.extend(cards)
    
    def sort_desc(self) -> None:
        """
        按大小排序，由大到小
        
        排序優先順序：
        1. 等級由大到小（等級 2 最高）
        2. 花色由大到小（suit 降序）
        """
        # 將等級 2 映射為 15（最高），其他保持原值
        def sort_key_func(card):
            rank_priority = 15 if card.rank == 2 else card.rank
            return (rank_priority, card.suit)
        
        self.sort(key=sort_key_func, reverse=True)
    
    def find_3_clubs(self) -> Optional[Card]:
        """
        尋找梅花 3（等級 3、花色 0 的牌）
        
        Returns:
            找到的 Card 或 None
        """
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None
    
    def remove_card(self, card: Card) -> bool:
        """
        移除指定牌
        
        Args:
            card: 要移除的牌
            
        Returns:
            成功移除回傳 True，否則 False
        """
        try:
            self.remove(card)
            return True
        except ValueError:
            return False


class Player:
    """
    玩家類別
    
    代表遊戲中的一個玩家（人類或 AI）
    """
    
    def __init__(self, name: str, is_ai: bool = False) -> None:
        """
        初始化玩家
        
        Args:
            name: 玩家名稱
            is_ai: 是否為 AI 玩家（預設 False=人類玩家）
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]) -> None:
        """
        收牌
        
        Args:
            cards: 收到的牌清單
        """
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        """
        出牌
        
        Args:
            cards: 要出的牌清單
            
        Returns:
            成功出牌回傳牌清單，否則回傳空清單
        """
        # 檢查是否所有牌都在手牌中
        for card in cards:
            if card not in self.hand:
                return []
        
        # 移除這些牌
        for card in cards:
            self.hand.remove(card)
        
        return cards
    
    def play_card(self, card: Card) -> Optional[Card]:
        """
        出一張牌
        
        Args:
            card: 要出的牌
            
        Returns:
            成功出牌回傳牌，否則回傳 None
        """
        if card in self.hand:
            self.hand.remove(card)
            return card
        return None


if __name__ == "__main__":
    # 簡單測試
    print("=" * 50)
    print("大二紙牌遊戲 - Phase 1 資料模型")
    print("=" * 50)
    
    # 建立牌堆
    print("\n【牌堆測試】")
    deck = Deck()
    print(f"牌堆初始化：{len(deck)} 張牌")
    print(f"首5張牌：{[str(card) for card in deck.cards[:5]]}")
    
    # 洗牌
    deck.shuffle()
    print(f"洗牌後首5張牌：{[str(card) for card in deck.cards[:5]]}")
    
    # 發牌
    print("\n【發牌測試】")
    dealt = deck.deal(5)
    print(f"發出5張：{[str(card) for card in dealt]}")
    print(f"剩餘：{len(deck)} 張牌")
    
    # 建立玩家
    print("\n【玩家測試】")
    player1 = Player("Alice", is_ai=False)
    player2 = Player("Bot", is_ai=True)
    
    print(f"玩家1：{player1.name} (AI={player1.is_ai})")
    print(f"玩家2：{player2.name} (AI={player2.is_ai})")
    
    # 收牌
    player1.take_cards(dealt)
    print(f"\nAlice 收牌：手牌數 = {len(player1.hand)}")
    print(f"Alice 手牌：{[str(card) for card in player1.hand]}")
    
    # 排序
    player1.hand.sort_desc()
    print(f"排序後：{[str(card) for card in player1.hand]}")
    
    # 查找梅花3
    print("\n【查找梅花3測試】")
    three_clubs = player1.hand.find_3_clubs()
    print(f"梅花3：{three_clubs}")
    
    # 出牌
    if three_clubs:
        result = player1.play_card(three_clubs)
        print(f"出牌『{result}』，剩餘 {len(player1.hand)} 張牌")
    
    print("\n" + "=" * 50)
    print("✅ 所有操作完成")
    print("=" * 50)
