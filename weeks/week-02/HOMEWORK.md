# Week 02 回家作業：實作排序與序列處理

> 依據 Week 01 先備（容器、迴圈、函式、排序比較）與 Week 02 範例（sequence / deque / heapq / defaultdict / Counter / groupby）設計。

---

## 作業目標

- 熟悉序列資料（`list` / `tuple`）的切片、重組與遍歷
- 熟悉排序（`sorted`, `key`, `reverse`）與穩定排序觀念
- 熟悉計數與分組（`Counter`, `defaultdict`, `groupby`）
- 練習撰寫可重複執行且可驗證結果的 Python 程式
- 在可使用 AI 協助下，培養「規格判讀、測資設計、結果驗證、錯誤復盤」能力

---

## 題目與交付

請在 `weeks/week-02/solutions/<student-id>/` 建立以下檔案：

```text
weeks/week-02/solutions/<student-id>/
├── task1_sequence_clean.py
├── task2_student_ranking.py
├── task3_log_summary.py
├── tests/
│   ├── test_task1.py
│   ├── test_task2.py
│   └── test_task3.py
├── TEST_CASES.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```

### AI 使用原則（本作業適用）

- 可以使用 AI 產生程式草稿或重構建議
- 不可直接貼上 AI 回答後不驗證就提交
- 你必須為最終答案負責，並能解釋每個關鍵邏輯

---

## Test-Oriented Development（本作業必做）

請以「先測試，後實作」方式進行，每題至少完成 1 次 `Red → Green → Refactor`：

1. **Red**：先寫測試，確認目前會失敗
2. **Green**：撰寫最小可行程式，讓測試通過
3. **Refactor**：重構程式（命名、函式拆分、重複邏輯）且測試仍全綠

### 測試要求

- 每題至少 3 個測試案例（正常、邊界、反例）
- 共至少 9 個測試函式（`test_...`）
- 建議使用 Python 內建 `unittest`（不需額外安裝套件）
- `tests/test_task*.py` 測試骨架必須由學生自行撰寫，不可直接複製他人模板

### 測試執行紀錄（必交）

請建立 `TEST_LOG.md`，貼上至少 2 次測試執行摘要：

1. 一次 **Red**（尚未通過）
2. 一次 **Green**（全部通過）

每次需包含：

- 執行指令
- 測試總數、通過數、失敗數
- 你做了哪些修改才從失敗變通過（1~2 句）

### 測試執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 你要把心思放在哪裡（AI 協助下）

- 規格拆解：先寫出輸入/輸出與排序規則
- 測試設計：先想「怎樣會錯」再寫程式
- 結果驗證：比對預期與實際，不憑感覺
- 錯誤復盤：記錄 AI 建議失效的原因與修正策略

---

## Task 1：Sequence Clean（30 分）

### 題目說明
給定一行以空白分隔的整數，請輸出：

1. 去重後（保留第一次出現順序）的序列
2. 由小到大排序結果
3. 由大到小排序結果
4. 偶數序列（維持原始順序）

### 輸入範例

```text
5 3 5 2 9 2 8 3 1
```

### 輸出範例

```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

### 限制

- 不可用 `set` 直接輸出去重結果（因為會破壞順序）
- 必須用函式封裝主要流程

---

## Task 2：Student Ranking（35 分）

### 題目說明
給定多筆學生資料（`name score age`），請依規則排序：

1. `score` 由高到低
2. 同分時 `age` 由小到大
3. 再同時 `name` 字母序由小到大

輸出排序後前 `k` 名（`k` 由輸入給定）。

### 輸入格式

第一行：`n k`
接著 `n` 行：`name score age`

### 輸入範例

```text
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

### 輸出範例

```text
eva 92 20
zoe 92 21
bob 88 19
```

### 限制

- 必須使用 `sorted(..., key=...)`
- 不可手寫巢狀迴圈做交換排序

---

## Task 3：Log Summary（35 分）

### 題目說明
給定多行事件紀錄（`user action`），統計每位使用者行為次數，並輸出：

1. 每位使用者總事件數（依總數由大到小，若同數則使用者名稱由小到大）
2. 全域最常見 action 及其次數

### 輸入格式

第一行：整數 `m`（紀錄筆數）
接著 `m` 行：`user action`

### 輸入範例

```text
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
```

### 輸出範例

```text
bob 4
alice 3
chris 1
top_action: login 3
```

### 限制

- 需使用 `defaultdict` 或 `Counter`（至少一種）
- 程式需可處理空輸入（`m = 0`）

---

## README.md 內容要求

在 `weeks/week-02/solutions/<student-id>/README.md` 至少包含：

1. 完成題目清單（Task 1/2/3）
2. 執行方式（含 Python 版本）
	- 程式執行指令
	- 測試執行指令
3. 你的資料結構選擇理由（每題 1~2 句）
4. 你遇到的 1 個錯誤與修正方式
5. 各題 `Red → Green → Refactor` 摘要（每題至少 2~3 句）

---

## `TEST_CASES.md` 內容要求

至少提供 5 組你自行設計的測資，需包含：

1. 一般情況（正常輸入）
2. 邊界情況（空輸入或最小輸入）
3. 重複值/同分排序情況
4. 反例（容易寫錯的情況）
5. 你認為最能測出錯誤的一組

每組需寫出：

- 輸入
- 預期輸出
- 實際輸出
- 是否通過（PASS/FAIL）

並補充：

- 對應哪一個測試函式（例如 `tests/test_task2.py::test_tie_break_by_age`）
- 失敗到通過的關鍵修改點（1 句）

---

## `AI_USAGE.md` 內容要求

請記錄你如何使用 AI（簡要即可）：

1. 你問了哪些問題（可條列 3~5 條）
2. AI 給了哪些建議你有採用
3. AI 有哪些建議你拒絕（以及原因）
4. 至少 1 個「AI 可能誤導你」但你自行修正的案例

---

## 評分標準（100 分）

- Task 1 正確性與可讀性：20 分
- Task 2 排序邏輯正確性：20 分
- Task 3 統計正確性與邊界處理：20 分
- 測試骨架與 TDD 證據（`tests/` + `TEST_CASES.md` + `TEST_LOG.md`）：30 分
- AI 使用反思品質（`AI_USAGE.md`）：10 分

扣分項目：

- 修改到禁止路徑（`QUESTION-*.md`、`weeks/week-02/README.md`、`docs/*`）：-20 分
- 無法執行：-10 分
- 測試無法執行或測試數量不足（未達 9 個）：-10 分
- 測試骨架明顯非自行撰寫（含大量逐行相同）：-10 分
- 缺 `README.md` / `TEST_CASES.md` / `TEST_LOG.md` / `AI_USAGE.md` 任一檔案：-10 分（每缺一項）

---

## 提交規範（沿用課程規則）

- 分支：`submit/week-02`
- PR 標題：`Week 02 - <student-id> - <name>`
- 僅允許提交路徑：`weeks/week-02/solutions/<student-id>/`

參考：

- `weeks/week-02/GITHUB_WORKFLOW.md`
- `docs/SUBMISSION_GUIDE.md`
