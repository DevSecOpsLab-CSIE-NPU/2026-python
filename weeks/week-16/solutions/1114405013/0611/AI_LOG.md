# AI_LOG

## Stage 1：timeit 裝飾器

我先問 AI 要怎麼把 `timeit` 題目拆成測試。AI 建議至少測回傳值不變、函式名稱和說明文字要保留、要記錄執行時間、不能直接印出東西。

我先寫 `test_timing.py`，一開始因為還沒有 `timing.py`，所以測試紅燈。後來我再寫 `timing.py`，用 `functools.wraps` 保留函式資訊，用 `time.perf_counter()` 計時，並把時間存到 `last_elapsed` 和 `records`。

驗收方式：

```text
python -m unittest test_timing
```

## Stage 2：三種排序和 benchmark

我問 AI 三個排序要怎麼測。AI 提醒我要用同一組測試跑 `bubble_sort`、`quick_sort`、`merge_sort`，而且要確認排序後有回傳新的 list，不能改到原本的 list。

我新增 `test_sorts.py`，測空 list、單一元素、已排序、反向排序、重複數字、負數和隨機資料。紅燈後再寫 `sorts.py` 和 `benchmark.py`，並產生 `results.json`。

驗收方式：

```text
python -m unittest test_sorts test_timing
python benchmark.py
```

## Stage 3：加速實驗

我問 AI 目前是用什麼方式加速。這次沒有用 Cython，而是用演算法優化。

主要加速的是 `quick_sort_fast`：

- pivot 改成 median-of-three
- 小區間改用 insertion sort
- 減少遞迴深度

我也加了 `sorted_baseline` 當作內建排序的比較基準。4000 筆資料時，`quick_sort` 約 0.00173 秒，`quick_sort_fast` 約 0.00160 秒，大約是 1.08x 加速，換算約快 7.5%。

驗收方式：

```text
python -m unittest test_sorts test_timing
python benchmark.py
```

## Stage 4：畫圖和報告

我請 AI 繼續 Stage 4。AI 建議用 `matplotlib.use("Agg")`，這樣沒有視窗的環境也能畫圖。

我新增 `test_plot.py` 和 `plot.py`，讓程式讀 `results.json`，畫出 log scale 的折線圖，並輸出到 `assets/benchmark.png`。README 裡也補上圖和簡短解讀。

驗收方式：

```text
python -m unittest test_timing test_sorts test_plot
python plot.py
```

## Stage 5：安全性自掃

我請 AI 繼續 Stage 5。AI 根據 OpenSSF 的方向，幫我檢查數字邊界、JSON 讀檔、安全格式和例外處理。

我先寫 `test_security.py`，測三個問題：

1. `make_data(-1)` 應該拒絕負數
2. `run_benchmark(repeats=0)` 不應該造成除以 0
3. `load_results()` 不應接受非 `.json` 的檔案路徑

紅燈後，我在 `benchmark.py` 和 `plot.py` 補上 `ValueError` 檢查，並在 README 補上安全自掃表格。

驗收方式：

```text
python -m unittest test_timing test_sorts test_plot test_security
```

## 最後確認

最後五個階段都有照紅燈到綠燈的順序做，也都有對應 commit。最終測試結果是：

```text
python -m unittest test_timing test_sorts test_plot test_security
Ran 12 tests
OK
```
