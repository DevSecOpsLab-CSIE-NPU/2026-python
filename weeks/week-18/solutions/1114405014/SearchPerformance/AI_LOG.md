# AI_LOG

## AI 協作協議五個問題與回答

### 1. 函式簽名與回傳型態

我問 AI 什麼：

> 第四題需要哪些函式？每個函式的輸入與回傳型態應該怎麼設計？

AI 給了什麼：

> AI 建議拆成 `linear_search()`、`binary_search()`、`benchmark_search()`、`make_radar_chart()`、`solve()`，其中搜尋函式回傳 `(found, index, cmp_count)`。

我改了什麼：

> 我採用搜尋函式回傳三元組的設計，並確認 `index` 必須代表排序後陣列的位置，而不是原始輸入位置，避免輸出語意混淆。

---

### 2. 輸入範圍與邊界條件

我問 AI 什麼：

> 第四題輸入格式如何解析？陣列是否要先排序？搜尋目標是多少？

AI 給了什麼：

> AI 說明輸入格式為 `n` 後接 `n` 個整數，程式應先排序，再搜尋 `K = 100 + 14 = 114`。

我改了什麼：

> 我確認本題 `TARGET = 114`，並在 `solve()` 中先用 token-based parsing 讀取 `n` 與後續 `n` 個整數，再對陣列排序後搜尋。

---

### 3. 例外行為

我問 AI 什麼：

> 第四題哪些錯誤狀況需要處理？

AI 給了什麼：

> AI 建議處理空輸入、benchmark repeat 小於 1，以及 Matplotlib 在 pytest 環境可能出現 GUI backend 問題。

我改了什麼：

> 我讓 `solve()` 在空輸入時回傳空字串，讓 `benchmark_search()` 在 `repeat < 1` 時丟出 `ValueError`。後來 pytest 出現 Tkinter 錯誤後，我把圖表 backend 改成 `Agg`，避免測試環境需要 GUI。

---

### 4. Edge Cases

我問 AI 什麼：

> 第四題需要測哪些 edge cases？

AI 給了什麼：

> AI 建議測試找得到、找不到、空陣列、單一元素、重複元素、多行輸入、benchmark 指標與雷達圖檔案產生。

我改了什麼：

> 我保留搜尋主流程測試，並在後續重構後新增 `test_plot.py`，讓圖表模組可以單獨測試 `inverse_score()` 與 `make_radar_chart()`。

---

### 5. 驗收標準

我問 AI 什麼：

> 第四題怎樣才算完成？

AI 給了什麼：

> AI 說明完成條件包含搜尋結果正確、比較次數正確、輸出 timeit 結果、產生 `assets/radar.png`，並能通過 pytest。

我改了什麼：

> 我最後確認測試從 Red 階段錯誤、到修正 Matplotlib backend、再到拆分 `plot.py` 後，最終 pytest 結果為 `18 passed`，符合驗收標準。

---

## 一般 AI 協作紀錄

## 我問 AI 什麼

「說明第四題任務內容。」

## AI 給了什麼

AI 說明第四題是比較 Linear Search 與 Binary Search，搜尋目標為 `K = 114`，需要輸出搜尋狀態、index、比較次數、timeit 時間，並產生 `assets/radar.png`。

## 我改了什麼

我確認本題不只是寫二分搜尋，而是要同時比較線性搜尋與二分搜尋，並把效能分析與圖表輸出納入工作範圍。

---

## 我問 AI 什麼

「撰寫測試檔。」

## AI 給了什麼

AI 提供 `test_search_performance.py`，包含搜尋成功、搜尋失敗、空陣列、單一元素、重複元素、多行輸入、benchmark 與雷達圖產生測試。

## 我改了什麼

我將測試作為 TDD Red 階段的依據，並要求之後撰寫 tests 時都要附上 commit message，讓測試與 Git 紀錄一致。

---

## 我問 AI 什麼

「撰寫主程式。」

## AI 給了什麼

AI 提供 `search_performance.py`，包含搜尋函式、benchmark、雷達圖函式、`solve()` 與 `main()`。

## 我改了什麼

我檢查輸出格式是否能被測試檔驗證，並確認 `linear_cmp` 與 `binary_cmp` 都有出現在 `solve()` 輸出中。

---

## 我問 AI 什麼

「pytest 失敗，錯誤為 `_tkinter.TclError: invalid command name tcl_findLibrary`。」

## AI 給了什麼

AI 判斷錯誤原因是 Matplotlib 預設使用 Tk GUI backend，但 pytest 環境無法建立 Tk 視窗，因此建議使用非互動式 backend `Agg`。

## 我改了什麼

我在 `import matplotlib.pyplot as plt` 之前加入：

```python
import matplotlib
matplotlib.use("Agg")
```

修正後 `test_search_performance.py` 從 `13 passed, 1 failed` 變成 `14 passed`。

---

## 我問 AI 什麼

「主程式手動操作方式？」

## AI 給了什麼

AI 說明因為主程式使用 `sys.stdin.read()`，手動輸入後需要送出 EOF；也可以使用 PowerShell here-string 或檔案輸入避免手動 EOF。

## 我改了什麼

我將此操作方式整理進 README.md，讓手動 demo 時可以直接使用 here-string 或 sample.txt 測試。

---

## 我問 AI 什麼

「將圖表與主程式進行分離成 plot.py 並撰寫 test_plot.py。」

## AI 給了什麼

AI 將 `inverse_score()` 與 `make_radar_chart()` 分離到 `plot.py`，並新增 `test_plot.py` 測試分數轉換、PNG 產生與父資料夾建立。

## 我改了什麼

我採用模組分離，讓 `search_performance.py` 專注於搜尋與 benchmark，`plot.py` 專注於圖表輸出。這也讓圖表功能能被獨立測試。

---

## 我問 AI 什麼

「說明圖像維度。」

## AI 給了什麼

AI 說明雷達圖包含 Speed、Comparisons、Simplicity、No Sort Needed、Large Data 五個維度，分數越高越好，其中時間與比較次數採反向正規化。

## 我改了什麼

我將雷達圖維度與評分規則補進 README.md，讓圖表不是只有產生圖片，而是有可解釋的分析依據。

---

## 我問 AI 什麼

「撰寫 README.md AI_LOG.md 整理 TEST_LOG.md。AI_LOG 補上 AI 協作協議的五個問題與回答。」

## AI 給了什麼

AI 根據主程式、plot.py 拆分、測試紀錄與 AI 協作協議，整理 README.md、AI_LOG.md、TEST_LOG.md。

## 我改了什麼

我確認 AI_LOG 中每個協作項目都有「我改了什麼」，並補上五個協作問題與回答，避免只記錄 AI 給了什麼而沒有呈現自己的判斷。
