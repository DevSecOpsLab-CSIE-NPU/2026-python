# AI_LOG

## 我問 AI 什麼

請依照 week-16 6/11 排序效能實驗室規格，幫我在指定 solutions 目錄完成 Stage 1 到 Stage 5 的實作、測試、benchmark、圖表與安全性自掃。

（逐字提示詞）
"請依照 week-16 6/11 排序效能實驗室規格，幫我在指定 solutions 目錄完成 Stage 1 到 Stage 5 的實作、測試、benchmark、圖表與安全性自掃。"

## AI 給了什麼

整理出可落地的模組結構、測試策略與實作方案，包含 `timeit`、三種排序、benchmark、plot 與安全性測試。

## 我改了什麼

我依題目把完整程式放進 `weeks/week-16/solutions/1114405021/0611/`，並選擇演算法優化而非 Cython，讓專案不依賴額外編譯流程；實測後 `quick_sort_fast` 對 `quick_sort` 約有 1.24x 到 1.96x 的加速，README 已回填數據與圖檔資訊。

補充三項作業要求內容：

1) 加速多少百分比：
- `quick_sort_fast` 相對於 `quick_sort` 的觀察加速比約為 1.24x–1.96x，換算百分比約為 24%–96% 加速（依輸入大小而異，例：n=1000 約 96%）。

2) 演算法優化的策略：
- `bubble_sort_fast`: 提早停止（early-exit）並用 `last_swap` 縮小掃描範圍。
- `quick_sort_fast`: 採用 median-of-three 作為樞軸選取、對小區間使用插入排序（threshold=24），以減少遞迴與提升局部效能。
- `merge_sort_fast`: 小區間切換到插入排序（threshold=32）以降低遞迴開銷。

3) 依 Python 安全程式原則，修補的程式項目（共 3 項）：
- `make_data`：驗證 `n` 非負，對負值拋出 `ValueError`（避免不合理輸入導致不明行為）。
- `load_results`：使用 `json` 讀取 `results.json`、不使用 `pickle`，以降低反序列化風險 (CWE-502)。
- `timeit`：保持裝飾器內部無 `print` 或其他副作用，輸出責任交由 benchmark/plot 模組處理。