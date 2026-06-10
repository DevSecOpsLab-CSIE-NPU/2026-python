# Week 10 作業 — 資料格式轉換

學號：1114405019

## 完成項目

- [x] Task 1：CSV → JSON（`task1_csv_to_json.py`）
- [x] Task 2：JSON → XML（`task2_json_to_xml.py`）
- [x] Task 3：執行時間比較圖（`task3_plot_comparison.py`）
- [x] TDD 測試骨架（`tests/`，共 13 個測試）

## 執行方式

```bash
# 先執行 Task 1（產生 output/students.json）
python task1_csv_to_json.py

# 再執行 Task 2（讀取 JSON，產生 output/students.xml）
python task2_json_to_xml.py

# 執行 Task 3（重新計時並產生 output/timing_comparison.png）
python task3_plot_comparison.py

# 執行所有測試
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器說明

`timeit` 是一個接受函式為參數、回傳包裝函式的 higher-order function。內部的 `wrapper` 在呼叫原函式前後分別記錄 `time.perf_counter()`，相減得到執行秒數後印出，再把原始回傳值傳出。用 `@functools.wraps(func)` 保留原函式的 `__name__` 等 metadata，讓裝飾器對外透明。

## 最難理解的 bug 與修正

**問題：** Task 2 初版沒有設定 `total` 屬性為 `str(len(students))`，而是直接傳入 `int`，導致 `ET.Element` 在寫出 XML 時拋出 `TypeError: cannot serialize 42 (type int)`。

**修正：** XML 屬性值必須全為字串，改成 `'total': str(len(students))` 即可。這也是 `test_empty_student_list` 驗證 `root.attrib['total'] == '0'`（字串而非整數 0）的原因。
