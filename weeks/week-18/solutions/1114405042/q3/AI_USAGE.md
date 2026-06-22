# AI Usage - Q3: Digit Root (Base 16)

## 我問的問題
1. 數字根的數學公式是什麼（任意進位制）？
2. base-16 的 digit root 公式怎麼推導？

## 採用的建議
1. `1 + (n - 1) % (BASE - 1)` 公式，其中 BASE=16 → `% 15`
2. `n == 0` 單獨處理回傳 0
3. `n < 0` raise `ValueError`

## 自行修正案例
第一次測資寫 `digit_root_base16(100) == 1`，但 100 = 0x64 → 6+4=10，正確應為 10。修正測試後通過。
