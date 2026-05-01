# AI_USAGE.md

## 1. 我向 AI 詢問的問題

- Python 的 `csv.DictReader` 如何正確讀取 UTF-8-BOM 編碼的檔案？
- `xml.etree.ElementTree` 如何建立帶有屬性的元素，以及正確縮排輸出？
- `@functools.wraps` 裝飾器的作用是什麼？為什麼一定要加？
- 如何使用 `matplotlib` 繪製帶有數值標註的長條圖？
- TDD 的 Red → Green → Refactor 流程在 Python 中應該如何具體操作？

## 2. AI 建議我有採用的部分

- 使用 `encoding="utf-8-sig"` 來處理 UTF-8-BOM 檔案
- 使用 `ET.indent()` 來自動縮排 XML 輸出（Python 3.9+ 支援）
- 在 `@timeit` 裝飾器中使用 `functools.wraps` 保留原函式的 `__name__` 等中繼資料
- 使用 `ax.annotate` 在長條圖上標註數值
- 測試中使用 `sys.path.insert` 來正確引入上層模組

## 3. AI 建議我拒絕的部分及原因

- AI 建議使用 `lxml` 套件來處理 XML，但本作業要求使用標準函式庫 `xml.etree.ElementTree`，因此拒絕
- AI 建議在 Task 3 使用 seaborn 畫圖，但為保持程式簡單且符合基礎要求，選擇使用 matplotlib 即可
- AI 建議將路徑硬編碼，但我改為使用 `os.path` 動態計算相對路徑以提高可移植性

## 4. AI 輸出有誤的案例與修正過程

**錯誤案例**：AI 最初建議使用 `ET.tostring(root, encoding="unicode")` 來寫入 XML 檔案。

**問題**：這樣做不會產生 `<?xml version="1.0" encoding="utf-8"?>` 宣告行。

**修正過程**：改用 `ET.ElementTree(root)` 建立樹物件，再使用 `tree.write(filepath, encoding="utf-8", xml_declaration=True)` 來輸出，這樣會正確產生 XML 宣告。
