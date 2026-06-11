# AI_LOG

複製此檔到自己的 PR 根目錄，改名為 `AI_LOG.md` 後填寫。

期末考也會用這個格式，請熟練。

---

## 我問 AI 什麼

> 請幫我用 unittest 寫 timeit 裝飾子的測試，至少 3 個案例，測試 last_elapsed、records 累積、回傳值不變。

## AI 給了什麼

> 給了 3 個測試案例（從未呼叫、呼叫一次多次、回傳值不變），但沒寫裝飾器內不准 print 的驗證。

## 我改了什麼

> 我自己加了 `timeit` 裝飾器內不准 `print` 的測試，並確認 `last_elapsed` 和 `records` 正確記錄耗時。

---

## 我問 AI 什麼

> 請幫我寫三種排序函式（bubble、quick、merge）的 unittest，至少 3 個 test case 含 edge case，並確保不會 mutate 輸入。

## AI 給了什麼

> 給了 3 個測試案例（空 list、單元素、重複值），但沒寫「不可修改傳入 list」的驗證。

## 我改了什麼

> 我自己加了測試輸入 list 是否被 mutate 的驗證，並增加了負數、已排序、反序等 edge case。

---

## 我問 AI 什麼

> 請幫我寫 benchmark.py，包含 make_data(n, seed) 固定 seed、run_benchmark(sizes, repeats) 用 @timeit 量測平均、輸出比較表並存 results.json。

## AI 給了什麼

> 給了 benchmark.py 骨架，但沒寫 `make_data` 驗證 n 必須是正整數。

## 我改了什麼

> 我自己在 `make_data` 加上了 `if not isinstance(n, int) or n <= 0: raise ValueError` 的驗證。

---

## 我問 AI 什麼

> 請幫我寫 plot.py，讀 results.json 畫折線圖(y 軸 log scale),輸出 assets/benchmark.png。測試需驗證 PNG 產生且非空檔。

## AI 給了什麼

> 給了 plot.py 骨架，但沒寫 `load_results` 處理 missing file / invalid json 的 exception handling。

## 我改了什麼

> 我自己在 `load_results` 加上了 exception handling，確保 FileNotFoundError 和 JSONDecodeError 能被正確捕捉。

---

## 我問 AI 什麼

> 請幫我用 OpenSSF Secure Coding Guide for Python 掃 Stage 1–4 程式,找出安全問題，寫會紅的測試。

## AI 給了什麼

> 給了 3 個 OpenSSF 條目建議（08 Coding Standards、05 Exception Handling、04 Neutralization），但沒寫具體的 failing 測試。

## 我改了什麼

> 我自己寫了 5 個 failing 測試（包含 make_data 驗證、run_benchmark 驗證、load_results exception handling），並在 Stage 5 綠燈後 commit。

---

## 評分提示

| 「我改了什麼」內容 | 期末考此項得分 |
|---|---|
| 空白或「沒改」 | 0 分 |
| 「改了變數名」「調整縮排」這類無關判斷 | 部分分 |
| 有明確判斷（補測試、發現 AI 寫錯、改例外處理） | 滿分 |

→ AI 不會永遠對。**期末考要你證明你看得出來。**

---