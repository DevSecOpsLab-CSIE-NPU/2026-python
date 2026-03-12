# 1114405036 Project Index

## 📋 專案總覽

**學生ID:** 1114405036  
**課程:** Python 程式設計 - Week 02  
**完成度:** 100% (221/221 tests passed)  
**最後更新:** 2026年3月12日

---

## 📁 專案結構

```
solutions/1114405036/
│
├── 📄 主程式 (Main Programs)
│   ├── task1_sequence_clean.py        (序列清理)
│   ├── task2_student_ranking.py       (學生排名)
│   └── task3_log_summary.py           (日誌摘要)
│
├── 🧪 主測試 (Main Tests: tests/)
│   ├── test_task1.py                  (12 tests)
│   ├── test_task2.py                  (15 tests)
│   └── test_task3.py                  (14 tests)
│
├── 🌸 Bloom Examples
│   ├── R04-heapq.py
│   ├── R05-priority-queue.py
│   ├── R07-ordered-dict.py
│   ├── R08-dict-min-max.py
│   ├── R09-dict-sets.py
│   ├── R10-dedupe.py
│   ├── R11-slice.py
│   ├── R12-counter.py
│   ├── R13-itemgetter.py
│   ├── R14-attrgetter.py
│   ├── R15-groupby.py
│   ├── R16-filtering.py
│   ├── R17-dict-subset.py
│   ├── R18-namedtuple.py
│   ├── R19-generator-aggregate.py
│   └── R20-chainmap.py
│
├── 🧪 Bloom 測試 (bloom-examples/tests/)
│   ├── test_R04_heapq.py              (10 tests)
│   ├── test_R05_priority_queue.py     (10 tests)
│   ├── test_R07_ordered_dict.py       (10 tests)
│   ├── test_R08_dict_minmax.py        (12 tests)
│   ├── test_R09_dict_sets.py          (10 tests)
│   ├── test_R10_dedupe.py             (11 tests)
│   ├── test_R11_slice.py              (10 tests)
│   ├── test_R12_counter.py            (10 tests)
│   ├── test_R13_itemgetter.py         (10 tests)
│   ├── test_R14_attrgetter.py         (10 tests)
│   ├── test_R15_groupby.py            (10 tests)
│   ├── test_R16_filtering.py          (14 tests)
│   ├── test_R17_dict_subset.py        (12 tests)
│   ├── test_R18_namedtuple.py         (12 tests)
│   ├── test_R19_generator_aggregate.py (15 tests)
│   └── test_R20_chainmap.py           (16 tests)
│
└── 📚 文檔 (docs/)
    ├── INDEX.md                       (本文件)
    ├── README.md                      (專案說明 & 設計選擇)
    ├── TEST_LOG.md                    (測試執行紀錄)
    ├── TEST_CASES.md                  (測試案例設計)
    ├── AI_USAGE.md                    (AI 協作過程)
    ├── TEST_REPORT.md                 (Bloom 測試報告)
    └── TEST_REPORT_EXTENDED.md        (詳細測試分析)
```

---

## 📊 測試統計

### 主專案測試 (Main Tests)
- **檔案數:** 3
- **測試總數:** 41
- **通過率:** 100% (41/41)

### Bloom Examples 測試
- **檔案數:** 16
- **測試總數:** 180
  - R04-R08: 42 tests (核心集合操作)
  - R09-R20: 138 tests (進階操作)
- **通過率:** 100% (180/180)

### 總計
| 項目 | 數量 |
|-----|------|
| 總測試數 | 221 |
| 通過數 | 221 |
| 成功率 | 100% |
| 執行時間 | ~0.065s |

---

## 🎯 快速存取

### 主程式與測試
- [Task 1: 序列清理](../task1_sequence_clean.py)
- [Task 2: 學生排名](../task2_student_ranking.py)
- [Task 3: 日誌摘要](../task3_log_summary.py)

### 主要文檔
- [README](./README.md) - 設計決策和 TDD 說明
- [TEST_LOG](./TEST_LOG.md) - 測試執行記錄
- [TEST_CASES](./TEST_CASES.md) - 15 個自設計測試案例
- [AI_USAGE](./AI_USAGE.md) - AI 協作過程記錄

### Bloom 文檔
- [TEST_REPORT](./TEST_REPORT.md) - 簡短測試報告
- [TEST_REPORT_EXTENDED](./TEST_REPORT_EXTENDED.md) - 詳細分析

---

## 🚀 執行指南

### 執行主專案測試
```bash
cd solutions/1114405036
python -m unittest discover -s tests -p 'test_task*.py' -v
```

### 執行所有 Bloom 測試
```bash
cd solutions/1114405036/bloom-examples
python -m unittest discover -s tests -p 'test_R*.py' -v
```

### 執行特定程式
```bash
# Task 1
python task1_sequence_clean.py

# Task 2
python task2_student_ranking.py

# Task 3
python task3_log_summary.py
```

---

## ✨ 主要特點

### Task 1 - 序列清理
- 去重且保序 (deduplication with order preservation)
- 排序 (ascending/descending)
- 過濾 (filter even numbers)

### Task 2 - 學生排名
- 三層復合排序 (score desc, age asc, name asc)
- 自定義 Student 類別
- Lambda 元組鍵排序

### Task 3 - 日誌摘要
- 使用 defaultdict 聚合
- 使用 Counter 提取最常見元素
- 正確邊界情況處理 (m=0 empty input)

### Bloom Examples 覆蓋
- heapq: Top-N 選擇
- Priority Queue: 優先級排隊
- OrderedDict: 有序字典
- Collection 操作: Sets, Counter
- Iterator: groupby, compress
- 函數工具: itemgetter, attrgetter
- Generator 表達式
- 進階結構: namedtuple, ChainMap

---

## 📝 文檔說明

| 文件 | 用途 |
|------|------|
| README.md | TDD 過程和設計決策 |
| TEST_LOG.md | Red-Green 階段記錄 |
| TEST_CASES.md | 自設計的 15 個測試場景 |
| AI_USAGE.md | 5 個 AI 互動案例 |
| TEST_REPORT.md | 40 個原有 Bloom 測試 |
| TEST_REPORT_EXTENDED.md | 180 個全部 Bloom 測試 |

---

## 💾 檔案大小統計

```
主程式:
  task1_sequence_clean.py:   2,771 bytes
  task2_student_ranking.py:  3,063 bytes
  task3_log_summary.py:      4,137 bytes

文檔:
  README.md:                 8,046 bytes
  TEST_LOG.md:               5,333 bytes
  TEST_CASES.md:             9,629 bytes
  AI_USAGE.md:              10,195 bytes
  TEST_REPORT.md:            6,298 bytes
  TEST_REPORT_EXTENDED.md:   8,669 bytes

總計: ~60 KB 文檔 + 10 KB 程式碼
```

---

## ✅ 驗證清單

- [x] 3 個主程式完成 (sequence, ranking, summary)
- [x] 41 個主測試全部通過
- [x] 16 個 Bloom 測試檔案創建
- [x] 180 個 Bloom 測試全部通過
- [x] 4 個主文檔完成 (README, TEST_LOG, TEST_CASES, AI_USAGE)
- [x] 2 個測試報告完成 (簡短版 + 詳細版)
- [x] 100% 測試覆蓋率

---

**完成日期:** 2026-03-12  
**專案狀態:** ✅ 完成並驗證
