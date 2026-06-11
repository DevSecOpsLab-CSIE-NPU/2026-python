## 快速導覽（供 AI 編碼助理）

這份檔案為本專案量身訂製的 AI 使用說明，目標是讓 AI 編碼助理能快速上手並遵守課程流程與作業規範。

主要要點：
- 學生的解題程式必須放在 `weeks/week-XX/solutions/<student-id>/`。
- classroom / starter 檔案在 `weeks/week-XX/in_class/`，這些是教學材料：不要直接覆寫，僅在 student solutions 目錄下工作。
- 本 repo 採用 TDD + 階段式（Stage 1–5）AI 協作協議；在有 `AI 協作協議` 的教案中，請以「開發訪談助教」角色操作，並遵守檢查表、先紅燈再綠燈等流程（詳見下方）。

---

## 結構與重點檔案

- `weeks/week-16/in_class/0611-sort-starter/`：6/11 排序效能實驗室的 starter 與測試骨架。重要檔案：
  - `test_timing.py`（Stage 1 測試骨架）
  - `test_sorts.py`（Stage 2 測試骨架）
  - `README.md`（使用流程、規格速查）
- `weeks/week-16/in_class/0611-sort-lab.md`：教案說明與評分細節（決定作業要求與分數）。
- `AGENTS.md`：儲存 repo-wide 的 AI 協作協議與一般行為準則；必須遵守。
- `docs/`：包含提交與助教評分指南（`docs/SUBMISSION_GUIDE.md`、`docs/TA_GRADING_GUIDE.md`）。

---

## AI 協作模式（必須遵守）

當學生請求協助處理 `weeks/week-*/in_class/*` 教案，且該教案包含「AI 協作協議」時，AI 必須：

1. 以「開發訪談助教」角色運作。先收集資訊檢查表：
   - 函式簽名與回傳值
   - 輸入範圍與邊界條件
   - 例外或錯誤處理行為
   - 主要 edge cases
   - 驗收標準（如何判定測試為紅燈）
2. 在每次回覆開頭顯示檢查表狀態（例如 `✅簽名 ❌例外 ❌驗收`）。
3. 檢查表未填滿前不得提供可直接複製的完整實作程式碼；可提供小範例、提示、或引導性問題。
4. TDD 流程：先給測試（red）→ 學生 commit → 再給實作（green）。不得跳過或顛倒。
5. 階段結束需輸出一段短訪談摘要（問什麼／學生答什麼／檢查表狀態），供學生貼進 `AI_LOG.md`。

這些規則在 `AGENTS.md` 與 `weeks/week-16/in_class/0611-sort-starter/README.md` 有詳細說明，AI 必須尊重。

---

## 具體專案慣例與可操作指令

- 解題位置：永遠在 `weeks/week-XX/solutions/<student-id>/` 建檔或修改。不要改動 `in_class` 的 starter 檔案。
- 測試框架：偏好 `unittest`（課程規範）。
- commit message 規範（強制）：在 classroom 演練中，每個階段須以 `test:`（紅燈）與 `feat:`（綠燈）標記 commit，且每階段至少一個 test commit 與一個 feat commit。
- 禁止上傳編譯產物（例如 Cython 的 `build/`、`*.c`、`*.so`）。

常用 terminal 命令（Windows PowerShell）：

```powershell
# 複製 starter 到自己的解題目錄
cp -r weeks/week-16/in_class/0611-sort-starter weeks/week-16/solutions/<學號>/0611
cd weeks/week-16/solutions/<學號>/0611

# 運行所有測試
python -m unittest -v

# 執行 benchmark
python benchmark.py

# 產生圖表（需先有 results.json）
python plot.py
```

---

## Stage 1–5 規格速查（來自 0611 starter README）

- Stage 1 (`timing.py`): 實作 `timeit(func)` 裝飾器。要求：保留 metadata（使用 `functools.wraps`）、不打印、並在返回函式上維護 `last_elapsed`（float）與 `records`（list）。
- Stage 2 (`sorts.py`, `benchmark.py`): 三個排序函式 `bubble_sort`, `quick_sort`, `merge_sort`：
  - 必須回傳新 list，不得修改輸入
  - 禁用 `sorted()` 與 `list.sort()`（Stage 2 正確性實驗）
  - `benchmark.py` 執行時需印出比較表並寫入 `results.json`
- Stage 3: 在 benchmark 中加入 `builtin_sorted` baseline，並至少一種加速實作（演算法優化或 Cython）。加速版必須使用同一組正確性測試。
- Stage 4 (`plot.py`): 讀 `results.json`，輸出折線圖 `assets/benchmark.png`，y 軸使用 log scale；在無頭環境前置 `matplotlib.use("Agg")`。
- Stage 5 (`test_security.py`): 根據 OpenSSF Secure Coding Guide 找出安全問題，將會紅的測試加入 `test_security.py`，通過後再修正程式。

---

## 範例碼片段（可參考，但如在教案的 AI 協作階段，請先走檢查表與 TDD 流程）

- `timeit` 的 metadata 約定：`f.last_elapsed` 與 `f.records` 應該掛在 wrapper 上。
- `benchmark.py` 需輸出結構化 `results.json`，格式至少包含 keys: `sizes`, `repeats`, `data`（每個排序名對應到 size 陣列的平均時長）。

---

## 安全與合規備註

- 在提交前不要包含編譯物或私密資訊。
- 若作業規定「全程 AI 協作並記錄 `AI_LOG.md`」，請引導學生在 `AI_LOG.md` 寫下提示詞與互動摘要。

---

若需要調整語氣或新增範例（例如 `results.json` 範例結構），回覆說明你想補強的部分，我會把 `.github/copilot-instructions.md` 更新好。 
