# AI_LOG

## 我問 AI 什麼

> 「請幫我寫 digit_root 的測試案例，至少 3 個（含 edge case 與例外案例），還有實作。」

## AI 給了什麼

> 給了 3 個測試案例：basic 測試一位數、edge case 測試多位數 199、例外測試 -1 會 raise ValueError。並給了 digit_root 的實作（迴圈相加到剩一位數）。

## 我改了什麼

> 原本 AI 的 basic 測試寫 `digit_root(0)` 預期回傳 0，但題目規定 n < 1 要 raise ValueError（0 < 1），所以我改成 `digit_root(5)` 預期回傳 5，符合規格。
