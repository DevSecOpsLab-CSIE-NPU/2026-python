# Week 14（115/05/25－115/05/31）

- 主題：測試、除錯與例外 + 綜合練習
- 課堂範例：[`in_class/`](./in_class/) — Python3 Cookbook 第 14 章，依 Bloom's Taxonomy 分為 R/U 兩層共 5 個範例
- 解題：[11349](./QUESTION-11349.md) | [11417](./QUESTION-11417.md) | [11461](./QUESTION-11461.md) | [12019](./QUESTION-12019.md)
- 作業：完成 4 題並提交到 `weeks/week-14/solutions/<student-id>/`

---

## 課堂範例（in_class/）

涵蓋教材：[Python3 Cookbook 第 14 章：測試、調試和異常](https://python3-cookbook.readthedocs.io/zh-cn/latest/chapters/p14_test_debug_and_exceptions.html)

### 記憶層（R — Remember）

| 檔案 | 涵蓋節次 | 主題 |
|------|----------|------|
| [R01](./in_class/R01-unittest-basics.py) | 14.1–14.3 | unittest 基礎：`redirect_stdout` / `mock.patch` / `assertRaises` |
| [R02](./in_class/R02-exceptions-basic.py) | 14.6–14.8 | 例外處理基本：多例外 tuple / `except Exception` / 自定義例外 |
| [R03](./in_class/R03-profile-basic.py) | 14.13 | 效能測量：`timed` 裝飾器 / `timeit` / `cProfile` |

### 理解層（U — Understand）

| 檔案 | 涵蓋節次 | 主題 |
|------|----------|------|
| [U01](./in_class/U01-test-warnings-why.py) | 14.4, 14.5, 14.11 | 測試控制與警告：`skipIf` 的報表價值 / `stacklevel=2` / Warning 種類選擇 |
| [U02](./in_class/U02-debug-speedup-why.py) | 14.9, 14.10, 14.12, 14.14 | 例外、除錯與加速：四種 raise 寫法對照 / `print_exc` 必要性 / `LOAD_FAST` vs `LOAD_GLOBAL` |

詳細說明見 [`in_class/README.md`](./in_class/README.md)。

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 11349 | UVA 11349 — Symmetric Matrix | ⭐ | [QUESTION-11349.md](./QUESTION-11349.md) |
| 11417 | UVA 11417 — GCD | ⭐ | [QUESTION-11417.md](./QUESTION-11417.md) |
| 11461 | UVA 11461 — Square Numbers | ⭐ | [QUESTION-11461.md](./QUESTION-11461.md) |
| 12019 | UVA 12019 — Doom's Day Algorithm | ⭐ | [QUESTION-12019.md](./QUESTION-12019.md) |


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