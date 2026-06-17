# Week 12（115/05/11－115/05/17）

> 📢 **合併補課**：Week 11 停課（115/06/12 生成式 AI 論壇），本週合併上課。
> 上課順序：先補 Week 11（類別與模組），再接 Week 12（數論與位元運算）。

---

## Week 11 補課：類別與模組（封裝、矩陣與優化）

- 課堂範例：[`../week-11/in-class/`](../week-11/in-class/)
- 解題：[10409](../week-11/QUESTION-10409.md) | [10415](../week-11/QUESTION-10415.md) | [10420](../week-11/QUESTION-10420.md) | [10642](../week-11/QUESTION-10642.md) | [10783](../week-11/QUESTION-10783.md)

| 範例 | 主題 |
|------|------|
| [R01](../week-11/in-class/R01-class-basic.py) | `__init__` / 方法 / `__repr__` / 類別變數 vs 實例變數 |
| [R02](../week-11/in-class/R02-property.py) | `@property` / getter / setter / 唯讀屬性 |
| [R03](../week-11/in-class/R03-inheritance.py) | 繼承 / `super()` / 方法覆寫 / `isinstance` |
| [R04](../week-11/in-class/R04-special-methods.py) | `__eq__` / `__lt__` / `__len__` / `__iter__` / `@total_ordering` |
| [R05](../week-11/in-class/R05-dataclass.py) | `@dataclass` / `field` / `frozen` / `__post_init__` |
| [U01](../week-11/in-class/U01-die-game.py) | 骰子模擬：用 class 封裝狀態（對應 UVA 10409）|

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 10409 | UVA 10409 — Die Game | ⭐ | [QUESTION-10409.md](../week-11/QUESTION-10409.md) |
| 10415 | UVA 10415 — Eb Alto Saxophone Player | ⭐ | [QUESTION-10415.md](../week-11/QUESTION-10415.md) |
| 10420 | UVA 10420 — List of Conquests | ⭐ | [QUESTION-10420.md](../week-11/QUESTION-10420.md) |
| 10642 | UVA 10642 — Can You Solve It? | ⭐ | [QUESTION-10642.md](../week-11/QUESTION-10642.md) |
| 10783 | UVA 10783 | ⭐ | [QUESTION-10783.md](../week-11/QUESTION-10783.md) |

---

## Week 12 本週：整除性、位元運算、矩陣搜尋

- 課堂範例：[`in-class/`](./in-class/)（4 記憶層 R + 1 理解層 U + 1 課堂活動）
- 解題：[10812](./QUESTION-10812.md) | [10908](./QUESTION-10908.md) | [10922](./QUESTION-10922.md) | [10929](./QUESTION-10929.md) | [10931](./QUESTION-10931.md)
- 作業：完成 5 題並提交到 `weeks/week-12/solutions/<student-id>/`

### 課堂範例與題目對應

| 範例 | 主題 | 對應題目 |
|------|------|---------|
| [R01](./in-class/R01-divisibility.py) | 整除性規則：數字位數和、9-degree、11 的倍數 | **10922**, **10929** |
| [R02](./in-class/R02-big-number.py) | 大數字串讀入、逐位處理 | 10929 補充 |
| [R03](./in-class/R03-binary-bits.py) | `bin()` / `format(n,'b')` / 位元運算 / 計算 1 的個數 | **10931** |
| [R04](./in-class/R04-matrix-search.py) | 2D 矩陣中心擴張、找最大全同字元正方形 | **10908** |
| [U01](./in-class/U01-number-theory.py) | 整合應用：Beat the Spread! / 2 the 9s / Can You Solve It? | **10812**, 10922, 10642 |
| [U02 活動](./in-class/U02-gcd-blink-game.py) | 課堂暖身：LCM 閃燈視覺化（非必考，概念延伸）| — |

> **注意**：本週核心是「整除性規則」與「二進位」，不是 GCD/LCM。
> U02 閃燈遊戲是用來直觀感受 LCM 的課堂活動，與解題作業無直接關聯。

### 解題清單

| # | 題名 | 難度 | 核心概念 |
|---|------|------|---------|
| 10812 | UVA 10812 — Beat the Spread! | ⭐ | 一元一次方程：`(S+D)/2`，判斷整數解與非負 |
| 10908 | UVA 10908 — Largest Square | ⭐ | 2D 矩陣中心擴張，找最大全同字元正方形 |
| 10922 | UVA 10922 — 2 the 9s | ⭐ | 遞迴數字位數和，判斷 9 的倍數與計算深度 |
| 10929 | UVA 10929 | ⭐ | 大數（最多 1000 位）判斷是否為 11 的倍數 |
| 10931 | UVA 10931 — Parity | ⭐ | 整數轉二進位，計算 1 的個數 |


---

## AI 使用方式

1. 讀 {問題說明} 設計一版針對該問題的 python unit-test 程式，並加上繁體中文的註解放到 {指定目錄} 中
2. 幫我寫一版 python 程式，並跑完測試，並保留測試紀錄
3. 幫我加上繁體中文的註解說明
4. 有更簡單、更容易記憶的方式來寫這個程式，在檔名後加上 `-easy`
5. 幫我加上繁體中文的詳細註解說明

## 今天任務

因為 CPE 是要當場打程式設計出來，所以請手動把簡單版本程式在 `weeks/week-12/solutions/{學號}` 中打一遍你的程式，並進行測試。

以下是送出標準
- 參考 [GITHUB_WORKFLOW](GITHUB_WORKFLOW.md) 將程式 PR 出來
- 內容 (2 程式、1 測試 及 LOG 資料)要包括：
   - AI 教你的簡單版本，有中文註解
   - 你手打的程式
   - 測試程式
   - 你手打程式的測試 LOG 記錄