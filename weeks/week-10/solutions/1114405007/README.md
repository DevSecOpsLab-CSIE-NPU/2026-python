# Week 10 作業說明

## 完成項目

- [x] Task 1：CSV → JSON 轉換（過濾「聯合登記分發」、系所統計、輸出 `output/students.json`）
- [x] Task 2：JSON → XML 轉換（輸出 `output/students.xml`）
- [x] Task 3：函式耗時比較圖（輸出 `output/timing_comparison.png`）
- [x] TDD 測試（`tests/test_task1.py` 10 個、`tests/test_task2.py` 7 個，共 17 個測試全通過）
- [x] TIMING_REPORT.md、TEST_LOG.md、AI_USAGE.md

## 執行方式

```bash
# 依序執行三個 Task
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py

# 執行所有單元測試
python -m unittest discover -s tests -p "test_*.py" -v
```

## `@timeit` 裝飾器說明

`@timeit` 是一個高階函式（higher-order function），它接收被裝飾的函式 `func` 並回傳一個新的 `wrapper` 函式。`wrapper` 在呼叫原始函式前後各記錄一次時間戳，兩者差值即為執行耗時，並印出到終端機。使用 `@functools.wraps(func)` 可讓 `wrapper` 保留原函式的名稱與 docstring，避免除錯時混淆。

## 遇到的 Bug 及修正

**Bug：`write_xml` 產生的 XML 缺少宣告行**

問題：直接用 `tree.write(f, xml_declaration=True)` 時，編碼宣告變成 `<?xml version='1.0' encoding='utf-8'?>`（單引號），與作業要求的雙引號格式不符。

修正：改為手動寫入宣告行，再讓 ElementTree 輸出其餘內容：

```python
with open(filepath, "wb") as f:
    f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    tree.write(f, encoding="utf-8", xml_declaration=False)
```
