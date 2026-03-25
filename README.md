# 2026 Python CPE Weekly Practice

以開源專案常見結構整理每週課程與解題進度，方便協作、版本控管與後續擴充。

:point_right: 加入課程 DC https://discord.gg/uFzPj3TyW6

## 📁 目錄結構

```
.
├── .github/
│   └── workflows/
│       └── submission-policy-check.yml
├── assets/                         # 題目資料整理與輔助腳本
├── docs/
│   ├── COURSE_PLAN.md              # 課程計劃表
│   ├── SUBMISSION_GUIDE.md         # 學生作業提交指南
│   ├── TA_GRADING_GUIDE.md         # 助教評分指南
│   └── analysis/                   # 分析與報告
├── weeks/
│   ├── README.md
│   ├── week-01/ ~ week-18/
│   │   ├── README.md
│   │   ├── QUESTION-*.md           # 有題目之週次才會出現
│   │   └── solutions/
│   └── ...
├── CHECK_LIST.md                   # 題目文件品質檢查表
├── ENROLLMENT.md                   # 修課學生清單
├── GITHUB_WORKFLOW.md              # GitHub 使用流程
├── HOMEWORK.md                     # 作業 PR 繳交紀錄（含內容檢核）
├── IN_CLASS_EXERCISE.md            # 課堂練習 PR 繳交紀錄（每週匯整）
└── README.md                       # 本檔案
```

## 📚 使用說明

### 課程組織
- 每週資料放在 `weeks/week-XX/` 目錄
- 題目說明檔 `weeks/week-XX/QUESTION-*.md`
- 解題代碼放在各週的 `solutions/` 子目錄
- 每週概覽放在各週 `README.md`

### 查看分析與報告
進入 [`docs/analysis/`](docs/analysis/) 目錄查看：
- **FINAL_SUMMARY.md** - 完整驗證報告與優先級建議（推薦首先閱讀）
- **CLASSIFICATION_TABLE.txt** - 所有 49 題的分類清單
- **questions_analysis.json/csv** - 結構化資料（資料分析或系統整合用）

更詳細的導覽和使用方式，請參考 [`docs/analysis/README.md`](docs/analysis/README.md)

### 繳交狀況追蹤

| 文件 | 說明 |
|------|------|
| [`IN_CLASS_EXERCISE.md`](IN_CLASS_EXERCISE.md) | 課堂練習 PR 繳交紀錄，依學號列出每週出席與提交狀況 |
| [`HOMEWORK.md`](HOMEWORK.md) | 作業 PR 繳交紀錄，含 task / tests / docs 內容檢核 |

**Week 02 課堂練習**（2026-03-05）：✅ 24 人 ／ ⚠️ 4 人 ／ ❌ 27 人  
**Week 02 作業**：✅ 完整 11 人 ／ ⚠️ 部分缺失 2 人 ／ ❌ 未繳 42 人  
**Week 03 課堂練習**（2026-03-11）：✅ 10 人 ／ ⚠️ 2 人 ／ ❌ 43 人  
**Week 03 作業**：✅ 7 人 ／ ❌ 48 人

### 作業與批改規範
- 學生提交指南：[`docs/SUBMISSION_GUIDE.md`](docs/SUBMISSION_GUIDE.md)
- 助教評分指南：[`docs/TA_GRADING_GUIDE.md`](docs/TA_GRADING_GUIDE.md)

### Week 03 任務
- 週次說明：[`weeks/week-03/README.md`](weeks/week-03/README.md)
- 題目範圍：UVA 100、118、272、299、490
- 建議流程：
	1. 讀題目說明並先設計 Python unit test
	2. 完成正式解題程式並執行測試
	3. 補上繁體中文註解
	4. 額外提供一版 easy（好記憶）版本
	5. 補上 easy 版本的繁體中文詳細註解
- 送出內容（2 程式、1 測試、1 測試紀錄）：
	- AI 教學的簡單版本（含中文註解）
	- 你手打的正式程式
	- 測試程式
	- 你手打程式的測試 LOG 記錄
- 建議放置路徑：`weeks/week-03/solutions/<student-id>/`

### 題目文件品質狀態（依 `CHECK_LIST.md`）
- 最後更新：2026-03-04
- 品質檢查：49 / 49 題通過（繁體中文、Markdown 排版、粗體標記、真實題目）
- 目前有題目之週次：Week 03, 04, 05, 07, 08, 10, 11, 12, 13, 14
- 詳細清單：[`CHECK_LIST.md`](CHECK_LIST.md)

### 題號參考
題目來源與題解：<https://yuihuang.com/cpe-level-1/>