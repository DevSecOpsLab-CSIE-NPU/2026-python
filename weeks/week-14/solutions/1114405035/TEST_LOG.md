# Unittest Red → Green 測試紀錄

本文件紀錄了本週作業（4 題 CPE 演算法解題）在實作過程中，依循 TDD（測試驅動開發）流程，從測試失敗（Red）到修改程式後測試成功（Green）的歷程。

---

## 1. CPE 題目部分

### 題號 11349 (Symmetric Matrix)

*   **Red 階段（未建立主程式前運行測試）：**
    *   **指令：** `python -m unittest tests/test_11349.py`
    *   **結果：** 失敗 (FileNotFoundError: 11349.py does not exist)

*   **Green 階段（建立主程式 `11349.py` 後運行測試）：**
    *   **指令：** `python -m unittest tests/test_11349.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        ```

---

### 題號 11417 (GCD)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11417.py`
    *   **結果：** 失敗 (FileNotFoundError: 11417.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11417.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.017s

        OK
        ```

---

### 題號 11461 (Square Numbers)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_11461.py`
    *   **結果：** 失敗 (FileNotFoundError: 11461.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_11461.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.002s

        OK
        ```

---

### 題號 12019 (Doom's Day Algorithm)

*   **Red 階段：**
    *   **指令：** `python -m unittest tests/test_12019.py`
    *   **結果：** 失敗 (FileNotFoundError: 12019.py does not exist)

*   **Green 階段：**
    *   **指令：** `python -m unittest tests/test_12019.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        ```

---

## 2. 全域綜合測試（全部通過）

在 `solutions/1114405035/` 目錄下執行整體測試探索：

*   **指令：** `python -m unittest discover -s tests -p "test_*.py" -v`
*   **結果：**
    ```text
    test_sample_case (test_11349.Test11349.test_sample_case) ... ok
    test_sample_case (test_11417.Test11417.test_sample_case) ... ok
    test_sample_case (test_11461.Test11461.test_sample_case) ... ok
    test_sample_case (test_12019.Test12019.test_sample_case) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.012s

    OK
    ```
