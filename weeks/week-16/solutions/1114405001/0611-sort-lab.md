# 6/11 (四)｜分階段專題：排序效能實驗室

> 把 Week 10 的 `@timeit` 裝飾器、Week 13 的視覺化、Week 14-15 的 TDD + PR 流程,
> 整合成一個完整的小專題。**每個階段都要先紅燈再綠燈,commit 順序就是你的開發證據。**

## 學習目標

- 用 TDD 開發一個可被測試的 `@timeit` 計時裝飾器
- 實作 bubble / quick / merge 三種排序,並用自己的裝飾器量測效能
- 設計至少一種加速方案(Cython 化或演算法優化),用數據證明有效
- 把實驗結果畫成圖,寫出可信的效能報告
- 依 Python 安全程式原則自掃程式,修補並記錄安全問題

---

## 專題總覽(五個階段)

| 階段 | 產出 | 紅燈 commit | 綠燈 commit |
|------|------|------------|------------|
| 1 | `timing.py` — `@timeit` 裝飾器 | `test: stage1 timeit 裝飾器測試` | `feat: stage1 實作 timeit 裝飾器` |
| 2 | `sorts.py` + `benchmark.py` — 三種排序與量測 | `test: stage2 排序正確性測試` | `feat: stage2 實作三種排序與 benchmark` |
| 3 | 加速版排序(Cython 或演算法優化) | `test: stage3 加速版共用正確性測試` | `feat: stage3 加速版與量測數據` |
| 4 | `plot.py` + `assets/benchmark.png` | `test: stage4 繪圖輸出測試` | `feat: stage4 實驗結果圖表與報告` |
| 5 | `test_security.py` + 安全自掃報告 | `test: stage5 安全性規則測試` | `feat: stage5 修正安全性問題` |

### 每個階段都跑同一個 TDD 循環

| # | 步驟 | 做什麼 | 產出 |
|---|------|--------|------|
| 1 | **Read spec** | 讀該階段規格,確認函式簽名、行為、例外、驗收標準;不清楚的先問 AI 問清楚 | 你知道「做完長什麼樣」 |
| 2 | **Dev for red** | 寫測試(AI 給的自己驗收),`python -m unittest` **全紅** | commit `test: stageN ...` |
| 3 | **Dev for green** | 寫實作,跑到**全綠** | commit `feat: stageN ...` |
| 4 | **Commit to branch** | push 到 `feature/wk16-0611-<學號>`,才進入下一階段 | 遠端有紀錄 |

`git log --reverse` 必須能看到 **test → feat 交替出現十次**(可穿插 `refactor:`)。
任何一個階段「一開始就綠」、「先 feat 後 test」或「跳過 Read spec 直接叫 AI 全包」,該階段流程分 0 分。

---

## Stage 1｜`@timeit` 裝飾器(0:00–0:20)

寫 `timing.py`,提供裝飾器 `timeit`,規格:

- 被裝飾函式的**回傳值不變**
- 用 `functools.wraps` 保留 `__name__` / `__doc__`
- 每次呼叫後,把耗時(秒,`float`)記錄在:
  - `f.last_elapsed` — 最近一次的耗時
  - `f.records` — 歷次耗時的 list(累積)
- 裝飾器內**不准 `print`**——輸出格式化是 benchmark 的事,計時器保持安靜才能被重複利用

**必備 test case(≥3)**:規格的每一條都要有測試覆蓋。AI 給的測試齊不齊,自己驗收。

## Stage 2｜三種排序 + 量測(0:20–0:50)

寫 `sorts.py`,三個函式簽名固定:

```python
def bubble_sort(data: list) -> list: ...
def quick_sort(data: list) -> list: ...
def merge_sort(data: list) -> list: ...
```

- 一律**回傳新的 list,不可修改傳入的 list**(測試會驗)
- **禁用** `sorted()` / `list.sort()`——那是 Stage 3 的對照組

**必備 test case(每個函式都要過)**:一般案例之外,edge case 自己想(空的?重複?已排好?),
「不可修改傳入 list」也要有測試。三個函式共用同一組測試——用迴圈 + `subTest`,不要複製貼上三份。

