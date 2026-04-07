# Big Two Card Game - Complete Implementation

這是大貳紙牌遊戲的完整實現，包含所有6個階段的開發。

## 項目結構

```
HW/
├── game/              # 遊戲核心邏輯
│   ├── __init__.py
│   ├── models.py      # P1: 資料模型 (Card, Deck, Hand, Player)
│   ├── classifier.py  # P2: 手牌分類 (CardType, HandClassifier)
│   ├── finder.py      # P3: 手牌搜尋 (HandFinder)
│   ├── ai.py          # P4: AI 策略 (AIStrategy)
│   └── game.py        # P5: 遊戲流程 (BigTwoGame)
├── ui/                # 用戶介面
│   ├── __init__.py
│   ├── render.py      # P6: 渲染器 (Renderer)
│   ├── input.py       # P6: 輸入處理 (InputHandler)
│   └── app.py         # P6: 主應用程序 (BigTwoApp)
├── tests/             # 測試文件
├── main.py            # 主入口點
└── README.md          # 此文件
```

## 各階段說明

### P1: 資料模型 (models.py)
定義遊戲的基本數據結構：
- `Card`: 單張牌（花色 + 等級）
- `Suit`: 花色枚舉（♠♥♦♣ + 王牌）
- `Deck`: 54張牌的牌組（52張 + 2個王牌）
- `Hand`: 玩家的手牌
- `Player`: 玩家對象

### P2: 手牌分類 (classifier.py)
識別並分類牌型：
- `CardType`: 牌型枚舉（單張、對子、順子、同花、葫蘆、四條、同花順）
- `HandClassifier`: 手牌分類器
  - `classify()`: 分類手牌
  - `compare_hands()`: 比較兩手牌

### P3: 手牌搜尋 (finder.py)
尋找所有可能的出牌組合：
- `HandFinder`: 手牌搜尋器
  - `find_all_plays()`: 找出所有有效出牌
  - `get_best_play()`: 獲取最佳出牌
  - `has_valid_play()`: 檢查是否有可出牌

### P4: AI 策略 (ai.py)
AI 玩家的決策邏輯：
- `AIStrategy`: AI 策略引擎
  - `choose_play()`: 選擇最佳出牌
  - `evaluate_hand_strength()`: 評估手牌強度
  - `should_play_aggressively()`: 決定是否積極出牌

### P5: 遊戲流程 (game.py)
完整的遊戲邏輯控制：
- `GameState`: 遊戲狀態枚舉
- `BigTwoGame`: 主遊戲控制器
  - `start_game()`: 開始遊戲
  - `play_round()`: 進行一輪
  - `player_play()`: 處理玩家出牌
  - `get_valid_plays()`: 取得有效出牌

### P6: GUI (render.py, input.py, app.py)
圖形用戶介面：
- `Renderer`: 遊戲渲染引擎
  - 繪製遊戲板面
  - 顯示玩家手牌
  - 顯示遊戲狀態
- `InputHandler`: 用戶輸入處理
  - 處理滑鼠點擊
  - 處理鍵盤輸入
  - 卡牌選擇
- `BigTwoApp`: 主應用程序
  - 遊戲主循環
  - 集成所有組件

## 安裝依賴

```bash
pip install pygame
```

## 運行遊戲

```bash
python main.py
```

## 遊戲控制

- **滑鼠點擊**: 選擇/取消選擇手牌
- **空白鍵**: 提交出牌
- **P 鍵**: 跳過此回合
- **C 鍵**: 清除選擇
- **ESC 鍵**: 退出遊戲

## 遊戲截圖

### 遊戲進行中

```
+------ TABLE ------------------------------------------+
| Last Play: 17BJ (Big Joker - Highest Card)            |
+-------------------------------------------------------+

+------ PLAYERS ----------------------------------------+
| > You (Player)            [ACTIVE]     [5 cards]      |
| - Alice (AI)              [ACTIVE]     [7 cards]      |
| - Bob (AI)                [ACTIVE]     [6 cards]      |
| - Charlie (AI)            [OUT]        [0 cards]      |
+-------------------------------------------------------+

+------ YOUR HAND --------------------------------------+
| 3S  4H  5C  6D  9H  JC  QS  KH  AD                    |
+-------------------------------------------------------+

Selection: 3S, 4H (highlighted)
```

### 牌型識別演示

遊戲支持以下牌型的自動識別：

```
Single Card:    3S
Pair:          3S, 3H
Straight:      3S, 4H, 5D, 6C, 7H
Flush:         3S, 5S, 7S, 9S, JS
Full House:    3S, 3H, 3D, 5C, 5H
Four of Kind:  3S, 3H, 3D, 3C, 5H
Straight Flush: 3S, 4S, 5S, 6S, 7S
```

### 遊戲結束

```
===== GAME END =====

Winner: You!
Elimination Order:
  1. You (Winner!) - Finished at Round 5, Turn 28
  2. Alice       - Finished at Round 5, Turn 35
  3. Bob         - Finished at Round 6, Turn 12
  4. Charlie     - Eliminated (most cards left)

Game Statistics:
  Total Rounds Played: 6
  Average Turns Per Round: 7.8
```

詳細的遊戲截圖和演示見 [GAME_SCREENSHOT.txt](GAME_SCREENSHOT.txt)

## 遊戲規則

### 大貳基本規則

1. **參與人數**: 4 個玩家

2. **卡牌等級**:
   - 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A < 2
   - 王牌: 小王 < 大王

3. **花色大小**:
   - ♠ < ♥ < ♦ < ♣ < 小王 < 大王

4. **牌型**（按強度）：
   - 單張 (1 張)
   - 對子 (2 張相同等級)
   - 順子 (5 張連續等級)
   - 同花 (5 張相同花色)
   - 葫蘆 (3 張 + 2 張)
   - 四條 (4 張相同等級 + 1 張)
   - 同花順 (5 張連續相同花色)

5. **出牌規則**:
   - 首輪可出任何有效牌型
   - 之後的牌必須是相同牌型且更強
   - 3 個玩家連續跳過則該牌局結束

6. **勝利條件**:
   - 首先出完所有手牌的玩家獲勝

## 測試

測試文件位於 `tests/` 目錄。運行測試：

```bash
pytest tests/
```

或針對特定階段：

```bash
pytest tests/test_p1_models.py
pytest tests/test_p2_classifier.py
pytest tests/test_p3_finder.py
pytest tests/test_p4_ai.py
pytest tests/test_p5_game.py
pytest tests/test_p6_ui.py
```

## 設計特點

1. **模塊化架構**: 各階段獨立，易於擴展和測試
2. **完整的 AI**: 多層次的決策邏輯
3. **GUI 可視化**: 使用 Pygame 提供完整的遊戲界面
4. **靈活的遊戲引擎**: 支持人工玩家和 AI 混合對局

## 貢獻者

- 開發者: 蔡珽州 (1114405054)

## 許可證

MIT License
