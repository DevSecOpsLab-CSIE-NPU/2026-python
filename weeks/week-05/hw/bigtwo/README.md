# Big Two Card Game (大貳紙牌遊戲)

一個用 Python 實現的大貳撲克牌遊戲，包含完整的遊戲邏輯、AI 策略和 Pygame GUI 介面。

## 專案結構

```
bigtwo/
├── game/                    # 遊戲邏輯核心
│   ├── __init__.py
│   ├── models.py           # Phase 1: 資料模型 (Card, Deck, Hand, Player)
│   ├── classifier.py       # Phase 2: 牌型分類 (HandClassifier)
│   ├── finder.py          # Phase 3: 牌型搜尋 (HandFinder)
│   ├── ai.py              # Phase 4: AI 策略 (AIStrategy)
│   └── game.py            # Phase 5: 遊戲流程 (BigTwoGame)
│
├── ui/                      # GUI 使用者介面
│   ├── __init__.py
│   ├── render.py          # Phase 6: 渲染器 (Renderer)
│   ├── input.py           # Phase 6: 輸入處理 (InputHandler)
│   └── app.py             # Phase 6: 主應用 (BigTwoApp)
│
├── tests/                   # 單元測試
│   ├── __init__.py
│   ├── test_models.py     # Phase 1 測試
│   ├── test_classifier.py # Phase 2 測試
│   ├── test_finder.py     # Phase 3 測試
│   ├── test_ai.py         # Phase 4 測試
│   └── test_game.py       # Phase 5 測試
│
├── main.py                  # 程式入口
└── README.md               # 本檔案
```

## 功能特性

### Phase 1: 資料模型
- **Card**: 表示單張撲克牌
  - 42 種牌（3-15 rank，4 種 suit）
  - 支援大小比較
  
- **Deck**: 42 張牌的牌堆
  - 洗牌、發牌功能
  
- **Hand**: 玩家的手牌（繼承 list）
  - 排序、查找特定牌（如 3♣）
  
- **Player**: 玩家角色
  - 支援人類玩家和 AI 玩家

### Phase 2: 牌型分類
- 8 種牌型：單張、對子、三條、順子、同花、葫蘆、四條、同花順
- 牌型比較：自動判定大小關係
- 合法性檢查：驗證是否可以出牌

### Phase 3: 牌型搜尋
- 自動尋找所有可能的單張、對子、三條
- 複雜搜尋：找出所有合法的 5 張牌型組合
- 獲取合法出牌：根據上家牌型列出所有可行選擇

### Phase 4: AI 策略
- 貪心演算法：評分系統選擇最佳出牌
- 考慮因素：牌型、數字大小、剩餘牌數、花色
- 玩家有趣且有競爭力

### Phase 5: 遊戲流程
- 完整的回合管理系統
- 獲勝判定和計分
- AI 自動執行回合

### Phase 6: GUI 介面
- Pygame 視覺化介面
- 實時顯示所有玩家手牌
- 滑鼠點擊選牌，按鍵出牌或過牌
- 遊戲結束通知

## 遊戲規則

### 基本規則
- 4 位玩家（1 人 3 AI）
- 每位玩家發 13 張牌
- 誰先出完牌誰贏

### 牌的大小順序
**數字順序**: 2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
**花色順序**: ♠ > ♥ > ♦ > ♣

### 牌型規則（由小到大）
1. 單張
2. 對子
3. 三條
4. 順子 (5 張連續)
5. 同花 (5 張同花色)
6. 葫蘆 (3 張相同 + 2 張相同)
7. 四條 (4 張相同 + 1 張任意)
8. 同花順 (5 張連續同花色)

### 出牌規則
- 第一回合：只能出 3♣
- 其他回合：
  - 可以出相同牌數但更大的同類牌型
  - 可以升級到更大的牌型（如用對子蓋單張）
  - 無法出牌時可過牌
  - 連續 3 人過牌後，上家出牌重置

## 安裝與執行

### 前置需求
- Python 3.7+
- pygame

### 安裝
```bash
pip install pygame
```

### 執行遊戲
```bash
cd bigtwo
python main.py
```

### 執行測試
```bash
cd bigtwo
# 執行所有測試
python -m unittest discover tests -v

# 執行特定測試
python -m unittest tests.test_models -v
python -m unittest tests.test_classifier -v
python -m unittest tests.test_finder -v
python -m unittest tests.test_ai -v
python -m unittest tests.test_game -v
```

## 遊戲操作

### 人類玩家操作
| 操作 | 按鍵/滑鼠 |
|------|---------|
| 選擇牌 | 點擊牌 (重複點擊可取消) |
| 出牌 | 按 Enter 或點擊 "Play" 按鈕 |
| 過牌 | 按 P 或點擊 "Pass" 按鈕 |
| 重新開始 | 按 R (遊戲結束時) |
| 退出 | 按 Esc |

## 設計模式

### MVC 架構
- **Model**: `game/` 模塊 - 遊戲邏輯和狀態
- **View**: `ui/render.py` - 視覺呈現
- **Controller**: `ui/input.py` - 使用者輸入處理

### 物件導向設計
- 清晰的類別職責劃分
- 靜態方法用於無狀態邏輯
- 容易擴展和測試

## 代碼指標

- **總行數**: ~1,300 行
- **單元測試覆蓋**: Phase 1-5
- **複雜度**: 低-中等（適合學習）

## 改進方向

- [ ] 加入聲音和動畫效果
- [ ] 實現更複雜的 AI 策略
- [ ] 多人線上模式
- [ ] 遊戲記錄和統計
- [ ] 設置和主選單

## 授權

此專案為教學用途，歡迎修改和使用。

---

**製作日期**: 2026 年 4 月
**版本**: 1.0
