# Phase 4: AI 策略 - 開發設計

## 目標

實作 AIStrategy 類別，使用貪心演算法選擇最佳出牌。

## 檔案位置

`game/ai.py`

---

## 類別設計

### AIStrategy 類別

```
常數：
  TYPE_SCORES = {
    SINGLE: 1, PAIR: 2, TRIPLE: 3,
    STRAIGHT: 4, FLUSH: 5, FULL_HOUSE: 6,
    FOUR_OF_A_KIND: 7, STRAIGHT_FLUSH: 8
  }
  
  EMPTY_HAND_BONUS = 10000
  NEAR_EMPTY_BONUS = 500
  SPADE_BONUS = 5

靜態方法：

  score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float
    評分公式：
    score = 牌型×100 + 數字×10 + 剩餘加分
    
    - 牌型分數 × 100
    - 數字分數 × 10  
    - 剩1張: +10000
    - 剩≤3張: +500
    - ♠牌: +5/張

  select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]
    貪心策略：
    1. 第一回合: 只能選3♣
    2. 其他: 選分數最高者
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ai -v
```

---

## 重構檢查清單

- [ ] 提取分數常數
- [ ] 考慮更複雜策略
- [ ] 效能優化
- [ ] 加入隨機性