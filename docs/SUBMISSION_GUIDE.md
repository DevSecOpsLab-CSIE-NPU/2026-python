# 作業提交指南（學生版）

> 適用課程：2026 Python CPE Weekly Practice
> 
> 本課程採用 **GitHub Template + upstream 同步 + 每週 PR 提交**，不使用 GitHub Classroom。

---

## 1. Repository 設定（第一次）

1. 到課程模板建立自己的 repo（Use this template）
2. Clone 你的 repo 到本機
3. 在本機 repo 新增課程上游來源（upstream）

```bash
git remote add upstream https://github.com/DevSecOpsLab-CSIE-NPU/2026-python.git
```

可用以下指令確認：

```bash
git remote -v
```

---

## 2. 每次上課前同步教材

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

> 規範：同步前請先將自己的改動 commit，避免 merge 衝突。

---

## 3. 允許提交的目錄（非常重要）

作業只能放在：

```text
weeks/week-XX/solutions/<student-id>/
```

範例：

```text
weeks/week-03/solutions/411234001/
weeks/week-04/solutions/411234001/
```

禁止修改：

- `weeks/week-XX/README.md`
- `weeks/week-XX/QUESTION-*.md`
- `docs/*`（除非老師公告允許）

---

## 4. 每週提交流程（branch + PR）

以 week-03 為例：

```bash
git checkout -b submit/week-03
# 撰寫本週解答至 weeks/week-03/solutions/<student-id>/
git add .
git commit -m "Submit week-03"
git push origin submit/week-03
```

到 GitHub 開 Pull Request：

- base: `main`
- compare: `submit/week-03`
- 標題格式：`Week 03 - <student-id> - <姓名>`

例如：

```text
Week 03 - 411234001 - 王小明
```

---

## 5. PR 描述必填內容

請在 PR 描述中填寫：

- 完成題號（例：`QUESTION-100, QUESTION-118`）
- 執行方式（如何執行程式）
- 依賴套件（如果有）
- 其他補充說明（如未完成項目）

建議模板：

```markdown
## 完成題號
- QUESTION-100
- QUESTION-118

## 執行方式
- python3 solution.py < input.txt

## 依賴套件
- 無

## 補充說明
- QUESTION-118 尚未最佳化
```

---

## 6. 常見錯誤

- 直接在 `main` 開發，沒有建立 `submit/week-XX` 分支
- 修改到 `QUESTION-*.md` 或 `README.md`
- PR 標題格式不符規定
- 作業放錯資料夾（未放在 `solutions/<student-id>/`）

---

## 7. 快速檢查清單（提交前）

- [ ] 已先 `fetch + merge upstream/main`
- [ ] 作業僅在 `weeks/week-XX/solutions/<student-id>/`
- [ ] 分支名稱為 `submit/week-XX`
- [ ] PR 標題符合 `Week XX - 學號 - 姓名`
- [ ] PR 描述已填完成題號、執行方式、依賴套件
