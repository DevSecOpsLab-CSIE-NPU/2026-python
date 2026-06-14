## 完成項目

- Task 1：CSV → JSON 轉換（過濾、統計、輸出）
- Task 2：JSON → XML 轉換
- Task 3：函式耗時比較圖

## 執行方式

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器運作說明

`@timeit` 是一個裝飾器，它在函式執行前記錄開始時間，執行後計算結束時間，兩者相減得到耗時並印出。透過 `@functools.wraps` 保留原函式的中繼資料（如 `__name__`），確保被裝飾的函式行為不變。

## 最難理解的 bug 及修正方式

在 Task 2 中，使用 `ET.Element("students", attrib={...})` 時，發現 XML 屬性的順序與預期不同，導致測試比對屬性時失敗。修正方式：改用 Python 3.8+ 的 keyword argument 語法 `ET.Element("students", source=source, total=str(total))`，使屬性順序與傳入參數順序一致。
