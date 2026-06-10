# AI_USAGE.md

## 我問了哪些問題

1. `csv.DictReader` 讀取 UTF-8-BOM 編碼的 CSV 時應該用哪個 encoding 參數？
2. `xml.etree.ElementTree` 怎麼寫出帶有 XML 宣告（`<?xml version="1.0"?>`）的檔案？
3. `ET.indent()` 是哪個 Python 版本加入的？在 3.9 以下如何替代？
4. `@functools.wraps` 的作用是什麼，不加的話會有什麼問題？
5. 如何在 unittest 中測試一個函式回傳的 ElementTree 節點，而不需要真正寫檔？

## AI 建議有採用的部分

- 使用 `encoding='utf-8-sig'` 讀取 BOM 開頭的 CSV，AI 說明這樣可讓 `csv.DictReader` 自動去掉 BOM，欄位名稱不會帶 `﻿` 前綴。
- 以 `tree.write(f, encoding='utf-8', xml_declaration=True)` 搭配二進位模式（`'wb'`）開檔，確保寫出正確的 UTF-8 XML 宣告。
- 測試 `build_xml_tree` 時直接對回傳的 `ET.Element` 呼叫 `ET.tostring()` 再 `ET.fromstring()`，不需要磁碟 I/O，讓單元測試更純粹。

## AI 建議拒絕的部分及原因

- AI 建議用 `collections.Counter` 實作 `count_by_dept`。我拒絕了，改用普通 dict 累加，原因是作業要求我能自己解釋每行邏輯，`Counter` 雖然簡潔但隱藏了計數機制，不利學習理解。
- AI 建議在 `task3_plot_comparison.py` 用 `subprocess` 呼叫 task1、task2 並解析 stdout 取得時間。我拒絕了，直接 import 函式並用 `time.perf_counter()` 手動計時，這樣更乾淨且不依賴外部進程。

## AI 輸出執行後發現有誤的案例

AI 給出的 `write_xml` 範例使用了 `open(filepath, 'w', encoding='utf-8')`（文字模式）搭配 `tree.write(f, ...)`，執行後出現：

```
TypeError: write() argument must be str, not bytes
```

原因：`ElementTree.write()` 當 `encoding` 不是 `'unicode'` 時會輸出 bytes，必須用二進位模式 `'wb'` 開檔。修正後：

```python
with open(filepath, 'wb') as f:
    tree.write(f, encoding='utf-8', xml_declaration=True)
```

這個錯誤讓我理解了 Python 文字模式與二進位模式在 XML 寫出時的重要差異。
