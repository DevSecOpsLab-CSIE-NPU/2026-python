# AI_LOG

## 我問 AI 什麼

請幫我解決 `git push` 的 `orgin` 拼字錯誤，並協助我依照 TDD 流程完成 `0603-starter` 裡的 UVA 11417 GCD 題目。

## AI 給了什麼

修正了 git 指令拼寫，並為 `test_gcd.py` 提供三個測試案例（n=2, n=10, 還有 edge case n=1），以及在 `gcd.py` 實作了雙迴圈加總 `math.gcd(i, j)`。

## 我改了什麼

我要求 AI 必須嚴格遵守 TDD 流程：先將 `test_gcd.py` 中的 `sum_of_gcd` 引用解除註解，執行測試確認出現紅燈（ImportError），完成紅燈 Commit 後，才建立 `gcd.py` 進行實作並確認綠燈。
