# Week 18 — CPE 模擬實戰

## 學號
1114405007

## 各題參數
| 題目 | 參數對照 |
|------|---------|
| 題1 資料清理 | D = (7 % 4) + 2 = 5 |
| 題2 凱撒密碼 | SHIFT = 8 |
| 題3 數字根 | base = 11 (學號末位 7 → 對照表) |
| 題4 二分搜尋 | K = 100 + 07 = 107 |

## 執行方式
```bash
# 題1
python task1_sequence_clean.py < input.txt

# 題2
python task2_caesar_cipher.py < input.txt

# 題3
python task3_digit_root.py < input.txt

# 題4
python task4_search_lab.py

# 全部測試
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 題4 二分搜尋效能 — 雷達圖說明

### 維度定義與正規化

雷達圖比較「線性搜尋」與「二分搜尋」在 5 個維度上的表現，每項給分 1–10（10 = 最有利）：

| 維度 | 線性評分 | 二分評分 | 正規化理由 |
|------|---------|---------|-----------|
| **Large N Speed**（大 n 速度） | 3 | 9 | 200k 實測 binary 快約 3000 倍 |
| **Small N Speed**（小 n 速度） | 9 | 5 | n 很小時線性常數低，二分分支預測 overhead 明顯 |
| **No Sort Needed**（不需排序） | 9 | 3 | binary 需預排序 O(n log n)，線性不用 |
| **Easy to Implement**（實作簡易度） | 9 | 5 | 線性 3 行程式，二分需處理邊界 |
| **Worst-case Comparisons**（最壞比較次數） | 9 | 3 | 線性 n 次 vs 二分 log n 次，但二分加排序成本 |

### 解讀

沒有絕對贏家：**大 n 且查多次**時二分壓倒性勝出；但**小 n 或只查一次**時，線性的簡潔與免排序讓它更具實用性。雷達圖清楚呈現 trade-off：效能不是單一數字，而是多維權衡。
