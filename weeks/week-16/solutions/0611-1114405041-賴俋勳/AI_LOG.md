# AI_LOG

## Stage 1
- 詢問重點：timeit 需保留回傳值與 metadata。
- 驗收標準：`last_elapsed` 為 float，`records` 會累積。

## Stage 2
- 詢問重點：三排序是否會改到輸入 list。
- 驗收標準：共用 subTest 通過，輸入不可被修改。

## Stage 3
- 詢問重點：加速方案與 baseline 是否同時納入 benchmark。
- 決策：採用 quick median-of-three + 小區間 insertion sort。

## Stage 4
- 詢問重點：圖表輸出與 y 軸尺度。
- 驗收標準：`assets/benchmark.png` 非空且 y 軸為 log。

## Stage 5
- 詢問重點：安全條目適用性與修補方式。
- 修補項目：負數輸入拒絕、只允許 JSON、副檔名與格式錯誤轉 ValueError。
- 不適用：benchmark 非密碼學情境，不需改用 secrets。
