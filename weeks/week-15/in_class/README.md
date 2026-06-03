# Week 15 課堂範例：TDD + Git PR 流程演練

本週兩堂課的共同目標：**把期末上機考的 SOP 在低風險環境下跑兩次**。

- 6/3 (三)：[流程熱身](./0603-warmup-drill.md)，用舊題練 SOP
- 6/4 (四)：[TDD 應用](./0604-tdd-practice.md)，新題 + `AI_LOG`

---

## 期末考 SOP 檢查表（學生版・完整版）

> ⚠️ **期末考當天只發[精簡版](./exam-sop-checklist-lite.md)（僅 8 個步驟標題，沒有指令細節）。**
> 下面這張**完整版只在本週兩堂練習課使用**——指令、commit message 格式、PR 要寫什麼，
> 考試當天要靠這兩堂練熟、自己回想得出來。鷹架是會收掉的：
> 本週帶完整表練 → 期末考給精簡標題表 → 職場靠肌肉記憶。

請照著做、邊做邊記下「為什麼這一步」：

```
[ ] 0. 第一次：Fork 課程 repo 到自己的 GitHub 帳號，再 clone 自己的 fork
       → git clone <你的 fork 網址>
       → cd <repo 目錄> && git remote add upstream <課程 repo 網址>
[ ] 1. 從 main 開分支：feature/wk15-<日期>-<學號>
[ ] 2. 跟 AI 把題目拆成 ≥3 個 test case（含 ≥1 個 edge case）
[ ] 3. 寫進 test_*.py，確認全部紅燈（失敗）
       → git commit -m "test: add failing tests for <題目>"
[ ] 4. 跟 AI 寫實作，直到全部綠燈（通過）
       → git commit -m "feat: implement <題目>"
[ ] 5. git push -u origin <分支>（push 到自己的 fork）
[ ] 6. 在 GitHub 開 PR：你的 fork <分支> → 課程 repo 的 main，PR 描述包含：
       - 題目摘要
       - 測試結果（pytest / unittest 輸出截圖或貼字）
       - 我跟 AI 改了什麼地方
[ ] 7. 6/4 起：PR 附 AI_LOG.md（見 ai-log-template.md）
```

---

## 為什麼順序不能反？

- **先 test 再 impl**：commit 順序是期末考客觀評分的依據之一（`git log --reverse` 可驗證）。先寫實作再補測試 = 0 流程分。
- **必須是「紅燈 → 綠燈」**：才證明測試真的在測東西。一開始就綠燈的測試 = 沒用的測試。
- **必須開 PR**：在自己 fork 的 main 上 commit、不開 PR 不算完成。期末考也一樣。

---

## 相關文件

- [SOP 檢查表・完整版（本檔上方）](#期末考-sop-檢查表學生版完整版)
- [SOP 檢查表・精簡版（期末考當天版本）](./exam-sop-checklist-lite.md)
- [6/3 教案](./0603-warmup-drill.md)
- [6/4 教案](./0604-tdd-practice.md)
- [AI_LOG 範本](./ai-log-template.md)

## 對應 Week 14 學過的工具

- `unittest.TestCase` / `assertEqual` / `assertRaises`：[week-14/in_class/R01](../../week-14/in_class/R01-unittest-basics.py)
- 例外處理：[week-14/in_class/R02](../../week-14/in_class/R02-exceptions-basic.py)

期末考一定會用到 unittest，請熟練 R01 的三個 API。
