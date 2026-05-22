# TEST LOG (Red -> Green)

## Red 階段

- 先建立測試案例（Task1: 5 個、Task2: 5 個），此時功能尚未完整，測試預期會失敗。
- 主要失敗點：
  - 尚未實作資料讀取與統計函式。
  - 尚未實作郵遞區號對照與 top N 邏輯。

## Green 階段

- 補齊 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py` 的函式。
- 修正 `DATA_DIR` 路徑（原本少往上層，導致找不到 `assets/stu-data/*.csv`）。
- 安裝繪圖依賴後重新執行，全部通過（10/10）。

## 測試指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 結果摘要

- Task1 測試：全部通過
- Task2 測試：全部通過
- 總計：10 個測試全綠

實際測試輸出：

```text
Ran 10 tests in 0.032s
OK
```
