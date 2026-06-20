# Week 10（115/04/27－115/05/03）

- 主題：資料編碼與處理：CSV、JSON、XML、編碼轉換
- 教材：Python3 Cookbook 第六章
- 課堂範例：[`in-class/`](./in-class/)（5 記憶層 R + 1 理解層 U）
- 解題：[10226](./QUESTION-10226.md) | [10235](./QUESTION-10235.md) | [10242](./QUESTION-10242.md) | [10252](./QUESTION-10252.md) | [10268](./QUESTION-10268.md)
- 作業：完成 5 題並提交到 `weeks/week-10/solutions/<student-id>/`

---

## 課堂範例

| 範例 | 節次 | 主題 |
|------|------|------|
| [R01](./in-class/R01-csv-basic.py) | 6.1 | `csv.reader` / `DictReader` / `writer` |
| [R02](./in-class/R02-json-basic.py) | 6.2 | `json.loads` / `dumps` / `load` / `dump` |
| [R03](./in-class/R03-xml-parse.py) | 6.3 | `ElementTree` 基本解析 |
| [R04](./in-class/R04-encoding-hex-base64.py) | 6.9–6.10 | Hex / Base64 編碼解碼 |
| [R05](./in-class/R05-stats-counter.py) | 6.13 | `Counter` / `defaultdict` 統計 |
| [U01](./in-class/U01-timeit-decorator.py) | 6.1–6.3 | 計時裝飾器實作 + CSV / JSON / XML 速度比較 |

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 10226 | UVA 10226 | ⭐ | [QUESTION-10226.md](./QUESTION-10226.md) |
| 10235 | UVA 10235 | ⭐ | [QUESTION-10235.md](./QUESTION-10235.md) |
| 10242 | UVA 10242 | ⭐ | [QUESTION-10242.md](./QUESTION-10242.md) |
| 10252 | UVA 10252 | ⭐ | [QUESTION-10252.md](./QUESTION-10252.md) |
| 10268 | UVA 10268 | ⭐ | [QUESTION-10268.md](./QUESTION-10268.md) |


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