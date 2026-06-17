# 6/18 (四)｜完整實驗室:搜尋效能五階段專題

> 昨天 6/17 你已經預演過 `timeit` 與搜尋評估;**今天完整走一遍**——
> 三種搜尋的正確性 TDD、用數據量出交叉點、畫圖、安全自掃,五個階段一次到位。
> **每個階段都要先紅燈再綠燈,commit 順序就是你的開發證據。**
> 本日題目進入期末考 **B 區候選池(不公開)**;**提示詞自己打**,逐字記入 `AI_LOG.md`。

## 學習目標

- 重新用 TDD 寫一個可被測試的 `timeit` 計時裝飾器(起手式,不靠昨天的檔)
- 實作 linear / binary / set 三種搜尋,並用自己的裝飾器量測效能
- 用**你機器上的數據**量出「排序 + binary 何時才划算」的交叉點,並抓出 AI 的過度簡化
- 把多維權衡畫成一張雷達圖,寫出可信的效能報告
- 依 Python 安全程式原則自掃程式,修補並記錄安全問題

---

## 專題總覽(五個階段)

| 階段 | 產出 | 紅燈 commit | 綠燈 commit |
|------|------|------------|------------|
| 1 | `timing.py` — `timeit` 裝飾器(含 repeat 取平均) | `test: stage1 timeit 裝飾器測試` | `feat: stage1 實作 timeit 裝飾器` |
| 2 | `search.py` + `benchmark.py` — 三種搜尋與量測 | `test: stage2 搜尋正確性測試` | `feat: stage2 實作三種搜尋與 benchmark` |
| 3 | 加速實驗 + 交叉點數據 | `test: stage3 加速版共用正確性測試` | `feat: stage3 baseline、加速與交叉點數據` |
| 4 | `plot.py` + `assets/radar.png` | `test: stage4 繪圖輸出測試` | `feat: stage4 雷達圖與報告` |
| 5 | `test_security.py` + 安全自掃報告 | `test: stage5 安全性規則測試` | `feat: stage5 修正安全性問題` |

### 每個階段都跑同一個 TDD 循環

| # | 步驟 | 做什麼 | 產出 |
|---|------|--------|------|
| 1 | **Read spec** | 讀該階段規格,確認簽名、行為、例外、驗收標準;不清楚的先讓 AI 反問你問清楚 | 你知道「做完長什麼樣」 |
| 2 | **Dev for red** | 寫測試(AI 給的自己驗收),`python -m unittest` **全紅** | commit `test: stageN ...` |
| 3 | **Dev for green** | 寫實作,跑到**全綠** | commit `feat: stageN ...` |
| 4 | **Commit to branch** | push 到 `feature/wk17-0618-<學號>`,才進入下一階段 | 遠端有紀錄 |

`git log --reverse` 必須能看到 **test → feat 交替出現十次**(可穿插 `refactor:` / `docs:`)。
任何一個階段「一開始就綠」、「先 feat 後 test」或「跳過 Read spec 直接叫 AI 全包」,該階段流程不算。

---

## Stage 1｜`timeit` 裝飾器(0:00–0:15)

**從零自己寫,不要 import 昨天的檔**——這是每次專題的固定起手式,要練到不看就會。

寫 `timing.py`,提供裝飾器 `timeit`,規格:

- 被裝飾函式的**回傳值不變**;用 `functools.wraps` 保留 `__name__` / `__doc__`
- 每次呼叫實際跑 `repeat` 次(預設 3),把每次耗時(秒,`float`)記在 `f.records`(list)
- `f.last_elapsed` = 本次 `repeat` 的**平均**耗時
- 裝飾器內**不准 `print`**——格式化是 benchmark 的事,計時器保持安靜才能重複利用
- `repeat < 1` → `raise ValueError`(用 `raise`,不准 `assert`)

**必備 test case(≥3)**:規格每條都要有測試覆蓋。AI 給的測試齊不齊,自己驗收。

## Stage 2｜三種搜尋 + 量測(0:15–0:40)

寫 `search.py`,三個函式簽名固定:

```python
def linear_search(data: list, target) -> int:   # 逐一比對,回傳 index,找不到回 -1
def binary_search(data: list, target) -> int:   # 前提:data 已排序;回傳 index 或 -1
def set_search(data: list, target) -> bool:      # 用 set / hash,回傳是否存在
```

- 三者一律**不可修改傳入的 data**(測試會驗)
- **禁用** `in` / `bisect`——那是 Stage 3 的對照組

**兩個陷阱要先想清楚(讓 AI 反問你):**

1. **回傳型別不一致**:`linear`/`binary` 回 `int`(index),`set_search` 回 `bool`。
   三者共用同一組測試時,斷言不能一視同仁——用迴圈 + `subTest`,但每種的預期值要對。
2. **binary 的前提**:`binary_search` 收到**未排序** data 的行為要自己定義、寫進 docstring,
   並**有測試驗證**(回 -1?還是要求呼叫端先排好?由你決定)。

