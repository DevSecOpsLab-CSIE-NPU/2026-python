# Phase 2: 牌型分類 - 開發設計

## 目標

實作 HandClassifier 類別，通過 Phase 2 的所有測試。

## 檔案位置

`game/classifier.py`

---

## 類別設計

### CardType 列舉

```
值：
  SINGLE = 1        # 單張
  PAIR = 2          # 對子
  TRIPLE = 3       # 三條
  STRAIGHT = 4      # 順子
  FLUSH = 5         # 同花
  FULL_HOUSE = 6    # 葫芦
  FOUR_OF_A_KIND = 7 # 四條
  STRAIGHT_FLUSH = 8 # 同花順
```

---

### HandClassifier 類別

```
靜態方法：

  _is_straight(ranks: List[int]) -> bool
    - 檢查是否為順子
    - 需處理 A-2-3-4-5 特殊情況

  _is_flush(suits: List[int]) -> bool
    - 檢查是否為同花

  classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]
    - 分類牌型
    - 回傳 (牌型, 數字, 花色) 或 None

  compare(play1: List[Card], play2: List[Card]) -> int
    - 比較兩手牌大小
    - 回傳 1=play1大, -1=play2大, 0=平手

  can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool
    - 檢查是否可以出牌
    - 第一回合只能出3♣
```

---

## 分類邏輯

```
輸入：cards 列表

1. n == 1: 單張
2. n == 2: 若rank相同=對子
3. n == 3: 若rank相同=三條
4. n == 5:
   - 檢查同花 + 順子 => 同花順
   - 檢查4張相同 => 四條
   - 檢查3+2 => 葫芦
   - 檢查同花 => 同花
   - 檢查順子 => 順子
5. 其他: None
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_classifier -v
```

---

## 重構檢查清單

- [ ] 提取 _is_straight 邏輯
- [ ] 提取 _count_ranks 方法
- [ ] 加入型別註解
- [ ] 效能優化