# Week 18 — CPE 模擬實戰

**學號：** 1114405007

---

## 檔案結構

```
weeks/week-18/solutions/1114405007/
│
├── A 區 ────
│   ├── task1_sequence_clean.py   # 題1 資料清理 (D=5)
│   ├── task2_caesar_cipher.py    # 題2 凱撒密碼 (SHIFT=8)
│   ├── README.md                 # 本檔
│   ├── AI_LOG.md                 # AI 協作紀錄
│   └── TEST_LOG.md               # 測試執行紀錄
│
├── B 區 ────
│   ├── task3_digit_root.py       # 題3 數字根 (base=11)
│
├── C 區 ────
│   ├── task4_search_lab.py       # 題4 二分搜尋 (K=107)
│   └── assets/radar.png          # 雷達圖
│
└── tests/
    ├── test_task1.py             # 題1 測試 (14 cases)
    ├── test_caesar.py            # 題2 測試 (10 cases)
    ├── test_digit_root.py        # 題3 測試 (11 cases)
    └── test_search_lab.py        # 題4 測試 (18 cases)
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
python task1_sequence_clean.py < input.txt

# 題2：凱撒密碼
python task2_caesar_cipher.py < input.txt

# 題3：數字根
python task3_digit_root.py < input.txt

# 題4：二分搜尋 + 雷達圖
python task4_search_lab.py

# 全部測試（54 項）
python -m unittest discover -s tests -p "test_*.py" -v
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
