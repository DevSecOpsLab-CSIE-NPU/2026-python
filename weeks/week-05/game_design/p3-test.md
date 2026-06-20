# Phase 3: 牌型搜尋 - 測試設計

## 目標

實作 HandFinder 類別，找出所有可能的牌型組合。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_finder.py`

---

## 測試案例設計

### 1. 單張搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_find_singles | `[♠A,♥K,♣3]` | 3個單張 |
| test_find_singles_empty | `[]` | 0個 |

---

### 2. 對子搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_find_pairs_one | `[♠A,♥A,♣3]` | 1個對子A |
| test_find_pairs_two | `[♠A,♥A,♠K,♣K]` | 2個對子 |
| test_find_pairs_none | `[♠A,♥K,♣3]` | 0個 |

---

### 3. 三條搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_find_triples_one | `[♠A,♥A,♦A,♣3]` | 1個三條A |
| test_find_triples_with_extra | `[AAA,KK]` | 1個 |

---

### 4. 五張牌型搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_find_straight | 有順子牌型 | 有順子 |
| test_find_flush | 有同花牌型 | 有同花 |
| test_find_full_house | 有葫芦牌型 | 有葫芦 |
| test_find_four_of_a_kind | 有四條牌型 | 有四條 |
| test_find_straight_flush | 有同花順牌型 | 有同花順 |

---

### 5. 合法出牌搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_first_turn | hand有3♣, last=None | 只能出3♣ |
| test_with_last_single | last=單5 | 只回單張 |
| test_with_last_pair | last=對5 | 只回對子 |
| test_no_valid | 無法大於上家 | 空清單 |

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_finder -v
```

---

## 預期結果

- **Red**: 測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構