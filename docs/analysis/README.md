# 📊 分析文件 (Analysis Documents)

此目錄包含 CPE 題目系統的完整分析、驗證報告與資料匯出。

## 📋 文件清單

### 核心報告（優先閱讀）

| 檔案 | 用途 | 時間 |
|------|------|------|
| **FINAL_SUMMARY.md** | 完整驗證報告 + 優先級建議（推薦首先閱讀） | 15 min |
| **VERIFICATION_REPORT.md** | 驗證結果與優先級詳細說明 | 10 min |
| **ANALYSIS_REPORT.md** | 課程設計與演算法分析 | 10 min |

### 快速查詢

| 檔案 | 用途 | 格式 |
|------|------|------|
| **CLASSIFICATION_TABLE.txt** | 所有 49 題的分類表 | 純文字表格 |
| **README_ANALYSIS.md** | 分析概覽與導覽 | Markdown |
| **ANALYSIS_INDEX.md** | 詳細導覽索引 | Markdown |

### 結構化資料（資料整合）

| 檔案 | 用途 | 格式 | 大小 |
|------|------|------|------|
| **questions_analysis.json** | 49 題完整分析資料 | JSON | 32 KB |
| **questions_analysis.csv** | 試算表匯入格式 | CSV | 1.9 KB |

### 待補充題目清單

| 檔案 | 用途 | 格式 |
|------|------|------|
| **INCOMPLETE_QUESTIONS.md** | 待補充題目清單（Markdown） | Markdown |
| **INCOMPLETE_QUESTIONS_INVENTORY.csv** | 待補充清單（Excel） | CSV |
| **INCOMPLETE_QUESTIONS_INVENTORY.json** | 待補充清單（JSON） | JSON |

---

## 🎯 快速開始

### 我是教師/課程規劃者
👉 **讀這個**: FINAL_SUMMARY.md (15 分鐘)
- 了解完整驗證結果
- 掌握 49 題分配狀況
- 獲得優先級行動建議

### 我是開發者/資料分析師
👉 **用這個**: questions_analysis.json 或 .csv
- 完整結構化資料
- 易於導入試算表或資料庫
- 包含所有關鍵欄位（難度、演算法、週次等）

### 我想快速查詢特定題目
👉 **看這個**: CLASSIFICATION_TABLE.txt
- 所有 49 題列表
- 按週次組織
- 難度與關鍵詞標籤

### 我要規劃補充工作
👉 **參考這個**: VERIFICATION_REPORT.md + INCOMPLETE_QUESTIONS.md
- Priority 1-4 行動計劃
- 待補充題目清單
- 工作量估計

---

## 📊 檔案內容概述

### FINAL_SUMMARY.md
**重點摘要**:
- ✅ 49 題正確分配，難度遞進合理
- 🎯 4 層優先級行動計劃 (Priority 1-4)
- 📈 系統評分 (結構 5/5, 難度遞進 5/5, 完成度 4/5)

**何時閱讀**: 首次了解時

---

### VERIFICATION_REPORT.md
**重點內容**:
- 驗證結果詳細說明
- Priority 1-3 補充計劃（含工作量估計）
- 演算法多樣性改進建議

**何時閱讀**: 規劃補充工作時

---

### ANALYSIS_REPORT.md
**重點內容**:
- 課程設計分析
- 難度分布與週次對應
- 演算法覆蓋分析

**何時閱讀**: 深入了解課程設計時

---

### CLASSIFICATION_TABLE.txt
**內容**: 49 題完整清單，組織方式：
```
按週次分組
  ├─ Week 2 (5 題)
  ├─ Week 3 (5 題)
  ├─ Week 4 (5 題)
  └─ ...以此類推
```

**欄位**: UVA ID, 題名, 難度, 關鍵詞, 字數

**何時使用**: 快速查詢或列印參考

---

### questions_analysis.json
**格式**: JSON 陣列，49 個物件

**欄位範例**:
```json
{
  "uva_id": 100,
  "week": 2,
  "title": "題目 100",
  "keywords": "graph",
  "difficulty": "Medium",
  "content_length": 827
}
```

**何時使用**: 資料整合、程式處理

---

### questions_analysis.csv
**欄位**: UVA_ID, Current_Week, Title, Keywords, Difficulty, Content_Length

**何時使用**: Excel/Google Sheets 匯入

---

### INCOMPLETE_QUESTIONS.md
**內容**: 15 個待補充題目的清單
- 題號與所在週次
- 缺失欄位說明
- 補充建議

**何時使用**: 規劃補充優先級時

---

## 🚀 建議工作流程

### 第 1 步：了解現況
1. 讀 FINAL_SUMMARY.md (15 min)
2. 掌握 49 題分配與優先級

### 第 2 步：選擇行動
1. 根據優先級選擇 Priority 1/2/3
2. 參考 VERIFICATION_REPORT.md 了解工作量

### 第 3 步：查詢與規劃
1. 用 CLASSIFICATION_TABLE.txt 查詢具體題目
2. 用 INCOMPLETE_QUESTIONS.md 識別待補充項目

### 第 4 步：資料匯出
1. 需要在 Excel 分析？→ 用 .csv 檔
2. 需要整合進系統？→ 用 .json 檔

---

## 📈 統計數字速查

| 指標 | 數值 |
|------|------|
| 總題目數 | 49 |
| 覆蓋週次 | 10 (Week 2,3,4,6,7,9,10,11,12,13) |
| 完整題目 | 34 (69%) |
| 待補充題目 | 15 (31%) |
| 簡單難度 | 8 題 (16%) |
| 中等難度 | 34 題 (69%) |
| 困難難度 | 7 題 (14%) |
| 識別演算法 | 9 種 |
| 基礎通才題 | 36 (73.5%) |

---

## 🔗 相關資源

- **題目來源**: https://yuihuang.com/cpe-level-1/
- **ZeroJudge**: https://zerojudge.tw/
- **UVA Online Judge**: https://uva.onlinejudge.org/

---

**最後更新**: 2026-02-25  
**驗證狀態**: ✅ 完整驗證，可立即使用
