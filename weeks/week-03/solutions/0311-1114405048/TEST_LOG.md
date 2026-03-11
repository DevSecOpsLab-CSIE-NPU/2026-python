# 測試 LOG 記錄

- 測試日期：2026-03-11
- 學號：1114405048
- Python 版本：3.14
- 測試框架：unittest

---

## Q100（UVA 100 — 3n+1 問題）

### 測試結果：18/18 全部通過

```
test_memoization_consistency (test_question_100.TestCycleLength.test_memoization_consistency)
連續呼叫同一個 n，結果應一致（驗證快取正確性） ... ok
test_n_is_1 (test_question_100.TestCycleLength.test_n_is_1)
n=1 時，序列只有 [1]，長度為 1 ... ok
test_n_is_2 (test_question_100.TestCycleLength.test_n_is_2)
n=2 → 2, 1，長度為 2 ... ok
test_n_is_22 (test_question_100.TestCycleLength.test_n_is_22)
題目範例：n=22 的 cycle-length 為 16 ... ok
test_n_is_large (test_question_100.TestCycleLength.test_n_is_large)
測試較大數字 n=999999，確認不會出錯且回傳正整數 ... ok
test_n_is_odd (test_question_100.TestCycleLength.test_n_is_odd)
測試奇數起點 n=3 → 3,10,5,16,8,4,2,1，長度為 8 ... ok
test_n_is_power_of_2 (test_question_100.TestCycleLength.test_n_is_power_of_2)
2 的冪次只會一直除以 2：n=16 → 16,8,4,2,1，長度為 5 ... ok
test_cycle_length_positive (test_question_100.TestEdgeCases.test_cycle_length_positive)
任何有效 n 的 cycle-length 都應 >= 1 ... ok
test_large_range (test_question_100.TestEdgeCases.test_large_range)
較大區間 [1, 1000]，結果應為正整數 ... ok
test_n_equals_1_range (test_question_100.TestEdgeCases.test_n_equals_1_range)
最小有效輸入：區間 [1, 1] ... ok
test_small_range (test_question_100.TestEdgeCases.test_small_range)
小區間 [1, 3]，手動驗算：1→1, 2→2, 3→8，最大為 8 ... ok
test_adjacent_numbers (test_question_100.TestMaxCycleLength.test_adjacent_numbers)
兩個相鄰數字的區間，取其中較大的 cycle-length ... ok
test_reversed_input (test_question_100.TestMaxCycleLength.test_reversed_input)
輸入 i > j 時，結果應與 i < j 相同（題目允許 i > j） ... ok
test_sample_100_200 (test_question_100.TestMaxCycleLength.test_sample_100_200)
題目範例：區間 [100, 200] 最大 cycle-length 為 125 ... ok
test_sample_1_10 (test_question_100.TestMaxCycleLength.test_sample_1_10)
題目範例：區間 [1, 10] 最大 cycle-length 為 20 ... ok
test_sample_201_210 (test_question_100.TestMaxCycleLength.test_sample_201_210)
題目範例：區間 [201, 210] 最大 cycle-length 為 89 ... ok
test_sample_900_1000 (test_question_100.TestMaxCycleLength.test_sample_900_1000)
題目範例：區間 [900, 1000] 最大 cycle-length 為 174 ... ok
test_single_element (test_question_100.TestMaxCycleLength.test_single_element)
區間只有一個數字 (i == j)，結果為該數的 cycle-length ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.003s

OK
```

---

## Q118（UVA 118 — 乖乖的機器人）

### 測試結果：24/24 全部通過

