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