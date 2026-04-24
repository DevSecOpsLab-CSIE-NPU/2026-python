# UVA 10189 (Minesweeper) 測試紀錄

## 執行指令
```bash
python -m unittest test_10189.py -v
```

## 執行輸出
```text
test_all_mines (test_10189.TestUVA10189)
邊界測試：全是地雷的極端情況 ... ok
test_no_mines (test_10189.TestUVA10189)
邊界測試：完全沒有地雷 ... ok
test_sample_case_1 (test_10189.TestUVA10189)
測試題目範例 1：4x4 網格 ... ok
test_sample_case_2 (test_10189.TestUVA10189)
測試題目範例 2：3x5 網格 ... ok
test_single_cell (test_10189.TestUVA10189)
邊界測試：最小的 1x1 網格 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)。利用偏移量 `dx`, `dy` 的雙層迴圈掃描策略，能夠精準地在不越界的情況下計算周圍八個方位的地雷總數。並成功處理全為地雷、毫無地雷以及極端大小的網格情況。

<br>

# UVA 10190 (自動傘與降雨量) 測試紀錄

## 執行指令
```bash
python -m unittest test_10190.py -v
```

## 執行輸出
```text
test_full_cover (test_10190.TestUVA10190)
邊界測試：一把傘完全遮住整條馬路 ... ok
test_no_umbrellas (test_10190.TestUVA10190)
邊界測試：完全沒有自動傘 ... ok
test_overlapping_static (test_10190.TestUVA10190)
進階測試：多把傘重疊，靜止不動 ... ok
test_partial_static (test_10190.TestUVA10190)
基礎測試：一把靜止的傘遮住一半馬路 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)。此解法採用一維區間合併演算法，將所有傘的覆蓋範圍視為線段，透過排序與合併計算出總遮蔽長度，進而推算出總降雨體積。此方法可正確處理所有靜態（v=0）的測試案例。

<br>

# UVA 10193 測試紀錄

## 執行指令
```bash
python -m unittest test_10193.py -v
```

## 執行輸出
```text
test_a_is_1 (test_10193.TestUVA10193)
基礎測試：a = 1 ... ok
test_a_is_2 (test_10193.TestUVA10193)
基礎測試：a = 2 ... ok
test_composite_N (test_10193.TestUVA10193)
進階測試：a=12, 此時 a^2+1 = 145 為合成數 ... ok
test_large_a (test_10193.TestUVA10193)
邊界測試：測試較大的 a 值，例如 a = 100 ... ok
test_prime_N (test_10193.TestUVA10193)
進階測試：a=20, 此時 a^2+1 = 401 為質數 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)。程式成功利用因數分解的數學推導，找出使得 $x+y$ 最小的最接近因數對，正確計算出了所有的 `b+c` 最小值，同時涵蓋了 $N$ 為質數和合成數的情況。

<br>

# UVA 10221 (Satellites) 測試紀錄

## 執行指令
```bash
python -m unittest test_10221.py -v
```

## 執行輸出
```text
test_180_degrees (test_10221.TestUVA10221)
邊界測試：角度為 180 度 ... ok
test_sample_case_1 (test_10221.TestUVA10221)
測試題目範例 1：角度單位為 'deg' ... ok
test_sample_case_2 (test_10221.TestUVA10221)
測試題目範例 2：角度單位為 'min' ... ok
test_sample_case_3 (test_10221.TestUVA10221)
測試題目範例 3 ... ok
test_zero_angle (test_10221.TestUVA10221)
邊界測試：角度為 0 ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## 結論
共執行 5 個測試案例，全數通過 (Green)。程式能正確處理 `deg` 和 `min` 兩種角度單位，並透過 `math.radians` 和 `math.sin` 函式精確計算出弧長與弦長。`assertAlmostEqual` 的使用確保了浮點數比較的穩定性。

<br>

# UVA 10222 (Decode the Mad man) 測試紀錄

## 執行指令
```bash
python -m unittest test_10222.py -v
```

## 執行輸出
```text
test_case_insensitive (test_10222.TestUVA10222)
大小寫測試：UVA 10222 規定輸入若包含大寫字母， ... ok
test_decode_with_spaces (test_10222.TestUVA10222)
空白字元測試：解碼過程中，空白鍵不應該被偏移，需保持原樣 ... ok
test_numbers_and_symbols (test_10222.TestUVA10222)
標點符號與數字測試： ... ok
test_standard_decode (test_10222.TestUVA10222)
基礎測試：測試標準字元的解碼。 ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 結論
共執行 4 個測試案例，全數通過 (Green)。利用內建的 QWERTY 鍵盤字串映射，成功實作了向左平移 2 個按鍵的解碼邏輯。測試涵蓋了包含大寫字母轉換為小寫、空白字元維持原狀、以及數字與標點符號的邊界平移。