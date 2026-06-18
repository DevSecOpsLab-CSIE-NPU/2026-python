# AI_LOG

## 我問 AI 什麼
1. 幫我進行 Pychon 專案的 6/18 搜尋效能實驗室 (Stage 1 至 Stage 5) 初始化與開發，並全程以「開發訪談助教」模式協作。
2. 請求協助實作符合測試規格的紅綠燈循環代碼（包括 `timing.py`、`search.py`、`benchmark.py`、`plot.py` 與對應的單元測試）。

## AI 給了什麼
1. 引導我對齊五個階段的所有細節規格，包括函式簽名、邊界、例外、邊角情況與紅燈定義。
2. 在規格完成對齊、並確認紅燈 commit 後，分別提供了 Stage 1 的 `@timeit` 裝飾器、Stage 2 的三種搜尋演算法、Stage 3 的內建與優化對照組及交叉點量測、Stage 4 的雷達圖繪製與 Stage 5 的防禦性安全性規則實作。

## 我改了什麼
1. **Stage 1**：確認裝飾器需使用 `functools.wraps` 以保護 metadata，並主動修正計時結果 `records` 屬性為「累積（append）」而 `last_elapsed` 屬性為「本次覆蓋（平均）」。
2. **Stage 2**：修正 `set_search` 的規格參數為 `list` 形式以保證與其他搜尋函式介面一致；設計了使用布林值 `(result_index != -1)` 的共同判準於 `subTest`，並在測試中以 copy 與 id 確保資料不被 mutate。
3. **Stage 3**：堅持內建對照組 `builtin_linear_search` 與 `builtin_binary_search` 的回傳型別也必須是 `int`（與 Stage 2 一致），以便直接加入 `SEARCH_FUNCTIONS` 共用測試；手動新增預測章節至 `README.md` 並先 commit 以通過 `git log --reverse` 順序驗證。
4. **Stage 4**：選取了「速度、預處理、空間、未排序支援、實作難度」等 5 個維度，並自訂了高分代表表現優異的轉化邏輯；設計 `test_plot.py` 來驗證繪圖輸出是否正確且檔案非空。
5. **Stage 5**：發現 `make_data(n)` 當 $N \le 0$ 時會默默回傳空 list，對後續搜尋演算法可能造成分母為零的致命漏洞；因此將安全測試設計為「動態拋出 ValueError」，並修補實作代碼以利全體測試轉綠。

---

## AI 反問我什麼 / 我怎麼回答

### Stage 1｜timeit 裝飾器
- **AI 問**：`timeit` 裝飾器如何定義？被裝飾函式的回傳值與 metadata 應該如何處理？`repeat` 參數代表什麼、預設值為多少？小於 1 應拋出什麼例外？計時結果記錄在哪裡？累積還是覆蓋？在這個階段，怎樣的測試結果會被判定為紅燈？
- **我答**：
  1. 採用三層裝飾器工廠，最外層 `timeit(repeat=3)`，使用 `@functools.wraps` 保留 metadata，回傳原函式最後一次結果。
  2. `repeat` 預設值為 3，當其 $<1$ 時應拋出 `ValueError`。必須使用 `raise` 而非 `assert`，防範 `-O` 模式失效。
  3. `records` 為累積 append 的 list，`last_elapsed` 為本次 repeat 的平均耗時。
  4. 紅燈是尚未建立 `timing.py` 導致 `test_timing.py` 發生 `ModuleNotFoundError`。

