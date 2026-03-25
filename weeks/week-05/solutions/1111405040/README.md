# Week 05 作業總結：UVA 基礎題組

## 基本資訊

- **學號**：1111405040
- **週次**：Week 05
- **作業主題**：UVA 10041、10050、10055、10056、10057
- **提交日期**：2026-03-25

---

## 1. 完成題號

本次完成以下 5 題：

1. `question_10041.py`：UVA 10041 - Vito's Family
2. `question_10050.py`：UVA 10050 - Hartals
3. `question_10055.py`：UVA 10055 - Hashmat the Brave Warrior
4. `question_10056.py`：UVA 10056 - What is the Probability?
5. `question_10057.py`：UVA 10057 - A mid-summer night's dream

---

## 2. 執行方式

### 環境需求

- Python 3.10+
- 依賴套件：無（僅使用 Python 內建模組）

### 執行全部測試

```powershell
cd weeks/week-05/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 執行單一題目測試

```powershell
cd weeks/week-05/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10041 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10050 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10055 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10056 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_10057 -v
```

### 手動執行程式

```powershell
cd weeks/week-05/solutions/1111405040

# UVA 10041
@'
2
2 2 4
3 2 4 6
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10041.py

# UVA 10050
@'
2
14
2
3
4
7
1
1
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10050.py

# UVA 10055
@'
10 12
10 10
1 10000000000
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10055.py

# UVA 10056
@'
3
3 0.0 1
1 0.5 1
3 0.5 2
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10056.py

# UVA 10057
@'
3
1
2
3
4
1
2
4
6
'@ | C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_10057.py
```

---

## 3. 測試結果摘要

- 測試檔：5 份
- 測試函式：20 個
- 結果：20/20 通過

---

## 4. 各題解法重點

### `question_10041.py`

- 先排序親戚住址。
- 取中位數當作集合點。
- 將每個住址到中位數的距離加總。

### `question_10050.py`

- 逐個政黨依照 hartal 週期標記罷工日。
- 使用 `set` 避免重複計算同一天。
- 跳過週五與週六。

### `question_10055.py`

- 題目只要求兩數差距。
- 直接輸出兩個整數的絕對值差即可。
- 讀到 EOF 為止。

### `question_10056.py`

- 這題是等比級數機率模型。
- 先算前面玩家都失敗、輪到第 `i` 位玩家成功的機率。
- 再除以一整輪有人成功的總機率。

### `question_10057.py`

- 先排序所有數字。
- 用中間位置找出最小可行值與最大可行值。
- 計算落在這個區間內的資料筆數，以及可行整數個數。

---

## 5. 一個 bug 與修正方式

### 問題

`question_10050.py` 的測試一開始把 14 天內 `hartal = 3` 的答案寫成 `2`。

### 原因

這題的 day 1 代表星期日，因此 14 天內的第 12 天仍是工作日，不是週末。  
我原本把週五、週六的位置算錯，導致測試預期值偏小。

### 修正

將 `tests/test_question_10050.py` 的預期值修正為：

- `count_lost_days(14, [3]) == 3`
- `count_lost_days(14, [3, 4]) == 5`

並同步調整整體輸出測試。

---

## 檔案結構

```text
weeks/week-05/solutions/1111405040/
├── question_10041.py
├── question_10050.py
├── question_10055.py
├── question_10056.py
├── question_10057.py
├── tests/
│   ├── test_question_10041.py
│   ├── test_question_10050.py
│   ├── test_question_10055.py
│   ├── test_question_10056.py
│   └── test_question_10057.py
├── TEST_CASES.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```
