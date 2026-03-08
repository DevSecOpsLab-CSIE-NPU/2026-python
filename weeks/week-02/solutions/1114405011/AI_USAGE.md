# AI_USAGE

## 我問 AI 的問題
- 如何把 Task 1 拆成可測試的函式?
- Task 2 的同分排序（score/age/name）要怎麼設計測試?
- Task 3 的 `m=0` 邊界測試要如何寫?
- `unittest discover` 在這個資料夾怎麼跑?

## 我採用的建議
- 先測試再實作（Red -> Green -> Refactor）
- 將 I/O 與邏輯分離（parse/process/format）
- 先補齊每題測試案例，再逐題完成實作
- Task 2 用 `sorted(..., key=...)` 寫多條件排序，避免手寫交換排序
- Task 3 用 `defaultdict + Counter` 處理使用者與動作統計

## 我拒絕的建議
- 直接跳過 Red 測試、先把三題程式一次寫完。
- 原因: 不符合本作業 TDD 要求，也不利於定位錯誤。

## AI 可能誤導但我修正的案例
- Task 3 初版未明確定義 top action 同分規則，我補上「同分取字母序較小」讓測試可穩定驗證。
- Task 2 初版排序只考慮分數高低，導致同分時順序錯誤；我改成 `(-score, age, name)` 才符合題目規格。
- Task 1 初版我只檢查正常輸入，差點忽略空字串輸入；後來加上邊界測試並在 `parse_input` 先處理空輸入。
