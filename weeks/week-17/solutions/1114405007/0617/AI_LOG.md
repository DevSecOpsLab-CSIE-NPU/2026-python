# AI_LOG — 0617 timeit + 搜尋評估預演

## 我問 AI 什麼

> 【任務一】「請幫我拆 timeit 裝飾器的 test case，≥3 個（含 ≥1 個 edge case），並逐一實作測試與程式。」
> 【任務二】「請幫我拆 linear_search + binary_search 的 test case，≥3 個（含 ≥1 個 edge case）。」

## AI 給了什麼

> 【任務一】以開發訪談助教模式反問規格檢查表五項，確認後給出 7 個 test case，紅燈→綠燈完成 timing.py。
> 【任務二】反問簽名、邊界、例外、edge、驗收後給出 19 個 test case，實作 search.py 並跑 benchmark。

## 我改了什麼

> 【任務一】修正 `repeat` 預設值從 1 改為 3（符合規格），決定 repeat 非 int 應 raise TypeError 而非 ValueError，補充「被裝飾函式有副作用」edge case。
> 【任務二】binary_search 預設回傳中間 index，我確認規格後改為「找第一個匹配」讓 duplicates 測試通過。

## AI 反問我什麼 / 我怎麼回答

| AI 問的問題 | 我的回答 |
|---|---|
| `timeit` 簽名與回傳型別？ | 分層裝飾器 `timeit(repeat=3)`，回傳包裝後的函式，維持原回傳值 |
| 輸入範圍與邊界？ | `repeat` 必須是 `int`，`>= 1` |
| 例外行為？ | `repeat < 1` → `ValueError`，非 `int` → `TypeError`，用 `raise` 不用 `assert` |
| Edge cases？ | repeat=1（邊界）、函式拋例外（不該被吞）、副作用（確認執行次數） |
| 驗收標準？ | 先紅燈（測試先錯）→ 綠燈（實作通過） |
| 為什麼取「平均」？ | 反映真實典型效能，不受快取最佳狀態影響，便於標準化比較 |
| 為什麼驗證在裝飾時間拋出？ | Fail fast，設定錯誤在定義時就發現，不需等到呼叫 |
| `search.py` target 是否限制型別？ | 不限，只要能與 data 元素比較即可 |
| 重複元素回傳哪個 index？ | linear_search 回傳第一個 |
| binary_search 排序方向？ | 只保證升序 |
| Edge cases 有哪些？ | 目標在頭/尾、單元素 list、全部元素相同 |
| 誰快？差多少？ | n=1M 時 binary 快約 9000 倍（3μs vs 28ms） |
| 排序 + binary 划不划算？ | 單次不划算（排序 0.18s > linear 0.028s），查詢 ≥7 次後開始划算 |
