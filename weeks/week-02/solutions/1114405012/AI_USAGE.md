# AI_USAGE

## 1) 我問了哪些問題（3~5 條）

1. 如何在不破壞順序下做去重？
2. `sorted(..., key=...)` 如何同時處理「分數降序、年齡升序、姓名升序」？
3. `Counter` 在空資料時如何安全取得最常見元素？
4. `unittest` 的測試案例如何覆蓋正常、邊界、反例？
5. 如何把邏輯拆成可測試函式（非全部寫在 `main`）？

## 2) AI 給的建議中我有採用的

- Task 1 採用「`set` 僅做 membership 判斷 + `list` 保序」的去重方式。
- Task 2 採用 `sorted(students, key=lambda x: (-x[1], x[2], x[0]))` 進行多條件排序。
- Task 3 採用 `Counter` 統計 user/action 次數，再做 tie-break 排序。
- 將每題拆成 `parse -> core logic -> format -> solve`，提高測試可讀性。

## 3) AI 建議中我拒絕的（含原因）

- 拒絕「Task 1 直接把 `set(numbers)` 當去重答案」：因為會破壞原始順序，不符合規格。
- 拒絕「Task 2 用手寫巢狀迴圈交換排序」：題目明確要求使用 `sorted(..., key=...)`。
- 拒絕「Task 3 空輸入時丟例外」：規格要求可處理 `m=0`，需有可輸出結果。

## 4) 1 個 AI 可能誤導但我自行修正的案例

AI 曾建議在環境中用 `python -m unittest` 直接執行，但目前機器只有 `python3` 指令，導致第一次命令失敗。我改成 `python3 -m unittest ...`，並在文件中統一使用 `python3`，避免重複發生執行錯誤。
