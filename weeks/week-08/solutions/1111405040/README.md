# Week 08 作業說明

## 完成題號
- QUESTION-10189
- QUESTION-10190
- QUESTION-10193
- QUESTION-10221
- QUESTION-10222

## 檔案說明
- `question_10189.py`
  - UVA 10189 Minesweeper
- `question_10190.py`
  - UVA 10190 Divide, But Not Quite Conquer!
- `question_10193.py`
  - UVA 10193 All You Need Is Love
- `question_10221.py`
  - UVA 10221 Satellites
- `question_10222.py`
  - UVA 10222 Decode the Mad man
- `tests/`
  - 各題對應的 `unittest` 測試

## 執行方式

### 方法 1：執行全部測試
```powershell
cd weeks/week-08/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一題目的測試
```powershell
# QUESTION-10189
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10189 -v

# QUESTION-10190
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10190 -v

# QUESTION-10193
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10193 -v

# QUESTION-10221
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10221 -v

# QUESTION-10222
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10222 -v
```

### 方法 3：手動執行程式
```powershell
cd weeks/week-08/solutions/1111405040

# QUESTION-10189
@'
4 4
*...
....
.*..
....
0 0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10189.py

# QUESTION-10190
@'
125 5
30 3
1 2
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10190.py

# QUESTION-10193
@'
3
1100
1000
101
10
110
100
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10193.py

# QUESTION-10221
@'
500 30 deg
700 60 min
200 45 deg
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10221.py

# QUESTION-10222
@'
k[r dyt I[o
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10222.py
```

## 依賴套件
- 無
- 使用 Python 3.10+ 內建模組即可

## 補充說明
- 共完成 5 題 UVA 題目。
- 共撰寫 5 份測試檔、17 個測試案例，全部通過。
- `QUESTION-10190.md`、`QUESTION-10193.md`、`QUESTION-10222.md` 的內容和實際 UVA 題號不一致，本次實作以 `week-08/README.md` 的題號清單與正式 UVA 題意為準。
