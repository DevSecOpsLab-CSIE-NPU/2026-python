# AI_LOG.md — 0618 搜尋效能五階段專題

## 我問 AI 什麼

### Stage 1
「請幫我寫 timeit 裝飾器，repeat 參數預設 3，記錄在 f.records，f.last_elapsed 是平均，用 wraps，repeat<1 要 raise ValueError，不准 print。」

### Stage 2
「請幫我寫 linear_search、binary_search、set_search，共用一組測試（subTest），不可修改傳入 data，binary 前提 data 已排序。」

### Stage 3
「請幫我加 benchmark baseline：內建 in 和 bisect，跑不同 size 比較五種方法。」

### Stage 4
「請幫我畫雷達圖，維度自己定，輸出 assets/radar.png，用 matplotlib.use('Agg')。」

### Stage 5
「請幫我寫安全測試：檢查 results.json 用 with 關檔、make_data 拒絕負數、plot.py 用 json 而非 pickle。」

## AI 給了什麼

- Stage 1: 標準 timeit 實作，time.perf_counter() + functools.wraps
- Stage 2: 三種搜尋實作 + subTest 共用測試骨架
- Stage 3: benchmark.py 含 make_data、run_benchmark、五種方法比較、results.json 輸出
- Stage 4: 雷達圖程式，五個自訂維度
- Stage 5: test_security.py 三條安全測試案例

## 我改了什麼

- **test_search.py**: _found() 中 bool 和 int 分開判斷，避免 `False >= 0` 誤判為「找到」
- **benchmark.py**: 加入 n < 0 時 raise ValueError（安全需求）
- **README.md**: 補上交叉點分析、雷達圖維度說明、安全自掃表格

## AI 反問我什麼 / 我怎麼回答

> AI 問：「set_search 回傳 type 是 bool，跟其他兩個的 int 不一致，測試怎麼共用？」
> 我答：用 _found() 包裝，檢查 bool 用 True/False，int 用 >= 0。

> AI 問：「binary_search 收到未排序 data 要回什麼？」
> 我答：回 -1 並在 docstring 說明行為未定義，排序是呼叫端責任。

> AI 問：「benchmark 的 queries 次數怎麼決定？」
> 我答：設 100 次，讓 set/binary 的優勢能在總時間中顯現。

> AI 問：「雷達圖要比哪些維度？」
> 我答：avg_time、scalability、simplicity、no_preprocess、memory。

> AI 問：「安全性測試要同時測 plot.py 存檔時有用 with 嗎？」
> 我答：不用，plot.py 的 savefig 已內部處理，不需要額外測試。
