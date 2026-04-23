# UVA 948 測試紀錄

## 執行指令
```bash
python -m unittest test_948.py -v
```

## 執行輸出
```text
test_complex_logic_deduction (test_948.TestUVA948)
進階邏輯測試：需要綜合多次秤重結果才能找出假幣的情況。 ... ok
test_single_weighing_equal (test_948.TestUVA948)
基礎測試：測試單次秤重且結果相等 (=) 的情況。 ... ok
test_undetermined_fake_coin (test_948.TestUVA948)
無法判定測試：測試線索不足以找出唯一假幣的情況。 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功涵蓋單次相等排除、線索不足及多步邏輯交集推導。

<br>

# UVA 948 (手打版) 測試紀錄

## 執行指令
```bash
python q948-Hand.py < input.txt
```

## 執行輸出與結論
確認手打版的 `q948-Hand.py` 透過標準輸入 (STDIN) 讀取測資測試，能夠正確產出與原版相同的推導結果，無語法錯誤且邏輯排除判斷正確。

<br>

# UVA 10008 測試紀錄

## 執行指令
```bash
python -m unittest test_10008.py -v
```

## 執行輸出
```text
test_basic_counting_and_sorting (test_10008.TestUVA10008)
基礎測試：驗證基本的字元統計以及雙重排序邏輯。 ... ok
test_case_insensitivity (test_10008.TestUVA10008)
大小寫不敏感測試： ... ok
test_ignore_non_alphabet (test_10008.TestUVA10008)
過濾字元測試： ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功驗證了 `Counter` 搭配 `lambda` 的雙重排序邏輯以及非字母的過濾機制。

<br>

# UVA 10008 測試紀錄

## 執行指令
```bash
python -m unittest test_10008.py -v
```

## 執行輸出
```text
test_basic_counting_and_sorting (test_10008.TestUVA10008)
基礎測試：驗證基本的字元統計以及雙重排序邏輯。 ... ok
test_case_insensitivity (test_10008.TestUVA10008)
大小寫不敏感測試： ... ok
test_ignore_non_alphabet (test_10008.TestUVA10008)
過濾字元測試： ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## 結論
共執行 3 個測試案例，全數通過 (Green)，成功利用 `Counter` 與 `lambda` 雙重排序完美驗證頻率降冪及字母升冪之邏輯，且大小寫過濾機制運作正常。

<br>

# UVA 10019 測試紀錄

## 執行指令
```bash
python -m unittest test_10019.py -v
```

## 執行輸出
```text
test_equal_soldiers (test_10019.TestUVA10019)
邊界測試：兩軍士兵數量相等的情況，預期差值為 0。 ... ok
test_hashmat_greater_than_enemy (test_10019.TestUVA10019)
反向測試：雖然題目敘述中提到「Hashmat 的士兵數絕不會比敵人的士兵數大」， ... ok
test_hashmat_less_than_enemy (test_10019.TestUVA10019)
基礎測試：Hashmat 的士兵數量少於敵人士兵數量的情況。 ... ok
test_large_numbers (test_10019.TestUVA10019)
極端值測試：測資保證數字不會超過 2^63 (題目上的 263 實際上是 2^63 的排版遺失)。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功驗證了絕對值 `abs()` 計算與 Python 大數運算的準確性。

<br>

# UVA 10035 測試紀錄

## 執行指令
```bash
python -m unittest test_10035.py -v
```

## 執行輸出
```text
test_different_lengths_and_chain_carry (test_10035.TestUVA10035)
進階/邊界測試：兩個數字長度不同，且產生「連鎖進位」的情況。 ... ok
test_multiple_carries (test_10035.TestUVA10035)
複數進位測試：發生 2 次以上進位的情況。 ... ok
test_no_carry (test_10035.TestUVA10035)
基礎測試：沒有任何進位發生的情況。 ... ok
test_one_carry (test_10035.TestUVA10035)
單數進位測試：只有發生 1 次進位的情況。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)，成功驗證了長度不同的連鎖進位處理以及 `No/1/N` 的單複數字串格式化結果。

<br>

# UVA 10038 測試紀錄

## 執行指令
```bash
python -m unittest test_10038.py -v
```

## 執行輸出
```text
test_duplicate_diffs (test_10038.TestUVA10038)
陷阱測試：相鄰差值重複，導致並未涵蓋 1 到 n-1。 ... ok
test_jolly_example (test_10038.TestUVA10038)
基礎測試：題目提供的 Jolly 範例。 ... ok
test_not_jolly_example (test_10038.TestUVA10038)
基礎測試：題目提供的 Not jolly 範例。 ... ok
test_out_of_bounds_diffs (test_10038.TestUVA10038)
陷阱測試：差值超出了 1 到 n-1 的範圍。 ... ok
test_single_element (test_10038.TestUVA10038)
邊界測試：序列長度 n=1。 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)，成功驗證了 Jolly/Not jolly 的基本判斷、n=1 的邊界情況，以及差值重複/越界的陷阱。