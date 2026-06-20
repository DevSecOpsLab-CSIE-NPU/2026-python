# AI_USAGE.md

## 我問 AI 的問題

1. 「幫我設計 Robot Lost 的 Robot 和 RobotWorld 類別，要支援 L/R/F、LOST、scent」
2. 「測試案例要覆蓋哪些面向才算完整？」
3. 「pygame 視覺化要顯示地圖、機器人方向、scent 標記」

## 我採用的建議與原因

- **Robot/RobotWorld 分離**：讓核心邏輯可獨立測試，不依賴 pygame
- **scent 用 set[tuple] 儲存**：O(1) 查詢效率高，自動去重
- **DIR_ORDER 用 list + 模運算旋轉**：比 if-else 簡潔且不易出錯
- **TDD 流程**：先寫測試（RED）再實作（GREEN），確保規格正確

## 我拒絕的建議與原因

- **整合 Robot 和 RobotWorld 為單一類別**：拒絕，耦合會讓測試和擴充都困難
- **scent 用 dict 存**：拒絕，dict 的 value 不需要，set 就夠了
- **用 argparse 做 CLI 版本**：拒絕，作業要求 pygame 互動優先

## AI 建議不完整、我自行修正的案例

AI 給的 `test_same_pos_different_dir_not_protected` 測試起點是 (0,5,E)，但 (0,5) 往 E 移動到 (1,5) 不會越界。我手動修正起點為 (5,5,E)，正確測試 scent 方向差異邏輯。
