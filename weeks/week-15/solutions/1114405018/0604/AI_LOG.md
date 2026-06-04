## 我問 AI 什麼
請幫我用 `unittest` 寫 `count_squares(a, b)` 的測試檔案，要求至少 3 個案例：基本案例、edge case、以及 `a > b` 的例外案例；另外幫我順便寫出最小可運作的實作骨架。

## AI 給了什麼
- 提供 `test_square_counter.py`，包含 `count_squares(1,10)==3`、`count_squares(100,100)==1`、`count_squares(5,2)` 應丟 `ValueError`。
- 提供 `square_counter.py` 最小實作，使用 `math.isqrt` 計算平方數個數。

## 我改了什麼
- 我把測試與實作放在 `weeks/week-15/solutions/1114405018/0604/`，並確保測試先紅燈再綠燈的 TDD 流程：先新增測試並提交（紅燈），接著完成 `square_counter.py` 讓測試全部通過，最後提交實作。
- 我也清理了分支上的其他週次解答檔（`0520`、`0527`、`0528` 與 `week-13/homework`）只保留本機檔案，讓 PR 內容只包含今天的變更。

## 補充註記
- 「我改了什麼」必須寫明具體修改；若是機器完全產生且未修改，請補上你手動加的內容以示學習歷程。
