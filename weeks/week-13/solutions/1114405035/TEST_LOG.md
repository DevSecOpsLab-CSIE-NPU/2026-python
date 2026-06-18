# Unittest Red → Green 測試紀錄

本文件紀錄了本週作業（5 題 CPE 演算法解題與 2 題資料視覺化邏輯）在實作過程中，依循 TDD（測試驅動開發）流程，從測試失敗（Red）到修改程式後測試成功（Green）的歷程。

---

## 1. CPE 題目部分

### 題號 11005 (Cheapest Base)

*   **Red 階段（未建立主程式前運行測試）：**
    *   **指令：** `python -m unittest tests/test_11005.py`
    *   **結果：** 失敗 (FileNotFoundError: 11005.py does not exist)
    *   **錯誤 Log 截圖/文字：**
        ```text
        FileNotFoundError: [Errno 2] No such file or directory: 'D:\\pychon\\2026-python\\weeks\\week-13\\solutions\\1114405035\\11005.py'
        ```

*   **Green 階段（建立主程式 `11005.py` 後運行測試）：**
    *   **指令：** `python -m unittest tests/test_11005.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.001s

        OK
        ```

---

### 題號 11063 (RGB -> XYZ)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11063.py`
    *   **結果：** 失敗 (FileNotFoundError: 11063.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11063.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.002s

        OK
        ```

---

### 題號 11150 (Frog Single Log Bridge)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11150.py`
    *   **結果：** 失敗 (FileNotFoundError: 11150.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11150.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        ```

---

### 題號 11321 (Inke's Trap Path)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11321.py`
    *   **結果：** 失敗 (FileNotFoundError: 11321.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11321.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        ..
        ----------------------------------------------------------------------
        Ran 2 tests in 0.000s

        OK
        ```

---

### 題號 11332 (Mirror Visibility)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11332.py`
    *   **結果：** 失敗 (FileNotFoundError: 11332.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11332.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        ..
        ----------------------------------------------------------------------
        Ran 2 tests in 0.001s

        OK
        ```

---

## 2. 視覺化資料處理邏輯部分

### Task 1 (Grouped Bar Chart)

*   **Red 階段（未撰寫 `task1_grouped_bar.py` 前運行測試）：**
    *   **指令：** `python -m unittest tests/test_task1.py`
    *   **結果：** ModuleNotFoundError (No module named 'task1_grouped_bar')

*   **Green 階段（完成 `task1_grouped_bar.py` 的資料載入與分析邏輯後）：**
    *   **指令：** `python -m unittest tests/test_task1.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.017s

        OK
        ```

---

### Task 2 (Origin Heatmap)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_task2.py`
    *   **結果：** ModuleNotFoundError (No module named 'task2_zipcode_heatmap')

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_task2.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.008s

        OK
        ```

---

## 3. 全域綜合測試（全部通過）

最後，在 `solutions/1114405035/` 目錄下執行整體測試探索：

*   **指令：** `python -m unittest discover -s tests -p "test_*.py" -v`
*   **結果：**
    ```text
    test_sample_case (test_11005.Test11005.test_sample_case) ... ok
    test_sample_case (test_11063.Test11063.test_sample_case) ... ok
    test_sample_case (test_11150.Test11150.test_sample_case) ... ok
    test_sample_case (test_11321.Test11321.test_sample_case) ... ok
    test_sample_case_2 (test_11321.Test11321.test_sample_case_2) ... ok
    test_sample_case_1 (test_11332.Test11332.test_sample_case_1) ... ok
    test_sample_case_2 (test_11332.Test11332.test_sample_case_2) ... ok
    test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ok
    test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ok
    test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ok
    test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ok
    test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ok
    test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ok
    test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ok
    test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ok
    test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ok
    test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ok

    ----------------------------------------------------------------------
    Ran 17 tests in 0.021s

    OK
    ```
