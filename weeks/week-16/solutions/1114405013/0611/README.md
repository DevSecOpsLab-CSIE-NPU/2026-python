# 6/11 排序效能實驗室

## Stage 4 圖表解讀

![benchmark](assets/benchmark.png)

`sorted_baseline` 最快，因為它是 Python 內建 Timsort 且底層有高度最佳化。`bubble_sort` 的線在 log scale 下仍明顯比 `quick_sort`、`merge_sort` 更陡，符合 O(n²) 與 O(n log n) 的差異。本次 `quick_sort_fast` 在 4000 筆資料約從 0.00171 秒降到 0.00162 秒，約 1.05x 加速。

## Stage 5 安全性自掃

| OpenSSF 條目 | 檢查結果 | 處理方式 |
|---|---|---|
| 03 Numbers | `make_data` 與 `run_benchmark` 原本未拒絕負數或 0 次重複，可能讓資料量語意錯誤或發生除以 0。 | 加入 `ValueError` 輸入驗證，並以 `test_security.py` 鎖住邊界條件。 |
| 04 Neutralization / CWE-502 | 實驗結果應以 JSON 讀取，不應接受非 JSON 路徑，避免未來改用不安全反序列化格式。 | `load_results` 只接受 `.json` 路徑；測試確認 `.txt` 即使內容像 JSON 也會拒絕。 |
| 08 Coding Standards | 寫入 `results.json`、讀取結果檔與產生 PNG 都需要正確關檔，避免資源外洩。 | 使用 `with open(...)` 與 `plt.close()`；保留現有做法並用輸出測試確認檔案可正常產生。 |
| 05 Exception Handling | 本專案沒有吞掉所有例外的 `except:`；檔案讀取錯誤會明確往外拋給呼叫端處理。 | 判定目前不需新增廣泛例外處理，避免隱藏真正的 I/O 或 JSON 格式錯誤。 |
| 不適用：`random` vs `secrets` | benchmark 的亂數只為產生可重現測資，不是密碼、token 或安全敏感值。 | 保留 `random.Random(seed)`，不改成 `secrets`。 |
