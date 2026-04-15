# Big Two Card Game - 完整實作

## 項目簡介

根據週 5 的遊戲設計文檔，完整實作 Big Two (鋤大弟) 紙牌遊戲，包括資料模型、牌型分類、搜尋、AI 策略、遊戲流程與 GUI。

## 專案結構

```
4488/
├── game/
│   ├── __init__.py
│   ├── models.py          # Phase 1: 資料模型
│   ├── classifier.py      # Phase 2: 牌型分類
│   ├── finder.py          # Phase 3: 牌型搜尋
│   ├── ai.py              # Phase 4: AI 策略
│   └── game.py            # Phase 5: 遊戲流程
├── ui/
│   ├── __init__.py
│   ├── render.py          # Phase 6: 渲染器
│   ├── input.py           # Phase 6: 輸入處理
│   └── app.py             # Phase 6: 應用主體
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_classifier.py
│   ├── test_finder.py
│   ├── test_ai.py
│   ├── test_game.py
│   └── test_ui.py
├── main.py                # 遊戲入口
└── README.md
```

## 執行方式

### 執行測試

```bash
cd 4488
python -m unittest discover -s tests -p "test_*.py" -v
```

### 執行遊戲

```bash
cd 4488
pip install pygame
python main.py
```

## Phase 說明

### Phase 1: 資料模型 (models.py)
- **Card**: 單張牌，含 rank (3-15) 和 suit (0-3)
- **Deck**: 含 52 張牌，支援洗牌和發牌
- **Hand**: 玩家手牌，支援排序、搜尋和移除
- **Player**: 玩家物件，管理手牌和分數

### Phase 2: 牌型分類 (classifier.py)
- **CardType 列舉**: 8 種牌型 (單張到同花順)
- **HandClassifier**: 
  - 分類牌組（單張、對子、三條、五張牌型等）
  - 比較兩手牌大小
  - 檢查出牌是否合法

### Phase 3: 牌型搜尋 (finder.py)
- **HandFinder**: 搜尋所有可用牌型
  - find_singles: 尋找所有單張
  - find_pairs: 尋找所有對子
  - find_triples: 尋找所有三條
  - find_fives: 尋找所有五張牌型
  - get_all_valid_plays: 取得該回合所有合法出牌

### Phase 4: AI 策略 (ai.py)
- **AIStrategy**: 貪心演算法選擇最佳出牌
  - score_play: 評分出牌 (牌型分 + 數字分 + 剩餘加分)
  - select_best: 選擇分數最高的出牌

### Phase 5: 遊戲流程 (game.py)
- **BigTwoGame**: 管理完整遊戲流程
  - setup: 初始化遊戲、發牌、決定先手
  - play: 執行出牌
  - pass_: 執行過牌
  - ai_turn: 執行 AI 回合
  - check_winner: 檢查獲勝者

### Phase 6: GUI (ui/render.py, input.py, app.py)
- **Renderer**: 使用 pygame 繪製牌面和介面
- **InputHandler**: 處理마우스和鍵盤輸入
- **BigTwoApp**: 主應用程式，管理遊戲迴圈

## 核心特性

1. **完整資料模型**: 牌、牌堆、手牌、玩家
2. **準確的牌型判定**: 支援所有 8 種牌型，含特殊情況 (A-2-3-4-5 順子)
3. **靈活的搜尋演算法**: 快速找出所有可用牌型組合
4. **智能 AI 策略**: 考慮牌型、數字、剩餘手牌數和花色加分
5. **完整遊戲流程**: 初始化、輪次、過牌重置、獲勝判定
6. **視覺化 GUI**: Pygame 介面，支援滑鼠和鍵盤操作

## 測試涵蓋

- **Phase 1**: Card、Deck、Hand、Player 建立和操作
- **Phase 2**: 牌型分類、比較、合法性檢查
- **Phase 3**: 單張、對子、三條、五張牌型搜尋
- **Phase 4**: AI 評分和選擇
- **Phase 5**: 遊戲初始化、出牌、過牌、獲勝判定
- **Phase 6**: UI 模組可靠性

## 執行環境

- Python 3.8+
- pygame (可選，用於 GUI)

## 執行結果

所有測試應通過，遊戲應可正常進行。
