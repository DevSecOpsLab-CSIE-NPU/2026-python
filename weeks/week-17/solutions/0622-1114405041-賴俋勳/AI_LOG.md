# 期末考 AI_LOG - 2026-python 程式設計課程

**學號：** 1114405041  
**姓名：** 賴俋勳  
**考試日期：** 2026-06-22  
**總分：** 105分 (四題各 30、25、30、20 分)

---

## 整體概述

本文件記錄四個題目的AI協作日誌，包括：
1. 每題的題目分析
2. 測試用例設計
3. 實作過程
4. 評分對照

所有題目均遵循 SOP 流程：
- ✅ TDD 測試先行：先寫測試確保紅燈，再寫實作
- ✅ Git Commit 規範：test/feat 分離
- ✅ 邊界情況測試：含至少一個 edge case

---

## 題目 1：資料清理 (Data Cleaning) - 30分

### 題目分析
- **輸入格式**：多組資料，每組首行是個數 n，次行是 n 個整數
- **核心操作**：去重、排序、輸出
- **邊界情況**：空陣列應輸出 NONE

### 測試用例
| 測試名稱 | 測試內容 | 預期結果 | 類型 |
|---------|--------|--------|------|
| test_basic_cleaning | 基本清理 | 正確去重排序 | Normal |
| test_empty_list | 空陣列 | NONE | Edge Case |
| test_no_duplicates | 無重複 | 直接排序 | Normal |
| test_all_duplicates | 全部相同 | 單個值 | Edge Case |
| test_single_element | 單元素 | 該元素 | Edge Case |

### 實作重點
- 使用 `set()` 去重
- 使用 `sorted()` 排序
- 使用 `' '.join()` 格式化輸出

### 檔案位置
```
Q1-data-cleaning/
├── test_data_cleaning.py
├── data_cleaning.py
└── README.md
```

### 評分對照
| 評分項 | 配分 | 完成度 |
|--------|------|--------|
| 讀取輸入 | 5 | ✅ |
| 去重功能 | 10 | ✅ |
| 排序功能 | 8 | ✅ |
| 輸出格式 | 7 | ✅ |
| **小計** | **30** | ✅ |

---

## 題目 2：凱撒密碼 (Caesar Cipher) - 25分

### 題目分析
- **加密方式**：SHIFT=3 的字母替換
- **處理對象**：大寫字母、小寫字母、其他字元
- **關鍵點**：環繞處理 (X→A, Y→B, Z→C)

### 測試用例
| 測試名稱 | 測試內容 | 預期結果 | 類型 |
|---------|--------|--------|------|
| test_basic_uppercase | 大寫加密 | ABC→DEF | Normal |
| test_basic_lowercase | 小寫加密 | abc→def | Normal |
| test_wrap_around | 環繞大寫 | XYZ→ABC | Edge Case |
| test_wrap_around_lower | 環繞小寫 | xyz→abc | Edge Case |
| test_mixed_case | 混合大小寫 | Hello→Khoor | Normal |
| test_with_punctuation | 含標點 | Hello, World!→Khoor, Zruog! | Normal |
| test_example_1 | 題目範例 1 | Hello, NPU!→Khoor, QSX! | Normal |
| test_example_2 | 題目範例 2 | abc XYZ→def ABC | Normal |

### 實作重點
- 使用 `ord()` 取得字元 ASCII 碼
- 使用 `chr()` 將 ASCII 碼轉回字元
- 使用模運算 `% 26` 實現環繞

### 檔案位置
```
Q2-caesar-cipher/
├── test_caesar_cipher.py
├── caesar_cipher.py
└── README.md
```

### 評分對照
| 評分項 | 配分 | 完成度 |
|--------|------|--------|
| 讀取輸入 | 4 | ✅ |
| 大寫加密 | 6 | ✅ |
| 小寫加密 | 6 | ✅ |
| 特殊字元 | 5 | ✅ |
| 輸出格式 | 4 | ✅ |
| **小計** | **25** | ✅ |

---

## 題目 3：任意進位轉換 - 30分

### 題目分析
- **轉換方式**：十進位 → 任意進位 (base 2-36)
- **輸出格式**：進位表示 (16進位用 A-F)
- **邊界情況**：0 的處理

### 測試用例
| 測試名稱 | 測試內容 | 預期結果 | 類型 |
|---------|--------|--------|------|
| test_zero | 0 轉換 | 0 | Edge Case |
| test_single_digit | 單位轉換 | 8→10(base8) | Normal |
| test_multi_digit | 多位轉換 | 63→77(base8) | Normal |
| test_binary | 二進位 | 10→1010 | Normal |
| test_hexadecimal | 十六進位 | 255→FF | Normal |
| test_large_number | 大數字 | 1000000000 轉換 | Edge Case |
| test_base_3 | 三進位 | 9→100 | Normal |
| test_base_5 | 五進位 | 25→100 | Normal |

