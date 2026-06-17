# AI_LOG

## 我問 AI 什麼

> （你填）

## AI 給了什麼

> （你填）

## 我改了什麼

> **這一行最重要，不能空白。**（你填）

## AI 反問我什麼 / 我怎麼回答

### Stage 1 — timeit（同 0617 規格，從零寫）

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| `@timeit` 和 `@timeit(repeat=N)` 都支援？ | 兩者都要 |
| repeat 合法值？ | ≥1 正整數；float → TypeError |
| 例外行為？ | <1 → ValueError；被裝飾函式拋例外 → 原樣傳遞 |
| Edge case？ | repeat=1、records 重置、classmethod/staticmethod |
| 驗收標準？ | 回傳值被改、print、self.fail 殘留 → 紅燈 |

### Stage 2 — 三種搜尋

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 共用測試怎麼處理回傳型別不一致？ | 用 `_found()` 統一轉 bool 再斷言 |
| binary 收到未排序 data？ | 回 -1，docstring 寫明前提 |
| data 非 list？ | 拋 TypeError |
| 重複元素 binary 回傳？ | 碰到的那個 |

### Stage 3 — 加速實驗 + 交叉點

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 預測交叉點 n？ | 40~80 |
| 實際交叉點？ | 單次查詢永不交叉；100 次查詢 n≈20 |
| AI 錯在哪？ | 說「binary 一定比 linear 快」→ 在需先排序、只查一次時是錯的 |

### Stage 4 — 雷達圖

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 比哪些維度？ | Time(100/1000/10000/100000)、Scalability、Simplicity |
| 怎麼正規化？ | Min-max 到 [0,1]，時間倒轉（小 = 好） |

### Stage 5 — 安全自掃

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 找到哪些適用條目？ | make_data 負數無檢查(03 Numbers)、open() 未指定 encoding(08 Coding)、assert 替代檢查 |
| 哪些不適用？ | 無 with 關檔（已全用 with）、pickle 汙染（用 json 正確）、random 非安全敏感場景 |
