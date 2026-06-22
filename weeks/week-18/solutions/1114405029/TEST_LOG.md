# TEST_LOG

## 測試環境

- Python：3.11
- 測試框架：unittest
- 作業路徑：`weeks/week-18/solutions/1114405029/`

## 學號參數

- 學號：1114405029
- 學號末兩碼：29
- Q1：`D = 3`
- Q2：`SHIFT = 10`
- Q3：`base = 6`
- Q4：`K = 129`

## TDD Red 證據

Red commit：

```text
8c03d84 test: add failing tests for exam questions
```

當時只建立 `test_*.py` 與 package marker，尚未建立 `q1.py`、`q2.py`、`q3.py`、`q4.py`。重新從該 commit 匯出後執行 unittest，結果為：

```text
q1.test_q1 ... ERROR
q2.test_q2 ... ERROR
q3.test_q3 ... ERROR
q4.test_q4 ... ERROR
FAILED (errors=4)
```

失敗原因：四題實作檔尚未存在，符合先寫測試並確認紅燈的 TDD 流程。

## Green 測試指令

完整測試指令：

```bash
python -m unittest discover -s weeks/week-18/solutions/1114405029 -p "test_*.py" -v
```

最後確認結果：

```text
Ran 26 tests
OK
```

## Q1 Data Cleaning 測試摘要

測試檔：

```text
weeks/week-18/solutions/1114405029/q1/test_q1.py
```

測試案例：

- `test_dedupe_filter_sort_general_case`：一般案例，驗證去重、篩選 D=3、排序。
- `test_no_matching_numbers_outputs_none`：全部被過濾掉，輸出 `NONE`。
- `test_negative_zero_and_duplicates`：負數、0、重複值。
- `test_multiple_groups_until_zero`：多組測資直到 `n=0`。
- `test_edge_single_number_empty_result`：單一數字且空結果。
- `test_invalid_divisor_raises`：非法 divisor 例外。

## Q2 Caesar Cipher 測試摘要

測試檔：

```text
weeks/week-18/solutions/1114405029/q2/test_q2.py
```

測試案例：

- `test_mixed_case_letters`：一般大小寫字母，驗證 `Hello, NPU! -> Rovvy, XZE!`。
- `test_wraparound_for_z_and_upper_z`：`z/Z` 循環與 `abc XYZ -> klm HIJ`。
- `test_punctuation_spaces_and_digits_unchanged`：標點、空白、數字不變。
- `test_multiple_lines_until_eof`：多行輸入直到 EOF。
- `test_edge_empty_line_is_preserved`：空行 edge case。
- `test_shift_larger_than_alphabet`：shift 大於 26 的取餘數行為。

## Q3 Digital Root in Base 測試摘要

測試檔：

```text
weeks/week-18/solutions/1114405029/q3/test_q3.py
```

測試案例：

- `test_zero_root_is_zero`：輸入 0 輸出 0。
- `test_general_case_eight`：`8 -> 3`。
- `test_general_case_sixty_three`：`63 -> 3`。
- `test_large_number`：大數 `1_000_000_000`。
- `test_multiple_lines_until_eof`：多行 EOF，輸出 `0\n3\n3`。
- `test_edge_invalid_base_raises`：非法 base 與負數例外。

## Q4 Search Performance 測試摘要

測試檔：

```text
weeks/week-18/solutions/1114405029/q4/test_q4.py
```

測試案例：

- `test_found_target`：找到 `K=129`，驗證 idx 與 cmp。
- `test_not_found_target`：找不到目標。
- `test_empty_array`：空陣列。
- `test_single_element`：單一元素。
- `test_edge_first_and_last_positions`：第一個與最後一個元素。
- `test_benchmark_and_normalized_metrics`：timeit benchmark 與雷達圖正規化資料。
- `test_create_radar_chart_file`：確認 `radar.png` 可產生。
- `test_solve_output_mentions_faster_strategy`：確認輸出包含 `FOUND <idx> cmp=<次數>` 與 faster 結論。

## Q4 實際輸出格式

目前 Q4 主程式輸出格式：

```text
linear: FOUND 128 cmp=129
binary: FOUND 128 cmp=7
linear: <time> s
binary: <time> s
=> binary faster
```

## 最終檢查

- Q1-Q4 測試檔存在。
- README.md 存在。
- AI_LOG.md 存在。
- `q4/assets/radar.png` 存在。
- `__pycache__` 與 `.pyc` 沒有被 git 追蹤。
