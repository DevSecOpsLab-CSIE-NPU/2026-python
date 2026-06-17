# AI_LOG

## 我的提示詞

幫我完成這項作業

## AI 反問我什麼 / 我怎麼回答

### 1. AI 問：`timeit` 要支援哪種用法？

我回答：

希望可以用 `@timeit()`，也可以用 `@timeit(repeat=5)`。`repeat` 預設是 3。

### 2. AI 問：被裝飾的函式跑多次時，回傳值要怎麼處理？

我回答：

每次呼叫被裝飾函式時，都實際執行 `repeat` 次，最後回傳最後一次執行的結果。

### 3. AI 問：計時結果要放在哪裡？

我回答：

每一次耗時都放進被裝飾函式的 `records` list。`last_elapsed` 則放這次呼叫的平均耗時。

### 4. AI 問：`repeat < 1` 要怎麼處理？

我回答：

要用 `raise ValueError`，不能用 `assert`，因為 `assert` 在最佳化模式可能會被關掉。

### 5. AI 問：測試要涵蓋哪些規格？

我回答：

測試至少要檢查：

- 回傳值不變
- `functools.wraps` 有保留 `__name__` 和 `__doc__`
- `repeat` 次數正確
- `records` 長度正確，裡面是 `float`
- `last_elapsed` 是平均耗時
- `repeat=1` 的 edge case
- `repeat=0` 會 raise `ValueError`

### 6. AI 問：`binary_search` 對未排序資料要怎麼定義？

我回答：

`binary_search` 的前提是資料已經由小到大排序。函式本身不排序、不修改傳入的 `data`，這個限制寫在 docstring 裡。

### 7. AI 問：搜尋效能比較要怎麼做？

我回答：

用 `list(range(100000))` 當測試資料，target 選最後一個 `99999`，讓 linear search 需要走到最後，比較容易看出差距。兩種搜尋都用 `timeit(repeat=5)` 量測。

## AI 幫我做了什麼

- 讀取作業 README 與 `test_timing.py`。
- 將原本只有 `self.fail()` 的測試改成真正會驗證規格的 unittest。
- 建立 `timing.py` 並實作 `timeit`。
- 建立 `search.py` 並實作 `linear_search` 和 `binary_search`。
- 使用臨時量測腳本比較 linear search 與 binary search。
- 補上 `README.md` 的搜尋效能比較結果。
- 補上 `TEST_LOG.md`。

## 我如何驗收 AI 給的結果

我用以下指令執行測試：

```bash
python -m unittest
```

結果：

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

我也執行搜尋效能比較：

```bash
python temporary benchmark script
```

結果摘要：

```text
linear_result: 99999
binary_result: 99999
linear_average: 0.0026701999999659163
binary_average: 0.0000024199999643315096
```

## 我的判斷

測試有涵蓋 `timeit` 的主要規格，而且 `linear_search` 與 `binary_search` 都能找到正確 index。

在已排序資料中，`binary_search` 明顯比 `linear_search` 快很多，因為它每次都把搜尋範圍砍半。不過如果資料原本沒有排序，還要先付出排序成本，所以只有在資料已排序，或同一份排序資料會被搜尋很多次時，binary search 才特別划算。

## 人工修改行數

0 行。
