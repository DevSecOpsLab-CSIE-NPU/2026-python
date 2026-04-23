import random

# 【第一階段：資料模型 - 簡單版】
# 我們要實作大老二的基本組件：卡片、牌組、玩家

class Card:
    """單張卡片類別"""
    def __init__(self, rank, suit):
        # rank 代表數字：3 到 15 (11=J, 12=Q, 13=K, 14=A, 15=2)
        # suit 代表花色：0=梅花, 1=方塊, 2=紅心, 3=黑桃
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # 這個方法決定了我們把物件印出來時的樣子
        suits = ['♣', '♦', '♥', '♠']
        # 轉換數字顯示，大老二的 10 通常簡寫成 T
        labels = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}
        display_rank = labels.get(self.rank, str(self.rank))
        return f"{suits[self.suit]}{display_rank}"

    # 比較大小：大老二優先比數字，數字一樣比花色
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

class Deck:
    """牌組類別，負責洗牌跟發牌"""
    def __init__(self):
        self.cards = []
        # 使用雙層迴圈產生 52 張牌
        for r in range(3, 16):
            for s in range(4):
                new_card = Card(r, s)
                self.cards.append(new_card)

    def shuffle_deck(self):
        # 呼叫 Python 內建的隨機模組進行洗牌
        random.shuffle(self.cards)

    def deal_cards(self, count):
        # 從牌組頂端發出指定張數的牌
        hand_cards = self.cards[:count]
        # 剩下的牌繼續留在牌組
        self.cards = self.cards[count:]
        return hand_cards

class Player:
    """玩家類別，儲存姓名與手牌"""
    def __init__(self, player_name):
        self.name = player_name
        self.hand = [] # 這裡存的是 Card 物件的清單

    def sort_hand(self):
        # 使用 Python 的 sort 功能，它會自動呼叫我們在 Card 裡面定義的 __lt__
        # 大老二看牌習慣從大排到小
        self.hand.sort(reverse=True)

    def show_info(self):
        # 印出玩家目前的狀況
        return f"【{self.name}】目前的牌：{self.hand}"

# --- 簡單的測試程式碼 ---
if __name__ == "__main__":
    print("--- 澎科大資管系：大老二專案 Phase 1 啟動 ---")
    game_deck = Deck()
    game_deck.shuffle_deck()

    me = Player("阿明")
    # 發 13 張牌給阿明
    me.hand = game_deck.deal_cards(13)
    me.sort_hand()
    print(me.show_info())
