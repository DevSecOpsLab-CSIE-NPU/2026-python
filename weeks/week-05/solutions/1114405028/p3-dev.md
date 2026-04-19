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

## 實作代碼

```python
from typing import List, Optional
from itertools import combinations
from game.models import Card, Hand
from game.classifier import HandClassifier

class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        # 回傳所有單張牌的列表
        return [[card] for card in hand]
    
    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        # 找所有對子組合
        pairs = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                # 使用 combinations 產生所有2張組合
                for pair in combinations(cards, 2):
                    pairs.append(list(pair))
        return pairs
    
    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        # 找所有三條組合
        triples = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                # 使用 combinations 產生所有3張組合
                for triple in combinations(cards, 3):
                    triples.append(list(triple))
        return triples
    
    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        # 找所有五張牌型
        fives = []
        # 找順子
        for start in range(3, 11):  # 3 to 10 for straight
            straight = HandFinder._find_straight_from(hand, start)
            if straight:
                fives.append(straight)
        # A-2-3-4-5 straight
        ace_low = HandFinder._find_straight_from(hand, 14)  # special for A2345
        if ace_low:
            fives.append(ace_low)
        
        # 其他五張牌型可以類似實作，但這裡簡化
        return fives
    
    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        # 從指定 rank 找順子
        needed_ranks = [start_rank + i for i in range(5)]
        if start_rank == 14:  # A2345
            needed_ranks = [14, 15, 3, 4, 5]
        
        rank_to_cards = {}
        for card in hand:
            if card.rank not in rank_to_cards:
                rank_to_cards[card.rank] = []
            rank_to_cards[card.rank].append(card)
        
        selected = []
        for rank in needed_ranks:
            if rank not in rank_to_cards:
                return None
            selected.append(rank_to_cards[rank][0])  # 取第一張
        
        return selected
    
    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        # 根據上家牌型，回傳所有合法出牌
        if last_play is None:
            # 第一回合，只能出3♣
            three_clubs = hand.find_3_clubs()
            if three_clubs:
                return [[three_clubs]]
            return []
        
        last_type = HandClassifier.classify(last_play)
        if last_type is None:
            return []
        
        valid_plays = []
        if last_type[0].name == 'SINGLE':
            singles = HandFinder.find_singles(hand)
            for play in singles:
                if HandClassifier.can_play(last_play, play):
                    valid_plays.append(play)
        elif last_type[0].name == 'PAIR':
            pairs = HandFinder.find_pairs(hand)
            for play in pairs:
                if HandClassifier.can_play(last_play, play):
                    valid_plays.append(play)
        # 類似 for other types
        
        return valid_plays
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