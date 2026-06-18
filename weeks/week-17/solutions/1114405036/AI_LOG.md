
# AI_LOG — 0618 搜尋效能五階段
 
## 我給 AI 的提示（逐字）
 
1.「依 0618-search-lab.md 的規格，用 TDD 把 Stage 1 的 timeit 裝飾器做出來：先補齊
   test_timing.py 跑紅燈 commit `test:`，再寫 timing.py 跑綠燈 commit `feat:`。」
2.「寫 Stage 2 的 linear_search / binary_search / set_search（都不可改入 data），
   三函式回傳型別不同，幫我用 subTest 共用一組測試。」
3.「Stage 3：把 `in` 與 `bisect` 加進 benchmark 當 baseline，量出『先排序 + binary』
   何時開始贏過 linear 的交叉點，寫進 results.json，並用我的數據反駁 AI。」
4.「Stage 4：畫一張雷達圖呈現三搜的多維權衡，輸出 assets/radar.png。」
5.「Stage 5：對照 OpenSSF Secure Coding Guide 找 3 條適用條目，先寫紅測再修。」
 
## 我做了什麼
 
- Stage 1：補 `test_timing.py` 六個測試（規格 1~6 全覆蓋 + repeat 自訂 + 不 print 的 edge case），
  再寫 `timing.py`（`@timeit` 與 `@timeit(repeat=n)` 兩種寫法、`raise` 不用 `assert`）。
- Stage 2：`search.py` 三搜 + `test_search.py`（subTest 共用、空 list、不改 data 等）。
- Stage 3：`benchmark.py` 加 `builtin_in`/`bisect_search` baseline 與 `find_crossover`，
  先寫預測（docs commit）再用實測數據覆蓋。
- Stage 4：`plot.py` 雷達圖（`matplotlib.use("Agg")`），`test_plot.py` 只驗 PNG 產生且非空。
- Stage 5：`test_security.py` 三條安全規則紅 → 修 `benchmark.py`（輸入驗證 + `load_results` 用 json）。
 
## AI 反問我什麼 / 我怎麼答
 
> 逐項記下 AI 在「開發訪談助教」模式問的規格問題與我的決定。
 
- Q：`repeat` 取**平均**還是取**最小值**？
  A：取平均。要反映一般情況；最小值偏樂觀、會藏掉雜訊。
- Q：`records` 是每次呼叫就**清空重來**，還是**跨呼叫累積**？
  A：累積。`records` 保留歷史，`last_elapsed` 只反映本次 repeat 的平均（用 `records[-repeat:]`）。
- Q：三個搜尋回傳型別不一致，subTest 裡要怎麼共用斷言？
  A：先正規化成 `found: bool`——linear/binary 看 `index >= 0`，set 看 `bool` 本身。
- Q：`binary_search` 收到**未排序** data 要怎麼辦？排序、報錯、還是回傳未定義？
  A：不偷偷排序、不檢查，前提交呼叫端；在 docstring 寫明「未排序時回傳值未定義」。
     偷排序會改動/複製資料，還會把 O(log n) 變成 O(n log n)。
- Q：`set_search` 每次重建 set 不是很慢嗎？要不要快取？
  A：依作業簽章每次帶 data，就如實每次重建並在分析裡說明它因此吃虧——這正是要量出來的重點。
- Q：量「排序成本」時，要對已排序還是未排序資料計時？
  A：未排序（打散後的副本）。對已排序資料 `sorted()` 會觸發 Timsort 的 O(n) 最佳情況、低估成本。
- Q：安全掃描時，`benchmark` 用的 `random` 要不要改成 `secrets`？
  A：不用。這是可重現的效能量測，不是密碼學用途，盲目替換反而是誤判。
 
## AI 給的東西我怎麼驗收（驗收標準）
 
- 測試覆蓋規格 1~6，每條至少一個測試，外加 edge case；TDD 順序先 `test:`（紅）再 `feat:`（綠）。
- 搜尋對不對：linear/binary 回同一 index；三搜在同一份 data 上「找到/找不到」結論一致。
- 評估有沒有根據：README 的判斷必須對得上 `benchmark.py` 跑出的 `results.json` 實數。
- AI 一開口說「binary 一定比 linear 快」時，用「單次查詢 + 需付排序成本」的小 n 情境反駁。
 
## AI 反駁紀錄
 
AI 起初斷言「binary_search 永遠比 linear_search 快」。我用實測反駁：在**只查 1 次**且
data 未排序時，必須先付 O(n log n) 排序成本，比單次 O(n) 的 linear 還貴；本機交叉點約落在
查 4～8 次，超過才划算（數據見 `results.json` 的 `crossover`）。