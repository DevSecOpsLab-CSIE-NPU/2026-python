# TEST_CASES.md — Data Cleaning（D=3）

## 1. 一般情況（正常輸入，含重複值）

輸入：
```
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

預期輸出：
```
6 9
3
```

實際輸出：
```
6 9
3
```

結果：PASS
對應測試：`tests/test_clean_sequence.py::test_dedup_filter_sort_sample1`、`test_dedup_filter_sort_sample2`
說明：這是題目自算範例（D=3），同時驗證「去重保序 → 篩選 → 排序」三步驟順序是否正確。

## 2. 邊界情況（單一元素）

輸入：
```
1
3
0
```

預期輸出：
```
3
```

實際輸出：
```
3
```

結果：PASS
對應測試：`tests/test_clean_sequence.py::test_single_element`
說明：長度為 1 時容易因切片/比較邏輯漏掉邊界，需單獨驗證。

## 3. 重複值情況（去重保序）

輸入：
```
5
6 3 6 9 3
0
```

預期輸出：
```
3 6 9
```

實際輸出：
```
3 6 9
```

結果：PASS
對應測試：`tests/test_clean_sequence.py::test_duplicates_preserve_first_then_filter`
說明：驗證去重發生在篩選之前，且保留「第一次出現」的那個值，不是任意保留。

## 4. 反例（負數整除，容易寫錯的情況）

輸入：
```
3
-9 -3 2
0
```

預期輸出：
```
-9 -3
```

實際輸出：
```
-9 -3
```

結果：PASS
對應測試：`tests/test_clean_sequence.py::test_negative_divisible`
說明：Python 的 `%` 對負數依數學定義成立（`-9 % 3 == 0`），但若改用 C 風格的截斷除法概念去手刻整除判斷，容易誤判負數情況，所以特別點名測試。

## 5. 最能測出錯誤的一組（n=0 立即結束 + 無命中 NONE 的組合）

輸入：
```
0
```

預期輸出：（無任何輸出，包含空行）

實際輸出：（無任何輸出）

結果：PASS
對應測試：`tests/test_main.py::test_main_n_zero_immediately_produces_no_output`
說明：這組最容易出包，因為直覺寫法常會「先讀 n 再不管三七二十一印一行」，或誤把迴圈寫成讀到 EOF 而非讀到 n=0 才停；也最容易在多組輸出時不小心多印一個空行。
