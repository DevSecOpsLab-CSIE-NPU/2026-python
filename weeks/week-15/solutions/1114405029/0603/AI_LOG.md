# AI_LOG

## 我問 AI 什麼

請幫我分析 UVA 11417 GCD 題目需求，說明題目要計算的內容，協助設計 unittest 測試案例（至少包含 1 個 edge case），並依照課堂要求的 TDD（Test-Driven Development）流程完成實作。另外請協助撰寫 gcd.py，使用函式結構與詳細繁體中文註解，並說明如何完成 Red → Green 的開發流程。

## AI 給了什麼

AI 先分析 UVA 11417 題目，說明需要計算所有滿足 1 ≤ i < j ≤ n 的配對之最大公因數（GCD）總和。

AI 提供了多個測試案例，包括：

* n = 1（edge case）
* n = 2
* n = 3
* n = 4
* n = 10（題目範例）

並提供 unittest 測試程式架構，以及 gcd.py 的函式實作，使用 Python 內建的 math.gcd() 計算所有合法配對的最大公因數總和。

AI 同時說明 TDD 的流程應為：

Red（測試失敗） → Test Commit → Green（測試成功） → Feature Commit。

## 我改了什麼

我先檢查 AI 提供的測試案例是否符合題目需求，確認除了題目範例 n=10 外，也保留 n=1 作為 edge case，驗證當不存在任何 (i,j) 配對時，函式是否能正確回傳 0。

在實作過程中，我發現自己已經先建立了 gcd.py 並完成實作，但這不符合課堂要求的 TDD 流程。因此我主動刪除 gcd.py，重新執行測試，確認出現：

ModuleNotFoundError: No module named 'gcd'

確保測試處於 Red（紅燈）狀態。

之後我先完成：

test: add failing tests for UVA 11417 GCD

再重新建立 gcd.py，完成 sum_of_gcd() 函式實作，並再次執行測試確認：

Ran 5 tests

OK

確認所有測試通過後，再完成：

feat: implement UVA 11417 GCD

藉此確保 commit 順序、Red → Green 流程以及 TDD 開發方式符合課堂 SOP 與期末考要求，而不是直接依照 AI 產生的結果一次完成實作。
