# Week 13 作業說明

## 完成題號
- UVA 11005
- UVA 11063
- UVA 11150
- UVA 11321
- UVA 11332

## 檔案說明
- `question_11005.py`、`question_11063.py`、`question_11150.py`、`question_11321.py`、`question_11332.py`
  - 本次提交的正式版程式。
- `question_11005_easy.py`、`question_11063_easy.py`、`question_11150_easy.py`、`question_11321_easy.py`、`question_11332_easy.py`
  - 較容易記憶的簡單版程式。
- `tests/test_question_*.py`
  - 驗證正式版與簡單版是否都符合題意。
- `TEST_CASES.md`
  - 整理每題的主要測試情境。
- `TEST_LOG.md`
  - 記錄測試過程與修正內容。
- `AI_USAGE.md`
  - 記錄本次 AI 協助方式。

## 執行方式

### 方法 1：執行全部測試
```powershell
cd weeks/week-13/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一題目的測試
```powershell
# UVA 11005
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_11005 -v

# UVA 11063
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_11063 -v

# UVA 11150
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_11150 -v

# UVA 11321
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_11321 -v

# UVA 11332
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_11332 -v
```

### 方法 3：手動執行正式版程式
```powershell
cd weeks/week-13/solutions/1111405040

# UVA 11005
@'
1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
2
0
5
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_11005.py

# UVA 11063
@'
4
1 2 4 8
4
1 2 2 4
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_11063.py

# UVA 11150
@'
1
2
8
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_11150.py

# UVA 11321
@'
15 3
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0 0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_11321.py

# UVA 11332
@'
24
39
999999999
0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_11332.py
```

### 方法 4：手動執行簡單版程式
- 將上面的檔名改成對應的 `question_xxxxx_easy.py` 即可。

## 依賴套件
- 無
- 使用 Python 3.10+ 內建模組即可

## 補充說明
- 本次依照 README 要求，每題提供正式版與簡單版兩份程式。
- 共撰寫 5 份測試檔，15 個測試案例，全部通過。
- `QUESTION-11063.md`、`QUESTION-11150.md`、`QUESTION-11321.md`、`QUESTION-11332.md` 的內容與實際 UVA 題號不一致，因此本次實作以 `week-13/README.md` 的題號清單與對應 UVA 正式題意為準。
