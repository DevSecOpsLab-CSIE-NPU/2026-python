# AI_LOG.md — 0617 timeit + 搜尋效能評估

## 我問 AI 什麼

1. 「請幫我用 Python 寫一個 timeit 裝飾器，支援 repeat 參數（預設 3），每次耗時記錄在 f.records，f.last_elapsed 是平均值，用 functools.wraps，repeat < 1 要 raise ValueError，不准 print。」

2. 「請幫我補齊 test_timing.py 的測試，至少 4 個案例：回傳值不變、metadata preserved、records 與平均正確、repeat < 1 拋錯。」

3. 「請幫我寫 linear_search 和 binary_search，不可修改傳入的 data，binary 收到未排序資料的行為自己定義。」

4. 「請幫我寫 benchmark.py，用 timeit 裝飾器量測 n=1,000,000 下 linear vs binary 的效能。」

## AI 給了什麼

1. 給了一個 timeit 裝飾器實作，使用 time.perf_counter()，repeat 參數放在 wrapper 上，records 存在 wrapper 函式物件上。

2. 給了 4 個測試案例，涵蓋基本規格，但缺少 repeat=1 的 edge case。

3. 給了 linear_search（逐一比對）和 binary_search（左右指標收縮），docstring 說明了未排序行為未定義。

4. 給了 benchmark.py，使用 timeit 裝飾器搭配 repeat=5 量測，輸出 records 與平均值。

## 我改了什麼

- 自己補了 test_repeat_one_records_single_value 這個 edge case，確保 repeat=1 時 records 只有一筆
- 將 AI 給的 `time()` 改成 `time.perf_counter()`，因為 perf_counter 更適合精確計時
- 調整 README.md 的評估敘述，加入排序+binary 的權衡分析

## AI 反問我什麼 / 我怎麼回答

> AI 問：「repeat 取平均還是取最小？」
> 我答：取平均，因為要反映一般情況，且規格明確寫平均。

> AI 問：「被裝飾的函式有參數時怎麼辦？」
> 我答：用 *args, **kwargs 傳遞，保持簽名通用。

> AI 問：「binary_search 收到未排序的 data 要怎麼處理？」
> 我答：在 docstring 說明行為未定義，不主動排序，因為排序成本應由呼叫端決定。

> AI 問：「repeat=0 或負數要怎麼處理？」
> 我答：raise ValueError，因為 repeat 至少要 1 次才有意義。

> AI 問：「要量多大的 n 才看得出差異？」
> 我答：n=1,000,000，因為 binary O(log n) 和 linear O(n) 在百萬級別差異明顯。
