# 程式設計期末考 解題方案

**學號：** 1114405041  
**姓名：** 賴俋勳  
**考試日期：** 2026-06-22

---

## 🎯 專案概述

本專案為期末考四題程式設計題目的完整解決方案，根據課程 SOP (Standard Operating Procedure) 完成，包括：
- ✅ **TDD 測試先行**：每題均先編寫單元測試
- ✅ **完整實作**：每題均提供可執行的程式
- ✅ **詳細文檔**：每題均有 README 說明與評分對照
- ✅ **AI 協作日誌**：見 [AI_LOG.md](./AI_LOG.md)

---

## 📋 四題總覽

### Q1：資料清理 (Data Cleaning) - 30分
```
檔案位置：Q1-data-cleaning/
目標：對輸入資料進行去重、排序、輸出
技能：集合運算、排序、字串格式化
```

**快速運行：**
```bash
cd Q1-data-cleaning
python -m unittest test_data_cleaning.py -v
```

---

### Q2：凱撒密碼 (Caesar Cipher) - 25分
```
檔案位置：Q2-caesar-cipher/
目標：使用凱撒密碼加密文字 (SHIFT=3)
技能：字元編碼、模運算、循環邏輯
```

**快速運行：**
```bash
cd Q2-caesar-cipher
python -m unittest test_caesar_cipher.py -v
```

---

### Q3：進位轉換 - 30分
```
檔案位置：Q3-number-base-conversion/
目標：將十進位數字轉換為任意進位
技能：進位演算法、除法運算、字符映射
```

**快速運行：**
```bash
cd Q3-number-base-conversion
python -m unittest test_number_base.py -v
```

---

### Q4：二分搜尋 - 20分
```
檔案位置：Q4-binary-search/
目標：實現高效的二分搜尋
技能：二分法、時間複雜度分析、性能測試
```

**快速運行：**
```bash
cd Q4-binary-search
python -m unittest test_binary_search.py -v
```

---

## 📁 目錄結構

```
0622-1114405041-賴俋勳/
├── AI_LOG.md                          # AI 協作日誌（對應評分標準）
├── README.md                          # 本文件
│
├── Q1-data-cleaning/                  # 題目 1：資料清理
│   ├── test_data_cleaning.py         # 單元測試
│   ├── data_cleaning.py              # 主程式
│   └── README.md                     # 題目說明
│
├── Q2-caesar-cipher/                  # 題目 2：凱撒密碼
│   ├── test_caesar_cipher.py         # 單元測試
│   ├── caesar_cipher.py              # 主程式
│   └── README.md                     # 題目說明
│
├── Q3-number-base-conversion/         # 題目 3：進位轉換
│   ├── test_number_base.py           # 單元測試
│   ├── number_base_conversion.py     # 主程式
│   └── README.md                     # 題目說明
│
└── Q4-binary-search/                  # 題目 4：二分搜尋
    ├── test_binary_search.py         # 單元測試
    ├── binary_search.py              # 主程式
    └── README.md                     # 題目說明
```

---

## 🧪 測試與驗證

### 全部測試
```bash
# 在根目錄執行
for dir in Q*/; do
    echo "Testing $dir..."
    cd "$dir"
    python -m unittest -v
    cd ..
done
```

### 個別測試
```bash
cd Q1-data-cleaning
python -m unittest test_data_cleaning.TestDataCleaning -v
```

---

## ✅ 評分對照表

### 總分統計

| 題號 | 題名 | 配分 | 評分項 | 細節 |
|------|------|------|--------|------|
| Q1 | 資料清理 | 30 | 讀取輸入(5) + 去重(10) + 排序(8) + 輸出(7) | [Q1 README](./Q1-data-cleaning/README.md) |
| Q2 | 凱撒密碼 | 25 | 讀取(4) + 大寫(6) + 小寫(6) + 特殊字元(5) + 輸出(4) | [Q2 README](./Q2-caesar-cipher/README.md) |
| Q3 | 進位轉換 | 30 | 讀取(4) + 算法(15) + 邊界(5) + 輸出(6) | [Q3 README](./Q3-number-base-conversion/README.md) |
| Q4 | 二分搜尋 | 20 | 讀取(3) + 搜尋(10) + 邊界(4) + 性能(3) | [Q4 README](./Q4-binary-search/README.md) |
| **合計** | | **105** | | |

### 邊界情況覆蓋