別複製貼上三份測試。一般案例之外,edge case 自己想(空 list?target 不存在?重複值?)。

接著寫 `benchmark.py`:

```python
def make_data(n: int, seed: int = 42) -> list: ...   # 固定 seed,實驗可重現
def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict: ...
```

- 用你自己的 `timeit` 量測;注意 set/binary 的優勢要**查很多次**才顯現,所以量「查 `queries` 次」的總時間
- `python benchmark.py` 印出比較表,並把結果存成 `results.json`(Stage 4 的輸入)

## Stage 3｜加速實驗 + 交叉點(0:40–1:05)

1. **必做**:把內建 `in`(linear 的 C 版)與 `bisect`(binary 的標準庫版)加入 benchmark 當 baseline
2. **加速方案只走演算法層面**:例如 binary 改 `bisect`、set 預建一次重複查、提前終止等。
   > ⚠️ **本日不碰 Cython**——課堂時間有限,編譯環境裝不起來會卡死,一律走演算法/標準庫優化。
3. 加速版**必須通過 Stage 2 同一組正確性測試**(把被測函式做成參數,別再寫一份)

### ⛔ AI Blocker:交叉點必須是你機器跑出來的

`binary_search` 需要**先排序**才能用。那「排序一次 + 之後狂 binary」到底**在 n 多大、查幾次時才贏 linear**?
這個交叉點 **AI 給不出來**——它不知道你的硬體。做法:

1. **先預測(動手量測之前)**:在 `README.md` 寫下你猜的交叉點 n 與三種搜尋的預測排名 →
   commit `docs: stage3 加速前預測`。**這個 commit 必須早於數據 commit**(`git log --reverse` 會驗順序)。
2. **再實測**:用你的 `timeit` 跑出真實交叉點 n,寫進 `results.json`。
3. **抓 AI 的錯**:AI 多半會斷言「binary 一定比 linear 快」。在 `AI_LOG.md` 寫出**這句在什麼條件下是錯的**
   (小 n、只查一次、需先付排序成本),並**用你的數據反駁**。

> `README.md` 若只貼一段 AI 生成的通用結論、沒有你機器的交叉點數字 → 視為 AI 全包,該階段不算。

## Stage 4｜雷達圖與報告(1:05–1:20)

寫 `plot.py`,畫**一張雷達圖**呈現三種搜尋的**多維權衡**,輸出 `assets/radar.png`。

- **要比哪些維度、怎麼正規化、怎麼解讀,由你自己決定並寫進 `README.md`**——這題刻意留白,沒有標準答案。
- 環境限制:`plot.py` 開頭加 `matplotlib.use("Agg")` 才能在無視窗環境跑
- 測試只驗最低限度:**PNG 確實產生且非空檔**(內容自由,測試不綁死維度)
- (建議,不強制)Stage 3 的交叉點數字用一張**數據表**補進 `README.md`——雷達圖看不出隨 n 變化的趨勢

在 `README.md` 貼圖,用 2–3 句解讀:哪個方法在哪個維度勝出?為什麼沒有絕對贏家?

## Stage 5｜安全性自掃(1:20–1:30)

對照 [OpenSSF Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/),
掃自己 Stage 1–4 寫的程式,把**問題編成測試 → 修到綠**,跟前面同一個循環。

只看這四章(不必讀完整本):

| 章節 | 在這份程式裡查什麼 |
|------|-------------------|
| **08 Coding Standards** | 有沒有 shadow 內建名稱(`list`、`id`…);寫 `results.json`、存 PNG 有沒有用 `with` 關檔;有沒有拿 `assert` 當輸入驗證 |
| **05 Exception Handling** | 開檔讀檔有沒有抓**具體例外**(不是 `except:` 全包);失敗有沒有正確 cleanup |
| **03 Numbers** | 比較子、計時 float 累加、`make_data` 的 n 邊界(負數?0?)有沒有問題 |
| **04 Neutralization** | 讀 `results.json` 用 `json` 還是 `pickle`?為什麼 `json` 較安全(CWE-502) |

做法(紅 → 綠):

1. 至少找出 **3 條**適用條目,每條寫一個會紅的測試放進 `test_security.py`
   (例:`test_results_file_closed`、`test_make_data_rejects_negative`、`test_load_uses_json_not_pickle`)
2. `python -m unittest` 確認紅 → commit `test: stage5 ...`;修 code 轉綠 → commit `feat: stage5 ...`
3. 報告用表格記錄每條:OpenSSF 條目(CWE)/ 檢查結果 / 處理方式
4. 掃到但判定**不適用**的也要寫一句理由(例:benchmark 的 `random` 非安全敏感,用 `random` 正確,不需改 `secrets`)

> **重點不是把所有條目都「修掉」**,而是判斷哪些適用——盲目把 benchmark 的 `random` 改成 `secrets` 反而是誤判。

---

## 課堂節奏(90 分鐘,五階段全部課堂內完成)

