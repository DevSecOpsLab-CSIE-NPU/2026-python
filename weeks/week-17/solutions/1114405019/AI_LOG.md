## 我問 AI 什麼

讀取 `weeks/week-17/in_class/0617-search-eval.md` 與 `weeks/week-17/README.md`,
照規格做出 `timeit` 裝飾器與 `linear_search` / `binary_search`,並把成品放進
`weeks/week-17/solutions/1114405019`。提問時已經自己先想清楚 *args/**kwargs
的轉發方式、`records` 要掛在 wrapper 物件上、邊界驗證範圍(int 且 >=1)、
例外不計入 records、以及至少 5 個驗收測試案例。

## AI 反問我什麼 / 我怎麼回答

> 本目錄的 `AGENTS.md` / `CLAUDE.md` 規定 AI 開工前要先問齊「函式簽名、邊界、
> 例外行為、edge case、驗收標準」五項,填滿才給 code。

- AI 檢查我貼的設計說明,確認五項是否已經填齊:
  - ✅ 函式簽名與回傳型別:`timeit(repeat=3)` 回傳裝飾器,`wrapper(*args, **kwargs)` 透傳並回傳原值。
  - ✅ 輸入範圍/邊界:`repeat` 必須是 `int` 且 `>= 1`,否則 `raise ValueError`。
  - ✅ 例外行為:被裝飾函式拋例外時原樣往外傳,且當次不計入 `records`。
  - ✅ edge case:`repeat=1`、有副作用的函式會被多算 `repeat` 次、例外當次不計入。
  - ✅ 驗收標準:至少 5 個測試(回傳值不變、跑 N 次、`repeat<1` 拋例外、`records` 跨呼叫累積、例外不計入)。
- 因為五項都已經在我的提問裡填好,AI 沒有再追問,直接照協議「先紅燈、再綠燈」往下做:
  先寫 `test_timing.py`(跑過確認 `ModuleNotFoundError`,紅燈),再寫 `timing.py`(全綠)。

## AI 給了什麼

- `timing.py`:`timeit(repeat=3)` 裝飾器工廠,參數驗證 `isinstance(repeat, int) and not isinstance(repeat, bool)` 且 `>=1`
  否則 `raise ValueError`;`wrapper` 用 `*args, **kwargs` 透傳;`records` / `last_elapsed` 掛在 `wrapper` 物件上。
- `test_timing.py`:8 個測試,覆蓋回傳值不變、metadata 保留、重複執行次數、`records` 累積、
  `last_elapsed` 是本次平均、`repeat` 型別與範圍檢查、例外傳播且不計入 records。
- `search.py`:`linear_search`、`binary_search`(都不修改傳入的 `data`),`binary_search` 的
  docstring 寫明「收到未排序資料時行為不保證正確,由呼叫端負責保證已排序」。
- `test_search.py`:6 個輕量測試(找得到/找不到/不修改輸入)。
- `bench.py`:用 `timeit` 在 n=200,000、最壞情況(找最後一個元素)下各跑 5 次,
  輸出 `records` 與 `last_elapsed`,量出 binary 比 linear 快約 1800 倍。

## 我改了什麼

- 把「`repeat` 必須是 int」這條額外加進測試與實作:題目範例只講 `repeat < 1`,
  但 AI 反問規格時我自己決定字串/浮點數也要拒絕(因為 `range(repeat)` 之類的邏輯
  假設是 int,傳字串或浮點數會在後面隱晦地壞掉),所以額外補了
  `test_repeat_non_int_raises` 並在 `timing.py` 加上 `isinstance` 檢查。
- 用 `isinstance(repeat, bool)` 排除 `True`/`False` 被當成合法 `repeat`
  (`bool` 是 `int` 的子類別,`True == 1` 會通過 `>=1` 檢查但語意上不該允許),
  這是我自己驗收時想到的邊角案例,題目原文沒提到。
- `binary_search` 收到未排序資料的行為,我自己定義成「不保證正確、也不檢查、
  不自動排序」,寫進 docstring,而不是丟例外——因為題目規格只要求自己定義並寫清楚,
  我認為呼叫端要先排序是更貼近真實 API 設計(例如 Python 內建 `bisect`)的做法。
- 確認跑了真正的紅燈(`ModuleNotFoundError: timing`)再寫 `timing.py`,沒有跳過這一步。
