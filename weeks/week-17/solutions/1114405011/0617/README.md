# 0617 Search Evaluation

## 實作內容

- `timing.py`：`timeit` 裝飾器，支援 `repeat`（預設 3），每次呼叫會跑多次並記錄到 `records`，本次平均寫到 `last_elapsed`。
- `search.py`：`linear_search` 與 `binary_search`。`binary_search` 若收到未排序資料會 `raise ValueError`。

## 測試

```bash
python -m unittest -v test_timing.py
```

## 搜尋效能評估（粗略）

- 量測條件：`n = 200000`、`target = 199999`、`repeat = 5`，結果約為 `linear = 0.00946s`、`binary = 0.00000486s`、`sort = 0.05185s`。
- 單次查詢時，`binary_search` 明顯快於 `linear_search`；但如果資料原本未排序且只查一次，`排序 + binary`（約 `0.05185 + 0.00000486s`）比 linear（約 `0.00946s`）更慢。
- 直覺上，當同一批資料要查很多次時，排序成本能被攤提，`binary_search` 會變成更划算的策略。

> 補充：本作法將「未排序輸入」定義為未驗證前置條件，結果可能不正確；實際使用時應先保證資料已排序。
