# Phase 3: 牌型搜尋 - 開發設計

## 目標

實作 HandFinder 類別，通過 Phase 3 的所有測試。

## 檔案位置

`game/finder.py`

---

## 類別設計

### HandFinder 類別

```
靜態方法：

  find_singles(hand: Hand) -> List[List[Card]]
    - 回傳 [[card1], [card2], ...]

  find_pairs(hand: Hand) -> List[List[Card]]
    - 使用 combinations 找相同 rank 的2張組合

  find_triples(hand: Hand) -> List[List[Card]]
    - 使用 combinations 找相同 rank 的3張組合

  find_fives(hand: Hand) -> List[List[Card]]
    - 找順子、同花、葫芦、四條、同花順

  _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]
    - 從指定 rank 找順子

  get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]
    - 根據上家的牌型，回傳所有合法出牌
```

---

## 演算法重點

### 找對子
```
1. 對每個 rank (3-14)
2. 找相同 rank 的牌
3. 使用 combinations(相同牌, 2) 產生所有組合
```

### 找順子
```
1. 對每個 rank 開始
2. 檢查是否有 5 張連續的牌
3. 處理 A-2-3-4-5 特殊情況
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_finder -v
```

---

## 重構檢查清單

- [ ] 優化順子搜尋演算法
- [ ] 減少重複計算
- [ ] 考慮使用生成器
- [ ] 效能優化