# AI_USAGE.md

## 我問了哪些問題

- 如何依照 Week 10 規格完成 CSV、JSON、XML 轉換？
- `@timeit` 裝飾器如何套用在讀寫函式上？
- unittest 如何涵蓋正常、邊界與錯誤格式？
- 如何用 matplotlib 繪製耗時比較圖？

## AI 建議我有採用的部分

- 使用 `csv.DictReader` 與 `encoding="utf-8-sig"` 讀取 CSV。
- 使用 `json.dump(..., ensure_ascii=False, indent=2)` 輸出可讀 JSON。
- 使用 `xml.etree.ElementTree` 建立 XML，避免手動拼接字串。
- Task 3 使用英文圖表標題與座標軸。

## AI 建議我拒絕的部分及原因

- 拒絕提交產生作業用的 shell 腳本，因為它不是 HOMEWORK.md 規定檔案。
- 拒絕修改 `weeks/week-10/solutions/1114405013/` 以外的檔案，避免 CI 失敗。

## AI 輸出有誤並修正的案例

一開始固定使用作業指定 CSV 路徑，但若本機資料夾位置不同會找不到檔案。後來改成 `find_csv_file()`，先嘗試指定路徑，再用 `rglob()` 搜尋 `113年新生資料庫.csv`。