### Stage 2｜三種搜尋與量測
- **AI 問**：`linear_search`、`binary_search` 與 `set_search` 的簽名與回傳型別分別為何？`binary_search` 收到未排序 data 的行為？空 list、重複值、找不到的處理？在 `subTest` 裡打算用什麼共同判準？如何驗證不可修改傳入 data？紅燈為何？
- **我答**：
  1. 前兩者回 `int`，`set_search` 接收 `list` 回傳 `bool`。
  2. 未排序 binary search 行為屬 Undefined Behavior。
  3. 空陣列與找不到時 `int` 回 `-1`，`bool` 回 `False`。重複值 linear 回第一個，binary 允許回傳任一。
  4. 例外 `TypeError` 讓其自然拋出。
  5. 共同判準用 `(index != -1) == expected_exists` 比較。不可修改 data 用 copy 的內容與原 id 來 assert。
  6. 紅燈是尚未定義 `search.py` 導致 `test_search.py` 拋出 `ModuleNotFoundError`。

### Stage 3｜加速對照組與交叉點
- **AI 問**：內建 `in` 與 `bisect` 簽名與如何設計？優化版 set 搜尋介面如何設計？交叉點實驗在程式中如何計算？bisect 面對未排序的行為？加速前的預測與排名？什麼是第一個合格的紅燈 commit？
- **我答**：
  1. 內建對照組 `builtin_linear_search` 與 `builtin_binary_search` 的回傳型別維持 `int` 以利共用測試。
  2. 優化版 set 在 `benchmark.py` 迴圈外部先做 `prebuilt_set = set(data)` 轉換，不修改原有 `set_search` 函式。
  3. 線性總時間 $T = \text{queries} \times \text{linear}$；二元總時間 $T = \text{sort} + \text{queries} \times \text{binary}$。
  4. `bisect` 面對未排序也是 Undefined Behavior。
  5. 預測排名：`Set-Opt > Bisect > Built-in in`。預估 $Q=100$ 時交叉點 $N \approx 500 \sim 1000$ 之間。
  6. 紅燈是 `test_search.py` 新增對照組 import 卻無法導入，引發 `ImportError`。

### Stage 4｜雷達圖與報告
- **AI 問**：`plot.py` 提供什麼函式？從哪裡讀取數據並產生圖檔？雷達圖評估哪 5 個維度？如何將速度正規化？ results.json 遺失或 assets 目錄不存在如何處理？為什麼加 `matplotlib.use("Agg")`？如何測試與紅燈？
- **我答**：
  1. 提供 `generate_radar_chart` 讀取 `results.json` 並輸出 `assets/radar.png`。
  2. 5 維度：搜尋速度、預處理代價、記憶體節約度、未排序支援、實作難易度。速度用 Min-Max 正規化公式對齊至 1~5 分。
  3. results.json 遺失拋 FileNotFoundError，assets 目錄不存在自動建立。
  4. `Agg` 後端是為了支援無視窗環境（CI/CD）不崩潰。
  5. `test_plot.py` 驗證 PNG 檔案存在且大於 0 bytes。紅燈是 `ModuleNotFoundError: No module named 'plot'`。

### Stage 5｜安全性自掃
- **AI 問**：預期建立的 3 個安全測試簽名？`make_data(n)` 負數有何問題？`json` 為什麼比 `pickle` 安全（CWE弱點）？不使用 `with` 的洩漏？except: 的 Ctrl+C 衝擊？挑哪三個條目測試？如何引發紅燈？
- **我答**：
  1. 測試簽名包含驗證無 pickle、驗證無 assert 輸入驗證、驗證 `make_data` 拒絕非正整數。
  2. 負數時原 `range(n)` 回傳空 array 易引起後續越界與 ZeroDivisionError。應拋 ValueError。
  3. `json` 是純數據，`pickle` 反序列化（CWE-502）時會執行 arbitrary 程式碼。
  4. 不使用 `with` 會洩漏 File Descriptor。裸 `except:` 會吞掉 KeyboardInterrupt（無法 Ctrl+C）。
  5. 測試一、二以靜態讀檔正則驗證無 pickle 與無 assert；測試三動態測試 `make_data(0)` 與 `make_data(-10)` 期望拋 ValueError。
  6. 紅燈是動態測試 `make_data(0)` 沒有拋出 ValueError。
