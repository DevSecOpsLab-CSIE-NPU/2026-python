# UVA 10041 測試紀錄

## 執行指令
```bash
python -m unittest test_10041.py -v
```

## 執行輸出
```text
test_duplicates (test_10041.TestUVA10041)
陷阱測試：包含重複的門牌號碼。 ... ok
test_sample_1 (test_10041.TestUVA10041)
基礎測試 1：題目提供的第一組測資。 ... ok
test_sample_2 (test_10041.TestUVA10041)
基礎測試 2：題目提供的第二組測資。 ... ok
test_single_relative (test_10041.TestUVA10041)
邊界測試：只有一個親戚的情況。 ... ok
test_unsorted_and_even (test_10041.TestUVA10041)
進階測試：未排序的偶數個元素。 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)，成功驗證了透過中位數計算距離總和的最佳解法，且未排序或帶有重複數字的測資皆能正確處理。

<br>

# UVA 10050 測試紀錄

## 執行指令
```bash
python -m unittest test_10050.py -v
```

## 執行輸出
```text
test_holiday_only_hartals (test_10050.TestUVA10050)
假日陷阱測試：罷會剛好都落在假日 (星期五或星期六)。 ... ok
test_large_days (test_10050.TestUVA10050)
極端值測試：模擬一年 (365天) ... ok
test_no_parties (test_10050.TestUVA10050)
邊界測試：若政黨沒有提交任何罷會參數 (空陣列)。 ... ok
test_overlapping_hartals (test_10050.TestUVA10050)
重疊測試：多個政黨在同一天罷會，只能算損失 1 個工作天。 ... ok
test_sample_case (test_10050.TestUVA10050)
基礎測試：題目敘述中提供的範例。 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)，成功利用集合 (Set) 去重，並正確過濾了星期五與星期六的假日罷會。

<br>

# UVA 10055 測試紀錄

## 執行指令
```bash
python -m unittest test_10055.py -v
```

## 執行輸出
```text
test_all_increasing (test_10055.TestUVA10055)
基礎測試：初始狀態下，所有函數都是增函數 (0)。 ... ok
test_edge_case_single_element (test_10055.TestUVA10055)
邊界測試：查詢區間長度只有 1 的情況。 ... ok
test_multiple_flips_and_parity (test_10055.TestUVA10055)
進階測試：奇偶性與 XOR 邏輯。 ... ok
test_single_flip (test_10055.TestUVA10055)
基礎測試：反轉一個函數的增減性。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功利用樹狀陣列 (BIT) 維護函數的狀態，且奇偶性與 XOR (異或) 反轉邏輯運作完美。

<br>

# UVA 10056 測試紀錄

## 執行指令
```bash
python -m unittest test_10056.py -v
```

## 執行輸出
```text
test_one_probability (test_10056.TestUVA10056)
邊界測試：如果成功機率為 1，第 1 個玩家擲骰子必定直接獲勝，後面的玩家勝率皆為 0。 ... ok
test_sample_case_1 (test_10056.TestUVA10056)
基礎測試 1：兩個玩家，成功機率約為 1/6 (0.166666)，求第 1 個玩家獲勝的機率。 ... ok
test_sample_case_2 (test_10056.TestUVA10056)
基礎測試 2：兩個玩家，成功機率約為 1/6 (0.166666)，求第 2 個玩家獲勝的機率。 ... ok
test_zero_probability (test_10056.TestUVA10056)
陷阱測試：如果單次成功的機率為 0，任何玩家都不可能獲勝。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功利用無窮等比級數公式解決機率計算，且妥善處理了 `p=0` 的除以零防護及 `p=1` 的邊界情況。

<br>

# UVA 10057 測試紀錄

## 執行指令
```bash
python -m unittest test_10057.py -v
```

## 執行輸出
```text
test_even_elements_distinct_medians (test_10057.TestUVA10057)
基礎測試 2：偶數個元素，且中間兩個數字不同。 ... ok
test_even_elements_same_medians (test_10057.TestUVA10057)
陷阱測試：偶數個元素，但中間兩個數字相同。 ... ok
test_odd_elements (test_10057.TestUVA10057)
基礎測試 1：奇數個元素。 ... ok
test_unsorted_elements (test_10057.TestUVA10057)
進階測試：未排序的輸入。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功利用中位數邏輯計算出最小最佳 A、對應的元素個數以及可能值的組合數，並能正確處理奇偶數及未排序的輸入。