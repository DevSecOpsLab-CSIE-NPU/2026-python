# AI_USAGE

## 我問 AI 的問題（3~5 條）
1. Task 1 如何在不破壞順序下做去重？
2. Task 2 三層排序規則應該如何寫成 `sorted` 的 key？
3. Task 3 使用 `Counter` 與 `defaultdict` 的最佳分工是什麼？
4. 空輸入（特別是 Task 3 的 `m=0`）應該如何定義輸出？

## 我採用的建議
- 採用 `set + list` 保序去重。
- 採用 `(-score, age, name)` 處理多鍵排序。
- 採用 `defaultdict(int)` 做 user 次數統計，`Counter` 做 action 排名。

## 我拒絕的建議與原因
- 拒絕在 Task 1 直接用 `set(numbers)` 當去重輸出，因為題目要求保留第一次出現順序。
- 拒絕手寫巢狀交換排序，因為題目明確要求使用 `sorted(..., key=...)`。

## AI 可能誤導但我自行修正的案例
- AI 初版對 Task 3 的 top action 沒有定義同次數處理，會造成輸出不穩定。
- 我改為 `(-count, action)` 排序，確保同次數時輸出固定且可測試。
