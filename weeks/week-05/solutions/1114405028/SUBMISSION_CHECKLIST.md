# Week 05 - Phase 1 提交清單

## 學號：1114405028

## 提交文件

### 核心代碼

- [x] `game/models.py` - Card、Deck、Hand、Player 實現（221 行）
- [x] `game/__init__.py` - 模組初始化

### 測試代碼

- [x] `tests/test_models.py` - 29 個單元測試
- [x] `tests/__init__.py` - 測試模組初始化

### 文檔

- [x] `README.md` - 提交說明和實現清單
- [x] `TEST_RESULTS.txt` - 測試執行結果
- [x] `SUBMISSION_CHECKLIST.md` - 本清單

## 測試統計

| 項目 | 數值 |
|------|------|
| 總測試數 | 29 |
| 通過 | 29 ✅ |
| 失敗 | 0 |
| 執行時間 | 0.003s |
| 成功率 | 100% |

## 實現統計

| 類別 | 方法數 | 測試數 | 狀態 |
|------|--------|--------|------|
| Card | 9 | 10 | ✅ |
| Deck | 4 | 8 | ✅ |
| Hand | 4 | 7 | ✅ |
| Player | 3 | 4 | ✅ |
| **總計** | **20** | **29** | **✅** |

## 代碼品質檢查

- [x] 型別註解完整
- [x] 文檔字符串完整
- [x] 中文註解清晰
- [x] PEP 8 規範
- [x] 無語法錯誤
- [x] 所有測試通過

## 快速開始

### 運行測試

```bash
cd 1114405028
python -m unittest tests.test_models -v
```

### 使用範例

```python
from game.models import Card, Deck, Hand, Player

# 創建卡牌
card = Card(rank=14, suit=3)  # ♠A
print(card)  # 輸出：♠A

# 創建牌組
deck = Deck()
deck.shuffle()

# 發牌
cards = deck.deal(5)

# 創建玩家
player = Player("Alice", is_ai=False)
player.take_cards(cards)

# 出牌
played = player.play_cards(cards[:2])
```

## 提交說明

- **實現日期**：2026-03-26
- **版本**：1.0
- **完成度**：100%（Phase 1）
- **下一步**：Phase 2 - 遊戲規則

---

提交者：1114405028