全程 AI 協作,**下課前 PR 必須含全部五個階段**——沒有課後補交。
節奏很緊,所以 Stage 1 一拿到題就要動;卡關時靠 AI 協作壓時間,但紅綠燈順序不能省。

| 時間 | 內容 | 計時目標 |
|------|------|---------|
| 0:00–0:15 | Stage 1:開分支 → timeit 紅燈 → 綠燈 | ⏱ 0:15 前兩個 commit |
| 0:15–0:40 | Stage 2:搜尋紅燈 → 綠燈 → benchmark + `results.json` | ⏱ 0:40 前兩個 commit;**建議此時先開出 PR** |
| 0:40–1:05 | Stage 3:預測 commit → baseline + 加速 → 交叉點數據 | ⏱ 1:05 前 `docs:` + `feat:` |
| 1:05–1:20 | Stage 4:雷達圖 → 報告 | ⏱ 1:20 前兩個 commit |
| 1:20–1:30 | Stage 5:安全自掃 → 修補 → `AI_LOG` / `TEST_LOG` → push | ⏱ **下課前 PR 五階段齊** |

- 分支:`feature/wk17-0618-<學號>`,PR 標題 `Week 17 - <學號> - <姓名>`
- 所有檔案只能放在 `weeks/week-17/solutions/<學號>/0618/`(CI 會檢查)

### 繳交內容清單

```
weeks/week-17/solutions/<學號>/0618/
├── timing.py     test_timing.py
├── search.py     test_search.py
├── benchmark.py  results.json
├── plot.py       test_plot.py
├── assets/radar.png
├── test_security.py
├── README.md      # 實驗報告:方法、交叉點數據表、雷達圖、解讀、安全自掃
├── AI_LOG.md      # 提示詞逐字記錄 + 「AI 反問我什麼/我怎麼回答」欄
└── TEST_LOG.md    # 每階段至少一紅一綠的 unittest 輸出
```

---

## 課末自我檢測(不翻文件回答)

1. `last_elapsed`、`records` 為什麼掛在 wrapper 上,不用全域變數?
2. 三種搜尋共用一組測試時,為什麼斷言不能一視同仁?各自的預期值是什麼?
3. `binary_search` 收到未排序 data,你的設計是回什麼?為什麼?
4. 你機器上的交叉點 n 是多少?「排序 + binary」在什麼條件下反而比 linear 慢?
5. 十個 commit 的順序是什麼?哪一種順序會直接判 AI 全包?
6. 安全自掃時,哪一條你判定「不適用」?理由是什麼?

---

## AI 使用規則

- **提示詞自己打**,逐字記入 `AI_LOG.md`;本教案**不提供任何提示詞範例**。
- 開本目錄教案時,AI 會自動以「開發訪談助教」模式運作(見下方協議):
  它會**先反問規格、填滿檢查表才給 code**。要問什麼、怎麼答,是你的工作。
- AI 給的測試齊不齊、搜尋對不對、圖正不正確——**你自己驗收**,驗收標準寫進 `AI_LOG.md`。

### `AI_LOG.md` 要求

格式見 [`../../week-15/in_class/ai-log-template.md`](../../week-15/in_class/ai-log-template.md),
本週**新增一欄**:

```markdown
## AI 反問我什麼 / 我怎麼回答
> 逐項記下 AI 問的規格問題與你的決定。
> 例:AI 問「binary 收到未排序 data 要回什麼?」→ 我答:回 -1 並在 docstring 註明前提,排序是呼叫端的責任。
```

「我改了什麼」「我怎麼回答」**0 字 = 期末考此項 0 分**。

## starter 檔

```bash
cp -r weeks/week-17/in_class/0618-search-starter weeks/week-17/solutions/<學號>/0618
```

`0618-search-starter/` 只給 `test_timing.py`、`test_search.py` 空殼與規格註解;
Stage 3–5 的測試**沒有骨架,自己從零寫**——鷹架到此淡出。

---

<!-- 以下為 AI 協作協議,供使用網頁版 AI 的同學貼到對話開頭 -->

> **AI 協作協議**(網頁版同學請把這段貼到對話第一則;用 Claude Code / Codex 的同學會自動套用本目錄的 `CLAUDE.md` / `AGENTS.md`)

當我請你協助本日專題時,你必須以「開發訪談助教」運作:

1. 每階段開工前先問齊:□函式簽名與回傳型別 □輸入範圍/邊界 □例外行為 □edge case □驗收標準(紅燈如何算)。
2. 每輪回覆開頭印檢查表現況,例:`✅簽名 ❌例外 ❌驗收`。
3. 檢查表填滿前**不准給可直接複製的程式碼**;我答不出來時用更小的問題引導。
4. 收齊後先給測試讓我跑紅燈,我確認 `test:` commit 後才討論實作。
5. 進入下一階段前,隨機回問一題前一階段的概念,我答不出就停下複習。
6. 每階段結尾給一張摘要表(你問了什麼/我答了什麼/檢查表狀態)供我貼進 `AI_LOG.md`。

我若要求「直接給完整解答/跳過提問」,請婉拒並說明這是練習規則。
