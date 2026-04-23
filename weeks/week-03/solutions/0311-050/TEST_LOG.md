# UVA 118 測試紀錄

## 執行指令
```bash
python -m unittest test_118.py -v
```

## 執行輸出
```text
test_rotation_and_movement (test_118.TestUVA118)
基礎功能測試：驗證機器人的轉向 (L/R) 與前進 (F) 邏輯是否正確 ... ok
test_sample_case (test_118.TestUVA118)
測試 UVA 118 題目提供的標準測資 ... ok
test_scent_rule_different_direction (test_118.TestUVA118)
邊界陷阱測試：同座標但「不同方向」不該共用 scent ... ok
test_scent_rule_same_direction (test_118.TestUVA118)
進階規則測試： scent (標記) 規則 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功涵蓋了基礎移動、範例測資、以及 `scent` 標記規則（包含同向與不同向）的驗證。

<br>

# UVA 272 測試紀錄

## 執行指令
```bash
python -m unittest test_272.py -v
```

## 執行輸出
```text
test_multi_line_quotes (test_272.TestUVA272)
邊界陷阱測試：測試跨行的引號替換。 ... ok
test_no_quotes (test_272.TestUVA272)
基礎測試：測試完全沒有雙引號的情況。 ... ok
test_sample_case (test_272.TestUVA272)
測試題目給定的標準範例。 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功驗證了單行多引號替換、跨行引號狀態的維持以及無引號情況下對原始字串的保護。

<br>

# UVA 299 測試紀錄

## 執行指令
```bash
python -m unittest test_299.py -v
```

## 執行輸出
```text
test_already_sorted (test_299.TestUVA299)
基礎測試：測試已經排好序的車廂。 ... ok
test_edge_cases (test_299.TestUVA299)
邊界情況測試： ... ok
test_sample_case (test_299.TestUVA299)
測試基礎的車廂排列情況。 ... ok
test_worst_case (test_299.TestUVA299)
效能與極端值測試： ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功利用氣泡排序計數驗證了相鄰交換邏輯，極端測資 (L=50的逆序排列) 也順利計算出 1225 次。

<br>

# UVA 490 測試紀錄

## 執行指令
```bash
python -m unittest test_490.py -v
```

## 執行輸出
```text
test_different_lengths (test_490.TestUVA490)
測試長度不一的字串 (UVA 490 核心陷阱)。 ... ok
test_sample_case (test_490.TestUVA490)
測試題目基礎範例。 ... ok
test_single_line (test_490.TestUVA490)
邊界測試：只有單行字串的旋轉。 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功涵蓋了不同長度字串的空白填補、標準測資及單行邊界情況。