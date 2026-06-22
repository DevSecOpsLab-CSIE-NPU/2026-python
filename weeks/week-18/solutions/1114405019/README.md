# 第四題：二分搜尋效能（學號 1114405019）

K = 100 + 19 = **119**（學號末兩碼 19）

## 檔案

- `search_perf-easy.py`：**AI 教的簡單版本**，只留 `linear_search` / `binary_search` 兩個核心函式，附詳細中文註解，給 CPE 練習時手打背誦用
- `search_perf.py`：**手打的完整版本**，加上 `generate_sorted_array` / `time_searches` / `collect_radar_metrics` / `main`，串接輸入輸出、timeit、畫圖
- `plot.py`：雷達圖（`matplotlib.use("Agg")`，無視窗環境可執行）
- `test_search_perf.py`：pytest 單元測試（只測搜尋正確性，不測 timeit / 畫圖）
- `assets/radar.png`：雷達圖輸出
- `test_log.txt`：測試執行紀錄（針對手打版本 `search_perf.py` 跑 `test_search_perf.py` 的結果）
- `requirements.txt`：依賴套件（`matplotlib`、`pytest`）
- `AI_LOG.md`：AI 使用紀錄

## 輸入/輸出

- 優先從 stdin 讀「第1行 m；第2行 m 個升冪整數」。
- 沒有 stdin 輸入時，自動用 `generate_sorted_array(m=200_000, target=119, present=True)` 產生陣列。
- 輸出：`FOUND idx cmp=次數` 或 `NOT FOUND cmp=次數`，接著印兩種搜尋的 timeit 結果與較快者。

## 陣列產生規則（如何控制 K 在不在）

`generate_sorted_array(m, target, present, seed)`：在排除 `target` 的整數範圍內取樣 `m`（或 `m-1`）個唯一整數、排序，
若 `present=True` 才用 `bisect.insort` 把 `target` 插入。因此：

- `present=True` → `target` **保證**恰好出現一次 → 結果必為 `FOUND`。
- `present=False` → `target` **保證**不出現 → 結果必為 `NOT FOUND`。

`main()` 自動生成時固定用 `present=True`，所以執行 `python search_perf.py`（無 stdin）一定會印出 `FOUND`；
`NOT FOUND` 與其他邊界情況（單元素陣列、K 為第一個/最後一個元素、off-by-one 邊界）改用單元測試裡手刻的固定陣列驗證，
因為這些情況需要精確控制元素位置，用隨機產生器反而不可控。

## 雷達圖：維度與正規化

選了 4 個維度（`plot.py` 的 `DIMENSIONS`）：

1. **small-n speed**：m=200 時的 timeit 耗時
2. **large-n speed**：m=200,000 時的 timeit 耗時
3. **fewer comparisons**：在 large-n 規模下的 cmp 次數
4. **no presort needed**：binary 需要事先排序好的陣列才能用，linear 不需要——這是類別變數（0/1），不是連續量

選這 4 個的原因：前 3 個是這題明確要求量測的指標（小 n 速度、大 n 速度、cmp），第 4 個補上一個 binary 的隱藏成本——
如果原始資料沒排序，要先付出排序成本，這在前 3 個維度裡看不出來，但是 binary search 真實使用情境裡很關鍵的權衡。

正規化方式（讓「越外凸代表越好」）：

- 連續且越小越好的維度（時間、cmp）：`score = min(linear, binary) / 該方法的值`。贏家分數恰好是 1，
  輸家是兩者的比例（沒有直接除以「全部方法的最大值」，因為時間/次數的量級差很多——例如 binary 的 cmp
  可能是個位數、linear 是六位數——直接除最大值會讓贏家的分數被輸家的尺度拉到幾乎貼著 0，反而看不出差異；
  用「最小值 / 自己」可以保證贏家永遠頂滿，輸家的分數則反映「贏家比我快幾倍」這個有意義的比例）。
- `needs_presort`（已經是 0/1）：直接 `score = 1 - value`，因為「不需要排序」才是優點，分數方向要跟其他維度一致（外凸=好）。

## 解讀（2-3 句）

雷達圖中 binary 在 **large-n speed**、**small-n speed**、**fewer comparisons** 三個維度都明顯外凸，
顯示資料量越大時 binary search 的優勢越明顯（這也對應到 O(log n) vs O(n) 的理論複雜度）。
但 linear 在 **no presort needed** 維度滿分、binary 是 0 分——binary search 要求資料先排序好，
若資料本身是無序的且只搜尋一次，排序成本可能蓋過 binary 省下來的搜尋時間，所以沒有絕對贏家，
要看「資料量大小」與「資料是否已經排序/會被重複查詢多次」來決定用哪種演算法。

## 測試

```
pytest test_search_perf.py -v
```

12 個測試，涵蓋：找到時 idx 正確、NOT FOUND 邊界（落在元素間隙、小於最小值、大於最大值）、
單元素陣列（FOUND / NOT FOUND）、K 為第一個/最後一個元素、cmp 次數理論上限、
linear 與 binary 在多組 target 上的 FOUND/NOT FOUND 與 idx 交叉一致性、
以及 `generate_sorted_array` 對 K 在不在陣列裡的保證。全數通過，紀錄於 `test_log.txt`。

## 執行

```
python search_perf.py
```

範例輸出（陣列由程式隨機生成，idx/cmp/timeit 數字每次執行會不同）：

```
FOUND 100323 cmp=18
linear : 0.0426 s
binary : 0.0000 s
=> binary faster
```
