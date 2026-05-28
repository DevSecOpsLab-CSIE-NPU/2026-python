# Week 11（115/05/04－115/05/10）

> ⚠️ **停課公告**：本週停課，同學出席 115/06/12 生成式 AI 論壇。
> 本週教學內容（類別與模組）已移至 [Week 12](../week-12/README.md) 合併上課。

- 主題：類別與模組：封裝、矩陣與優化
- 課堂範例：[`in-class/`](./in-class/)（5 記憶層 R + 1 理解層 U）
- 解題：[10409](./QUESTION-10409.md) | [10415](./QUESTION-10415.md) | [10420](./QUESTION-10420.md) | [10642](./QUESTION-10642.md) | [10783](./QUESTION-10783.md)
- 作業：完成 5 題並提交到 `weeks/week-11/solutions/<student-id>/`

---

## 課堂範例

| 範例 | 主題 |
|------|------|
| [R01](./in-class/R01-class-basic.py) | `__init__` / 方法 / `__repr__` / 類別變數 vs 實例變數 |
| [R02](./in-class/R02-property.py) | `@property` / getter / setter / 唯讀屬性 |
| [R03](./in-class/R03-inheritance.py) | 繼承 / `super()` / 方法覆寫 / `isinstance` |
| [R04](./in-class/R04-special-methods.py) | `__eq__` / `__lt__` / `__len__` / `__iter__` / `@total_ordering` |
| [R05](./in-class/R05-dataclass.py) | `@dataclass` / `field` / `frozen` / `__post_init__` |
| [U01](./in-class/U01-die-game.py) | 骰子模擬：用 class 封裝狀態（對應 UVA 10409）|

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 10409 | UVA 10409 — Die Game | ⭐ | [QUESTION-10409.md](./QUESTION-10409.md) |
| 10415 | UVA 10415 — Eb Alto Saxophone Player | ⭐ | [QUESTION-10415.md](./QUESTION-10415.md) |
| 10420 | UVA 10420 — List of Conquests | ⭐ | [QUESTION-10420.md](./QUESTION-10420.md) |
| 10642 | UVA 10642 — Can You Solve It? | ⭐ | [QUESTION-10642.md](./QUESTION-10642.md) |
| 10783 | UVA 10783 | ⭐ | [QUESTION-10783.md](./QUESTION-10783.md) |


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