# Phase 1: 資料模型 - 測試設計

## 目標

建立 Card、Deck、Hand、Player 類別，確保資料模型正確運作。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_models.py`

---

## 測試案例設計

### 1. Card 類別測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_card_creation | `Card(rank=14, suit=3)` | `rank==14, suit==3` |
| test_card_repr_ace | `Card(14,3)` | `repr()=="♠A"` |
| test_card_repr_three | `Card(3,0)` | `repr()=="♣3"` |
| test_card_compare_suit | `Card(14,3) > Card(14,2)` | `True` (♠>♥) |
| test_card_compare_suit_2 | `Card(14,2) > Card(14,1)` | `True` (♥>♦) |
| test_card_compare_suit_3 | `Card(14,1) > Card(14,0)` | `True` (♦>♣) |
| test_card_compare_rank_2 | `Card(15,0) > Card(14,3)` | `True` (2>A) |
| test_card_compare_rank_a | `Card(14,0) > Card(13,3)` | `True` (A>K) |
| test_card_compare_equal | `Card(14,3) > Card(14,3)` | `False` |
| test_card_sort_key | `Card(14,3).to_sort_key()` | `(14,3)` |

---

### 2. Deck 類別測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_deck_has_52_cards | `Deck()` | `len(cards)==52` |
| test_deck_all_unique | `Deck()` | `len(set(cards))==52` |
| test_deck_all_ranks | `Deck()` | `ranks=={3..14}` |
| test_deck_all_suits | `Deck()` | `suits=={0,1,2,3}` |
| test_deck_shuffle | `Deck().shuffle()` | 牌序改變 |
| test_deal_5_cards | `Deck().deal(5)` | 回傳5張，剩47張 |
| test_deal_multiple | `deck.deal(5)` then `deal(3)` | 剩44張 |
| test_deal_exceed | `Deck().deal(60)` | 回傳52張，剩0張 |

---

### 3. Hand 類別測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_hand_creation | `Hand([cards])` | `len==3` |
| test_hand_sort_desc | `Hand([3♣,♠A,♠3,♥K])` 排序 | `順序:♠A,♥K,♠3,♣3` |
| test_hand_find_3_clubs | `Hand([♠A,♣3,♦3])` | 回傳 `♣3` |
| test_hand_find_3_clubs_none | `Hand([♠A,♦3])` | 回傳 `None` |
| test_hand_remove | 移除指定牌 | 剩下1張 |
| test_hand_remove_not_found | 移除不存在牌 | 數量不變 |
| test_hand_iteration | `list(Hand([...]))` | 長度=2 |

---

### 4. Player 類別測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_player_human | `Player("Player1", False)` | `is_ai==False` |
| test_player_ai | `Player("AI_1", True)` | `is_ai==True` |
| test_player_take | `player.take_cards([cards])` | `len(hand)==2` |
| test_player_play | 出牌 | `hand減少，回傳出牌` |

---

## 實作測試代碼

```python
import unittest
from game.models import Card, Deck, Hand, Player

class TestModels(unittest.TestCase):
    def test_card_creation(self):
        # 測試 Card 初始化
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)
    
    def test_card_repr_ace(self):
        # 測試 ♠A 的表示
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three(self):
        # 測試 ♣3 的表示
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")
    
    def test_card_compare_suit(self):
        # 測試花色比較 ♠ > ♥
        spade_a = Card(14, 3)
        heart_a = Card(14, 2)
        self.assertTrue(spade_a > heart_a)
    
    def test_card_compare_suit_2(self):
        # 測試花色比較 ♥ > ♦
        heart_a = Card(14, 2)
        diamond_a = Card(14, 1)
        self.assertTrue(heart_a > diamond_a)
    
    def test_card_compare_suit_3(self):
        # 測試花色比較 ♦ > ♣
        diamond_a = Card(14, 1)
        club_a = Card(14, 0)
        self.assertTrue(diamond_a > club_a)
    
    def test_card_compare_rank_2(self):
        # 測試數字比較 2 > A
        two = Card(15, 0)
        ace = Card(14, 3)
        self.assertTrue(two > ace)
    
    def test_card_compare_rank_a(self):
        # 測試數字比較 A > K
        ace = Card(14, 0)
        king = Card(13, 3)
        self.assertTrue(ace > king)
    
    def test_card_compare_equal(self):
        # 測試相等比較
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertFalse(card1 > card2)
    
    def test_card_sort_key(self):
        # 測試排序鍵
        card = Card(14, 3)
        self.assertEqual(card.to_sort_key(), (14, 3))
    
    def test_deck_has_52_cards(self):
        # 測試牌組有52張牌
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_all_unique(self):
        # 測試所有牌唯一
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)
    
    def test_deck_all_ranks(self):
        # 測試所有數字
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        expected = set(range(3, 15)) | {15}
        self.assertEqual(ranks, expected)
    
    def test_deck_all_suits(self):
        # 測試所有花色
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})
    
    def test_deck_shuffle(self):
        # 測試洗牌
        deck = Deck()
        original = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original)
    
    def test_deal_5_cards(self):
        # 測試發5張牌
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)
    
    def test_deal_multiple(self):
        # 測試多次發牌
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)
    
    def test_deal_exceed(self):
        # 測試發超過牌數
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)
    
    def test_hand_creation(self):
        # 測試 Hand 初始化
        cards = [Card(3, 0), Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)
    
    def test_hand_sort_desc(self):
        # 測試排序
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        # 預期順序: ♠A (14,3), ♥K (13,2), ♠3 (3,3), ♣3 (3,0)
        expected = [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)]
        self.assertEqual(hand, expected)
    
    def test_hand_find_3_clubs(self):
        # 測試找3♣
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        found = hand.find_3_clubs()
        self.assertEqual(found, Card(3, 0))
    
    def test_hand_find_3_clubs_none(self):
        # 測試找不到3♣
        hand = Hand([Card(14, 3), Card(3, 1)])
        found = hand.find_3_clubs()
        self.assertIsNone(found)
    
    def test_hand_remove(self):
        # 測試移除牌
        hand = Hand([Card(3, 0), Card(14, 3)])
        hand.remove([Card(3, 0)])
        self.assertEqual(len(hand), 1)
        self.assertEqual(hand[0], Card(14, 3))
    
    def test_hand_remove_not_found(self):
        # 測試移除不存在牌
        hand = Hand([Card(3, 0), Card(14, 3)])
        hand.remove([Card(4, 0)])
        self.assertEqual(len(hand), 2)
    
    def test_hand_iteration(self):
        # 測試迭代
        hand = Hand([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(list(hand)), 2)
    
    def test_player_human(self):
        # 測試人類玩家
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)
    
    def test_player_ai(self):
        # 測試AI玩家
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)
    
    def test_player_take(self):
        # 測試拿牌
        player = Player("Player1")
        cards = [Card(3, 0), Card(14, 3)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)
    
    def test_player_play(self):
        # 測試出牌
        player = Player("Player1")
        player.take_cards([Card(3, 0), Card(14, 3)])
        played = player.play_cards([Card(3, 0)])
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(played, [Card(3, 0)])

if __name__ == '__main__':
    unittest.main()
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_models -v
```

---

## 預期結果

- **Red**: 所有測試失敗（類別未實作）
- **Green**: 實作後通過
- **Refactor**: 重構程式碼