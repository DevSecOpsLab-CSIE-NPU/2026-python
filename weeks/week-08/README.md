# Week 08（115/04/13－115/04/19）

- 主題：考前複習 ＋ 檔案與 I/O（Chapter 5）
- 解題：[10189](./QUESTION-10189.md) | [10190](./QUESTION-10190.md) | [10193](./QUESTION-10193.md) | [10221](./QUESTION-10221.md) | [10222](./QUESTION-10222.md)
- 作業：完成 5 題並提交到 `weeks/week-08/solutions/<student-id>/`

---

## 課堂練習：檔案與 I/O

**資料：** `in-class/stu-data/`（澎科大 109～114 學年度新生資料庫）  
**練習說明：** [in-class/WEEK08_EXERCISES.md](./in-class/WEEK08_EXERCISES.md)

| 題目 | 知識點 | 資料應用 | 難度 |
|------|-------|---------|------|
| 1 | `open()` + encoding + 篩選寫入 | 篩選繁星推甄學生 | ⭐ |
| 2 | `'x'` 模式 + `FileExistsError` | 年度報告防覆蓋 | ⭐ |
| 3 | `io.StringIO` 介面一致性 | 讓解析函式可單元測試 | ⭐⭐ |
| 4 | `gzip.open()` + `seaborn.lineplot` | 六年資料合併封存 + 趨勢折線圖 | ⭐⭐ |
| 5 | `pickle` 序列化 + `seaborn.barplot` | 招生統計快取 + 入學方式分佈圖 | ⭐⭐⭐ |

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 10189 | UVA 10189 — Minesweeper | ⭐ | [QUESTION-10189.md](./QUESTION-10189.md) |
| 10190 | UVA 10190 | ⭐ | [QUESTION-10190.md](./QUESTION-10190.md) |
| 10193 | UVA 10193 | ⭐ | [QUESTION-10193.md](./QUESTION-10193.md) |
| 10221 | UVA 10221 — Satellites | ⭐ | [QUESTION-10221.md](./QUESTION-10221.md) |
| 10222 | UVA 10222 — Decode the Mad man | ⭐ | [QUESTION-10222.md](./QUESTION-10222.md) |

## 今天任務

因為 CPE 是要當場打程式設計出來，所以請手動把簡單版本程式在 `week-#/solutions/{學號}` 中打一遍你的程式，並進行測試。

以下是送出標準
- 參考 [GITHUB_WORKFLOW](GITHUB_WORKFLOW.md) 將程式 PR 出來
- 內容 (2 程式、1 測試 及 LOG 資料)要包括：
   - AI 教你的簡單版本，有中文註解
   - 你手打的程式
   - 測試程式
   - 你手打程式的測試 LOG 記錄
