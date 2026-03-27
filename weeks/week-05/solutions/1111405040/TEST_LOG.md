# 測試與開發紀錄

## 開發方式

這次作業依照先測試、後實作的方式進行。

流程如下：

1. 先閱讀 `week-05/game_design` 的 `p1~p6` 文件。
2. 依模組拆出 `models`、`classifier`、`finder`、`ai`、`game`、`ui` 六組測試。
3. 先建立測試檔，再執行一次 `unittest`。
4. 在 import error 與邏輯缺口都明確之後，再逐步補實作。
5. 每完成一輪就重新執行全部測試，直到全部通過。

---

## Red 階段

第一次執行測試指令：

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

當時結果：

- 6 個測試模組全部失敗
- 主要原因是 `game` 與 `ui` 套件尚未建立
- 錯誤型態為 `ModuleNotFoundError`

這一步確認了測試已先建立完成，且目前確實處於紅燈狀態。

---

## Green 階段

接著依序補上以下模組：

1. `game/models.py`
2. `game/classifier.py`
3. `game/finder.py`
4. `game/ai.py`
5. `game/game.py`
6. `ui/render.py`
7. `ui/input.py`
8. `ui/app.py`
9. `main.py`

補完後重新執行測試，發現只剩 1 個失敗案例：

- `test_try_play_selected_cards`

原因是測試直接假設索引 `0` 就是梅花 3，但 `Hand` 初始化後會自動排序，因此索引位置會變動。

---

## 修正

針對最後一個失敗案例，將測試改為：

1. 先從手牌中找出 `Card(3, 0)` 的實際索引
2. 再設定 `selected_indices`

這樣測試意圖不變，但不再依賴錯誤的索引假設。

---

## 最終結果

最終再次執行：

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

結果如下：

- 52/52 測試通過

另外也實際執行：

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe main.py
```

結果可正常完成一局遊戲並輸出贏家。
