from typing import List
import random

class Card:
    # 類別屬性：花色和數字的符號
    SUIT_SYMBOLS = ['♣', '♦', '♥', '♠']  # 0=♣,1=♦,2=♥,3=♠
    RANK_SYMBOLS = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}
    
    def __init__(self, rank: int, suit: int):
        # 初始化牌的數字和花色
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        # 回傳牌的字串表示，例如 "♠A"
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"
    
    def __eq__(self, other) -> bool:
        # 比較兩張牌是否相等
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other) -> bool:
        # 比較兩張牌的大小：先比較數字，再比較花色
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit
    
    def __hash__(self) -> int:
        # 計算雜湊值，用於集合和字典
        return hash((self.rank, self.suit))
    
    def to_sort_key(self):
        # 回傳排序用的鍵值元組
        return (self.rank, self.suit)

class Deck:
    def __init__(self):
        # 初始化牌組，建立52張牌
        self.cards = self._create_cards()
    
    def _create_cards(self) -> List[Card]:
        # 建立52張牌：數字3-14，花色0-3，加上2(15)
        cards = []
        for suit in range(4):
            for rank in range(3, 15):
                cards.append(Card(rank, suit))
            cards.append(Card(15, suit))  # 2
        return cards
    
    def shuffle(self):
        # 洗牌
        random.shuffle(self.cards)
    
    def deal(self, n: int) -> List[Card]:
        # 發n張牌，如果不夠就發剩下的
        dealt = []
        for _ in range(min(n, len(self.cards))):
            dealt.append(self.cards.pop())
        return dealt

class Hand(list):
    def __init__(self, cards=None):
        # 初始化手牌
        super().__init__(cards or [])
    
    def sort_desc(self):
        # 排序：數字降序，花色升序
        self.sort(key=lambda c: (-c.rank, c.suit))
    
    def find_3_clubs(self):
        # 找3♣
        three_clubs = Card(3, 0)
        if three_clubs in self:
            return three_clubs
        return None
    
    def remove(self, cards):
        # 移除指定的牌
        for card in cards:
            if card in self:
                super().remove(card)

class Player:
    def __init__(self, name: str, is_ai: bool = False):
        # 初始化玩家
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]):
        # 拿牌到手牌
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        # 出牌
        self.hand.remove(cards)
        return cards