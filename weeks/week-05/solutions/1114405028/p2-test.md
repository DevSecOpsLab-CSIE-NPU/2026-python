# Phase 2: 牌型分類 - 測試設計

## 目標

實作 HandClassifier 類別，正確分類並比較牌型。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_classifier.py`

---

## 前置條件

已完成 Phase 1：Card, Deck, Hand, Player

---

## 測試案例設計

### 1. CardType 列舉測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_cardtype_values | 各牌型enum值 | SINGLE=1, PAIR=2, TRIPLE=3, STRAIGHT=4, FLUSH=5, FULL_HOUSE=6, FOUR_OF_A_KIND=7, STRAIGHT_FLUSH=8 |

---

### 2. 單張分類測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_classify_single_ace | `[♠A]` | `(SINGLE, 14, 3)` |
| test_classify_single_two | `[2♣]` | `(SINGLE, 15, 0)` |
| test_classify_single_three | `[♣3]` | `(SINGLE, 3, 0)` |

---

### 3. 對子分類測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_classify_pair | `[♠A,♥A]` | `(PAIR, 14, 0)` |
| test_classify_pair_diff_rank | `[♠A,♠K]` | `None` |
| test_classify_pair_from_three | `[♠A,♥A,♦A]` 取2張 | `(PAIR, 14, 0)` |

---

### 4. 三條分類測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_classify_triple | `[♠A,♥A,♦A]` | `(TRIPLE, 14, 0)` |
| test_classify_triple_not_enough | `[♠A,♥A]` | `None` |

---

### 5. 五張牌型分類測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_classify_straight | `[3♣,4♦,5♥,6♠,7♣]` | `(STRAIGHT, 7, 0)` |
| test_classify_straight_ace_low | `[A♣,2♦,3♥,4♠,5♣]` | `(STRAIGHT, 5, 0)` |
| test_classify_flush | `[♣3,♣5,♣7,♣9,♣J]` | `(FLUSH, 11, 0)` |
| test_classify_full_house | `[♠A,♥A,♦A,♣2,♦2]` | `(FULL_HOUSE, 14, 0)` |
| test_classify_four_of_a_kind | `[♠A,♥A,♦A,♣A,♦3]` | `(FOUR_OF_A_KIND, 14, 0)` |
| test_classify_straight_flush | `[♣3,♣4,♣5,♣6,♣7]` | `(STRAIGHT_FLUSH, 7, 0)` |

---

### 6. 牌型比較測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_compare_single_rank | `♠A` vs `♠K` | `1` (A>K) |
| test_compare_single_suit | `♠A` vs `♥A` | `1` (♠>♥) |
| test_compare_pair_rank | `對A` vs `對K` | `1` |
| test_compare_pair_suit | `♠♥A` vs `♦♣A` | `1` |
| test_compare_different_type | `對子` vs `單張` | `1` |
| test_compare_flush_vs_straight | 同花 vs 順子 | `1` |

---

### 7. 合法性檢查測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_can_play_first_3clubs | `None`, `[♣3]` | `True` |
| test_can_play_first_not_3clubs | `None`, `[♠A]` | `False` |
| test_can_play_same_type | 對5 vs 對6 | `True` |
| test_can_play_diff_type | 對5 vs 單張6 | `False` |
| test_can_play_not_stronger | 對10 vs 對5 | `False` |

---

## 實作測試代碼

```python
import unittest
from game.models import Card
from game.classifier import CardType, HandClassifier

class TestClassifier(unittest.TestCase):
    def test_cardtype_values(self):
        # 測試 CardType 列舉值
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)
    
    def test_classify_single_ace(self):
        # 測試單張 A
        cards = [Card(14, 3)]  # ♠A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 14, 3))
    
    def test_classify_single_two(self):
        # 測試單張 2
        cards = [Card(15, 0)]  # 2♣
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 15, 0))
    
    def test_classify_single_three(self):
        # 測試單張 3
        cards = [Card(3, 0)]  # ♣3
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 3, 0))
    
    def test_classify_pair(self):
        # 測試對子
        cards = [Card(14, 3), Card(14, 2)]  # ♠A, ♥A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.PAIR, 14, 3))  # max suit ♠
    
    def test_classify_pair_diff_rank(self):
        # 測試不同數字
        cards = [Card(14, 3), Card(13, 3)]  # ♠A, ♠K
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_classify_triple(self):
        # 測試三條
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]  # ♠A, ♥A, ♦A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.TRIPLE, 14, 3))  # max suit ♠
    
    def test_classify_triple_not_enough(self):
        # 測試三條不夠
        cards = [Card(14, 3), Card(14, 2)]  # ♠A, ♥A
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_classify_straight(self):
        # 測試順子
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 7, 3))  # max rank 7, max suit ♠
    
    def test_classify_straight_ace_low(self):
        # 測試 A-2-3-4-5 順子
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 5, 3))  # max rank 5, max suit ♠
    
    def test_classify_flush(self):
        # 測試同花
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]  # all ♣
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FLUSH, 11, 0))  # max rank J=11
    
    def test_classify_full_house(self):
        # 測試葫芦
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]  # AAA22
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FULL_HOUSE, 14, 3))  # three A, max suit ♠
    
    def test_classify_four_of_a_kind(self):
        # 測試四條
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]  # AAAA3
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FOUR_OF_A_KIND, 14, 3))  # four A, max suit ♠
    
    def test_classify_straight_flush(self):
        # 測試同花順
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]  # ♣3-7
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT_FLUSH, 7, 0))
    
    def test_compare_single_rank(self):
        # 比較單張數字
        play1 = [Card(14, 3)]  # ♠A
        play2 = [Card(13, 3)]  # ♠K
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_single_suit(self):
        # 比較單張花色
        play1 = [Card(14, 3)]  # ♠A
        play2 = [Card(14, 2)]  # ♥A
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_pair_rank(self):
        # 比較對子數字
        play1 = [Card(14, 3), Card(14, 2)]  # ♠♥A
        play2 = [Card(13, 3), Card(13, 2)]  # ♠♥K
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_different_type(self):
        # 比較不同牌型
        play1 = [Card(14, 3), Card(14, 2)]  # 對A
        play2 = [Card(15, 3)]  # 單2
        self.assertEqual(HandClassifier.compare(play1, play2), 1)  # PAIR > SINGLE
    
    def test_can_play_first_3clubs(self):
        # 第一回合出3♣
        cards = [Card(3, 0)]
        self.assertTrue(HandClassifier.can_play(None, cards))
    
    def test_can_play_first_not_3clubs(self):
        # 第一回合不出3♣
        cards = [Card(14, 3)]
        self.assertFalse(HandClassifier.can_play(None, cards))
    
    def test_can_play_same_type(self):
        # 同牌型，且更大
        last = [Card(5, 3), Card(5, 2)]  # 對5
        current = [Card(6, 3), Card(6, 2)]  # 對6
        self.assertTrue(HandClassifier.can_play(last, current))
    
    def test_can_play_diff_type(self):
        # 不同牌型
        last = [Card(5, 3), Card(5, 2)]  # 對5
        current = [Card(6, 3)]  # 單6
        self.assertFalse(HandClassifier.can_play(last, current))
    
    def test_can_play_not_stronger(self):
        # 同牌型，但不大
        last = [Card(10, 3), Card(10, 2)]  # 對10
        current = [Card(5, 3), Card(5, 2)]  # 對5
        self.assertFalse(HandClassifier.can_play(last, current))

if __name__ == '__main__':
    unittest.main()
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_classifier -v
```

---

## 預期結果

- **Red**: 所有測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構