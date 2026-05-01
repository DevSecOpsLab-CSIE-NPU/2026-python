# AI_USAGE.md

## 我問了哪些問題

1. `xml.etree.ElementTree` 中 `ET.indent()` 是哪個 Python 版本開始支援？
2. 用 `csv.DictReader` 讀取 UTF-8-BOM 檔案時，`encoding='utf-8-sig'` 與 `'utf-8'` 的差異是什麼？
3. `@functools.wraps(func)` 的作用是什麼？不加會發生什麼事？
4. `matplotlib` 在沒有螢幕的環境（CI）要怎麼避免 `UserWarning: cannot connect to X server`？
5. `ET.tostring()` 輸出的 XML 不含 `<?xml ...?>` 宣告，要怎麼加？

## AI 建議我有採用的部分

- 使用 `matplotlib.use("Agg")` 避免無視窗環境報錯，改為直接輸出圖檔。
- 在 `write_xml()` 中手動寫入 `<?xml version="1.0" encoding="utf-8"?>` 再接 ElementTree 輸出，確保宣告行正確。
- 使用 `os.makedirs(..., exist_ok=True)` 自動建立輸出資料夾，避免 FileNotFoundError。

## AI 建議我拒絕的部分及原因

- AI 建議直接用 `minidom.toprettyxml()` 做格式化輸出，但它會額外加入空白行，導致 XML 驗證較麻煩，改用 `ET.indent()` 較簡潔。
- AI 建議測試中直接讀取 `output/students.json` 做整合測試，但這樣會讓測試依賴外部檔案存在，不符合單元測試原則，改為傳入假資料 dict。

## AI 輸出執行後發現有誤的案例

**案例：`json.dump` 預設不保留中文**

AI 建議的初版程式：
```python
json.dump(data, f)
```

執行後 `students.json` 內容變成：
```json
"\u5b78\u865f": "\u31311234001"
```

所有中文都被 escape 成 Unicode 碼點。  
修正方式：加上 `ensure_ascii=False`：
```python
json.dump(data, f, ensure_ascii=False, indent=2)
```
修正後中文正常顯示。
