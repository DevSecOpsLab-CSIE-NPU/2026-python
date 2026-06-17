# AI_LOG

## 我問 AI 什麼

我請 AI 協助完成 6/3 課堂暖身題（UVA 11417 GCD），需求包含：

1. 先讀題目與 starter。
2. 建立 `test_gcd.py`，至少 3 個測試。
3. 建立 `gcd.py` 並實作 `sum_of_gcd(n)`。
4. 檔案放到指定路徑：`weeks/week-15/solutions/0603-1114405015-簡嘉佑/0603/`。
5. 跑測試並保留可驗證結果。

## AI 給了什麼

AI 先讀了 `0603-warmup-drill.md` 與 starter，然後提供：

1. `test_gcd.py` 三個測試案例：
	- `n=2`，預期 `1`
	- `n=10`，預期 `67`
	- `n=1`（edge case），預期 `0`
2. `gcd.py` 的 `sum_of_gcd(n)` 實作：
	- 使用雙層迴圈列舉所有 `1 <= i < j <= n`
	- 以 `math.gcd(i, j)` 累加總和
3. 執行 `python -m unittest test_gcd.py`，得到 `Ran 3 tests ... OK`。

## 我改了什麼

我不是直接照貼，實際做了以下判斷與確認：

1. 確認 edge case 要保留 `n=1`，避免只測範例值。
2. 檢查實作是否符合題目條件 `i < j`，避免重複計算或含 `i=j`。
3. 確認檔案路徑放在老師指定的 solutions 目錄，而不是修改 starter。
4. 補上課堂要求文件（`AI_LOG.md`、`test_log.md`），確保提交流程完整。

## 驗證紀錄

- 執行指令：`python -m unittest test_gcd.py`
- 結果摘要：`Ran 3 tests in 0.000s`，`OK`
- 驗證重點：測試已涵蓋最小有效輸入、題目範例、與邊界條件。

## 這次學到的事

1. 先寫測試再寫實作，比較能快速確認邏輯是否偏題。
2. AI 給的內容要自己核對題目限制（尤其是迴圈範圍和 edge case）。
3. 題目會寫不難，但流程（測試、紀錄、PR）才是這次練習重點。
