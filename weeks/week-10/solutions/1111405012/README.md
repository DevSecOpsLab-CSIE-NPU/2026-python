# Week 10 任務完成說明

## 完成內容

- 完成 Task 1：讀取 CSV，篩選 `入學方式 == "聯合登記分發"`，統計各系所人數並輸出 JSON。
- 完成 Task 2：讀取 Task 1 產生的 JSON，轉換成 HOMEWORK 指定格式的 XML。
- 完成 Task 3：依 `@timeit` 結果產生函式耗時比較圖。
- 使用 `unittest` 完成 Task 1 與 Task 2 測試，共 13 個測試案例。
- 補上 `TEST_CASES.md`、`TEST_LOG.md`、`TIMING_REPORT.md` 與 `AI_USAGE.md`。

## 檔案位置

```text
weeks/week-10/solutions/1111405012/
├── task1_csv_to_json.py
├── task2_json_to_xml.py
├── task3_plot_comparison.py
├── output/
│   ├── students.json
│   ├── students.xml
│   └── timing_comparison.png
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
├── TEST_CASES.md
├── TEST_LOG.md
├── TIMING_REPORT.md
├── AI_USAGE.md
└── README.md
```

## 執行方式

本機可用版本：

```bash
python3 --version
```

本次驗證使用：

```text
Python 3.12.3
```

執行 Task 1：

```bash
python3 -B task1_csv_to_json.py
```

執行 Task 2：

```bash
python3 -B task2_json_to_xml.py
```

執行 Task 3：

```bash
python3 -B task3_plot_comparison.py
```

執行測試：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

## 測試結果摘要

```text
Ran 13 tests in 0.003s
OK
```

輸出檔驗證：

- `output/students.json`：`總人數` 為 189。
- `output/students.xml`：`<student>` 數量為 189。
- `output/timing_comparison.png`：已產生有效 PNG 檔。

## `@timeit` 裝飾器說明

`@timeit` 會把原本的函式包在 `wrapper()` 裡面，在函式執行前用 `time.perf_counter()` 記錄開始時間，執行後再計算差值並印出耗時。使用 `functools.wraps(func)` 可以保留原函式名稱與說明，避免除錯時只看到 `wrapper`。

## 遇到的 bug 與修正方式

Task 3 原本假設環境可以使用 `matplotlib`，但本機沒有安裝。為了仍能產生 `output/timing_comparison.png`，程式改成先嘗試 `matplotlib`，若套件不存在則使用標準函式庫產生簡易 PNG 長條圖。

fallback PNG 第一次執行時出現 `TypeError: can't concat str to bytes`，原因是 PNG chunk type 必須是 bytes。已修正為 `b"IHDR"`、`b"IDAT"`、`b"IEND"`。

## 補充說明

- 本次所有變更只放在 `weeks/week-10/solutions/1111405012/`。
- 原始教材檔案、HOMEWORK 與 docs 沒有修改。
- CSV 使用新資料路徑：`assets/stu-data/113年新生資料庫.csv`。
