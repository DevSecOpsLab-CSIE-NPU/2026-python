# Phase 5: 遊戲流程 - 測試設計

## 目標

實作 BigTwoGame 類別，控制完整遊戲流程。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_game.py`

---

## 測試案例設計

### 1. 遊戲初始化

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_game_has_4_players | `game.setup()` | 4位玩家 |
| test_each_player_13_cards | setup後 | 每人13張 |
| test_total_cards_distributed | setup後 | 總共52張 |
| test_first_player_has_3_clubs | setup後 | 先手有3♣ |
| test_one_human_three_ai | setup後 | 1人3AI |

---

### 2. 出牌流程

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_play_removes_cards | 出牌 | 手牌-1 |
| test_play_sets_last_play | 出牌 | last_play設定 |
| test_invalid_play | 非法出牌 | 回傳False |
| test_pass_increments | 過牌 | pass_count+1 |

---

### 3. 回合判定

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_three_passes_resets | 3人過牌 | 重置last_play |
| test_turn_rotates | next_turn() | 輪到下家 |

---

### 4. 獲勝判定

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_detect_winner | 手牌空 | 回傳獲勝者 |
| test_no_winner_yet | 有牌 | 回傳None |
| test_game_ends | 有獲勝者 | is_game_over=True |

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_game -v
```

---

## 預期結果

- **Red**: 測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構