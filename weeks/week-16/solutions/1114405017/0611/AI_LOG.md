# AI_LOG.md (範本)

請完整紀錄你與 AI 的互動提示詞與摘要（依作業規範，至少包含以下項目）：

- 學號 / 名稱：
- 階段 (Stage 1–5)：
- 提示詞（完全照打）：
- AI 回覆要點（摘要）：
- 你做了什麼修改（檔案 / commit）：
- 加速量化（Stage3，如適用）：
- 安全性修補摘要（Stage5，如適用）：

---

範例：

- 學號：1114405017
- Stage 1
- 提示詞："請幫我寫一個 timeit 裝飾器，保留 metadata 並維護 last_elapsed 與 records" 
- AI 回覆要點：提供裝飾器範本、提醒使用 functools.wraps
- 我做了：新增 `timing.py`，commit: `feat: stage1 實作 timeit`
