# 🧪 測試執行紀錄 (Test Execution Log)

## 📅 測試日期：2026-04-12
* **測試環境**: Windows 11 / Python 3.10
* **測試模組**: `tests/test_robot_core.py`, `tests/test_robot_scent.py`
* **測試結果**: ✅ PASS (14/14)

### 📊 詳細測試清單
| 編號 | 測試項目 | 預期結果 | 狀態 | 備註 |
| :--- | :--- | :--- | :--- | :--- |
| Core 01-03 | 旋轉邏輯 | L/R 旋轉正確且連續旋轉能回到原向 | PASS | |
| Core 04-05 | 移動與掉落 | 正常移動座標正確，越界觸發 LOST | PASS | |
| Core 06-07 | Scent 系統 | 同位同向攔截成功，同位異向不攔截 | PASS | |
| Core 08 | 狀態保護 | LOST 後不再執行後續指令 | PASS | |
| Core 09-10 | 異常與原點 | 非法指令忽略、(0,0) 邊界判定正常 | PASS | |
| Scent 01 | Scent 建立 | 掉落時正確於最後安全位置留下氣味 | PASS | |
| Scent 02-03 | 攔截與多向 | 成功攔截致命指令，同格多向獨立運作 | PASS | |
| Scent 04 | 持久性測試 | 機器人重置後，地圖 Scent 依然保留 | PASS | |

### 🐛 歷史 Bug 修復紀錄
* **Issue #01**: 機器人在邊界掉落時，Scent 座標記錄偏移。
    * *修正*: 確認 `move_forward` 判斷越界後，應記錄「掉落前」的座標 `(self.x, self.y)`。
* **Issue #02**: Pygame 畫面與核心座標 Y 軸相反。
    * *修正*: 在 `robot_game.py` 實作 `grid_to_screen` 進行座標轉換。