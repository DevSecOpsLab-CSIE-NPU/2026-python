# Week 04 作業總結：UVA 基礎題組

## 基本資訊

- **學號**：1111405040
- **週次**：Week 04
- **作業主題**：UVA 948、10008、10019、10035、10038
- **提交日期**：2026-03-18

---

## 1. 完成題號

本次完成以下 5 題：

1. `question_948.py`：UVA 948 - Fibonaccimal Base
2. `question_10008.py`：UVA 10008 - What's Cryptanalysis?
3. `question_10019.py`：UVA 10019 - Funny Encryption Method
4. `question_10035.py`：UVA 10035 - Primary Arithmetic
5. `question_10038.py`：UVA 10038 - Jolly Jumpers

---

## 2. 執行方式

### 環境需求

- Python 3.10+
- 依賴套件：無（僅使用 Python 內建模組）

### 執行全部測試

```powershell
cd weeks/week-04/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 執行單一題目測試

```powershell
cd weeks/week-04/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_948 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10008 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10019 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10035 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10038 -v
```

### 手動執行程式

```powershell
cd weeks/week-04/solutions/1111405040

# UVA 948
@'
3
1
2
10
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_948.py

# UVA 10008
@'
3
This is a test.
Count me in.
AAB!
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10008.py

# UVA 10019
@'
3
10
26
265
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10019.py

# UVA 10035
@'
123 456
555 555
123 594
0 0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10035.py

# UVA 10038
@'
4 1 4 2 3
5 1 4 2 -1 6
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10038.py
```

---

## 3. 測試結果摘要

- 測試檔：5 份
- 測試函式：24 個
- 結果：24/24 通過

---

## 4. 各題解法重點

### `question_948.py`

- 先建立 `1, 2, 3, 5, 8, ...` 的 Fibonacci 數列。
- 由大到小做 greedy 選取，組出 Zeckendorf representation。
- 輸出格式為 `N = representation (fib)`。

### `question_10008.py`

- 逐字掃描輸入文字，將字母統一轉成大寫。
- 使用 `Counter` 統計 A-Z 頻率，忽略非字母字元。
- 以「出現次數遞減、字母遞增」排序後輸出。

### `question_10019.py`

- 第一個答案：直接計算十進位數值的二進位 `1` 的個數。
- 第二個答案：把輸入數字的十進位字串當成十六進位字串再轉成整數，計算其二進位 `1` 的個數。
- 例如 `265` 會同時計算 `265` 與 `0x265`。

### `question_10035.py`

- 以逐位加總模擬小學直式加法。
- 每一位若總和大於等於 10，便記錄一次進位。
- 依題目要求輸出 `No carry operation.`、`1 carry operation.` 或 `n carry operations.`。

### `question_10038.py`

- 計算相鄰元素差值的絕對值。
- 將差值集合與 `1` 到 `n - 1` 比對。
- 完全一致則輸出 `Jolly`，否則輸出 `Not jolly`。

---

## 5. 一個 bug 與修正方式

### 問題

`question_10019.py` 的測試中，原本把輸入 `10` 的第二個 bit count 寫成 `2`。

### 原因

題目第二個值是把十進位輸入字串當成十六進位整數解讀。  
`10` 應解讀為 `0x10 = 16`，其二進位為 `10000`，`1` 的個數應為 `1`。

### 修正

將 `tests/test_question_10019.py` 的預期值由 `(2, 2)` 修正為 `(2, 1)`，並同步更新整體輸出測試。

---

## 檔案結構

```text
weeks/week-04/solutions/1111405040/
├── question_948.py
├── question_10008.py
├── question_10019.py
├── question_10035.py
├── question_10038.py
├── tests/
│   ├── test_question_948.py
│   ├── test_question_10008.py
│   ├── test_question_10019.py
│   ├── test_question_10035.py
│   └── test_question_10038.py
├── TEST_CASES.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```
