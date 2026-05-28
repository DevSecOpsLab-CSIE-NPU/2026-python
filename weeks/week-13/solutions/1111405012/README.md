# Week 13 解題紀錄

student-id：`1111405012`

## 完成項目

- [HOMEWORK](../../HOMEWORK.md)：招生資料視覺化分析

## 目錄結構

```
weeks/week-13/solutions/1111405012/
├── task1_grouped_bar.py       # Task 1：112/113/114 學年三年並排長條圖
├── task2_zipcode_heatmap.py   # Task 2：縣市 × 年份招生人數熱力圖
├── output/                    # 自動產生的圖表
│   ├── task1.png
│   └── task2.png
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
├── TEST_LOG.md                # Red → Green 測試紀錄
├── REPORT.md                  # 資料分析心得
├── AI_USAGE.md                # AI 使用紀錄
└── README.md
```

## 依賴套件

```
matplotlib
numpy
```

安裝：

```bash
pip install matplotlib numpy
```

## 執行方式

### Task 1（三年並排長條圖）

```bash
python weeks/week-13/solutions/1111405012/task1_grouped_bar.py
```

### Task 2（縣市熱力圖）

```bash
python weeks/week-13/solutions/1111405012/task2_zipcode_heatmap.py
```

### 單元測試

```bash
python -m unittest discover -s "weeks/week-13/solutions/1111405012/tests" -p "test_*.py" -v
```

## 資料來源

`assets/stu-data/109～114年新生資料庫.csv`（位於 repo 根目錄）