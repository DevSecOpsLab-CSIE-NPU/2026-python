# Week 10 回家作業：資料格式轉換

1. **完成項目**
   - Task 1: CSV -> JSON 轉換 (`task1_csv_to_json.py`)。成功載入資料、過濾並統計輸出。
   - Task 2: JSON -> XML 轉換 (`task2_json_to_xml.py`)。建立 DOM Tree 並正確呈現 pretty XML。
   - Task 3: 畫圖比較 (`task3_plot_comparison.py`)。用 matplotlib 建立柱狀圖。
   - TDD Unit Tests (`tests/test_task1.py` 和 `tests/test_task2.py`)。

2. **執行方式**
   ```bash
   python task1_csv_to_json.py
   python task2_json_to_xml.py
   python task3_plot_comparison.py
   python -m unittest discover -s tests -p "test_*.py" -v
   ```

3. **`@timeit` 裝飾器的運作說明**
   `@timeit` 是一個閉包工廠。當它被加上到函式上時，這層外衣會將原函式綁架、在開始前先取得目前的系統時間（`perf_counter`），接著跑原函式並收集其回傳值；最後再計算當前時間與開始時間的誤差來算出整體耗時並列印。

4. **最難理解的一個 bug 及修正方式**
   一開始 TDD 撰寫 Task 2 的 `build_xml_tree()` 時找不到 JSON 裡的值卻報錯，後來才發現如果是找不到的話 `dict.get("學號", "")` 就非常穩固，再也不會因 Key Error 引發系統崩潰，而修正方式就是全面改採用 `.get()` 代替 `[]`。