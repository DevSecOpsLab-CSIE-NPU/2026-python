# AI Usage

## 我問了哪些問題

- 如何把只有頂層示範輸出的腳本改成可被 `unittest` 驗證的函式？
- 對這 6 支範例程式，各自最值得測的正常案例、邊界案例、反例是什麼？
- 在 Windows 環境下，JSON 檔案 I/O 要怎麼寫才不會綁死 `/tmp`？
- 帶有連字號的檔名如何在測試中安全載入？
- `-su` 與 `-easy` 版本怎樣安排，才兼顧可手打與可閱讀？

## 有採用的建議

- 先寫 `tests/`，用 `importlib.util.spec_from_file_location()` 依路徑載入帶有連字號的檔案
- 把每支原始腳本的頂層行為移入 `main()`，避免匯入時就產生副作用
- 讓正式版檔案專注在「可測函式 + 示範輸出」，另外再補 `-su` 與 `-easy` 兩種教學版本
- 用 `TemporaryDirectory()` 取代固定寫入系統暫存路徑

## 有拒絕的建議

- 沒有把所有範例硬湊成同一個大模組，因為這會破壞原本一題一檔的教學結構
- 沒有把 `-su` 版本直接寫成呼叫正式版函式的包裝器，因為那樣不利於手打練習與記憶

## AI 可能誤導但後來自行修正的案例

- 第一版測試匯入用了 `from tests.support import load_module`。這在一般套件結構常見，但這次 `unittest discover -s tests` 的載入方式會讓 `tests` 不在可匯入根路徑上，實際執行後全部 `ModuleNotFoundError`。後來改成 `from support import load_module` 才符合這個資料夾的測試啟動方式。
