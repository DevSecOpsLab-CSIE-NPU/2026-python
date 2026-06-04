# AI_LOG

## 我問 AI 什麼
請幫我用 unittest 寫 count_squares(a, b) 的測試案例，並請根據題目要求包含 ValueError 的測試。

## AI 給了什麼
給了 3 個測試案例（基本、邊界單點、ValueError 異常），並實作了使用 `math.ceil` 和 `math.floor` 的高效演算法。

## 我改了什麼
1. 修正了目錄結構：嚴格移除所有嵌套的 starter 資料夾，確保檔案直接位於 `solutions/1112405041/0603` 與 `solutions/1112405041/0604` 下。
2. 實施嚴格 TDD：確保 0603 與 0604 兩個任務都擁有獨立的分支，且 Commit 順序嚴格遵守 `test: (Red Light)` -> `feat: (Green Light)`。
3. 修正 0603 實作：補齊了之前遺漏的 `gcd.py` 並通過所有單元測試。
