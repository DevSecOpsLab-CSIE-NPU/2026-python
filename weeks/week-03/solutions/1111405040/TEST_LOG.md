# Week 03 測試執行日誌

## 執行環境

- Python 版本：3.10
- 測試框架：unittest（Python 內建）
- 執行時間：2026-03-11
- 學號：1111405040
- 主要直譯器：`C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe`

---

## 第一次執行：環境檢查（失敗）

### 情境說明

先使用一般 `python` 指令執行測試，確認目前終端環境是否可直接呼叫 Python。

### 執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 執行結果

```text
'python.exe' 程式無法執行: 系統無法存取該檔案
```

### 統計

- **測試總數**：0（尚未進入測試流程）
- **通過**：0
- **失敗**：1（環境指令失敗）

### 修正方式

- 改用 Python 3.10 的完整路徑執行所有測試與程式。

---

## 第二次執行：單元測試（通過）

### 情境說明

完成五題實作與測試檔後，執行整包單元測試。

### 執行指令

```bash
cd weeks/week-03/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 執行結果摘要

```text
Ran 19 tests in 0.001s
OK
```

### 統計

- **測試總數**：19
- **通過**：19
- **失敗**：0
- **成功率**：100%

### 覆蓋題目

- QUESTION-100：5 個
- QUESTION-118：3 個
- QUESTION-272：3 個
- QUESTION-299：5 個
- QUESTION-490：3 個

---

## 第三次執行：題目範例驗證（通過）

### 情境說明

針對五題分別用範例輸入手動執行，確認輸出格式與內容。

### QUESTION-100

執行指令：

```bash
@'
1 10
100 200
201 210
900 1000
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_100.py
```

輸出結果：

```text
1 10 20
100 200 125
201 210 89
900 1000 174
```

### QUESTION-118

執行指令：

```bash
@'
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_118.py
```

輸出結果：

```text
1 1 E
3 3 N LOST
2 3 S
```

### QUESTION-272

執行指令：

```bash
@'
"To be or not to be," quoth the bard, "that is the question."
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_272.py
```

輸出結果：

```text
``To be or not to be,'' quoth the bard, ``that is the question.''
```

### QUESTION-299

執行指令：

```bash
@'
3
3
1 3 2
4
4 3 2 1
2
1 2
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_299.py
```

輸出結果：

```text
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 0 swaps.
```

### QUESTION-490

執行指令：

```bash
@'
HELLO
WORLD
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_490.py
```

輸出結果：

```text
WH
OE
RL
LL
DO
```

---

## 總結

| 階段 | 通過 | 失敗 | 備註 |
|------|------|------|------|
| **環境檢查** | 0 | 1 | `python` 指令不可用，改用完整路徑 |
| **單元測試** | 19 | 0 | 全部測試通過 |
| **範例驗證** | 5 題 | 0 | 五題範例輸出一致 |