接著寫 `benchmark.py`:

```python
def make_data(n: int, seed: int = 42) -> list: ...   # 固定 seed,實驗可重現
def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict: ...
```

- 用你自己的 `@timeit` 量測,每個 n 重複 `repeats` 次取 `records` 平均
- `python benchmark.py` 印出比較表,並把結果存成 `results.json`(Stage 4 的輸入)

## Stage 3｜加速實驗(0:50–1:10)

1. **必做**:把內建 `sorted()`(Timsort,C 實作)加入 benchmark 當 baseline
2. **至少一種加速方案**,自選:
   - **Cython 化**:把任一排序改寫成 `sorts_fast.pyx`(加上 `cdef` 型別註記),
     用 `pip install cython` + `setup.py build_ext --inplace` 或 `pyximport` 編譯
   - **演算法優化**:bubble 提前停止、quick 改 median-of-three、小區間切換插入排序等
3. 加速版**必須通過 Stage 2 同一組正確性測試**(把被測函式做成參數,別再寫一份測試)
4. 加速前後的數據都要進 `results.json`,報告要寫出加速比(例:`bubble 4000 筆:2.31s → 0.18s,12.8x`)

> ⚠️ Cython 編譯產物 `build/`、`*.c`、`*.so` **不准 commit**——只交 `.pyx` 原始碼與編譯指令說明。
> ⏱ 課堂時間有限:Cython 需要編譯環境,若現場 5 分鐘內裝不起來,**果斷改走演算法優化**,不要卡死。

## Stage 4｜畫圖與報告(1:10–1:30)

寫 `plot.py`:

```python
def load_results(path: str) -> dict: ...
def plot_results(results: dict, out_path: str) -> None: ...
```

- 折線圖:x 軸 = 資料量 n,y 軸 = 平均秒數(**y 軸用 log scale**,不然 O(n²) 會把其他線壓扁)
- 每個演算法一條線(含 baseline 與加速版),輸出 `assets/benchmark.png`
- 測試需驗證 PNG 確實產生且非空檔;環境限制:`plot.py` 開頭加 `matplotlib.use("Agg")` 才能在無視窗環境跑
- 在你的 `README.md` 貼圖並用 2–3 句解讀:誰最快?O(n²) 和 O(n log n) 的線斜率差在哪?加速比多少?

## Stage 5｜安全性自掃(1:15–1:30)

對照 [OpenSSF Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/),
掃自己 Stage 1–4 寫的程式,把**問題編成測試 → 修到綠**,跟前面同一個循環。

只看這四章(不必讀完整本):

| 章節 | 在這份程式裡查什麼 |
|------|-------------------|
| **08 Coding Standards** | 排序有沒有「邊迭代邊改 list」;有沒有 shadow 內建名稱;寫 `results.json`、存 PNG 有沒有用 `with` 關檔;有沒有拿 `assert` 當輸入驗證 |
| **05 Exception Handling** | 開檔讀檔有沒有抓**具體例外**(不是 `except:` 全包);失敗有沒有正確 cleanup |
| **03 Numbers** | 排序比較子、計時 float 累加、迴圈計數有沒有邊界/精度問題 |
| **04 Neutralization** | 讀 `results.json` 用 `json` 還是 `pickle`?為什麼 `json` 較安全(CWE-502) |

做法(紅 → 綠):

1. 至少找出 **3 條**適用條目,每條寫一個會紅的測試放進 `test_security.py`
   (例:`test_results_file_closed`、`test_make_data_rejects_negative`、`test_load_uses_json_not_pickle`)
2. `python -m unittest` 確認紅 → commit `test: stage5 ...`;修 code 轉綠 → commit `feat: stage5 ...`
3. 報告用表格記錄每條:OpenSSF 條目(CWE)/ 檢查結果 / 處理方式
4. 掃到但判定**不適用**的也要寫一句理由(例:benchmark 的 `random` 非安全敏感,用 `random` 正確,不需改 `secrets`)

