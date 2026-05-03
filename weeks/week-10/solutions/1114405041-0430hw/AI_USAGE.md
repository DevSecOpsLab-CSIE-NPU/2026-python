## 我問了哪些問題（3-5 條）

1. CSV 用 `utf-8-sig` 讀取時要注意哪些欄位名稱問題？
2. `@timeit` 裝飾器如何保留原函式名稱與註解？
3. JSON 轉 XML 時，如何把中文欄位映射成英文字串屬性？
4. `xml.etree.ElementTree` 要怎麼輸出 XML 宣告與 utf-8 編碼？
5. matplotlib 長條圖上方要如何標出秒數文字？

## AI 建議有採用的部分

1. 使用 `functools.wraps` 包裝 `timeit`，避免函式 metadata 遺失。
2. Task 1 先拆成 `filter_by_admission` 與 `count_by_dept`，測試更容易寫。
3. Task 2 用 `build_xml_tree` 單獨負責節點建構，再由 `write_xml` 輸出。
4. 使用 `Path(...).parent.mkdir(parents=True, exist_ok=True)` 自動建立 output 目錄。

## AI 建議我拒絕的部分及原因

1. 建議把所有邏輯寫在 `main()`：拒絕，因為不利測試與重用。
2. 建議直接把 CSV 全欄位輸出到 JSON：拒絕，作業指定只要特定欄位。

## 至少 1 個 AI 輸出有誤的案例與修正

- 問題：AI 初版把 Task 1 的篩選值寫成 `分科測驗`。
- 為何有誤：本次作業指定篩選條件是 `聯合登記分發`。
- 修正：將常數改為 `ADMISSION_METHOD = "聯合登記分發"`，並重新執行測試與輸出確認。
