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