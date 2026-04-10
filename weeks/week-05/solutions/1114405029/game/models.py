import random

class Card:
    """卡牌實體：支援絕對權重比較"""
    def __init__(self, rank, suit):
        self.rank = rank  # 3~15 (11=J, 12=Q, 13=K, 14=A, 15=2)
        self.suit = suit  # 0=♣, 1=♦, 2=♥, 3=♠

    def __repr__(self):
        suits = {0: "♣", 1: "♦", 2: "♥", 3: "♠"}
        ranks = {11: "J", 12: "Q", 13: "K", 14: "A", 15: "2"}
        return f"{suits[self.suit]}{ranks.get(self.rank, str(self.rank))}"

    def __lt__(self, other):
        """大老二核心比較：先比數字，數字相同比花色"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

class Deck:
    """牌堆：負責洗牌與公平發牌"""
    def __init__(self):
        self.cards = [Card(r, s) for r in range(3, 16) for s in range(4)]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, n=13):
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return sorted(dealt)

class Player:
    """玩家實體：包含經濟系統與狀態"""
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.hand = []
        self.gold = 5000  # 上市標準：起始金幣給多一點，容錯率高，玩家才不會馬上流失
        self.is_bankrupt = False
        self.skip_count = 3

    def remove_cards(self, cards_to_remove):
        for c in cards_to_remove:
            # 依據值移除，避免物件參考問題
            target = next((hc for hc in self.hand if hc.rank == c.rank and hc.suit == c.suit), None)
            if target:
                self.hand.remove(target)