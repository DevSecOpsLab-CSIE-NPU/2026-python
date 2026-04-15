# AI_USAGE

## 1) 我問了哪些問題

- 如何依照作業規格拆成可測試的函式介面？
- Task 2 多條件排序的 key 要怎麼寫才不會漏 tie-break？
- Task 3 在 m=0 時輸出格式該怎麼設計較一致？
- unittest 要如何組織成可 discover 的測試結構？
- 怎麼在不破壞順序下完成去重？

## 2) 我採用的 AI 建議

- 先定義 pure function，再把 stdin/stdout 留給 main。
- Task 2 使用 sorted(students, key=lambda s: (-s[1], s[2], s[0]))。
- 測試中加入正常、邊界、反例，避免只測 happy path。

## 3) 我拒絕的 AI 建議

- 拒絕直接用 set 輸出 Task 1 去重結果，因為會破壞原始順序且不符合題目限制。
- 拒絕手寫雙層迴圈交換排序，因為題目要求要用 sorted(key=...)。

## 4) 一個 AI 可能誤導但我修正的案例

- AI 初版建議 Task 3 top_action 直接用 Counter.most_common(1)。
- 這在同次數時的 tie-break 並不明確，可能受插入順序影響。
- 我改成 sorted(action_counter.items(), key=lambda p: (-p[1], p[0]))[0]，保證同次數時 action 名稱小者優先。
