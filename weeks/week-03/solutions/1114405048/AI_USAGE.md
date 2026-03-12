# AI_USAGE

## 1) 我問 AI 的問題（共 5 題）

1. UVA 118 的 `scent` 為什麼要包含方向？
2. 如何設計 `robot_core.py` 才能跟 pygame 畫面解耦？
3. `unittest` 至少 10 個測試要怎麼分組才好維護？
4. 如何設計 LOST 後停止執行的狀態機？
5. 回放功能不輸出 GIF 時，有哪些等效做法？

## 2) 我採用的建議與原因

- 採用 `set[tuple[int, int, str]]` 存 scent：查詢快且規則對應清楚。
- 採用 `RobotWorld` + `RobotState` 分層：讓測試只依賴核心邏輯。
- 測試拆成 `core` 與 `scent` 兩份：對應評分重點，閱讀成本低。

## 3) 我拒絕的建議與原因

- 拒絕把 pygame 事件直接寫進 `robot_core.py`：會造成高耦合，難測試。
- 拒絕只做單一整合測試：無法精準定位旋轉/越界/scent 問題。

## 4) 一個 AI 建議不完整、我自行修正的案例

- AI 一開始建議 scent 只記錄座標 `(x, y)`，忽略方向維度。
- 我補上 `dir` 成為 `(x, y, dir)`，並新增「同格不同方向不共用 scent」測試確認修正。
