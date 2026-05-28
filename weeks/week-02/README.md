# Week 02（115/03/02－115/03/08）

- 主題：資料結構基礎（序列與字典技巧，排序與計數）
- 解題：本週無 `QUESTION-*.md`（題目已順延至 Week 03）
- 作業：完成繁中作業單（排序與序列處理，見 [HOMEWORK.md](./HOMEWORK.md)）
- 本週 GitHub 操作流程：[GITHUB_WORKFLOW.md](./GITHUB_WORKFLOW.md)

---

## 本週操作重點

- 熟悉 `origin` / `upstream` 的概念與同步流程
- 練習建立 `submit/week-02` 分支
- 練習在 `weeks/week-02/solutions/<student-id>/` 內提交檔案
- 練習建立 PR 並使用規定格式標題

---

## 本週回家作業（繁體中文）

詳細規格請見：[HOMEWORK.md](./HOMEWORK.md)

### 作業題目

1. **序列清理（Sequence Clean）**：去重（保留順序）、排序、偶數篩選
2. **學生成績排序（Student Ranking）**：多條件排序（分數、年齡、姓名）
3. **紀錄彙整（Log Summary）**：統計使用者事件次數與最常見動作

### 開發方式（Test-Oriented Development）

- 每題至少完成 1 次 `Red → Green → Refactor`
- 測試骨架需由學生自行撰寫（`tests/test_task*.py`）
- 需提交測試紀錄 `TEST_LOG.md`（至少 1 次失敗 + 1 次全通過）

### 繳交內容

- 程式檔：`task1_sequence_clean.py`、`task2_student_ranking.py`、`task3_log_summary.py`
- 測試檔：`tests/test_task1.py`、`tests/test_task2.py`、`tests/test_task3.py`
- 文件：`README.md`、`TEST_CASES.md`、`TEST_LOG.md`、`AI_USAGE.md`

### 提交規範

- 目錄：`weeks/week-02/solutions/<student-id>/`
- 分支：`submit/week-02`
- PR 標題：`Week 02 - <student-id> - <name>`
---

## 範例清單（Bloom 第 1 階 / 第 2 階）

### 記憶（R1–R20）

- `bloom-examples/R01-sequence-unpack.py`
- `bloom-examples/R02-star-unpack.py`
- `bloom-examples/R03-deque.py`
- `bloom-examples/R04-heapq-topn.py`
- `bloom-examples/R05-priority-queue.py`
- `bloom-examples/R06-defaultdict.py`
- `bloom-examples/R07-ordered-dict.py`
- `bloom-examples/R08-dict-min-max.py`
- `bloom-examples/R09-dict-sets.py`
- `bloom-examples/R10-dedupe.py`
- `bloom-examples/R11-slice.py`
- `bloom-examples/R12-counter.py`
- `bloom-examples/R13-itemgetter.py`
- `bloom-examples/R14-attrgetter.py`
- `bloom-examples/R15-groupby.py`
- `bloom-examples/R16-filtering.py`
- `bloom-examples/R17-dict-subset.py`
- `bloom-examples/R18-namedtuple.py`
- `bloom-examples/R19-generator-aggregate.py`
- `bloom-examples/R20-chainmap.py`

### 理解（U1–U10）

- `bloom-examples/U01-unpack-mismatch.py`
- `bloom-examples/U02-star-unpack-list.py`
- `bloom-examples/U03-deque-maxlen.py`
- `bloom-examples/U04-heapq-core.py`
- `bloom-examples/U05-priority-queue-index.py`
- `bloom-examples/U06-defaultdict-why.py`
- `bloom-examples/U07-ordered-dict-tradeoff.py`
- `bloom-examples/U08-dict-minmax-zip.py`
- `bloom-examples/U09-groupby-sort.py`
- `bloom-examples/U10-zip-iterator.py`


---

## AI 使用方式

1. 讀 {問題說明} 設計一版針對該問題的 python unit-test 程式，並加上繁體中文的註解放到 {指定目錄} 中
2. 幫我寫一版 python 程式，並跑完測試，並保留測試紀錄
3. 幫我加上繁體中文的註解說明
4. 有更簡單、更容易記憶的方式來寫這個程式，在檔名後加上 `-easy`
5. 幫我加上繁體中文的詳細註解說明

## 今天任務

因為 CPE 是要當場打程式設計出來，所以請手動把簡單版本程式在 `week-#/solutions/{學號}` 中打一遍你的程式，並進行測試。

以下是送出標準
- 參考 [GITHUB_WORKFLOW](GITHUB_WORKFLOW.md) 將程式 PR 出來
- 內容 (2 程式、1 測試 及 LOG 資料)要包括：
   - AI 教你的簡單版本，有中文註解
   - 你手打的程式
   - 測試程式
   - 你手打程式的測試 LOG 記錄