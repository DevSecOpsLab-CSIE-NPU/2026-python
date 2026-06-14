# AI_USAGE

## 我問了哪些問題
- 如何用 csv.DictReader 讀取 UTF-8-BOM 的 CSV，避免欄位名稱出現異常字元？
- Task 1 的輸出 JSON 應該如何設計欄位結構，才符合作業格式？
- XML 轉換時要怎麼用 ElementTree 建立屬性節點？
- unittest 要怎麼覆蓋正常、邊界、反例三種情境？
- matplotlib 長條圖上如何加上每個 bar 的秒數標籤？

## AI 建議有採用的部分
- 使用 pathlib 以目前檔案位置組合資料路徑，降低硬編碼風險。
- Task 1/Task 2 分離為可測試函式，再由 main 負責流程串接。
- 在 Task 3 使用 Agg backend，避免無視窗環境繪圖失敗。

## AI 建議我拒絕的部分與原因
- 建議把所有邏輯寫在單一大函式中：我拒絕，因為不利於 TDD 與單元測試。
- 建議引入額外第三方套件做 XML pretty print：我拒絕，作業需求用標準庫即可完成，避免增加環境依賴。

## 一個 AI 輸出有誤的案例與修正
- 錯誤建議：直接使用 weeks/week-08/in-class/stu-data/113年新生資料庫.csv 作為讀檔路徑。
- 實際問題：目前專案不存在這個路徑，執行時會出現 FileNotFoundError。
- 修正方式：改為 assets/stu-data/113年新生資料庫.csv，並使用 pathlib 由 task1_csv_to_json.py 的位置動態組路徑。
- 修正結果：task1 可以正常讀檔、輸出 students.json，後續 task2 也可順利轉出 students.xml。