每題均包含至少 1 個 edge case：

| Q1 | Q2 | Q3 | Q4 |
|----|----|----|----|
| ✅ 空陣列 | ✅ 字母環繞 | ✅ 零值 | ✅ 空陣列 |
| ✅ 單元素 | ✅ 混合字元 | ✅ 大數字 | ✅ 單元素 |
| ✅ 全重複 | ✅ 特殊字元 | ✅ 各進位系統 | ✅ 首末元素 |

---

## 🔧 技術細節

### 使用的 Python 標準庫
```python
import unittest          # 單元測試框架
import timeit           # 性能測試
```

### 核心演算法

**Q1 - 去重排序：**
```python
unique_sorted = sorted(set(numbers))
```

**Q2 - 凱撒加密：**
```python
encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
```

**Q3 - 進位轉換：**
```python
digit = number % base
number //= base
```

**Q4 - 二分搜尋：**
```python
mid = (left + right) // 2
```

---

## 📊 時間複雜度分析

| 題目 | 算法 | 時間 | 空間 | 備註 |
|------|------|------|------|------|
| Q1 | 排序 | O(n log n) | O(n) | 使用內建 sorted |
| Q2 | 字串遍歷 | O(n) | O(n) | n = 字串長度 |
| Q3 | 進位轉換 | O(log n) | O(1) | n = 輸入數字 |
| Q4 | 二分搜尋 | O(log n) | O(1) | 常數空間 |

---

## 📝 SOP 檢查清單

按照課程 SOP，本專案完成以下步驟：

- ✅ **步驟 0**：Fork 課程 repo 並 clone
- ✅ **步驟 1**：從 main 開分支 `feature/exam-0622-1114405041`
- ✅ **步驟 2**：與 AI 拆分 ≥3 個 test case（含 ≥1 edge case）
  - Q1：5 個測試（2 個 edge case）
  - Q2：8 個測試（3 個 edge case）
  - Q3：8 個測試（3 個 edge case）
  - Q4：7 個測試（4 個 edge case）
- ✅ **步驟 3**：寫測試 → 確認紅燈 → `git commit -m "test: add failing tests for Qx"`
- ✅ **步驟 4**：寫實作 → 跑到綠燈 → `git commit -m "feat: implement Qx"`
- ✅ **步驟 5**：`git push -u origin feature/exam-0622-1114405041`
- ✅ **步驟 6**：開 PR (fork → course main)
- ✅ **步驟 7**：附 [AI_LOG.md](./AI_LOG.md)

---

## 🚀 快速開始

### 環境準備
```bash
# 進入題目資料夾
cd Q1-data-cleaning

# 直接運行測試
python -m unittest -v
```

### 單個題目測試
```bash
# 例如測試 Q2
cd Q2-caesar-cipher
python -m unittest test_caesar_cipher.TestCaesarCipher.test_example_from_problem -v
```

### 手動測試程式
```bash
# 例如 Q1
cd Q1-data-cleaning
python data_cleaning.py
# 輸入測試資料...
```

---

## 📖 相關文件

- [主課程 SOP 檢查表](../../week-15/in_class/exam-sop-checklist-lite.md)
- [完整 SOP 說明](../../week-15/in_class/README.md)
- [AI_LOG 範本](../../week-15/in_class/ai-log-template.md)

---

## 💡 學習重點

### 測試驅動開發 (TDD)
1. 先寫**失敗的測試**（紅燈）
2. 再寫**最小實作**使測試通過（綠燈）
3. 重構代碼保持測試通過（重構階段）

### 邊界情況考慮
- 空輸入
- 單個元素
- 最大/最小值
- 特殊字元

### 時間複雜度重要性
- 線性搜尋 O(n) vs 二分搜尋 O(log n)：在大數據時差異巨大
- 排序 O(n log n) vs 去重 O(n)

---

## 📞 問題排查

### 測試失敗？
1. 檢查是否正確安裝 Python 3.7+
2. 確認在正確的目錄執行測試
3. 檢查程式碼縮進（Python 對縮進敏感）

### 程式無法執行？
1. 確認輸入格式正確
2. 檢查是否在末尾輸入 EOF 信號
3. 查看錯誤信息並對應 README

---

## 📄 授權與致謝

本解決方案為課程期末考作業。

---

**最後更新：** 2026-06-22  
**狀態：** ✅ 完成
