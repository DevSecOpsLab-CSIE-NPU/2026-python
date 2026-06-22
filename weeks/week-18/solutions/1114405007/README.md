# Week 18 — CPE 模擬實戰

**學號：** 1114405007

---

## 檔案結構

```
weeks/week-18/solutions/1114405007/
│
├── problem1/          # A區：資料清理 (D=5)
│   ├── task1_sequence_clean.py
│   └── test_task1.py           (14 tests)
│
├── problem2/          # A區：凱撒密碼 (SHIFT=8)
│   ├── task2_caesar_cipher.py
│   └── test_caesar.py          (10 tests)
│
├── problem3/          # B區：數字根 (base=11)
│   ├── task3_digit_root.py
│   └── test_digit_root.py      (12 tests)
│
├── problem4/          # C區：二分搜尋 (K=107)
│   ├── task4_search_lab.py
│   ├── test_search_lab.py      (18 tests)
│   └── assets/radar.png
│
├── README.md          # 本檔
├── AI_LOG.md          # AI 協作紀錄
└── TEST_LOG.md        # 測試執行紀錄
```

---

## 各題參數

| 區 | 題目 | 參數 | 公式 | 值 |
|----|------|------|------|----|
| A | 題1 資料清理 | D | u%4+2 (u=7) | **5** |
| A | 題2 凱撒密碼 | SHIFT | u%25+1 (u=7) | **8** |
| B | 題3 數字根 | base | 末位對照表 (7→11) | **11** |
| C | 題4 二分搜尋 | K | 100+末兩碼 (07) | **107** |

## 執行方式

```bash
# 題1：資料清理
cd problem1 && python task1_sequence_clean.py < input.txt

# 題2：凱撒密碼
cd problem2 && python task2_caesar_cipher.py < input.txt

# 題3：數字根
cd problem3 && python task3_digit_root.py < input.txt

# 題4：二分搜尋 + 雷達圖
cd problem4 && python task4_search_lab.py

# 各題測試
cd problem1 && python -m unittest -v
cd problem2 && python -m unittest -v
cd problem3 && python -m unittest -v
cd problem4 && python -m unittest -v
```

---

## 範例執行

### 題1：資料清理（A區）

**輸入**
```
7
4 7 4 2 9 2 6
3
1 5 3
0
```

**輸出**
```
NONE
5
```

---

### 題2：凱撒密碼（A區）

**輸入**
```
Hello, NPU!
abc XYZ
```

**輸出**
```
Pmttw, VXC!
ijk FGH
```

---

### 題3：任意進位數字根（B區）

**輸入**
```
0
8
63
```

**輸出**
```
0
8
3
```

---

### 題4：二分搜尋效能（C區）

**輸出**（內建參數 K=107，N=200000）
```
NOT FOUND cmp=34
linear : 0.010573 s
binary : 0.000003 s
=> binary faster
radar chart saved to assets/radar.png
```

---

## 題4 二分搜尋 — 雷達圖說明

### 維度定義與正規化（1–10 給分，10 = 最有利）

| 維度 | 線性 | 二分 | 正規化理由 |
|------|------|------|-----------|
| **Large N Speed** | 3 | 9 | 200k 實測 binary 快約 3000 倍 |
| **Small N Speed** | 9 | 5 | n 很小時線性常數低，分支預測 overhead |
| **No Sort Needed** | 9 | 3 | binary 需先排序 O(n log n) |
| **Easy to Implement** | 9 | 5 | 線性 3 行 vs 二分邊界判斷 |
| **Worst-case Comparisons** | 9 | 3 | 線性 n 次 vs 二分 log n 次 |

### 解讀

沒有絕對贏家：大 n 且查多次時二分壓倒性勝出；小 n 或只查一次時，線性的簡潔與免排序更具實用性。
