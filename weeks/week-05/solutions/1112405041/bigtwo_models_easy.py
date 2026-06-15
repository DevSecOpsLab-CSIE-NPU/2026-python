import random

# 【第一階段：資料模型 - 大一入門版】
# 我們要實作大老二的基本組件：卡片、牌組、玩家

class Card:
    """單張卡片類別"""
    def __init__(self, rank, suit):
        # rank 代表數字：3 到 15 (其中 11=J, 12=Q, 13=K, 14=A, 15=2)
        # suit 代表花色：0=梅花, 1=方塊, 2=紅心, 3=黑桃
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # 這個方法決定了我們把卡片「印出來」時的樣子
        suits_icons = ['♣', '♦', '♥', '♠']
        # 轉換顯示標籤，10 以上用字母表示
        labels = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

        display_val = str(self.rank)
        if self.rank in labels:
            display_val = labels[self.rank]

        return suits_icons[self.suit] + display_val

    # 比較大小：大老二優先比數字，數字一樣才比花色
    def __lt__(self, other):
        if self.rank != other.rank:
            # 數字不同，直接比數字
            return self.rank < other.rank
        # 數字相同，比較花色
        return self.suit < other.suit

class Deck:
    """牌組類別，負責洗牌跟發牌"""
    def __init__(self):
        self.cards = []
        # 使用兩層迴圈產生 52 張牌 (13 個數字 x 4 種花色)
        for r in range(3, 16):
            for s in range(4):
                new_card = Card(r, s)
                self.cards.append(new_card)

    def shuffle_deck(self):
        # 呼叫 Python 內建的隨機模組進行隨機洗牌
        random.shuffle(self.cards)

    def deal_cards(self, count):
        # 從牌組頂端發出指定張數的牌
        hand_cards = []
        for i in range(count):
            if len(self.cards) > 0:
                # 拿出最後一張牌
                last_card = self.cards.pop()
                hand_cards.append(last_card)
        return hand_cards

class Player:
    """玩家類別，儲存姓名與手上的牌"""
    def __init__(self, player_name):
        self.name = player_name
        self.hand = [] # 這裡存放的是 Card 物件的清單

    def sort_hand(self):
        # 使用 Python 的排序功能，它會自動對應我們在 Card 裡面寫的比較邏輯
        # 大老二看牌習慣從大排到小，所以我們用 reverse=True
        self.hand.sort(reverse=True)

    def show_status(self):
        # 回傳玩家目前的名字跟手牌狀況
        return "玩家 " + self.name + " 的手牌：" + str(self.hand)

# --- 測試小腳本 ---
if __name__ == "__main__":
    print("--- 澎科大資工系：大老二專案測試 ---")
    d = Deck()
    d.shuffle_deck()

    p = Player("阿明")
    # 發 13 張牌給玩家
    p.hand = d.deal_cards(13)
    p.sort_hand()
    print(p.show_status())
