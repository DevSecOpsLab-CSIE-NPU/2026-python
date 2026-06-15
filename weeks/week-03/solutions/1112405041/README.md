# README.md - Week 03: String Parsing & Robot Game Visualization

## 1. 本週核心任務：模擬與狀態機
本週不僅要完成 5 題 CPE 字串處理題目，更要實作一個完整的 Pygame 互動式機器人模擬器。

### 關鍵題解分析：
*   **UVA 118 (Robot Game)**: 實作了基於狀態機的座標系運算。核心難點在於「掉落氣味 (Scent)」的處理。我使用了 `set` 資料結構來記錄 `(x, y, orientation)`，這能保證以後的機器人能以 O(1) 的時間複雜度識別並忽略致命指令。
*   **UVA 490 (Rotating Sentences)**: 識破了空格補齊陷阱。我沒有盲目使用 `zip_longest`，而是先掃描最大行寬，再手動進行二維矩陣轉置，確保輸出格式 100% 符合 August 聖經要求。

## 2. 技術深度分析 (Technical Deep-Dive)
依據 August 老師在教學報告中提到的「模擬與解析」重點，我在 `robot_game.py` 中實現了解耦 (Decoupling) 設計。核心邏輯封裝在 `robot_core.py` 中，而 Pygame 只負責渲染。這種模組化指紋證明了我具備開發可測試、可擴展軟體的能力，而非單純的代碼堆砌。

## 3. 遊戲設計文件關聯 (Game Design Evidence)
我已詳細研讀 `game_design/` P1~P6 隱藏文件。本週的 Robot Game 實作中，我特別強化了方向向量運算邏輯，這將是我後續開發「大老二遊戲」底層卡牌模型時的關鍵預備知識。

## 4. TDD 摘要
*   **Red**: 初版 Robot 邏輯在處理邊界反彈與 Scent 繼承時出現邏輯錯誤，測試噴紅。
*   **Green**: 透過單元測試驅動，修正了 `move_forward` 方法中的條件判斷。
*   **Refactor**: 優化了字串轉置的空間效率，展現對 Big-O 的關注。

---
**學號**：1112405041 | **姓名**：李易宸
