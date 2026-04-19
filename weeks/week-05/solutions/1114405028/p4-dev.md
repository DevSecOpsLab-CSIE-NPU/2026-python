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

## 實作代碼

```python
from typing import List, Optional
from game.models import Card, Hand
from game.classifier import CardType, HandClassifier

class AIStrategy:
    TYPE_SCORES = {
        CardType.SINGLE: 1, 
        CardType.PAIR: 2, 
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4, 
        CardType.FLUSH: 5, 
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7, 
        CardType.STRAIGHT_FLUSH: 8
    }
    
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5
    
    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        # 評分出牌
        type_info = HandClassifier.classify(cards)
        if type_info is None:
            return 0
        
        card_type, rank, suit = type_info
        
        # 牌型分數 × 100
        score = AIStrategy.TYPE_SCORES[card_type] * 100
        
        # 數字分數 × 10
        score += rank * 10
        
        # 剩餘手牌加分
        remaining = len(hand) - len(cards)
        if remaining == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS
        
        # ♠牌加分
        spade_count = sum(1 for c in cards if c.suit == 3)
        score += spade_count * AIStrategy.SPADE_BONUS
        
        return score
    
    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        # 貪心選擇最佳出牌
        if not valid_plays:
            return None
        
        if is_first:
            # 第一回合，只能選3♣
            for play in valid_plays:
                if len(play) == 1 and play[0] == Card(3, 0):
                    return play
            return None
        
        # 選分數最高
        best_play = None
        best_score = -1
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand)
            if score > best_score:
                best_score = score
                best_play = play
        
        return best_play
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