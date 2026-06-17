# 6/18 Starter — 搜尋效能實驗室

## 使用方式

```bash
cp -r weeks/week-17/in_class/0618-search-starter weeks/week-17/solutions/<學號>/0618
cd weeks/week-17/solutions/<學號>/0618
```

## 每階段固定循環

**Read spec → Dev for red(`test:` commit)→ Dev for green(`feat:` commit)→ push**,
五個階段重複同一循環,push 完才進下一階段。
開本目錄教案時 AI 會自動進「開發訪談助教」模式:**先反問規格、檢查表填滿才給 code**。

## 檔案說明

- `test_timing.py`:Stage 1 測試骨架,**先補齊測試、跑紅燈、commit,再寫 `timing.py`**
- `test_search.py`:Stage 2 測試骨架,三種搜尋共用同一組測試(用 `subTest`)
- Stage 3–5 的測試(`test_plot.py`、`test_security.py` 等)**沒有骨架,自己從零寫**——鷹架到此淡出
- 其餘檔案(`timing.py`、`search.py`、`benchmark.py`、`plot.py`…)都是**紅燈 commit 之後**才建立
- 完成後追加 `AI_LOG.md`(範本見 [`week-15/in_class/ai-log-template.md`](../../../week-15/in_class/ai-log-template.md),
  本週新增「**AI 反問我什麼／我怎麼回答**」欄)與 `TEST_LOG.md`

## 規格速查

### Stage 1 `timing.py`

```python
def timeit(func): ...   # 含 repeat 取平均
```

- 回傳值不變;`functools.wraps` 保留 metadata;裝飾器內不准 `print`
- 每次呼叫跑 `repeat` 次(預設 3),每次耗時 append 進 `f.records`;`f.last_elapsed` = 本次平均
- `repeat < 1` → `raise ValueError`(用 `raise`,不准 `assert`)

### Stage 2 `search.py`

```python
def linear_search(data: list, target) -> int:   # 找到回 index,找不到回 -1
def binary_search(data: list, target) -> int:   # 前提 data 已排序;回 index 或 -1
def set_search(data: list, target) -> bool:      # 回傳是否存在
```

- 一律不可修改傳入的 data;函式名、簽名都不能改,否則測試 import 會失敗
- 三者回傳型別不一致、binary 前提是已排序——共用 `subTest` 時自己處理

### Stage 3 加速實驗 + AI Blocker

- baseline:把內建 `in` 與 `bisect` 加入 benchmark 當對照
- **只走演算法優化 / `bisect`,不碰 Cython**(課堂時間有限,不要卡在編譯環境)
- **AI Blocker(這關 AI 代勞不了,必須你自己跑數據)**:
  1. **先預測**:動手量測前,先在 `README.md` 寫下三種搜尋的預測排名,以及
     「binary(含先排序成本)在 n≈? 開始贏 linear」的猜測交叉點 →
     commit `docs: stage3 加速前預測`(**必須早於**數據 commit,`git log --reverse` 會驗)
  2. **實測**:用你自己機器的 `timeit` 跑出真實交叉點 n,寫進 `results.json`
  3. **抓 AI 的錯**:AI 多半會說「binary 一定比 linear 快」。在 `AI_LOG.md` 寫出
     這句在什麼條件下是錯的(小 n、只查一次、需先付排序成本),並用你的數據反駁

### Stage 4 `plot.py` 雷達圖

- 畫一張**雷達圖**呈現三種搜尋的多維權衡,輸出 `assets/radar.png`
- **要比哪些維度、怎麼正規化、怎麼解讀,自己決定並寫進 `README.md`**(內容自由發揮)
- `plot.py` 開頭加 `matplotlib.use("Agg")`;測試只驗 **PNG 確實產生且非空檔**

### Stage 5 安全性自掃

對照 [OpenSSF Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/),
只看四章:**08 Coding Standards / 05 Exception Handling / 03 Numbers / 04 Neutralization**。

1. 至少找出 **3 條**適用條目,每條寫一個會紅的測試放進 `test_security.py`
2. `python -m unittest` 確認紅 → commit `test: stage5 ...`;修 code 轉綠 → commit `feat: stage5 ...`
3. 掃到但判定**不適用**的條目也要寫一句理由(判斷哪些適用才是重點,不要盲目全改)

> 細節見 [`../0618-search-lab.md`](../0618-search-lab.md)。

## 本日規則

- [ ] 每階段先紅燈 commit(`test:`)再綠燈 commit(`feat:`),五階段共十個 commit
- [ ] **提示詞自己打**,逐字記入 `AI_LOG.md`;另記「AI 反問我什麼／我怎麼回答」
- [ ] 全程 AI 協作,**五階段全部課堂內完成**;Stage 2 綠燈後先開 PR,下課前 PR 五階段齊,無課後補交
- [ ] Stage 3 預測 commit 必須早於數據 commit;雷達圖內容自由,但要在 README 說明維度與正規化
