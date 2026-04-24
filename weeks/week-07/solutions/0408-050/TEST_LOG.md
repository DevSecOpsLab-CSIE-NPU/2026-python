# UVA 10062 測試紀錄

## 執行指令
```bash
python -m unittest test_10062.py -v
```

## 執行輸出
```text
test_all_zeros (test_10062.TestUVA10062)
極端測試：所有牛前面「都沒有」比自己小的牛。 ... ok
test_general_case (test_10062.TestUVA10062)
基礎測試：驗證一般隨機排列的情況。 ... ok
test_increasing (test_10062.TestUVA10062)
極端測試：隊伍是完全遞增的狀態。 ... ok
test_minimum_cows (test_10062.TestUVA10062)
邊界測試：測試題目允許的最小 N 值 (N=2)。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功驗證了從後往前反推的邏輯，且樹狀陣列 (BIT) 搭配二元提升維護排名的機制運作正確。

<br>

# UVA 10071 (六元組問題) 測試紀錄

## 執行指令
```bash
python -m unittest test_10071.py -v
```

## 執行輸出
```text
test_no_solution (test_10071.TestUVA10071)
基礎測試：集合中只有一個非零數字，無法構成等式。 ... ok
test_simple_case (test_10071.TestUVA10071)
基礎測試：包含 0 和 1 的簡單情況。 ... ok
test_symmetric_case (test_10071.TestUVA10071)
進階測試：包含正負數與零的對稱情況。 ... ok
test_zero_only (test_10071.TestUVA10071)
邊界測試：集合中只有 0。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功利用中間相遇法 (Meet-in-the-middle) 搭配 `Counter` 驗證了六元組的組合計數，並能正確處理包含 0 與正負數的邊界情況。

<br>

# UVA 10093 (炮兵部隊) 測試紀錄

## 執行指令
```bash
python -m unittest test_10093.py -v
```

## 執行輸出
```text
test_all_mountains (test_10093.TestUVA10093)
邊界測試：全是山地 (H)。 ... ok
test_classic_example (test_10093.TestUVA10093)
經典範例測試： ... ok
test_single_row_plains (test_10093.TestUVA10093)
基礎測試：只有單列且全是平原 (P)。 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.015s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功利用狀態壓縮 DP (State Compression DP) 與位元運算處理攻擊範圍及地形遮罩，正確計算出最大佈署數量。

<br>

# UVA 10101 (火柴棒問題) 測試紀錄

## 執行指令
```bash
python -m unittest test_10101.py -v
```

## 執行輸出
```text
test_larger_numbers (test_10101.TestUVA10101)
測試較大數字的轉換。 ... ok
test_move_between_digits (test_10101.TestUVA10101)
測試在不同數字間移動火柴（一增一減）。 ... ok
test_move_within_digit_lhs (test_10101.TestUVA10101)
測試在等號左側、單一數字內移動火柴。 ... ok
test_move_within_digit_rhs (test_10101.TestUVA10101)
測試在等號右側、單一數字內移動火柴。 ... ok
test_negative_numbers (test_10101.TestUVA10101)
測試包含負數的情況。 ... ok
test_no_solution (test_10101.TestUVA10101)
測試確定無解的情況。 ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

## 結論
共執行 6 個測試案例，全數通過 (Green)。測試涵蓋了在等號左側、右側的數字內部移動火柴，以及跨數字移動火柴（一增一減）的核心邏輯。同時也驗證了包含負數、較大數字以及無解的邊界情況，確認演算法的正確性與穩健性。

<br>

# UVA 10170 (無限房間旅館) 測試紀錄

## 執行指令
```bash
python -m unittest test_10170.py -v
```

## 執行輸出
```text
test_large_input (test_10170.TestUVA10170)
極端測試：極大的 D，驗證程式是否會超時 (Time Limit Exceeded) ... ok
test_minimum_input (test_10170.TestUVA10170)
邊界測試：查詢非常早期的天數 ... ok
test_sample_case_1 (test_10170.TestUVA10170)
題目範例測試 1 ... ok
test_sample_case_2 (test_10170.TestUVA10170)
題目範例測試 2 ... ok
test_simple_case (test_10170.TestUVA10170)
基礎測試：從 1 開始的簡單累加 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)。成功利用等差數列公式搭配 O(log N) 的二分搜尋法 (Binary Search) 來解題，並且順利通過了 $10^{15}$ 極端大測資的考驗，不會發生超時 (TLE) 的問題。