> **重點不是把所有條目都「修掉」**,而是判斷哪些適用——盲目把 benchmark 的 `random` 改成 `secrets` 反而扣分。
> (選做・加分)`pip install bandit && bandit -r .`,把工具輸出和你人工找到的對照,寫一句兩者差異。

---

## 課堂節奏(90 分鐘,五階段全部課堂內完成)

全程 AI 協作,**下課前 PR 必須含全部五個階段**——沒有課後補交。
節奏很緊,所以 Stage 1 一拿到題就要動;卡關時靠 AI 協作壓時間,但紅綠燈順序不能省。

| 時間 | 內容 | 計時目標 |
|------|------|---------|
| 0:00–0:15 | Stage 1:開分支 → timeit 紅燈 → 綠燈 | ⏱ 0:15 前兩個 commit |
| 0:15–0:40 | Stage 2:排序紅燈 → 綠燈 → benchmark + `results.json` | ⏱ 0:40 前兩個 commit;**建議此時先開出 PR** |
| 0:40–1:00 | Stage 3:baseline + 加速版(過同一組測試) | ⏱ 1:00 前兩個 commit |
| 1:00–1:15 | Stage 4:畫圖 → 報告 | ⏱ 1:15 前兩個 commit |
| 1:15–1:30 | Stage 5:安全自掃 → 修補 → `AI_LOG` / `TEST_LOG` → push | ⏱ **下課前 PR 五階段齊** |

- 分支:`feature/wk16-0611-<學號>`,PR 標題 `Week 16 - <學號> - <姓名>`
- 所有檔案只能放在 `weeks/week-16/solutions/<學號>/0611/`(CI 會檢查)

### 繳交內容清單

```
weeks/week-16/solutions/<學號>/0611/
├── timing.py  test_timing.py
├── sorts.py   test_sorts.py
├── benchmark.py  results.json
├── sorts_fast.pyx(或演算法優化版)
├── plot.py    test_plot.py
├── assets/benchmark.png
├── test_security.py
├── README.md      # 實驗報告:方法、數據表、圖、解讀、加速比、安全自掃
├── AI_LOG.md      # 提示詞逐字記錄(規則同 6/10)
└── TEST_LOG.md    # 每階段至少一紅一綠的 unittest 輸出
```

### 評分(納入作業成績)

| 項目 | 配分 |
|------|------|
| Stage 1 timeit 正確 + 測試完整 | 15 |
| Stage 2 三排序正確 + 共用測試 + benchmark 可重現 | 25 |
| Stage 3 加速有效 + 通過共用測試 + 數據佐證 | 10 |
| Stage 4 圖表正確 + 解讀合理 | 10 |
| Stage 5 安全自掃 + 修補 + 不適用判斷合理 | 10 |
| Code Style(命名、繁中註解、無重複測試碼) | 15 |
| 報告與紀錄(README / AI_LOG / TEST_LOG / commit 順序) | 15 |

> **五階段全部下課前完成**,以 PR 為準,沒有課後補交。未在下課前綠燈 push 的階段不計分。

---

## 課末自我檢測(不翻文件回答)

1. `last_elapsed` 為什麼掛在 wrapper 上,不用全域變數?
2. 為什麼測試要驗「原 list 未被修改」?哪個排序最容易不小心改到?
3. benchmark 為什麼要固定 seed、重複多次取平均?
4. 你的加速方案如果只跑 n=500 看不出差異,該怎麼設計實驗?
5. 十個 commit 的順序是什麼?哪一種順序會直接 0 流程分?
6. 安全自掃時,哪一條你判定「不適用」?理由是什麼?

---

## AI 使用規則(同 6/10)

提示詞自己打、逐字記入 `AI_LOG.md`;「我改了什麼」0 字 = 期末考此項 0 分。
AI 給的測試齊不齊、排序對不對、圖正不正確——**你自己驗收**,驗收標準寫進 AI_LOG。

## starter 檔

```bash
cp -r weeks/week-16/in_class/0611-sort-starter weeks/week-16/solutions/<學號>/0611
```
