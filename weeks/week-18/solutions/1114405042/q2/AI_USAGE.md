# AI Usage - Q2: Caesar Cipher (SHIFT=3)

## 我問的問題
1. Python 中字母循環位移（wraparound）怎麼實現？
2. `ord()` / `chr()` 用法？
3. 大寫小寫如何分開處理？

## 採用的建議
1. `chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a'))` 公式
2. 分別判斷 `'a' <= ch <= 'z'` 和 `'A' <= ch <= 'Z'`
3. 非字母直接 `else: result.append(ch)`

## 自行修正案例
AI 建議用 `sys.stdin.read()` 取代 `readline()`，但題目只有一行輸入，`readline()` 更精確。
