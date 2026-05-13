# Week 12 作業說明

## 完成題號
- QUESTION-10812
- QUESTION-10908
- QUESTION-10922
- QUESTION-10929
- QUESTION-10931

## 檔案說明
- `question_10812.py`：UVA 10812 解法
- `question_10908.py`：UVA 10908 解法
- `question_10922.py`：UVA 10922 解法
- `question_10929.py`：UVA 10929 解法
- `question_10931.py`：UVA 10931 解法
- `tests/`：各題單元測試
- `TEST_CASES.md`：測試案例整理
- `TEST_LOG.md`：測試與開發紀錄
- `AI_USAGE.md`：AI 協助紀錄

## 執行方式

### 方法 1：執行全部測試
```powershell
cd weeks/week-12/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一題目的測試
```powershell
# 只測試 QUESTION-10812
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10812 -v

# 只測試 QUESTION-10908
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10908 -v

# 只測試 QUESTION-10922
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10922 -v

# 只測試 QUESTION-10929
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10929 -v

# 只測試 QUESTION-10931
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10931 -v
```

### 方法 3：手動執行程式
```powershell
cd weeks/week-12/solutions/1111405040

# QUESTION-10812
@'
2
40 20
20 40
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10812.py

# QUESTION-10908
@'
1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10908.py

# QUESTION-10922
@'
999999999
12345
0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10922.py

# QUESTION-10929
@'
121
123456
0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10929.py

# QUESTION-10931
@'
1
2
10
21
0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10931.py
```

## 依賴套件
- 無（使用 Python 3.10+ 內建模組）

## 補充說明
- 共完成 5 題 UVA 題目。
- 共撰寫 5 份測試檔、20 個測試函式。
- 每題皆提供獨立的 `solve()`，方便測試與重複使用。
- 所有內容皆放在 `weeks/week-12/solutions/1111405040/`。
