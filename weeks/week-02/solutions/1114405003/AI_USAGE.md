# AI_USAGE

## 提問
1. 如何用 TDD 的方式實作 Task 1~3？
2. `sorted` key 應該怎麼寫才能實現多重排序？
3. `Counter` 與 `defaultdict` 哪個比較適合 log 統計？
4. unittest discover 為何顯示 NO TESTS RAN？
5. 要寫至少 9 個單測函式，應該如何拆分題目？

## 採用建議
- 直接從每一題先寫 3 個 unittest case，再實作程式。
- Task2 一定要用 `sorted(..., key=...)` 及 tuple 為排序依據。
- Task3 使用 `collections.Counter` 進行統計並排序。
- 對於 `m=0` 的空輸入要明確處理。

## 拒絕建議
- 不採用 `set` 直接去重（破壞順序）
- 不採用手寫巢狀迴圈做排序（題目要求 `sorted`）

## AI 可能誤導的案例
- AI 最初提出對 Task2 同分年齡撞名時 `x` 應先於 `c`，實際反而是按字母序 `c` 先。後來我自己根據題目規則修正。
