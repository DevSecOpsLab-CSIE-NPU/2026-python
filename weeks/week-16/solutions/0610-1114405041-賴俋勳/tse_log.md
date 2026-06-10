# TSE Log

## 檔案位置
- weeks/week-16/solutions/0610-1114405041-賴俋勳

## 我做了什麼
1. 依題目規格檢查 `digit_root(n: int) -> int` 行為。
2. 檢查例外規格是否精確符合：當 n < 1 時，必須丟出 ValueError("n must be >= 1")。
3. 檢查測試是否至少包含：基本案例、edge case、例外案例。
4. 實際執行 unittest 驗證程式可執行且測試全綠。
5. 額外做函式直接呼叫驗證輸出值。

## 測試內容
- 基本案例：digit_root(199) == 1
- Edge case（一位數）：digit_root(5) == 5
- Edge case（大數）：digit_root(2_000_000_000) == 2
- 例外案例：digit_root(0) 觸發 ValueError，且訊息精確為 n must be >= 1

## 實際執行指令與結果
1. 指令：python -m unittest -v
   - 結果：Ran 4 tests in 0.002s，OK
2. 指令：python -c "from digit_root import digit_root; print(digit_root(24), digit_root(9999))"
   - 結果：輸出 6 9

## 結論
- 已完成題目要求。
- 程式可執行，且測試全數通過。
