# AI 互動紀錄 (AI_LOG.md)

| 階段 (Stage) | AI 反問我什麼 / 提出的概念題 | 我怎麼回答 / 核心點總結 |
| :--- | :--- | :--- |
| **Stage 1** | 為什麼 `timeit` 裝飾器裡用 `time.perf_counter()` 而不是 `time.time()` 來計時？ | 指出 `perf_counter()` 具備單調性（Monotonicity），不受系統校時干擾，且具備微秒/奈秒級的高解析度，適合效能基準測試。 |
| **Stage 2** | 1. 針對未排序輸入，`binary_search` 的規格傾向？<br>2. 為什麼 `set_search` 用 `target in set(data)` 而不是 `target in data`？ | 1. 選擇不檢查、假設已排序以維持 $O(\log n)$ 效能。<br>2. 說明 list 是 $O(n)$ 線性掃描，而 set 是 $O(1)$ 雜湊表查詢，在重複/多次查詢時具有巨大的攤銷成本優勢。 |
| **Stage 3** | 在 benchmark 中，為什麼 `bisect` 在 $n=10$ 時輸給 `builtin_in`，但到 $n=100000$ 時卻能拉開到約 1700 倍的差距？ | 解釋小數據量下由「常數因子（額外變數初始化與邏輯計算開銷）」主導勝負；大數據量下則由「時間複雜度 $O(\log n)$ vs $O(n)$」決定生死。 |
| **Stage 4** | 雷達圖中 `set_search` 在「記憶體效率」拿了最低的 1 分，但它明明只回傳一個 `bool`，為什麼？ | 強調空間複雜度取決於內部建立的資料結構。`set_search` 為了達到 $O(1)$ 速度在內部執行 `set(data)`，配置了 $O(n)$ 的線性空間與雜湊表槽位，因此開銷最大。 |
| **Stage 5** | 為什麼 `type(repeat) is not int` 比 `not isinstance(repeat, int)` 更安全？兩者在處理 `repeat=True` 時有什麼差異？ | 揭示 Python 中 `bool` 是 `int` 的子類別。`isinstance(True, int)` 會判定為真而漏過檢查，只有 `type() is not int` 才能精準攔截並剔除 `bool` 冒充的情況。 |
