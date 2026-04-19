# 赤壁戰役 - 測試執行日誌

## Stage 1: 資料讀取 (RED -> GREEN)

### RED
- 初始尚未實作 `load_generals`，資料讀取測試失敗。

### GREEN
- 實作檔案 I/O 與 EOF 結尾判斷。
- 建立 `General` namedtuple 並完成欄位型別轉換。

## Stage 2: 戰鬥邏輯 (GREEN)

- 實作 `get_battle_order` 速度排序。
- 實作 `calculate_damage` 並結合 `Counter`、`defaultdict`。
- 實作三波戰鬥、傷害排名、勢力統計、戰敗名單。

## Stage 3: 重構與報告 (REFACTOR)

- 增加 ASCII 開場與統計報表方法。
- 確保報表方法不改變統計資料。

## 最終測試結果

以下為本次在 `solution` 目錄執行結果摘要：

```text
Ran 16 tests in 0.013s
OK
```

- 總測試數: 16
- 失敗數: 0
- 結論: 全部通過
