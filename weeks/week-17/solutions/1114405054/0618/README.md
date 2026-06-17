# 6/18 — 搜尋效能實驗室報告

## Stage 3 加速前預測

> 此預測在實測數據之前寫入，commit `docs: stage3 加速前預測`。

**我的預測：**
- 在多次搜尋下，交叉點（排序+binary 開始贏 linear）約在 **n ≈ 40 ~ 80**。
- n 小時 linear 有 cache 優勢且無排序開銷；n 變大後 binary 的 O(log n) 優勢會補回排序成本。
- 預測排名（多次查詢，大 n）：set_search > binary_search > linear_search。
