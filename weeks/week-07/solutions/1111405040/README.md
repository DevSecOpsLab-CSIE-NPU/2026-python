# Week 07 作業說明

## 完成題號
- UVA 10062
- UVA 10071
- UVA 10093
- UVA 10101
- UVA 10170

## 檔案說明
- `question_10062.py`、`question_10071.py`、`question_10093.py`、`question_10101.py`、`question_10170.py`
  - 本次提交的正式版程式。
- `question_10062_easy.py`、`question_10071_easy.py`、`question_10093_easy.py`、`question_10101_easy.py`、`question_10170_easy.py`
  - 較容易記憶的簡單版程式。
- `tests/test_question_*.py`
  - 驗證正式版與簡單版是否都符合題意。

## 執行方式

### 方法 1：執行全部測試
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一題目的測試
```powershell
# UVA 10062
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10062 -v

# UVA 10071
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10071 -v

# UVA 10093
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10093 -v

# UVA 10101
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10101 -v

# UVA 10170
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10170 -v
```

### 方法 3：手動執行正式版程式
```powershell
cd weeks/week-07/solutions/1111405040

# UVA 10062
@'
AAABBC
aA!
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10062.py

# UVA 10071
@'
0 0
5 12
10 10
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10071.py

# UVA 10093
@'
3
+5
-A
q12345
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10093.py

# UVA 10101
@'
23764
45897458973958
0
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10101.py

# UVA 10170
@'
1 6
3 10
3 14
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10170.py
```

### 方法 4：手動執行簡單版程式
- 將上面的檔名改成對應的 `question_xxxxx_easy.py` 即可。

## 依賴套件
- 無
- 使用 Python 3.10+ 內建模組即可

## 補充說明
- 本次依照 README 要求，每題提供正式版與簡單版兩份程式。
- 共撰寫 5 份測試檔，21 個測試案例，全部通過。
- 題目資料夾中的部分 `QUESTION-*.md` 內容與題號不一致，因此本次實作以 `week-07/README.md` 的題號清單與對應 UVA 正式題意為準。
