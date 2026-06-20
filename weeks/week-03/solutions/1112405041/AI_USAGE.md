# AI_USAGE.md

## 我問 AI 的問題

1. Robot 和 RobotWorld 怎麼拆比較好？要支援 L/R/F 還有 LOST 跟 scent
2. 測試要測哪些？怕漏掉 edge case
3. 能不能幫我弄一個 pygame 的畫面顯示地圖和機器人方向

## 我採用的建議與原因

- **Robot/RobotWorld 分離**：核心邏輯獨立測試，不綁 pygame
- **scent 用 set[tuple] 存**：查詢快，不用擔心重複
- **旋轉用 list + mod**：比 if-else 乾淨
- **TDD RED→GREEN**：先寫測試再實作比較穩

## 我拒絕的建議與原因

- **Robot 跟 RobotWorld 合併**：耦合太緊，之後難改
- **scent 用 dict**：沒必要，set 就夠了
- **做 CLI 版**：作業要 pygame 就先做 pygame

## AI 建議不完整、我自行修正的案例

AI 給的 `test_same_pos_different_dir_not_protected` 起點設 (0,5,E)，但 (0,5) 往 E 走到 (1,5) 不會出界。我改成 (5,5,E) 才對。
