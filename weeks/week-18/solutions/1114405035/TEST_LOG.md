# TEST_LOG - 期末考測試紀錄

本文件紀錄期末考各題在實作過程中，由測試失敗（Red）到修改程式後測試成功（Green）的歷程。

---

## 第一題：資料清理 (Data Cleaning)

*   **Red 階段（未實作核心邏輯時運行測試）：**
    *   **指令：** `python -m unittest test_data_cleaning.py`
    *   **結果：** 失敗 (FFFFF)
    *   **錯誤 Log 節錄：**
        ```text
        AssertionError: None != [6, 9]
        AssertionError: None != [3]
        AssertionError: None != []
        AssertionError: None != [-3, 0]
        FAILED (failures=5)
        ```

*   **Green 階段（實作核心邏輯後運行測試）：**
    *   **指令：** `python -m unittest test_data_cleaning.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.000s

        OK
        ```

---

## 第二題：凱撒密碼 (Caesar Cipher)

*   **Red 階段（未實作核心邏輯時運行測試）：**
    *   **指令：** `python -m unittest test_caesar_cipher.py`
    *   **結果：** 失敗 (FFFFF)
    *   **錯誤 Log 節錄：**
        ```text
        AssertionError: None != 'Aa'
        AssertionError: None != '123!@# 澎科大'
        AssertionError: None != ''
        AssertionError: None != 'Nkrru, TVA!'
        AssertionError: None != 'ghi DEF'
        FAILED (failures=5)
        ```

*   **Green 階段（實作核心邏輯後運行測試）：**
    *   **指令：** `python -m unittest test_caesar_cipher.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.000s

        OK
        ```

---

## 第三題：任意進位的數字根

*   **Red 階段（未實作核心邏輯時運行測試）：**
    *   **指令：** `python -m unittest test_digital_root.py`
    *   **結果：** 失敗 (FFFFF)
    *   **錯誤 Log 節錄：**
        ```text
        AssertionError: None != 1
        AssertionError: None != 5
        AssertionError: ValueError not raised
        AssertionError: None != 0
        FAILED (failures=5)
        ```

*   **Green 階段（實作核心邏輯後運行測試）：**
    *   **指令 :** `python -m unittest test_digital_root.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.000s

        OK
        ```

---

## 第四題：二分搜尋效能

*   **Red 階段（未實作核心邏輯時運行測試）：**
    *   **指令：** `python -m unittest test_search_bench.py`
    *   **結果：** 失敗 (EEEEF)
    *   **錯誤 Log 節錄：**
        ```text
        TypeError: cannot unpack non-iterable NoneType object
        AssertionError: False is not true (radar.png not generated)
        FAILED (failures=1, errors=4)
        ```

*   **Green 階段（實作核心邏輯後運行測試）：**
    *   **指令：** `python -m unittest test_search_bench.py`
    *   **結果：** 成功 (OK)
    *   **成功 Log：**
        ```text
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.286s

        OK
        ```



