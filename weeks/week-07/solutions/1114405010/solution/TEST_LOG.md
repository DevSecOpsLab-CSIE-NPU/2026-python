# 赤壁戰役 - 測試執行日誌

## Stage 1: 資料讀取

### RED
- 初始尚未實作 load_generals，測試失敗。

### GREEN
- 實作檔案讀取與 EOF 終止。
- 4 個 Stage 1 測試通過。

## Stage 2: 戰鬥模擬

### GREEN
- 實作速度排序、傷害計算、Counter 與 defaultdict 統計。
- 9 個 Stage 2 測試通過。

## Stage 3: 重構與視覺化

### REFACTOR
- 新增 ASCII 報表輸出，不改變統計結果。
- 所有測試維持通過。

## 最終結果
- python -m pytest solution/test_chibi.py -v
- 15 tests passed, 0 failed
