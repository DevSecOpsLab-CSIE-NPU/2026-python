
# 0617 Starter — timeit + 搜尋效能評估(預演)

> 本日是 6/18 完整實驗室的**預演**:先把 `timeit` 做出來,再用它對搜尋做一次粗略評估。
> 細節與課堂節奏見 [`../0617-search-eval.md`](../0617-search-eval.md)。

## 使用方式

```bash
cp -r weeks/week-17/in_class/0617-starter weeks/week-17/solutions/<學號>/0617
cd weeks/week-17/solutions/<學號>/0617
```

## 固定循環

**Read spec → Dev for red(`test:` commit)→ Dev for green(`feat:` commit)→ push**。

## 檔案說明

- `test_timing.py`:任務一測試骨架,**先補齊測試、跑紅燈、commit,再寫 `timing.py`**
- `search.py` 與它的測試**沒有骨架,自己從零寫**——鷹架到此淡出
- `timing.py` 在**紅燈 commit 之後**才建立
- 完成後追加 `AI_LOG.md`(範本見 [`../../week-15/in_class/ai-log-template.md`](../../week-15/in_class/ai-log-template.md))與 `TEST_LOG.md`

## 規格速查

### 任務一 `timing.py`(走完整 TDD)

```python
def timeit(func): ...        # 帶 repeat 參數,預設 3
```

- 回傳值不變;`functools.wraps` 保留 metadata
- 每次呼叫實際跑 `repeat` 次,每次耗時 append 到 `f.records`
- `f.last_elapsed` = 本次 `repeat` 的平均耗時(float 秒)
- 裝飾器內不准 `print`
- `repeat < 1` → `raise ValueError`(用 `raise`,**不准 `assert`**)

### 任務二 `search.py`(輕量評估,不要求完整紅綠燈)

```python
def linear_search(data: list, target) -> int:   # 逐一比對,回傳 index,找不到回 -1
def binary_search(data: list, target) -> int:   # 前提:data 已排序;回傳 index 或 -1
```

- 兩者**不可修改傳入的 data**
- `binary_search` 收到未排序 data 的行為,自己定義並寫進 docstring
- 用你的 `timeit` 量 linear vs binary,把評估(誰快/排序划不划算/直覺)寫進 `README.md`

> 精確交叉點是明天 6/18 才用數據量出來的——今天先寫直覺。

## 任務二搜尋評估(我的數據與判斷)

用任務一的 `timeit`(`repeat=3` 取平均)量 `linear_search` vs `binary_search`,
腳本見 [`benchmark.py`](benchmark.py)。條件:`n = 2,000,000`、`data = range(n)`(已排序)、
`target` = 最後一個元素(linear 的最壞情況)。實測:

| 函式 | 平均耗時(秒) |
|------|--------------|
| `linear_search` | ~0.0506 |
| `binary_search` | ~0.0000044 |

1. **誰快?差多少?** 在已排序、目標在尾端時,`binary_search` 快約 **11,000 倍**
   (0.0506s vs 0.0000044s)。原因是 linear 是 O(n) 要走完 200 萬筆,binary 是
   O(log n) 約 21 步就結束。
2. **「排序 + binary」划不划算?(直覺)** 只搜尋**一次**的話**不划算**:排序成本是
   O(n log n),比 linear 的單次 O(n) 還貴,先排序反而虧。binary 的優勢要在
   **同一份資料反覆搜尋很多次**時才攤提得回來——排序一次、之後每次查詢都享受 O(log n)。
3. **交叉點:** 大概是「查詢次數多到 `q·n`(linear 總成本)超過 `n log n + q·log n`
   (排序一次 + q 次 binary)」的那一刻。精確的交叉點等明天 6/18 用數據量。

## 本日規則

- [x] 任務一先紅燈 commit(`test:`)再綠燈 commit(`feat:`)
- [x] **提示詞自己打**,逐字記入 `AI_LOG.md`;本目錄教案會讓 AI 自動進「開發訪談助教」模式,
      它會先反問規格、填滿檢查表才給 code
- [x] `AI_LOG.md` 新增「AI 反問我什麼 / 我怎麼回答」欄,逐項記下問答
- [x] 任務二搜尋評估**不要求完整紅綠燈**,重點是跑出數據、做出判斷
- [x] 45 分鐘內 push 並開出合法 PR