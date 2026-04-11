# 🤖 AI 協作使用說明 (AI Usage Statement)

本專案在開發過程中參考了 AI (Gemini) 的建議與輔助，主要應用範圍如下：

### 1. 代碼架構優化
* 將方向旋轉邏輯從大量的 `if-else` 改為方向列表 `DIRECTIONS` 配合 `modulo (%)` 運算。
* 輔助設計 `RobotWorld` 與 `Robot` 的類別關聯，落實 SoC (職責分離) 原則。

### 2. Pygame 視覺化實作
* 協助解決 Pygame 與座標系 Y 軸反轉的映射邏輯。
* 提供 `Pillow` 套件整合方案，實作 `replay_and_save_gif` 功能。

### 3. 測試驅動開發 (TDD)
* AI 協助生成了 `tests/` 資料夾下的 14 個測試案例，涵蓋了基本移動、旋轉邏輯以及進階的 Scent 氣味攔截機制。

---
*本文件旨在透明化 AI 在專案中的角色，所有邏輯最終均由開發者進行審核與整合。*