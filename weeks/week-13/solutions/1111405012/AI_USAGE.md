# AI Usage

## 我問了哪些問題

- 如何把只有頂層示範輸出的腳本改成可被 `unittest` 驗證的函式？
- 對這 6 支範例程式，各自最值得測的正常案例、邊界案例、反例是什麼？
- 在 Windows 環境下，JSON 檔案 I/O 要怎麼寫才不會綁死 `/tmp`？
- 帶有連字號的檔名如何在測試中安全載入？
- `-su` 與 `-easy` 版本怎樣安排，才兼顧可手打與可閱讀？
- `@property` 的初始化驗證要不要直接重用 setter？
- 多型示範若只有 `print()`，要怎麼改成比較好測的形式？
- 示範特殊方法的模組若一匯入就列印，最小修改應該怎麼收斂成可測版本？

## 有採用的建議

- 先寫 `tests/`，用 `importlib.util.spec_from_file_location()` 依路徑載入帶有連字號的檔案
- 把每支原始腳本的頂層行為移入 `main()`，避免匯入時就產生副作用
- 讓正式版檔案專注在「可測函式 + 示範輸出」，另外再補 `-su` 與 `-easy` 兩種教學版本
- 用 `TemporaryDirectory()` 取代固定寫入系統暫存路徑
- 在 `Circle.__init__` 直接走 `self.radius = radius`，讓初始化與 setter 共用驗證規則
- 把 `make_sounds()` 改成回傳字串列表，讓多型結果可以直接比對
- 把特殊方法題的頂層示範碼搬進 `main()`，保持類別定義可安靜匯入

## 有拒絕的建議

- 沒有把所有範例硬湊成同一個大模組，因為這會破壞原本一題一檔的教學結構
- 沒有把 `-su` 版本直接寫成呼叫正式版函式的包裝器，因為那樣不利於手打練習與記憶
- 沒有把 `Circle.area` 做成可寫入屬性，因為這會破壞「面積由半徑推導」的封裝意圖
- 沒有額外替 `Score` 補上自訂 `__gt__`，因為 `@total_ordering` 已能由 `__eq__` 與 `__lt__` 推導

## AI 可能誤導但後來自行修正的案例

- 第一版測試匯入用了 `from tests.support import load_module`。這在一般套件結構常見，但這次 `unittest discover -s tests` 的載入方式會讓 `tests` 不在可匯入根路徑上，實際執行後全部 `ModuleNotFoundError`。後來改成 `from support import load_module` 才符合這個資料夾的測試啟動方式。
- `R03-inheritance.py` 原本的 `make_sounds()` 看起來「有輸出就算完成」，但一寫測試就發現它其實沒有可驗證的回傳值。後來改成回傳列表，再把列印行為留在 `main()`。
- `R04-special-methods.py` 原本類別行為其實都對，但測試一加入「匯入不該有副作用」就暴露出頂層示範碼的問題。後來把輸出改收斂到 `main()`，不去碰既有特殊方法邏輯。
