# Week-09 完成報告 - 學號 1114405001

## 任務概述
按照 Week-09 README 要求，完成資料夾 1114405001 的所有作業。

---

## ✅ 完成內容

### 1. 複習紀錄 (README.md)
- **檔案**: [README.md](README.md)
- **內容**: 
  - 7 個範例檔案的知識點整理
  - Bloom 分類進度表
  - 重點記憶方法與效能守則
  - 測試覆蓋範圍檢查表

### 2. 原始程式範例 (7 個檔案)
已保留所有原始教學範例：
- `R01-text-io-basics.py` - 文本 I/O 基本式
- `R02-path-and-listing.py` - 路徑操作與目錄列舉
- `U03-bytes-and-encoding.py` - 文字 vs 位元組、編碼觀念
- `U04-stringio-and-lines.py` - 類檔案物件 StringIO
- `U_02_itertools.py` - itertools 工具函數
- `A05-file-tasks.py` - 綜合應用：檔案操作
- `A06-gzip-tempfile-pickle.py` - 壓縮檔、臨時資料夾、物件序列化

### 3. 簡化版本（易記憶）- 7 個 (-easy) 檔案
✨ 新增「易記版」，包含更詳細的中文註解和實用技巧：
- `R01-text-io-basics-easy.py` - **重點**：write_text/read_text/逐行讀
- `R02-path-and-listing-easy.py` - **重點**：Path / exists / glob
- `U03-bytes-and-encoding-easy.py` - **重點**：'t' vs 'b' 一句話法則
- `U04-stringio-and-lines-easy.py` - **重點**：StringIO = 記憶體檔案
- `U_02_itertools-easy.py` - **重點**：5 個必記函數
- `A05-file-tasks-easy.py` - **重點**：'x' 模式 + 目錄統計
- `A06-gzip-tempfile-pickle-easy.py` - **重點**：3 個進階技巧

### 4. 單元測試程式
- **檔案**: [test_week09.py](test_week09.py)
- **涵蓋**: 
  - R01: 5 個測試
  - R02: 5 個測試
  - U03: 3 個測試
  - U04: 4 個測試
  - U_02: 6 個測試
  - A05: 2 個測試
  - A06: 3 個測試
  - **總計**: 28 個測試
- **測試結果**: ✅ 全部通過 (28/28)

### 5. 測試 LOG 記錄
- **檔案**: [test_log.txt](test_log.txt)
- **內容**: 完整的測試執行記錄
  ```
  Ran 28 tests in 0.034s
  成功率：100.0%
  ```

---

## 📊 測試覆蓋清單

| 模塊 | 測試項目 | 狀態 |
|------|---------|------|
| **R01** | 檔案讀寫、逐行迭代、分隔符控制 | ✅ |
| **R02** | 路徑操作、檔案搜尋、存在判定 | ✅ |
| **U03** | 編碼/解碼、位元組處理、異常捕捉 | ✅ |
| **U04** | StringIO、CSV 記憶體操作、行號加工 | ✅ |
| **U_02** | islice、dropwhile、takewhile、排列組合 | ✅ |
| **A05** | 獨占建立、目錄統計、檔案計數 | ✅ |
| **A06** | gzip 讀寫、臨時檔案清理、pickle | ✅ |

---

## 🎯 核心知識點掌握度

### Remember (記憶層)
- ✅ open() 的三種模式 ('r', 'w', 'a')
- ✅ encoding='utf-8' 必需
- ✅ Path 物件組合與屬性
- ✅ glob() vs rglob() 的差異

### Understand (理解層)
- ✅ 文字模式 vs 二進位模式的本質
- ✅ StringIO 作為鴨子型別的意義
- ✅ itertools 函數背後的迭代設計
- ✅ 編碼錯誤的成因與預防

### Apply (應用層)
- ✅ 日記工具的檔案模式設計
- ✅ 程式碼統計的遞迴走訪
- ✅ gzip 與檔案操作的整合
- ✅ tempfile 的實驗與測試應用

---

## 📝 檔案清單

```
1114405001/
├── README.md                          ← 複習紀錄
├── test_week09.py                    ← 單元測試程式（28 個測試）
├── test_log.txt                      ← 測試執行 LOG
├── R01-text-io-basics.py             ← 原始範例
├── R01-text-io-basics-easy.py        ← 簡化版（易記）
├── R02-path-and-listing.py           ← 原始範例
├── R02-path-and-listing-easy.py      ← 簡化版（易記）
├── U03-bytes-and-encoding.py         ← 原始範例
├── U03-bytes-and-encoding-easy.py    ← 簡化版（易記）
├── U04-stringio-and-lines.py         ← 原始範例
├── U04-stringio-and-lines-easy.py    ← 簡化版（易記）
├── U_02_itertools.py                 ← 原始範例
├── U_02_itertools-easy.py            ← 簡化版（易記）
├── A05-file-tasks.py                 ← 原始範例
├── A05-file-tasks-easy.py            ← 簡化版（易記）
├── A06-gzip-tempfile-pickle.py       ← 原始範例
└── A06-gzip-tempfile-pickle-easy.py  ← 簡化版（易記）
```

---

## 🚀 後續建議

### Level 1: 鞏固基礎
- 執行所有 -easy 版本，理解簡化邏輯
- 修改 -easy 版本，練習變化用法

### Level 2: 課堂延伸挑戰
1. **A05 挑戰**：
   - 日記工具改為 'a' 模式（同一天多次追寫）
   - count_py_files 加上「註解行數」統計
   - 統計結果寫到 `stats.tsv`

2. **自訂練習**：
   - 建立簡單的 CSV 資料分析工具
   - 用 gzip 壓縮舊日誌檔
   - pickle 儲存個人筆記的 dict

### Level 3: 預習 Week 10
- 準備 5 題新題型的分析

---

## ✨ 完成度檢查

- [x] 撰寫 README.md 記錄複習成果
- [x] 保留所有原始範例程式
- [x] 建立 -easy 簡化版本（7 個）
- [x] 編寫單元測試程式（28 個測試）
- [x] 執行測試並記錄 LOG
- [x] 所有測試通過 (100%)
- [x] 驗證簡化版本可執行性

---

**完成日期**: 2026-06-15  
**測試狀態**: ✅ 全數通過  
**程式碼品質**: ⭐⭐⭐⭐⭐
