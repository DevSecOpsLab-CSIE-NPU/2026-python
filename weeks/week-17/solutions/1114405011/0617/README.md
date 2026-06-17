# 0617 Search Evaluation

## 實作內容

- `timing.py`：`timeit` 裝飾器，支援 `repeat`（預設 3），每次呼叫會跑多次並將每輪耗時 `append` 記錄到 `records`（不重設，跨呼叫持續累積），本次呼叫的平均耗時則寫到 `last_elapsed`。裝飾器內部不進行 `print`，且當 `repeat < 1` 時會明確 `raise ValueError`。
- `search.py`：包含 `linear_search` 與 `binary_search`。兩者皆不可修改傳入的 `data`。基於效能考量，`binary_search` 不會主動驗證輸入資料是否排序；若收到未排序資料，其行為與回傳結果為未定義（Undefined Behavior）。

## 測試

```bash
python -m unittest -v test_timing.py