```
test_move_east (test_question_118.TestMoveForward.test_move_east)
面東前進：x + 1 ... ok
test_move_north (test_question_118.TestMoveForward.test_move_north)
面北前進：y + 1 ... ok
test_move_south (test_question_118.TestMoveForward.test_move_south)
面南前進：y - 1 ... ok
test_move_west (test_question_118.TestMoveForward.test_move_west)
面西前進：x - 1 ... ok
test_multiple_scents (test_question_118.TestScentMechanism.test_multiple_scents)
多個 scent 可以同時存在 ... ok
test_scent_direction_specific (test_question_118.TestScentMechanism.test_scent_direction_specific)
scent 只對同一方向有效，不同方向仍會掉落 ... ok
test_scent_prevents_fall (test_question_118.TestScentMechanism.test_scent_prevents_fall)
有 scent 標記的位置+方向，後續機器人不會掉落 ... ok
test_fall_off_east (test_question_118.TestSimulateRobot.test_fall_off_east)
從東方邊界掉落：(5,0,E) F → (5,0,E) LOST（世界 5x5） ... ok
test_fall_off_north (test_question_118.TestSimulateRobot.test_fall_off_north)
從北方邊界掉落：(0,5,N) F → (0,5,N) LOST（世界 5x5） ... ok
test_fall_off_south (test_question_118.TestSimulateRobot.test_fall_off_south)
從南方邊界掉落：(0,0,S) F → (0,0,S) LOST ... ok
test_fall_off_west (test_question_118.TestSimulateRobot.test_fall_off_west)
從西方邊界掉落：(0,0,W) F → (0,0,W) LOST ... ok
test_no_commands (test_question_118.TestSimulateRobot.test_no_commands)
空指令：機器人原地不動 ... ok
test_only_turns (test_question_118.TestSimulateRobot.test_only_turns)
只有轉向指令：座標不變，方向改變 ... ok
test_sample_robot_1 (test_question_118.TestSimulateRobot.test_sample_robot_1)
題目範例第一個機器人：(1,1,E) RFRFRFRF → 原地繞圈回到 (1,1,E) ... ok
test_sample_robot_2 (test_question_118.TestSimulateRobot.test_sample_robot_2)
題目範例第二個機器人：(3,2,N) FRRFLLFFRRFLL → 掉落，最終 (3,3,N) LOST ... ok
test_sample_robot_3 (test_question_118.TestSimulateRobot.test_sample_robot_3)
題目範例第三個機器人：前面機器人留下 scent，(0,3,W) LLFFFLFLFL → (2,3,S) ... ok
test_east_to_north (test_question_118.TestTurnLeft.test_east_to_north)
面東左轉後應面北 ... ok
test_north_to_west (test_question_118.TestTurnLeft.test_north_to_west)
面北左轉後應面西 ... ok
test_south_to_east (test_question_118.TestTurnLeft.test_south_to_east)
面南左轉後應面東 ... ok
test_west_to_south (test_question_118.TestTurnLeft.test_west_to_south)
面西左轉後應面南 ... ok
test_east_to_south (test_question_118.TestTurnRight.test_east_to_south)
面東右轉後應面南 ... ok
test_north_to_east (test_question_118.TestTurnRight.test_north_to_east)
面北右轉後應面東 ... ok
test_south_to_west (test_question_118.TestTurnRight.test_south_to_west)
面南右轉後應面西 ... ok
test_west_to_north (test_question_118.TestTurnRight.test_west_to_north)
面西右轉後應面北 ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.004s

OK
```

---

## Q272（UVA 272 — TeX 引號替換）

### 測試結果：18/18 全部通過

```
test_adjacent_quotes (test_question_272.TestBasicConversion.test_adjacent_quotes)
緊鄰的引號對 ... ok
test_sample_input (test_question_272.TestBasicConversion.test_sample_input)
題目範例輸入 ... ok
test_single_pair (test_question_272.TestBasicConversion.test_single_pair)
一對引號：第一個變 ``，第二個變 '' ... ok
test_three_pairs (test_question_272.TestBasicConversion.test_three_pairs)
三對引號：正確交替六次 ... ok
test_two_pairs (test_question_272.TestBasicConversion.test_two_pairs)
兩對引號：交替替換 ``...''...``...'' ... ok
test_empty_quote_pairs (test_question_272.TestEdgeCases.test_empty_quote_pairs)
連續空引號對： → ``''``'' ... ok
test_four_pairs (test_question_272.TestEdgeCases.test_four_pairs)
四對引號，確認交替正確 ... ok
test_long_text_between_quotes (test_question_272.TestEdgeCases.test_long_text_between_quotes)
引號間有大量文字 ... ok
test_multiline_two_pairs (test_question_272.TestMultiLine.test_multiline_two_pairs)
多行文字中有兩對引號 ... ok
test_newline_preserved (test_question_272.TestMultiLine.test_newline_preserved)
換行符應被保留 ... ok
test_quote_across_lines (test_question_272.TestMultiLine.test_quote_across_lines)
引號狀態跨行：第一行開引號，第二行閉引號 ... ok
test_empty_string (test_question_272.TestNoQuotes.test_empty_string)
空字串應回傳空字串 ... ok
test_no_quotes (test_question_272.TestNoQuotes.test_no_quotes)
無引號的文字應原樣輸出 ... ok
test_only_spaces (test_question_272.TestNoQuotes.test_only_spaces)
只有空白的字串應原樣輸出 ... ok
test_with_backticks (test_question_272.TestSpecialCharacters.test_with_backticks)
輸入中已有反引號，不應被影響 ... ok
test_with_numbers (test_question_272.TestSpecialCharacters.test_with_numbers)
引號包圍數字 ... ok
test_with_punctuation (test_question_272.TestSpecialCharacters.test_with_punctuation)
引號旁有標點符號 ... ok
test_with_single_quotes (test_question_272.TestSpecialCharacters.test_with_single_quotes)
輸入中有單引號，不應被影響 ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.004s

OK
```

---

## Q299（UVA 299 — 火車車廂交換）

### 測試結果：17/17 全部通過

