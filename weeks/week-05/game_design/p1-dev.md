# Phase 1: 資料模型 - 開發設計

## 目標

實作 Card、Deck、Hand、Player 類別，通過 Phase 1 的所有測試。

## 檔案位置

`game/models.py`

---

## 類別設計

### Card 類別

```
屬性：
  - rank: int (3-14, 其中14=A, 15=2)
  - suit: int (0=♣,1=♦,2=♥,3=♠)

方法：
  - __init__(rank, suit): 初始化
  - __repr__(): 回傳 "♠A" 格式
  - __eq__(other): 比較相等
  - __lt__(other): 比較大小 (先比rank再比suit)
  - __hash__: 雜湊值
  - to_sort_key(): 回傳 (rank, suit) 元組
```

---

### Deck 類別

```
屬性：
  - cards: List[Card] (52張牌)

方法：
  - __init__(): 初始化52張牌
  - _create_cards(): 建立牌組
  - shuffle(): 洗牌
  - deal(n): 發n張牌，回傳List[Card]
```

---

### Hand 類別

```
繼承：list

方法：
  - __init__(cards=None): 初始化
  - sort_desc(): 排序（rank倒序,suit正序）
  - find_3_clubs(): 找3♣，回傳Card或None
  - remove(cards): 移除指定的牌
```

---

### Player 類別

```
屬性：
  - name: str
  - is_ai: bool
  - hand: Hand
  - score: int

方法：
  - __init__(name, is_ai=False): 初始化
  - take_cards(cards): 拿牌到手牌
  - play_cards(cards): 出牌，回傳出牌列表
```

---

## 比較邏輯

```
數字順序：2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
花色順序：♠ > ♥ > ♦ > ♣
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_models -v
```

---

## 重構檢查清單

- [ ] Card.__repr__ 使用類別屬性
- [ ] Deck._create_cards 提取為方法
- [ ] Hand.remove 處理不存在情況
- [ ] 加入型別註解 (type hints)