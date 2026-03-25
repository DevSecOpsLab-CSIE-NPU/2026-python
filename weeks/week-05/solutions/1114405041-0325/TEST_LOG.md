# UVA 10041 測試紀錄

- 題號：10041
- 日期：2026-03-25
- 學號資料夾：`1114405041-0325`

## 測試指令

```bash
python -m unittest test_uva10041.py -v
```

## 測試結果

- 執行時間：2026-03-25
- 測試檔案：`test_uva10041.py`
- 測試總數：7
- 通過數：7
- 失敗數：0

```text
test_duplicate_addresses (test_uva10041.TestUVA10041.test_duplicate_addresses) ... ok
test_even_count_addresses (test_uva10041.TestUVA10041.test_even_count_addresses) ... ok
test_full_io_easy (test_uva10041.TestUVA10041.test_full_io_easy) ... ok
test_full_io_main (test_uva10041.TestUVA10041.test_full_io_main) ... ok
test_main_and_easy_consistency (test_uva10041.TestUVA10041.test_main_and_easy_consistency) ... ok
test_sample_case_easy (test_uva10041.TestUVA10041.test_sample_case_easy) ... ok
test_sample_case_main (test_uva10041.TestUVA10041.test_sample_case_main) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

# UVA 10050 / 10055 / 10056 / 10057 測試紀錄

- 日期：2026-03-25
- 學號資料夾：`1114405041-0325`

## 測試指令

```bash
python -m unittest test_uva10050.py test_uva10055.py test_uva10056.py test_uva10057.py -v
```

## Run 1（Red）

- 測試總數：14
- 通過數：13
- 失敗數：1
- 失敗項目：`test_uva10050.TestUVA10050.test_full_io`
- 問題說明：測試預期值誤寫為 `5\n10`，正確應為 `5\n14`。

## Run 2（Green）

- 測試總數：14
- 通過數：14
- 失敗數：0

```text
test_basic_case (test_uva10050.TestUVA10050.test_basic_case) ... ok
test_full_io (test_uva10050.TestUVA10050.test_full_io) ... ok
test_main_easy_consistency (test_uva10050.TestUVA10050.test_main_easy_consistency) ... ok
test_weekend_excluded (test_uva10050.TestUVA10050.test_weekend_excluded) ... ok
test_abs_diff (test_uva10055.TestUVA10055.test_abs_diff) ... ok
test_full_io (test_uva10055.TestUVA10055.test_full_io) ... ok
test_consistency (test_uva10056.TestUVA10056.test_consistency) ... ok
test_full_io (test_uva10056.TestUVA10056.test_full_io) ... ok
test_known_case (test_uva10056.TestUVA10056.test_known_case) ... ok
test_zero_probability (test_uva10056.TestUVA10056.test_zero_probability) ... ok
test_duplicates (test_uva10057.TestUVA10057.test_duplicates) ... ok
test_even_count (test_uva10057.TestUVA10057.test_even_count) ... ok
test_full_io (test_uva10057.TestUVA10057.test_full_io) ... ok
test_odd_count (test_uva10057.TestUVA10057.test_odd_count) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```
