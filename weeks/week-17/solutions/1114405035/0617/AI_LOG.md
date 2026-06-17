# AI 協作記錄 - 6/17 (三)｜預演：`timeit` + 搜尋效能評估

## AI 反問我什麼 / 我怎麼回答
- AI 問：「timeit 裝飾器是否應設計為接受 repeat 參數且預設為 3 的形式（例如：@timeit(repeat=3)）？被裝飾的函式簽名是否需要支援任意參數與關鍵字引數（*args, **kwargs），且其回傳值與回傳型別需保持完全不變？」
  我答：「是的。當裝飾器需要接收自訂參數（如 repeat=3）時，它的結構會從原本的「兩層函式」變成「三層函式」（即裝飾器工廠模式）。Wrapper 的設計：是的。被裝飾的 wrapper 函式簽名必須使用 *args, **kwargs，以 100% 完美相容原函式的任何輸入。回傳值與回傳型別完全不變，wrapper 必須擷取原函式執行時的回傳值，並在結尾 return。」
- AI 問：「repeat 的輸入是否限定為大於等於 1 的整數？」
  我答：「是的。repeat 的合法輸入必須是大於等於 1 的整數（>= 1）。」
- AI 問：「當 repeat < 1 時，是否應 raise ValueError，且不准使用 assert？」
  我答：「是的。當輸入 repeat < 1 或傳入非整數型態時，裝飾器工廠應拋出 ValueError。嚴禁使用 assert 做輸入驗證，因為在 Python 執行時如果帶有 -O 優化參數，所有的 assert 語句都會被忽略失效。商務邏輯的輸入檢查必須使用 if ...: raise ValueError(...)。」
- AI 問：「Edge Case 清單：若 repeat = 1 時該如何處理？若被裝飾的函式本身具有副作用，重複執行 repeat 次會導致該副作用被觸發多次，這是否為預期行為？」
  我答：「repeat = 1 的情況是合法的邊界值。裝飾器應正常執行該函式剛好 1 次，計算該次耗時並記錄。函式自帶副作用是預期行為，任何全域變數累加、寫入資料庫或印出 log 的副作用必然會被觸發多次。」
- AI 問：「紅燈的驗收標準是否為：執行 python -m unittest 且您提供的 test_timing.py 測試案例全部失敗（fail）？」
  我答：「是的。在實作 timing.py 之前，執行測試時必須看到全部失敗（Fail / Error）。」

## 我問 AI 什麼
- 與 AI 協作，討論 `timing.py` 計時裝飾器 `@timeit` 的規格、輸入邊界條件、錯誤處理設計，並請 AI 提供符合這些規格的 `test_timing.py` 測試案例。

## AI 給了什麼
- 提供了符合規格的 `test_timing.py` 測試程式（包含回傳值不變、保留 metadata、記錄 repeat 次數與平均耗時、拒絕無效 repeat 參數等測試案例）。

## 我改了什麼
- 審查並補齊了測試案例與裝飾器的詳細設計（包括同時支持 `@timeit`、`@timeit()` 及 `@timeit(repeat=n)` 寫法），並將裝飾器的計時結果儲存在 wrapper 函式的 `records` 屬性上，確保每次呼叫皆能累積並計算每次呼叫的平均值（`last_elapsed`），且不使用 `assert` 來進行輸入驗證，改為拋出 `ValueError`。
