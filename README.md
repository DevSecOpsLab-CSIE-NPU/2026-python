# 2026 Python CPE Weekly Practice

以開源專案常見結構整理每週課程與解題進度，方便協作、版本控管與後續擴充。

:point_right: 加入課程 DC https://discord.gg/uFzPj3TyW6

## 📁 目錄結構

```
.
├── .github/
│   └── workflows/
│       └── submission-policy-check.yml
├── assets/                         # 資料整理與腳本
├── docs/
│   ├── COURSE_PLAN.md              # 課程計劃表
│   ├── SUBMISSION_GUIDE.md         # 學生作業提交指南
│   ├── TA_GRADING_GUIDE.md         # 助教評分指南
│   └── analysis/                   # 📊 分析與報告（新增）
│       ├── README.md               # 分析文件導覽
│       ├── FINAL_SUMMARY.md        # 完整驗證報告（⭐ 從這裡開始）
│       ├── VERIFICATION_REPORT.md  # 優先級建議
│       ├── ANALYSIS_REPORT.md      # 課程分析
│       ├── questions_analysis.json # 結構化資料
│       ├── questions_analysis.csv  # Excel 匯入格式
│       └── ... (其他分析檔案)
├── weeks/
│   ├── week-01/ ~ week-18/
│   │   ├── README.md
│   │   ├── QUESTION-*.md
│   │   └── solutions/
├── CHECK_LIST.md                   # 題目文件品質檢查表
├── IN_CLASS_EXERCISE.md            # 課堂練習 PR 繳交紀錄（每週匯整）
├── HOMEWORK.md                     # 作業 PR 繳交紀錄（含內容檢核）
└── README.md (本檔案)
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

**Week 02 課堂練習**（2026-03-05）：✅ 24 人 ／ ⚠️ 11 人（含 7 筆補交）／ ❌ 20 人  
**Week 02 作業**：✅ 完整 11 人 ／ ⚠️ 部分缺失 2 人 ／ ❌ 未繳 42 人  
**Week 03 課堂練習**（2026-03-11）：✅ 10 人 ／ ⚠️ 2 人 ／ ❌ 43 人  
**Week 03 作業**：✅ 7 人 ／ ❌ 48 人  
**Week 04 課堂練習**（2026-03-18）：進行中，詳見 [IN_CLASS_EXERCISE.md](IN_CLASS_EXERCISE.md)

### 作業與批改規範
- 學生提交指南：[`docs/SUBMISSION_GUIDE.md`](docs/SUBMISSION_GUIDE.md)
- 助教評分指南：[`docs/TA_GRADING_GUIDE.md`](docs/TA_GRADING_GUIDE.md)

### Week 04 課堂範例（新增）

- 課堂範例目錄：[`weeks/week-04/in-class/`](weeks/week-04/in-class/)
- 涵蓋教材：Python3 Cookbook 第二章（字串）＋ 第三章（數字與日期時間）
- 共 **16 個範例檔**（9 記憶層 R + 7 理解層 U）

| 範例 | 節次 | 主題 |
|------|------|------|
| [R01](weeks/week-04/in-class/R01-strings-split-match.py) | 2.1–2.3 | `re.split` / `startswith` / `fnmatch` |
| [R02](weeks/week-04/in-class/R02-strings-regex.py) | 2.4–2.8 | 正則搜尋、替換、非貪婪、多行 |
| [R03](weeks/week-04/in-class/R03-strings-format.py) | 2.11–2.16 | `strip` / 對齊 / `join` / `format` |
| [R04](weeks/week-04/in-class/R04-strings-bytes.py) | 2.20 | `bytes` / `bytearray` |
| [R05](weeks/week-04/in-class/R05-numbers-basic.py) | 3.1–3.4 | `round` / `Decimal` / 進制轉換 |
| [R06](weeks/week-04/in-class/R06-numbers-special.py) | 3.7–3.11 | `inf` / `NaN` / `Fraction` / `random` |
| [R07](weeks/week-04/in-class/R07-datetime-basics.py) | 3.12–3.13 | `timedelta` / 指定星期計算 |
| [R08](weeks/week-04/in-class/R08-datetime-calendar.py) | 3.14–3.15 | 月份範圍 / `strptime` |
| [R09](weeks/week-04/in-class/R09-datetime-timezone.py) | 3.16 | `zoneinfo` 時區 |

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