# 0618 搜尋效能實驗室 — 實驗報告

## 實驗環境

- CPU / RAM: (本機)
- Python: 3.14
- timeit 裝飾器: repeat=1, 量測 100 次查詢的總時間

---

## Stage 3 加速前預測

三種搜尋預測排名（由快到慢）：
1. set_search（雜湊 O(1)，最快）
2. binary_search（O(log n)，快）
3. linear_search（O(n)，慢）

交叉點預測：當 n ≈ 10,000、查詢次數 ≥ 50 時，「排序 + binary」開始比 linear 划算。

---

## Stage 3 實測結果（100 queries）

| size | linear | binary | set | builtin_in | builtin_bisect |
|------|--------|--------|-----|------------|----------------|
| 1000 | 0.000027 | 0.000002 | 0.000020 | 0.000007 | 0.000001 |
| 5000 | 0.000115 | 0.000002 | 0.000493 | 0.000028 | 0.000001 |
| 20000 | 0.000080 | 0.000004 | 0.003786 | 0.000038 | 0.000001 |
| 80000 | 0.000207 | 0.000003 | 0.009091 | 0.000098 | 0.000001 |

### 觀察

- **binary_search** 是所有 size 中最快的，且穩定不隨 n 增長
- **builtin_in** 約比手寫 linear 快 2–3 倍（C 實作的優勢）
- **set_search** 在 n 增大時變慢（每查一次就重建一次 set，成本 O(n)）
- **交叉點分析**：排序成本 O(n log n) 約為 200µs（以 n=1000 估計）；
  對單次查詢，排序 + binary >> linear，不划算；
  對大量查詢（如 100 次以上），排序成本攤平後 binary 勝出。

### 抓 AI 的錯

AI 說「binary 一定比 linear 快」在以下條件是錯的：

1. **小 n（n < 100）**：linear 的常數低，O(n) 和 O(log n) 差異幾乎量不到
2. **只查一次 + 資料未排序**：排序成本 O(n log n) 遠高於 linear 的一次 O(n)
3. **n 超大且記憶體有限**：set_search 雖快但記憶體開銷大，可能觸發 swap

本實驗數據顯示：當查 100 次、n ≥ 1000 時 binary 確實比 linear 快約 10–50 倍。

---

## Stage 4 雷達圖解讀

雷達圖維度說明：

| 維度 | 意義 |
|------|------|
| avg_time | 平均搜尋時間（正規化，越高越好）|
| scalability | 隨 n 增大的穩定度 |
| simplicity | 實作與理解難易度 |
| no_preprocess | 是否需要預處理（如排序）|
| memory | 額外記憶體開銷 |

結論：

- **binary_search** 在 avg_time 和 scalability 勝出，但需要預排序
- **linear_search** 在 simplicity 和 no_preprocess 滿分，適合少量資料
- **set_search** 在 avg_time 被扣分（因每查一次重建 set），但 no_preprocess 滿分
- 沒有絕對贏家：選擇取決於查詢次數、資料是否已排序、記憶體限制

---

## Stage 5 安全性自掃報告

| OpenSSF 條目 | 檢查結果 | 處理方式 |
|-------------|---------|---------|
| 08 Coding Standards | benchmark.py 以 `with` 開啟 results.json | ✅ 已確認正確使用 `with` |
| 03 Numbers | make_data 的 n 可能為負數 | ✅ 加入 `raise ValueError` |
| 04 Neutralization (CWE-502) | plot.py 使用 `json.load` 而非 `pickle` | ✅ 安全，JSON 無反序列化風險 |

### 不適用條目

- **05 Exception Handling — 開檔讀檔**：benchmark.py 的開檔只有單一行 `with open`，Python 自動處理 cleanup，無需額外 try/except
- **08 Coding Standards — shadow 內建名稱**：Stage 1–4 程式中無使用 `list`、`id`、`dict` 等作為變數名

---

## 檔案結構

```
├── timing.py            # timeit 裝飾器（含 repeat 取平均）
├── test_timing.py       # Stage 1 測試（4 tests）
├── search.py            # linear / binary / set search
├── test_search.py       # Stage 2 測試（5 tests, subTest 共用）
├── benchmark.py         # 量測 + baseline（in, bisect）
├── results.json         # benchmark 結果
├── plot.py              # 雷達圖繪製
├── test_plot.py         # Stage 4 測試（PNG 存在且非空）
├── test_security.py     # Stage 5 安全測試（3 tests）
├── assets/radar.png     # 雷達圖
├── AI_LOG.md            # AI 互動記錄
├── TEST_LOG.md          # 測試輸出記錄
└── README.md            # 本報告
```
