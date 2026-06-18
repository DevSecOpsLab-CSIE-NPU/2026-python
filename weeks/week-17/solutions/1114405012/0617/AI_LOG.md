# AI_LOG.md — 0617 timeit + 搜尋效能評估

## 我問 AI 什麼

提示詞 1（任務一規格確認）：
> 我要寫一個 Python 裝飾器 `timeit`，放在 `timing.py`。規格：
> 支援 `@timeit` 和 `@timeit(repeat=5)` 兩種用法；被裝飾函式回傳值不變；
> `functools.wraps` 保留 metadata；每次呼叫跑 `repeat` 次，耗時 append 到
> `wrapper.records`；`last_elapsed` = 平均耗時；不准 print；`repeat < 1` raise ValueError。
> 請先反問我規格，不要直接給程式碼。

提示詞 2（edge case 決策）：
> repeat=1 時 records 長度應該是 1；有副作用的函式在 repeat=3 時會被執行 3 次，這是預期行為。

提示詞 3（任務二搜尋）：
> 寫 `search.py`：linear_search 逐一比對回傳 index；binary_search 前提已排序，
> 未排序行為靜默執行並寫進 docstring，不加前置排序檢查。

## AI 給了什麼

- 任務一：先反問了函式簽名、records 累積方式、last_elapsed 計算方式、edge case 處理、驗收標準五項；確認後給出裝飾器工廠結構（支援兩種呼叫語法）與完整測試骨架。
- 任務二：給出 linear_search（enumerate 逐一比對）和 binary_search（lo/hi 指標迴圈）的實作，未排序行為寫進模組 docstring。

---

## AI 反問我什麼 / 我怎麼回答

| # | AI 反問 | 我的決定 |
|---|---------|---------|
| 1 | `repeat` 取平均還是取最小值？ | 取平均，反映一般執行情況（含 OS 抖動），最小值只反映最佳 cache 狀態 |
| 2 | `records` 是每次呼叫重置，還是跨呼叫累積？ | 跨呼叫累積，讓使用者能觀察多次呼叫的分布 |
| 3 | 有副作用的函式 repeat=3 時，副作用被多算幾次？是 bug 還是 spec？ | 是 spec，預期行為，使用者必須意識到這點；測試裡用 docstring 說明 |
| 4 | `binary_search` 的未排序行為要拋例外還是靜默執行？ | 靜默執行，把責任交給呼叫者，docstring 寫清楚；加前置檢查反而多了 O(n) 成本 |
| 5 | `last_elapsed` 在多次呼叫後要反映「最後一次」還是「所有呼叫的平均」？ | 最後一次，all-time 平均可以從 `records` 自行計算 |

---

## 驗收紀錄

```
Ran 26 tests in 0.026s
OK
```

- test_timing.py：9 個 test case，全涵蓋規格 1-5 與 edge case
- test_search.py：17 個 test case，涵蓋空 list、邊界、重複元素、不修改 data

---

## 我改了什麼（相對於 starter）

- `test_timing.py`：補齊 4 個骨架測試 + 新增 5 個 edge case 測試，解除 `from timing import timeit` 的註解
- 新建 `timing.py`：實作支援兩種呼叫語法的裝飾器工廠
- 新建 `search.py`：linear_search（O(n)）和 binary_search（O(log n)），均不修改 data
- 新建 `test_search.py`：從零撰寫 17 個測試
- 新建 `README.md`：效能量測結果與評估（N=500,000，binary 快 ~1900×）

---

## 效能量測摘要

| 指標 | 數值 |
|------|------|
| N | 500,000 |
| linear_search 平均（repeat=5） | 7.58 ms |
| binary_search 平均（repeat=5） | 0.0039 ms |
| 加速比 | ~1,900× |
| sorted() 成本（N=500,000） | ~133 ms |
| linear 最壞情況 | ~51 ms |
| 排序+binary vs 1次linear | 133 ms vs 51 ms → 1次不划算 |

直覺：需要搜 **至少數十次** 才能攤平排序成本——精確交叉點明天 6/18 用數據量。
