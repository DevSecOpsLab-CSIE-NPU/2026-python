# Week 10 Homework

## 完成項目

- Task 1：讀取 CSV，篩選 `入學方式 == "聯合登記分發"` 的學生資料，統計各系所人數，並輸出 `output/students.json`
- Task 2：讀取 `output/students.json`，將學生清單轉換成 XML 格式，並輸出 `output/students.xml`
- Task 3：使用 `seaborn` 繪製函式耗時比較圖，並輸出 `output/timing_comparison.png`
- 完成 `unittest` 測試，Task 1 與 Task 2 合計 10 個測試案例

---

## 執行方式

### 執行 Task 1

```powershell
python task1_csv_to_json.py
```

### 執行 Task 2

```powershell
python task2_json_to_xml.py
```

### 執行 Task 3

```powershell
python task3_plot_comparison.py
```

### 執行 unittest

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## @timeit 裝飾器說明

`@timeit` 是用來量測函式執行時間的裝飾器。  
當函式執行前，裝飾器會先記錄開始時間；函式執行結束後，再記錄結束時間，兩者相減即可得到函式耗時。  
本作業將 `@timeit` 套用在 `read_csv()`、`write_json()`、`read_json()`、`write_xml()`，用來比較 CSV、JSON、XML 相關操作的執行效率。

---

## 遇到的問題與修正

本次作業中最難理解的問題是 CSV 檔案路徑錯誤。

一開始程式依照題目文件中的路徑讀取：

```text
weeks/week-08/in-class/stu-data/113年新生資料庫.csv
```

但是實際專案中的檔案位置是：

```text
assets/stu-data/113年新生資料庫.csv
```

因此執行 Task 1 時發生 `FileNotFoundError`。  
後來重新檢查專案資料夾結構，並修改 `get_csv_path()`，讓程式從正確位置讀取 CSV，才成功產生 `output/students.json`。

---

## Bonus

本作業有完成以下加分項目：

- 使用 `seaborn` 製作更具設計感與可讀性的函式耗時比較圖
- 圖表加入不同顏色的長條、白色網格背景與清楚的版面配置
- 圖中中文標題、座標軸、註解文字皆能正常顯示，沒有亂碼或缺字
- 在圖中加入摘要註解與結論，說明本次執行中 `read_csv` 是最耗時的函式