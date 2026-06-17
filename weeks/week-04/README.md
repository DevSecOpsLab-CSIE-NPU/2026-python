# Week 04（115/03/16－115/03/22）

- 主題：數字與日期：進位與循環模擬
- 解題：[948](./QUESTION-948.md) | [10008](./QUESTION-10008.md) | [10019](./QUESTION-10019.md) | [10035](./QUESTION-10035.md) | [10038](./QUESTION-10038.md)
- 作業：完成 5 題並提交到 `weeks/week-04/solutions/<student-id>/`
- 課堂範例：[in-class/](./in-class/) — Python3 Cookbook 第二章（字串）＋ 第三章（數字與日期）

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 948 | UVA 948 | ⭐ | [QUESTION-948.md](./QUESTION-948.md) |
| 10008 | UVA 10008 | ⭐ | [QUESTION-10008.md](./QUESTION-10008.md) |
| 10019 | UVA 10019 | ⭐ | [QUESTION-10019.md](./QUESTION-10019.md) |
| 10035 | UVA 10035 | ⭐ | [QUESTION-10035.md](./QUESTION-10035.md) |
| 10038 | UVA 10038 | ⭐ | [QUESTION-10038.md](./QUESTION-10038.md) |

---

## 課堂範例：字串、數字與日期時間

範例目錄：[`in-class/`](./in-class/)　｜　共 **16 個範例檔**（9 記憶層 + 7 理解層）

### 記憶層（R）

| 檔案 | 節次 | 主題 |
|------|------|------|
| [R01](./in-class/R01-strings-split-match.py) | 2.1–2.3 | `re.split` / `startswith` / `fnmatch` |
| [R02](./in-class/R02-strings-regex.py) | 2.4–2.8 | 正則搜尋、替換、非貪婪、多行 |
| [R03](./in-class/R03-strings-format.py) | 2.11–2.16 | `strip` / 對齊 / `join` / `format` / `textwrap` |
| [R04](./in-class/R04-strings-bytes.py) | 2.20 | `bytes` / `bytearray` |
| [R05](./in-class/R05-numbers-basic.py) | 3.1–3.4 | `round` / `Decimal` / 數字格式化 / 進制轉換 |
| [R06](./in-class/R06-numbers-special.py) | 3.7–3.11 | `inf` / `NaN` / `Fraction` / `random` |
| [R07](./in-class/R07-datetime-basics.py) | 3.12–3.13 | `timedelta` / 指定星期日期計算 |
| [R08](./in-class/R08-datetime-calendar.py) | 3.14–3.15 | 月份範圍 / `strptime` / `strftime` |
| [R09](./in-class/R09-datetime-timezone.py) | 3.16 | `zoneinfo` 時區操作 |

### 理解層（U）

| 檔案 | 主題 | 關鍵陷阱 / 進階概念 |
|------|------|---------------------|
| [U01](./in-class/U01-strings-split-gotchas.py) | 分割與匹配陷阱 | 捕獲分組 / `startswith` 只接受 tuple / `strip` 不處理中間空白 |
| [U02](./in-class/U02-regex-advanced.py) | 正則進階 | 預編譯效能 / `sub` 回呼 / 大小寫一致替換 |
| [U03](./in-class/U03-strings-format-perf.py) | 格式化效能 | `join` vs `+` / `format_map` 缺失鍵 / `bytes` 索引回傳整數 |
| [U04](./in-class/U04-numbers-precision.py) | 數字精度 | 銀行家捨入 / `NaN != NaN` / `float` vs `Decimal` |
| [U05](./in-class/U05-datetime-gotchas.py) | 日期時間陷阱 | `timedelta` 不支援月份 / `strptime` 效能 |
| [U06](./in-class/U06-datetime-timezone.py) | 時區最佳實踐 | UTC 優先 / 夏令時邊界 |
| [U07](./in-class/U07-random-advanced.py) | 隨機進階 | 種子可重現性 / `secrets` 密碼學安全亂數 |
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
