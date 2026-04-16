# AI_USAGE

## 1) 我問 AI 的 5 個問題

1. 如何把 UVA 118 的規則拆成可測試的 `robot_core.py`？
2. `scent` 為什麼要用 `(x, y, dir)`，不能只存 `(x, y)`？
3. 如何設計最少 10 個測試，覆蓋旋轉、越界、scent？
4. pygame 介面要怎麼做到「一步指令」與「回放」？
5. `TEST_LOG.md` 的 Red/Green 紀錄該怎麼寫才可追溯？

## 2) 我採用的建議與原因

- 採用「核心邏輯與 UI 分離」：`robot_core.py` 不依賴 pygame，方便單元測試。
- 採用 `set[tuple]` 保存 scent：查詢速度快，且能直接判斷同格同方向。
- 採用回放快照序列（`ReplayFrame`）：每步都可重播，符合作業需求。
- 採用 `unittest discover` 的固定命令：與作業規格一致，便於 TA 重現。

## 3) 我拒絕的建議與原因

- 拒絕「把規則直接寫在 pygame 事件迴圈」：會讓測試困難、耦合過高。
- 拒絕「非法指令直接忽略」：規格要求明確策略，改採 `ValueError` 更清楚。
- 拒絕「只做 GIF、不做程式回放」：本作業要求可重播，內建回放更穩定。

## 4) AI 建議不完整、我自行修正的案例

- 不完整建議：早期建議把 scent 定義成 `(x, y)`。
- 我的修正：改為 `(x, y, dir)`，並新增測試 `test_same_cell_different_direction_does_not_share_scent`。
- 修正效果：避免同一格不同方向被誤判為安全，規則與 UVA 118 一致。
