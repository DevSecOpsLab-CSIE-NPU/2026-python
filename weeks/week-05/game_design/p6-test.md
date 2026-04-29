# Phase 6: GUI - 測試設計

## 目標

實作 Pygame GUI，提供視覺化遊戲介面。

## 測試方式

整合測試 + 手動測試

## 測試檔案

`tests/test_ui.py`

---

## 測試案例設計

### 1. 渲染測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_card_render | Card(♠A) | surface寬度>0 |
| test_hand_render | Hand有3張牌 | surface正常 |

---

### 2. 整合測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_game_init | BigTwoApp() | 4位玩家 |
| test_card_selection | 點擊座標 | 正確轉換 |
| test_button_click | 點擊按鈕區 | 正確回應 |

---

### 3. E2E 測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_complete_flow | 模擬完整遊戲 | 遊戲正確結束 |

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ui -v
```

---

## 備註

- GUI 測試主要依賴手動測試
- 使用 mock 隔離 pygame 依賴