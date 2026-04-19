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

## 實作代碼

```python
from typing import List, Optional, Tuple
from game.models import Deck, Player, Card
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy

class BigTwoGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1
    
    def setup(self) -> None:
        # 建立4位玩家
        self.players = [Player(f"Player{i+1}", is_ai=(i > 0)) for i in range(4)]
        
        # 洗牌
        self.deck.shuffle()
        
        # 發13張牌
        for _ in range(13):
            for player in self.players:
                cards = self.deck.deal(1)
                player.take_cards(cards)
        
        # 排序手牌
        for player in self.players:
            player.hand.sort_desc()
        
        # 找3♣決定先手
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                self.current_player = i
                break
        
        # 初始化狀態
        self.last_play = None
        self.pass_count = 0
        self.winner = None
    
    def play(self, player: Player, cards: List[Card]) -> bool:
        # 出牌
        if not self._is_valid_play(cards):
            return False
        
        # 移除手牌
        player.play_cards(cards)
        
        # 設定last_play
        self.last_play = (cards, player.name)
        self.pass_count = 0
        
        # 檢查獲勝
        if len(player.hand) == 0:
            self.winner = player
        
        return True
    
    def pass_(self, player: Player) -> bool:
        # 過牌
        self.pass_count += 1
        return True
    
    def next_turn(self) -> None:
        # 下一位
        self.current_player = (self.current_player + 1) % 4
    
    def _is_valid_play(self, cards: List[Card]) -> bool:
        # 檢查合法性
        return HandClassifier.can_play(self.last_play[0] if self.last_play else None, cards)
    
    def check_round_reset(self) -> None:
        # pass_count >=3 時重置
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1
    
    def check_winner(self) -> Optional[Player]:
        # 檢查獲勝
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None
    
    def is_game_over(self) -> bool:
        # 遊戲結束
        return self.winner is not None
    
    def get_current_player(self) -> Player:
        # 當前玩家
        return self.players[self.current_player]
    
    def ai_turn(self) -> bool:
        # AI回合
        player = self.get_current_player()
        valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play[0] if self.last_play else None)
        best_play = AIStrategy.select_best(valid_plays, player.hand, self.last_play is None)
        
        if best_play:
            return self.play(player, best_play)
        else:
            return self.pass_(player)
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