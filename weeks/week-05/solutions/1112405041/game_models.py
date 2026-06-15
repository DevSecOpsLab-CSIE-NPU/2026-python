import random

# 撲克牌類別 - 定義單張牌的屬性與比較
class Card:
    # 花色圖示與權重 (梅花 < 方塊 < 紅心 < 黑桃)
    SUIT_ICONS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    # 數字顯示對應
    RANK_LABELS = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

    def __init__(self, rank, suit):
        self.rank = rank  # 數字: 3-15
        self.suit = suit  # 花色: 0-3

    def __repr__(self):
        # 顯示格式，例如 "♠A"
        label = self.RANK_LABELS.get(self.rank, str(self.rank))
        if self.rank == 10: label = "T" # 十通常用 T 表示
        return f"{self.SUIT_ICONS[self.suit]}{label}"

    def __eq__(self, other):
        if not isinstance(other, Card): return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        # 比較大小的邏輯：先比數字，數字相同比花色
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

# 牌組類別 - 負責洗牌與發牌
class Deck:
    def __init__(self):
        self.cards = []
        self._create_cards()

    def _create_cards(self):
        # 建立 52 張牌 (3 到 2 之中的 13 個數字 x 4 種花色)
        for r in range(3, 16):
            for s in range(4):
                self.cards.append(Card(r, s))

    def shuffle(self):
        # 使用 random 模組進行隨機洗牌
        random.shuffle(self.cards)

    def deal(self, n):
        # 從牌組中發出 n 張牌
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt

# 手牌類別 - 處理玩家手上的牌
class Hand(list):
    def sort_desc(self):
        # 依照大老二規則降序排列 (大的在前)
        # 這裡利用我們在 Card 定義的 __lt__ 進行反向排序
        self.sort(reverse=True)

    def find_3_clubs(self):
        # 尋找梅花 3 (開局必備)
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

# 玩家類別 - 定義玩家行為
class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards):
        # 將拿到的牌加入手牌並排序
        self.hand.extend(cards)
        self.hand.sort_desc()

    def __repr__(self):
        return f"玩家 {self.name} (手牌: {len(self.hand)})"
