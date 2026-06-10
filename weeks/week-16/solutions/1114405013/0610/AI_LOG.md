# AI_LOG

我問 AI 什麼

```text
https://github.com/DevSecOpsLab-CSIE-NPU/2026-python/blob/main/weeks/week-16/in_class/0610-timed-drill.md
看一下這個告訴我接下來應該要怎麼規劃？
跟 AI 拆 ≥3 個 test case（含 ≥1 個 edge case）
那就先用這個
請幫我把 digit_root(n) 這題拆成至少 3 個 pytest 測試案例，必須包含：
1. 至少 1 個基本案例
2. 至少 1 個 edge case
3. 至少 1 個錯誤輸入案例
...

## AI 給了什麼

AI 建議了 3 個必要測試：基本案例 `38 -> 2`、edge case `1 -> 1`、錯誤輸入 `0` 應該 raise `ValueError("n must be >= 1")`，另外建議可以加第 4 個大數 edge case `2_000_000_000 -> 2`。

## 我改了什麼

- 我把 AI 建議的 pytest 寫法改成 starter 檔案使用的 `unittest` 寫法，讓它可以用 `python -m unittest` 執行。
- 我保留基本案例 `38 -> 2`，確認多位數會反覆加總到一位數。
- 我加入兩個 edge case：`1 -> 1` 測最小合法輸入，`2_000_000_000 -> 2` 測題目給定的最大合法輸入。
- 我加入例外案例 `0`，並用 `assertRaisesRegex` 檢查錯誤訊息必須是一字不差的 `n must be >= 1`。
- 實作時我選擇用迴圈反覆加總各位數，符合題目描述，沒有使用數字根公式。
