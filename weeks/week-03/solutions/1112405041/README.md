# Week 03 作業 - Robot Lost

## 功能清單

- 格子地圖顯示 (6x6，含邊界)
- 機器人位置與朝向（圓形 + 方向箭頭）
- scent 標記（紅點）
- 鍵盤控制：L/R/F 單步執行
- N 新增機器人（保留 scent）
- C 清除 scent
- ESC 離開
- LOST 狀態顯示（紅圈 + LOST 文字）
- scent 保護機制（同位置同方向忽略危險 F）

## 執行方式

```bash
cd weeks/week-03/solutions/1112405041
pip install pygame
python robot_game.py
```

## 測試方式

```bash
cd weeks/week-03/solutions/1112405041
python -m unittest discover -s tests -p "test_*.py" -v
```

測試結果：27 tests 全部 PASS

## 資料結構選擇理由

1. **scent 用 `set[tuple[int, int, str]]`**：O(1) 查詢，自動去重，且 tuple 可 hash
2. **Robot 與 RobotWorld 分離**：核心邏輯不依賴 pygame，便於測試
3. **DIR_ORDER 用 list + index 旋轉**：`(idx ± 1) % 4` 即可旋轉，無需字典對映表

## Bug 與修正

- **Bug**：`test_same_pos_different_dir_not_protected` 測試起點設錯 (0,5)，機器人往 E 移動不會越界
- **修正**：將起點改為 (5,5, E)，往 E 走一格到 (6,5) 正確觸發 LOST

## 遊玩截圖

![gameplay](assets/gameplay.png)

## 重播方式

輸入指令時會記錄到 `replay_steps`，可擴充為 GIF 匯出（按 G 鍵預留）
