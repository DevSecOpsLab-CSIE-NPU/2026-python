# Search Performance

## 題目說明

本題為 Week 18 第四題 Search Performance。目標是比較：

```text
Linear Search
vs
Binary Search
```

程式會讀取一組整數陣列，先將陣列排序，接著在排序後的陣列中搜尋指定目標值 `K = 114`，並輸出搜尋結果、index、比較次數、執行時間，以及產生雷達圖 `assets/radar.png`。

---

## 個人參數

學號末兩碼：`14`

| 參數 | 計算方式 | 結果 |
|---|---:|---:|
| 搜尋目標 `K` | `100 + 14` | `114` |

因此本題固定搜尋：

```text
K = 114
```

---

## 檔案說明

```text
SearchPerformance/
├── search_performance.py
├── plot.py
├── test_search_performance.py
├── test_plot.py
├── README.md
├── AI_LOG.md
└── TEST_LOG.md
```

| 檔案 | 說明 |
|---|---|
| `search_performance.py` | 主程式，負責搜尋、benchmark、輸入解析與輸出 |
| `plot.py` | 圖表模組，負責雷達圖分數轉換與 PNG 產生 |
| `test_search_performance.py` | 搜尋與主流程測試 |
| `test_plot.py` | 圖表模組測試 |
| `README.md` | 題目、執行方式、圖表維度與測試方式說明 |
| `AI_LOG.md` | AI 協作紀錄 |
| `TEST_LOG.md` | 測試紀錄整理 |

---

## AI 協作協議五個問題

### 1. 函式簽名與回傳型態

本題主要函式設計如下：

```python
def linear_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    ...

def binary_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    ...

def benchmark_search(arr: list[int], target: int, repeat: int = 1000) -> dict[str, float]:
    ...

def solve(input_text: str, target: int = 114) -> str:
    ...
```

圖表模組：

```python
def inverse_score(value: float, best: float, worst: float) -> float:
    ...

def make_radar_chart(metrics: dict, output_path: str | Path = "assets/radar.png") -> None:
    ...
```

`linear_search()` 與 `binary_search()` 回傳：

```text
(found, index, cmp_count)
```

其中：

- `found`: 是否找到目標值
- `index`: 在排序後陣列中的 index，找不到為 `-1`
- `cmp_count`: 比較次數

---

### 2. 輸入範圍與邊界條件

輸入格式：

```text
n
a1 a2 ... an
```

程式會先讀取 `n`，再讀取接下來 `n` 個整數。

輸入可以分行，也可以用空白分隔。

範例：

```text
8
5 114 20 7 9 100 3 50
```

或：

```text
8 5 114 20 7 9 100 3 50
```

本題會先排序後再搜尋，因此 index 代表排序後陣列的位置，不是原始輸入位置。

---

### 3. 例外行為

本題測試目前主要針對正確格式輸入。額外處理：

- 空輸入時，`solve()` 回傳空字串
- `benchmark_search()` 的 `repeat < 1` 時，丟出 `ValueError`
- 圖表輸出使用 Matplotlib `Agg` backend，避免 pytest 或無 GUI 環境出現 Tkinter 錯誤

---

### 4. Edge Cases

本題測試涵蓋：

- 找得到 `K = 114`
- 找不到 `K = 114`
- 空陣列
- 單一元素找到
- 單一元素找不到
- 重複元素時，回傳任一合法 index
- 輸入資料跨多行
- benchmark 回傳時間欄位
- 雷達圖 PNG 檔案產生
- 圖表模組建立父資料夾
- `inverse_score()` 正規化邊界

---

### 5. 驗收標準

本題完成標準：

1. `TARGET = 114`
2. 搜尋前會先排序
3. `linear_search()` 與 `binary_search()` 都能回傳 found、index、cmp
4. `solve()` 輸出包含：
   - `FOUND` 或 `NOT FOUND`
   - `index=...`
   - `linear_cmp=...`
   - `binary_cmp=...`
   - `linear_time=...`
   - `binary_time=...`
   - `faster=...`
   - `chart=assets/radar.png`
5. 能產生 `assets/radar.png`
6. `pytest` 最終結果為 `18 passed`

---

## 主程式設計

### `linear_search(arr, target)`

從左到右逐一搜尋。

時間複雜度：

```text
O(n)
```

比較次數定義：

```text
每檢查一次 value == target，cmp_count + 1
```

---

### `binary_search(arr, target)`

在已排序陣列中使用二分搜尋。

時間複雜度：

```text
O(log n)
```

比較次數定義：

```text
每一輪 while 以 arr[mid] 和 target 進行判斷時，cmp_count + 1
```

---

### `benchmark_search(arr, target, repeat=1000)`

使用 `timeit` 分別測量：

```text
linear_search
binary_search
```

回傳：

```python
{
    "linear_time": ...,
    "binary_time": ...
}
```

---

### `solve(input_text, target=114)`

流程：

```text
讀取 n
讀取接下來 n 個整數
排序
線性搜尋
二分搜尋
benchmark
呼叫 plot.py 產生 radar.png
輸出結果
```

---

## 圖表模組設計

圖表功能已經從 `search_performance.py` 分離到 `plot.py`。

目的：

```text
讓主程式只負責搜尋與效能比較
讓 plot.py 專門負責圖表分數與圖像輸出
讓 test_plot.py 可以單獨測試圖表邏輯
```

---

## 雷達圖維度說明

雷達圖共有 5 個維度，分數範圍為 1 到 5 分，分數越高代表表現越好。

| 維度 | 說明 | 評分方式 |
|---|---|---|
| Speed | 搜尋執行時間 | 由 `timeit` 測得，時間越短分數越高 |
| Comparisons | 搜尋比較次數 | 比較次數越少分數越高 |
| Simplicity | 實作簡單度 | 固定評分，Linear = 5，Binary = 3 |
| No Sort Needed | 是否不需要排序 | 固定評分，Linear = 5，Binary = 2 |
| Large Data | 大資料表現 | 固定評分，Linear = 2，Binary = 5 |

時間與比較次數採用反向正規化，因為這兩項都是數值越小越好。

---

## 範例

### Input

```text
8
5 114 20 7 9 100 3 50
```

排序後：

```text
3 5 7 9 20 50 100 114
```

`114` 在排序後的 index 為 `7`。

### Output 範例

實際時間會依電腦狀態略有不同。

```text
FOUND index=7
linear_cmp=8
binary_cmp=4
linear_time=...
binary_time=...
faster=binary
chart=assets/radar.png
```

---

## 執行方式

```bash
python search_performance.py
```

輸入：

```text
8
5 114 20 7 9 100 3 50
```

因為主程式目前使用 `sys.stdin.read()`，手動輸入後需要送出 EOF。

Windows PowerShell / CMD：

```text
Ctrl + Z
Enter
```

Linux / WSL / Git Bash：

```text
Ctrl + D
```

也可以使用 PowerShell here-string：

```powershell
@"
8
5 114 20 7 9 100 3 50
"@ | python search_performance.py
```

或使用檔案輸入：

```bash
python search_performance.py < sample.txt
```

---

## 測試方式

```bash
pytest
```

最終測試結果：

```text
18 passed
```

---

## Commit 建議

```bash
git add test_search_performance.py
git commit -m "test: add search performance tests"

git add search_performance.py
git commit -m "feat: implement search performance comparison"

git add search_performance.py
git commit -m "fix: use non-interactive matplotlib backend"

git add plot.py test_plot.py search_performance.py
git commit -m "refactor: split search plotting module"

git add README.md AI_LOG.md TEST_LOG.md
git commit -m "docs: document search performance solution"
```
