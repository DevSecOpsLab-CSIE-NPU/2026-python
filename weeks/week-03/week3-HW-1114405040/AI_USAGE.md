# AI_USAGE

## 我問 AI 的問題

1. 如何把 Robot Lost 的核心規則拆成容易測試的 `Robot` 與 `World` 模組？
2. scent 為什麼必須同時記錄座標與方向？
3. 在 Python 3.14 上如果 `pygame` 安裝困難，有沒有相容方案？
4. 如何把 pygame 畫面歷程輸出成 GIF，而不是只做即時顯示？
5. README 應該怎麼整理，才能對齊作業規格中的功能、測試與素材要求？

## 我採用的建議與原因

1. 採用 `set[tuple[int, int, str]]` 儲存 scent，因為查詢快且可以正確區分方向。
2. 採用「核心邏輯與 UI 分離」的結構，讓 `robot_core.py` 不依賴 pygame，測試可以單獨執行。
3. 採用 `FrameState` 保存每一步畫面狀態，因為這樣可以同時支援即時渲染、截圖與 GIF 匯出。
4. 採用本地 `.venv` 與 `pygame-ce`，因為 Python 3.14 下比傳統 `pygame` 更容易安裝成功。

## 我拒絕的建議與原因

1. 拒絕把所有規則直接寫進 `robot_game.py`，因為那會讓測試依賴畫面邏輯，違反作業要求。
2. 拒絕只做文字版輸出、不做互動畫面，因為作業明確要求 pygame MVP 與遊玩截圖。
3. 拒絕用單一布林值記錄 scent 是否存在，因為不同座標與方向會互相覆蓋，規則不正確。

## AI 建議不完整、我自行修正的案例

AI 一開始傾向直接安裝 `pygame`。這個建議在 Python 3.14 的 Windows 環境下不完整，因為沒有合適 wheel 時可能卡在編譯。後來我自行修正成：先建立本地 `.venv`，再安裝 `pygame-ce` 與 `pillow`，保留 `import pygame` 的程式介面，同時讓整份作業可以實際執行與輸出素材。