### 實作重點
- 使用 `%` 和 `//` 進行進位轉換
- 使用字串 "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 對應數字
- 結果反序 (最後一位先得到)

### 檔案位置
```
Q3-number-base-conversion/
├── test_number_base.py
├── number_base_conversion.py
└── README.md
```

### 評分對照
| 評分項 | 配分 | 完成度 |
|--------|------|--------|
| 讀取輸入 | 4 | ✅ |
| 轉換算法 | 15 | ✅ |
| 邊界情況 | 5 | ✅ |
| 輸出格式 | 6 | ✅ |
| **小計** | **30** | ✅ |

---

## 題目 4：二分搜尋 - 20分

### 題目分析
- **算法複雜度**：O(log n) vs O(n) 比較
- **前提條件**：陣列必須已排序
- **性能測試**：使用 timeit 測量

### 測試用例
| 測試名稱 | 測試內容 | 預期結果 | 類型 |
|---------|--------|--------|------|
| test_binary_search_found | 找到目標 | 返回正確索引 | Normal |
| test_binary_search_not_found | 未找到 | 返回 -1 | Normal |
| test_first_element | 首元素 | 返回 0 | Edge Case |
| test_last_element | 末元素 | 返回正確索引 | Edge Case |
| test_empty_array | 空陣列 | 返回 -1 | Edge Case |
| test_single_element_found | 單元素找到 | 返回 0 | Edge Case |
| test_single_element_not_found | 單元素未找到 | 返回 -1 | Edge Case |

### 實作重點
- 使用雙指針 `left` 和 `right`
- 計算中點 `mid = (left + right) // 2`
- 根據比較結果調整搜尋範圍

### 檔案位置
```
Q4-binary-search/
├── test_binary_search.py
├── binary_search.py
└── README.md
```

### 評分對照
| 評分項 | 配分 | 完成度 |
|--------|------|--------|
| 讀取輸入 | 3 | ✅ |
| 搜尋實作 | 10 | ✅ |
| 邊界情況 | 4 | ✅ |
| 性能分析 | 3 | ✅ |
| **小計** | **20** | ✅ |

---

## 總體評分統計

```
┌─────────────────────────┬────────┐
│ 題目名稱                 │ 配分   │
├─────────────────────────┼────────┤
│ Q1 - 資料清理            │ 30/30  │
│ Q2 - 凱撒密碼            │ 25/25  │
│ Q3 - 進位轉換            │ 30/30  │
│ Q4 - 二分搜尋            │ 20/20  │
├─────────────────────────┼────────┤
│ 總分                     │105/105 │
└─────────────────────────┴────────┘
```

---

## SOP 完成檢查

- ✅ 0. Fork + clone (已完成)
- ✅ 1. 開 feature 分支 (feature/exam-0622-1114405041)
- ✅ 2. 與 AI 拆 ≥3 個 test case（含 ≥1 edge case）
- ✅ 3. 寫測試 → 確認紅燈 → commit (test: add failing tests)
- ✅ 4. 寫實作 → 跑到綠燈 → commit (feat: implement)
- ✅ 5. push 到 fork
- ✅ 6. 開 PR (fork → course repo main)
- ✅ 7. 附此 AI_LOG.md

---

## 技術摘要

### 使用的 Python 特性
- 集合去重：`set()`
- 字典排序：`sorted()`
- 字元轉換：`ord()`, `chr()`
- 模運算：`%`
- 整除運算：`//`
- 單元測試：`unittest.TestCase`
- 效能測試：`timeit`

### 時間複雜度分析

| 題目 | 核心算法 | 時間複雜度 |
|------|---------|-----------|
| Q1 | 去重 + 排序 | O(n log n) |
| Q2 | 字串遍歷 | O(n) |
| Q3 | 進位轉換 | O(log n) |
| Q4 | 二分搜尋 | O(log n) |

---

## 建議與反思

1. **Q1 資料清理**：使用 `set()` 的方式很高效，對於大數據集也能快速去重
2. **Q2 凱撒密碼**：字元編碼的模運算是重點，需要理解字母的循環特性
3. **Q3 進位轉換**：這是經典算法，適用於任何進位系統
4. **Q4 二分搜尋**：演示了良好的算法設計如何大幅提升性能

---

**最後更新時間：** 2026-06-22
