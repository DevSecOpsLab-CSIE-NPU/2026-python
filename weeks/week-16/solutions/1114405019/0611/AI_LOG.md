# AI_LOG — Week 16 排序效能實驗室

學號：1114405019
日期：2026-06-11

---

## Stage 1 — @timeit 裝飾器

### 我問 AI 什麼（逐字）

> 我要寫一個 Python 裝飾器 `timeit`，規格如下：
> 1. 被裝飾函式的回傳值不能改變
> 2. 用 `functools.wraps` 保留 `__name__` 和 `__doc__`
> 3. 每次呼叫後把耗時（秒，float）存到 `f.last_elapsed`（最近一次）和 `f.records`（累積 list）
> 4. 裝飾器內不准 `print`
>
> 請先幫我列出所有需要測試的 case，說明每個 case 要測什麼，但不要直接給測試程式碼。

### AI 回答重點

AI 列出了四個測試方向：回傳值不變、`__name__`/`__doc__` 保留、`last_elapsed` 與 `records` 正確累積、無 print 輸出。

### 我改了什麼

- AI 給的測試方向少了「`last_elapsed` 應等於 `records[-1]`（最後一次）」，我自己補上。
- AI 建議的 `test_no_print_output` 沒有 `try/finally` 保護 `sys.stdout`，若測試中途拋例外會讓 stdout 永久被替換，我改成 `try/finally` 確保恢復。
- 我把 `records` 初始化為 `[]` 放在 wrapper 外（wrapper 本身上面），而非每次呼叫都重建。

### 驗收標準

`python -m unittest test_timing -v` 五個測試全綠。

---

## Stage 2 — 三種排序 + benchmark

### 我問 AI 什麼（逐字）

> 我需要實作三個排序函式：`bubble_sort`、`quick_sort`、`merge_sort`，規格：
> - 簽名都是 `def fn(data: list) -> list`
> - 一律回傳新 list，不能修改傳入的 list
> - 禁用 `sorted()` 和 `list.sort()`
>
> 請先告訴我，這三個函式各有哪些 edge case 應該要測試，不要給程式碼。

### AI 回答重點

AI 列出：空 list、單元素、已排序、逆序、含重複值、含負數、不修改輸入。

### 我改了什麼

- AI 沒提到「三個函式共用同一組 test，用迴圈 + subTest」，我看規格後自己設計 `SORT_FUNCTIONS` list + `for fn in SORT_FUNCTIONS: with self.subTest(fn=fn.__name__)` 的結構。
- `benchmark.py` 的 `make_data` AI 一開始沒有加 `seed` 參數和 `random.Random(seed)` 的隔離，我要求加上確保可重現。

### 驗收標準

`python -m unittest test_sorts -v` 六個測試（含 Stage 3 fast sorts）全綠；`python benchmark.py` 成功輸出比較表並產生 `results.json`。

---

## Stage 3 — 加速實驗

### 我問 AI 什麼（逐字）

> 我選擇演算法優化而不是 Cython。請說明這三種排序各自最容易做哪一種演算法層面的優化，以及各優化的原理，不要給程式碼。

### AI 回答重點

- bubble：早停（no-swap flag），已排序輸入從 O(n²) → O(n)
- quick：中間元素或 median-of-three 當 pivot，避免已排序輸入退化成 O(n²)
- merge：bottom-up 迭代版，省去遞迴函式呼叫的堆疊開銷

### 我改了什麼

- AI 給的 `_partition_mid` 先把中間元素和最後元素交換再走 Lomuto 分割，邏輯正確，我直接採用。
- bottom-up merge sort 的 `width *= 2` 迴圈 AI 給的版本沒有正確處理奇數大小的 sub-array（`mid = min(i + width, n)` 和 `right = min(i + 2*width, n)` 要做邊界保護），我自己加上 `if mid < right` 才合併，否則空 sub-array 會出現。
- AI 沒有提醒加速版需要通過 Stage 2 同一組測試，我在 `test_sorts.py` 的 `SORT_FUNCTIONS` 裡直接 append 了 fast 版，無需另開測試。

### 加速比（n=4000）

| 優化 | 策略 | 原始 | 優化後 | 說明 |
|------|------|------|--------|------|
| bubble_fast | 早停 | 0.4746s | 0.4908s | 隨機資料效益不明顯 |
| quick_fast | 中間 pivot | 0.003330s | 0.003359s | 已排序輸入才顯著 |
| merge_fast | bottom-up | 0.005459s | 0.006012s | 隨機小資料無優勢 |

### 驗收標準

所有 fast 函式通過 `SORT_FUNCTIONS` 共用測試；`results.json` 含全部 7 個演算法的數據。

---

## Stage 4 — 畫圖與報告

### 我問 AI 什麼（逐字）

> 我要用 matplotlib 畫折線圖，x 軸是資料量 n（整數），y 軸是平均秒數用 log scale，每個演算法一條線，資料來自 `results.json`。圖要存成 PNG。有哪些實作細節容易踩坑？

### AI 回答重點

- 必須在 import matplotlib 後立刻 `matplotlib.use("Agg")` 才能在無視窗環境跑
- `ax.set_yscale("log")` 而不是在 `plt.plot` 里設
- 存圖用 `plt.savefig` 後記得 `plt.close(fig)` 避免記憶體洩漏

### 我改了什麼

- 測試中把 `plot_results` 傳入 temp dir 路徑，AI 沒提到 `os.makedirs(dir_name, exist_ok=True)`，若 `assets/` 不存在會 FileNotFoundError，我自己加上。
- 中文 label 在 Windows 的 DejaVu Sans 字型下會顯示方塊，我改成英文 label 確保圖表可讀。

### 驗收標準

`python -m unittest test_plot -v` 五個測試全綠；`assets/benchmark.png` 存在且大小 > 100 bytes。

---

## Stage 5 — 安全性自掃

### 我問 AI 什麼（逐字）

> 我的專題有 timing.py / sorts.py / sorts_fast.py / benchmark.py / plot.py。請依照 OpenSSF Secure Coding Guide for Python 的第 03、04、05、08 章，幫我找出每個檔案可能有哪些安全問題（不要直接給我修改後的程式碼，只說問題）。

### AI 回答重點

- 08：`load_results` 和 benchmark 寫檔應用 `with`
- 05：不應 bare except，應讓 FileNotFoundError / JSONDecodeError 自然傳播
- 04：確認用 json 不是 pickle 讀取 results.json
- 03：`make_data(-1)` 應明確 raise 而非靜默

### 我改了什麼

- `make_data` 已加 `if n < 0: raise ValueError(...)` 明確邊界。
- 我自己判定 `random.Random(seed)` 非安全敏感，不適用 `secrets`，AI 同意這個判斷。
- `test_security.py` 用 AST 掃描 bare except，AI 給的版本沒有 `skipTest` 邏輯（檔案不存在時），我加上 `if not os.path.exists(filename): self.skipTest(...)` 讓測試更健壯。

### 驗收標準

`python -m unittest test_security -v` 12 個測試全綠。