```
test_single_element (test_question_299.TestAlreadySorted.test_single_element)
只有一個元素 [1]：不需交換 ... ok
test_sorted_3 (test_question_299.TestAlreadySorted.test_sorted_3)
已排序 [1, 2, 3]：不需交換 ... ok
test_sorted_5 (test_question_299.TestAlreadySorted.test_sorted_5)
已排序 [1, 2, 3, 4, 5]：不需交換 ... ok
test_does_not_modify_original (test_question_299.TestEdgeCases.test_does_not_modify_original)
確認函式不會修改原始陣列 ... ok
test_empty_array (test_question_299.TestEdgeCases.test_empty_array)
空陣列（L=0）：不需交換 ... ok
test_large_reverse (test_question_299.TestEdgeCases.test_large_reverse)
較大的完全逆序陣列：C(50,2) = 1225 ... ok
test_large_sorted (test_question_299.TestEdgeCases.test_large_sorted)
較大的已排序陣列 ... ok
test_reverse_2 (test_question_299.TestReverseSorted.test_reverse_2)
[2, 1] → 1 次交換 ... ok
test_reverse_3 (test_question_299.TestReverseSorted.test_reverse_3)
[3, 2, 1] → 3 次交換（逆序對：3-2, 3-1, 2-1） ... ok
test_reverse_5 (test_question_299.TestReverseSorted.test_reverse_5)
[5, 4, 3, 2, 1] → C(5,2) = 10 次交換 ... ok
test_sample_1 (test_question_299.TestSampleCases.test_sample_1)
範例第一組：[1, 3, 2] → 需要 1 次交換 ... ok
test_sample_2 (test_question_299.TestSampleCases.test_sample_2)
範例第二組：[4, 3, 2, 1] → 完全逆序，需要 6 次交換 ... ok
test_sample_3 (test_question_299.TestSampleCases.test_sample_3)
範例第三組：[2, 1] → 需要 1 次交換 ... ok
test_first_to_last (test_question_299.TestSpecialCases.test_first_to_last)
[5, 1, 2, 3, 4]：5 需要從最前移到最後，4 次交換 ... ok
test_last_to_first (test_question_299.TestSpecialCases.test_last_to_first)
[2, 3, 4, 5, 1]：1 需要從最後移到最前，4 次交換 ... ok
test_multiple_inversions (test_question_299.TestSpecialCases.test_multiple_inversions)
[3, 1, 2]：逆序對為 3-1, 3-2，共 2 次交換 ... ok
test_swap_middle (test_question_299.TestSpecialCases.test_swap_middle)
[1, 3, 2, 4]：只有中間兩個逆序，1 次交換 ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

---

## Q490（UVA 490 — 旋轉句子）

### 測試結果：15/15 全部通過

```
test_hello_world (test_question_490.TestBasicRotation.test_hello_world)
經典範例：HELLO 和 WORLD 旋轉 ... ok
test_single_char_lines (test_question_490.TestBasicRotation.test_single_char_lines)
每行只有一個字元 ... ok
test_single_line (test_question_490.TestBasicRotation.test_single_line)
單行輸入：每個字元變成一行 ... ok
test_two_lines_same_length (test_question_490.TestBasicRotation.test_two_lines_same_length)
兩行等長 ... ok
test_all_spaces (test_question_490.TestEdgeCases.test_all_spaces)
全部是空格 ... ok
test_empty_and_nonempty (test_question_490.TestEdgeCases.test_empty_and_nonempty)
含空行與非空行 ... ok
test_empty_input (test_question_490.TestEdgeCases.test_empty_input)
空輸入 ... ok
test_many_lines (test_question_490.TestEdgeCases.test_many_lines)
多行輸入，確認旋轉後行數等於最長行長度 ... ok
test_single_char (test_question_490.TestEdgeCases.test_single_char)
只有一個字元 ... ok
test_with_numbers (test_question_490.TestSpecialCharacters.test_with_numbers)
輸入含數字 ... ok
test_with_punctuation (test_question_490.TestSpecialCharacters.test_with_punctuation)
輸入含標點符號 ... ok
test_with_spaces (test_question_490.TestSpecialCharacters.test_with_spaces)
輸入含空格 ... ok
test_first_shorter (test_question_490.TestUnequalLengths.test_first_shorter)
第一行較短，需補空格 ... ok
test_second_shorter (test_question_490.TestUnequalLengths.test_second_shorter)
第二行較短，需補空格 ... ok
test_three_lines_different_lengths (test_question_490.TestUnequalLengths.test_three_lines_different_lengths)
三行不同長度 ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.005s

OK
```

---

## 總結

| 題目 | 測試數 | 通過 | 失敗 |
|------|--------|------|------|
| Q100 | 18     | 18   | 0    |
| Q118 | 24     | 24   | 0    |
| Q272 | 18     | 18   | 0    |
| Q299 | 17     | 17   | 0    |
| Q490 | 15     | 15   | 0    |
| **合計** | **92** | **92** | **0** |
