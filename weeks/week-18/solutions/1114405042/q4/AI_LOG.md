# AI 反问我什麼 / 我怎麼回答

## AI 問的規格問題與我的決定

> **timeit 裝飾器的設計**
> AI 問：「裝飾器是否需要被包裝在 `functools.wraps` 裡？"
> 我的回答：需要，我要保留原函式的 `__name__` 和 `__doc__`，讓裝飾器透明化。

> **timeit 的輸入驗證**
> AI 問：「repeat < 1 應該用 `assert` 還是 `raise ValueError`？"
> 我的回答：用 `raise ValueError`，因為 `assert` 在最佳化模式會被拿掉，輸入驗證不能用 `assert`。

> **search.py 的設計**
> AI 問：「linear_search、binary_search、set_search 是否可以修改傳入的 data？"
> 我的回答：不可以，我們要保持輸入的 data 不變，測試會驗證。

> **binary_search 的前提**
> AI 問：「如果 `binary_search` 收到未排序 data 要回什麼？"
> 我的回答：回 -2 並在 docstring 註明前提，排序是呼叫端的責任。

> **benchmark.py 的設計**
> AI 問：「benchmark 應該用 `json` 還 `pickle` 來儲存結果？"
> 我的回答：用 `json`，因為 `json` 較安全（CWE-502），且人間の可讀性更好。

> **plot.py 的設計**
> AI 問：「雷達圖要比較哪些維度、怎麼正規化、怎麼解讀？"
> 我的回答：自己決定並寫進 `README.md`——這題刻意留白，沒有標準答案。

---

## 我改了什麼

1. **timing.py**
   - 實作 `timeit` 裝飾器
   - 使用 `functools.wraps` 保留 metadata
   - 每次呼叫跑 `repeat` 次，記錄每次耗時在 `wrapper.records`
   - `wrapper.last_elapsed` = 本次 `repeat` 的平均耗時
   - `repeat < 1` → `raise ValueError`
   - 裝飾器內不准 `print`

2. **search.py**
   - 實作 `linear_search`、`binary_search`、`set_search`
   - 三者一律不可修改傳入的 data
   - `linear`/`binary` 回 `int`，`set_search` 回 `bool`
   - `binary_search` 收到未排序 data 回 -2，並在 docstring 註明

3. **benchmark.py**
   - 實作 `make_data(n, seed)`、`run_benchmark(sizes, queries)`
   - 使用自己的 `timeit` 量測，記錄總耗時、平均耗時和 records
   - 產生 `results.json` 儲存實驗數據

4. **plot.py**
   - 畫雷達圖呈現三種搜尋的多維權衡
   - 產生 `assets/radar.png`

5. **README.md**
   - 完整實驗報告：方法、交叉點數據表、雷達圖、解讀、安全自掃

6. **安全自掃**：發現了 `make_data` 接受負數邊界條件，進行修補

---

## 我怎麼回答

> **timeit 裝飾器**：我解釋了 `functools.wraps` 的重要性，並明確了 `raise ValueError` 的原因。
> **binary_search 設計**：我考慮了未排序數據的處理，選擇了回 -2 的方式來提示呼叫者。
> **search.py 的不變性**：我堅持了不可修改輸入數據的原則，這是測試的要求。
> **plot.py 的自由設計**：我解釋了雷達圖設計的開放性，決定從五個維度進行評估。
> **安全自掃**：我發現了 `make_data` 的邊界條件問題，進行了修補。

> **AI 的誤解糾正**：AI 通常會說「binary 一定比 linear 快」，但我用數據證明了在小規模數據上，linear 可能更快，因為 binary 需要排序開銷。

> **多維權衡分析**：我設計了五個維度來評估：平均查找時間、記憶體開銷、可擴展性、數據準備成本和實現複雜度。