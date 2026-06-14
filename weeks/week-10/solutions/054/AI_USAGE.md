## 1. 我問了哪些問題

1. CSV 的 encoding='utf-8-sig' 是什麼意思？何時需要使用？
2. xml.etree.ElementTree 如何建立帶有屬性的元素？
3. matplotlib 如何在 bar chart 的每個 bar 上方標註數值？

## 2. AI 建議我有採用的部分

- 使用 `csv.DictReader` 代替 `csv.reader`，程式碼更簡潔且可讀性更高
- 使用 `ET.SubElement` 加上屬性 dict 參數一次設定多個屬性
- 在 bar chart 使用 `ax.text()` 配合迴圈逐一標註數值

## 3. AI 建議我拒絕的部分及原因

- AI 建議使用 `pandas.read_csv` 讀取 CSV — 拒絕，因為作業要求自行實作 CSV 讀取邏輯，不使用第三方套件
- AI 建議直接複製課堂範例的 @timeit 裝飾器 — 拒絕，因為作業要求自行重新實作

## 4. AI 輸出我執行後發現有誤的案例

AI 提供的 `build_xml_tree` 中使用了 `ET.Element("students", attrib={"source": source, "total": str(total)})`，但執行後發現 XML 屬性順序不一致。修正方式：改使用關鍵字參數直接傳入 `ET.Element("students", source=source, total=str(total))`，確保屬性順序與輸出格式要求一致。
