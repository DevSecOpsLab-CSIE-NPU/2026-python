# 助教評分指南（TA Grading Guide）

> 適用課程：2026 Python CPE Weekly Practice

本課程採 PR 作為主要批改與溝通介面；正式成績以 LMS/成績表為準。

---

## 1. 批改對象與基本原則

- 每位學生每週建立一個 PR（`submit/week-XX` → `main`）
- 助教只審核該 PR 的變更內容
- 以「可執行、可重現、可追溯」為原則

---

## 2. 批改前檢查（必做）

1. PR 標題是否符合：`Week XX - <student-id> - <姓名>`
2. 變更路徑是否只在：`weeks/week-XX/solutions/<student-id>/`
3. 是否修改禁止路徑（`QUESTION-*.md`、`README.md`、`docs/*`）
4. PR 描述是否完整（完成題號、執行方式、依賴套件）

若不符合規範，先要求學生修正再進入評分。

---

## 3. 建議評分面向（100 分）

- Correctness：60 分
- Code Style：20 分
- Report/Docs：20 分

可依課程週次彈性調整比例，但請在公告同步規則。

---

## 4. PR 留言格式（統一模板）

請使用固定格式留言（或 Review）：

```text
Correctness: __/60
Code Style: __/20
Report/Docs: __/20
Total: __/100
Notes:
- 
```

建議補充：

- 至少 1 個優點
- 至少 1 個可改進項
- 若需重交，明確列出修正條件

---

## 5. 改分流程（需可追溯）

若學生修正後需改分：

- 方式 A：編輯原評分留言
- 方式 B：新增留言 `Score updated: old -> new`

建議採方式 B，保留完整歷史軌跡。

---

## 6. 建議標籤（可選）

可在 PR 使用以下 labels：

- `grading/pending`
- `grading/done`
- `needs-fix`
- `late-submission`

---

## 7. 爭議與例外處理

- 執行環境差異：以學生 PR 中提供的執行方式為主
- 疑似抄襲：標記 `needs-review`，交由授課教師處理
- 逾期提交：依課程公告扣分規則處理，並在 PR 留言註記

---

## 8. TA 快速檢查清單

- [ ] PR 標題格式正確
- [ ] 僅修改允許路徑
- [ ] 描述資訊完整
- [ ] 已給固定格式分數
- [ ] 改分有紀錄可追溯
