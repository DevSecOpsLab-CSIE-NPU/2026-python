# Phase 5: 遊戲流程 - 開發設計

## 目標

實作 BigTwoGame 類別，控制完整遊戲流程。

## 檔案位置

`game/game.py`

---

## 類別設計

### BigTwoGame 類別

```
屬性：
  deck: Deck
  players: List[Player] (4位)
  current_player: int (0-3)
  last_play: Optional[Tuple[List[Card], str]]
  pass_count: int
  winner: Optional[Player]
  round_number: int

方法：

  setup() -> None
    - 建立牌堆、洗牌
    - 發13張牌給每位玩家
    - 找3♣決定先手
    - 初始化遊戲狀態

  play(player: Player, cards: List[Card]) -> bool
    - 檢查合法性
    - 移除手牌
    - 設定last_play
    - 檢查獲勝

  pass_(player: Player) -> bool
    - 玩家過牌
    - pass_count+1

  next_turn() -> None
    - current_player = (current+1) % 4

  _is_valid_play(cards: List[Card]) -> bool
    - 使用HandClassifier.can_play

  check_round_reset() -> None
    - pass_count>=3 時重置

  check_winner() -> Optional[Player]
    - 回傳手牌為空的玩家

  is_game_over() -> bool
    - winner is not None

  get_current_player() -> Player

  ai_turn() -> bool
    - AI自動回合
```

---

## 遊戲流程

```
初始化 → 回合循環 → 遊戲結束

回合循環：
  1. 取得當前玩家
  2. 如果是AI: ai_turn()
  3. 如果是人: 等待輸入
  4. 檢查回合重置
  5. 檢查獲勝
  6. 輪到下位
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_game -v
```

---

## 重構檢查清單

- [ ] 提取回合邏輯
- [ ] 加入遊戲記錄
- [ ] 支援暫停/恢復
- [ ] 加入計分系統