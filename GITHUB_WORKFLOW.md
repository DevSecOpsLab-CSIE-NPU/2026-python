# Visual Studio Code GitHub 操作流程

## A. 每週目標（Week #）

1. 在 VS Code 完成教材同步
2. 建立 `submit/week-#-<student-id>` 分支
3. 只在 `weeks/week-#/solutions/<student-id>/` 放作業
4. 由 VS Code 或 GitHub 建立 PR

---

## B. 進入作業前（VS Code 設定）

### 1) 開啟專案

- VS Code → `File` → `Open Folder...`
- 選擇你的課程 repo（學生自己的 repo）

### 2) 安裝建議擴充套件

- `GitHub Pull Requests and Issues`

### 3) 確認 Git 狀態

- 左側 `Source Control`（分支圖示）
- 底部狀態列確認目前分支（建議先在 `main`）

---

## C. 第一次設定 upstream（只做一次）

在 VS Code Terminal（`Terminal` → `New Terminal`）執行：

```bash
git remote add upstream https://github.com/DevSecOpsLab-CSIE-NPU/2026-python.git
git remote -v
```

你應看到：

- `origin`：你的 repo
- `upstream`：老師教材 repo

---

## D. Week # 實作流程（VS Code 版）

### Step 1：同步教材到 `main`

在 VS Code Terminal 執行：

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

> 同步前若有未提交變更，先 commit 或 stash。

### Step 2：建立本週分支

方式一（GUI）：

- 點底部左下角分支名稱
- `Create new branch...`
- 輸入：`submit/week-#-<student-id>`

方式二（Terminal）：

```bash
git checkout -b submit/week-#-<student-id>
```

### Step 3：建立本週作業目錄

在 Explorer 建立資料夾：

```text
weeks/week-#/solutions/<student-id>/
```

建議最少兩個檔案：

- `README.md`（完成題號、執行方式）
- `practice.md`（練習紀錄）

### Step 4：在 Source Control 提交

1. 到 `Source Control` 檢查變更檔案
2. 確認只有 `weeks/week-#/solutions/<student-id>/...`
3. 在訊息欄輸入：`Submit week-#`
4. 按 `Commit`
5. 按 `Publish Branch` 或 `Push`

若用 Terminal：

```bash
git add weeks/week-02/solutions/<student-id>/
git commit -m "Submit week-02"
git push -u origin submit/week-02-<student-id>
```

### Step 5：建立 PR

方式一（VS Code 擴充）：

- `Source Control` → `Create Pull Request`

方式二（GitHub 網站）：

- base：`main`
- compare：`submit/week-#-<student-id>`

PR 標題格式：

```text
Week # - <student-id> - <name>
```

範例：

```text
Week # - 411234001 - 王小明
```

---

## E. 路徑規範（一定要遵守）

### ✅ 允許提交

```text
weeks/week-02/solutions/<student-id>/
```

### ❌ 禁止修改

- `weeks/week-02/QUESTION-*.md`
- `weeks/week-02/README.md`
- `docs/*`（除非老師公告允許）

---

## F. PR 描述模板

```markdown
## 完成題號
- QUESTION-100
- QUESTION-118

## 執行方式
- python3 solution.py < input.txt

## 依賴套件
- 無

## 補充說明
- 目前已通過基本測資
```

---

## G. 提交前檢查清單

- [ ] 已同步 `upstream/main`
- [ ] 當前分支是 `submit/week-#-<student-id>`
- [ ] 只改到 `weeks/week-#/solutions/<student-id>/`
- [ ] PR 標題符合格式 -> :star: 回家作業請加上 "-HW-" 以示別
- [ ] PR 描述已填完整

---

## H. 評分與改分說明

- 助教會在 PR Review 留評語與分數
- 若後續修正，會用更新留言保留改分紀錄
- 正式成績以 LMS/成績表為準

---

## 延伸閱讀

- 學生版完整指南：`docs/SUBMISSION_GUIDE.md`
- 助教評分規範：`docs/TA_GRADING_GUIDE.md`
- PR 規範檢查：`.github/workflows/submission-policy-check.yml`
