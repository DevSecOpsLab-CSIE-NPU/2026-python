## Task 1 — CSV → JSON

### Red（失敗紀錄）
執行指令：python -m unittest test_read_csv.py -v
結果：
  ImportError: cannot import name 'read_csv'
  Ran 1 test in 0.000s — FAILED
失敗原因：read_csv 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest test_read_csv.py -v
結果：5 tests passed — OK
關鍵修改：實作 read_csv，使用 csv.DictReader 逐行讀取

### Red（失敗紀錄）
執行指令：python -m unittest test_task1_filter.py -v
結果：
  AttributeError: module 'task1_csv_to_json' has no attribute 'count_by_dept'
  Ran 1 test in 0.001s — FAILED
失敗原因：filter_by_admission 和 count_by_dept 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest test_task1_filter.py -v
結果：5 tests passed — OK
關鍵修改：實作 filter_by_admission（篩選入學方式）與 count_by_dept（分科系計數）

### Red（失敗紀錄）
執行指令：python -m unittest test_write_json.py -v
結果：
  TypeError: write_json() missing 1 required positional argument: 'filepath'
  Ran 1 test in 0.002s — FAILED
失敗原因：write_json 簽名與測試預期不符

### Green（通過紀錄）
執行指令：python -m unittest test_write_json.py -v
結果：4 tests passed — OK
關鍵修改：補齊 write_json 簽名 (data, filepath) 並實作 json.dump

## Task 2 — JSON → XML

### Red（失敗紀錄）
執行指令：python -m unittest test_read_json.py -v
結果：
  NotImplementedError
  Ran 4 tests in 0.003s — FAILED
失敗原因：read_json 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest test_read_json.py -v
結果：4 tests passed — OK
關鍵修改：實作 read_json，加入 JSONReadError 自訂例外包裹 JSONDecodeError

### Red（失敗紀錄）
執行指令：python -m unittest test_xml.py -v
結果：
  ModuleNotFoundError: No module named 'task2_json_to_xml'
  Ran 1 test in 0.001s — FAILED
失敗原因：build_xml_tree / write_xml 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest test_xml.py -v
結果：6 tests passed — OK
關鍵修改：用 xml.etree.ElementTree 手動建立 XML 樹，root 設為 <students>，每個學生包成 <student> 子節點

## Task 3 — 視覺化比較

### Red（失敗紀錄）
執行指令：python -m unittest test_plot.py -v
結果：
  ImportError: cannot import name 'plot_comparison'
  Ran 1 test in 0.002s — FAILED
失敗原因：plot_comparison 尚未實作

### Green（通過紀錄）
執行指令：python -m unittest test_plot.py -v
結果：1 test passed — OK
關鍵修改：實作 plot_comparison，用 matplotlib 畫長條圖並存檔

## Stage 5 — 安全掃描

### Red（失敗紀錄）
執行指令：python -m unittest test_security.py -v
結果：
  AssertionError: import os not found at top of file
  Ran 4 tests in 0.010s — FAILED (failures=1)
失敗原因：import os 放在 write_json / write_xml 函式內，未搬到檔案頂層

### Green（通過紀錄）
執行指令：python -m unittest test_security.py -v
結果：4 tests passed — OK
關鍵修改：將 import os 移至檔案最上方，count_by_dept 加入 type hint 及 is not None 判斷
