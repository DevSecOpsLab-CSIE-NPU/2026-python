# Week 10 任務完成說明

## 完成內容

- 完成 Task 1：讀取 CSV，篩選 `入學方式 == "聯合登記分發"`，統計各系所人數並輸出 JSON。
- 完成 Task 2：讀取 Task 1 產生的 JSON，轉換成 HOMEWORK 指定格式的 XML。
- 完成 Task 3：依 `@timeit` 結果產生函式耗時比較圖。
- 完成加分版程式：`task1_csv_to_json_bonus.py`、`task2_json_to_xml_bonus.py`、`task3_plot_comparison_bonus.py`。
- 使用 `unittest` 完成 Task 1 與 Task 2 測試，共 13 個測試案例。
- 補上 `TEST_CASES.md`、`TEST_LOG.md`、`TIMING_REPORT.md` 與 `AI_USAGE.md`。

## 檔案位置

```text
weeks/week-10/solutions/1111405012/
├── task1_csv_to_json.py
├── task1_csv_to_json_bonus.py
├── task2_json_to_xml.py
├── task2_json_to_xml_bonus.py
├── task3_plot_comparison.py
├── task3_plot_comparison_bonus.py
├── output/
│   ├── students.json
│   ├── students_bonus.json
│   ├── students.xml
│   ├── students_bonus.xml
│   ├── timing_comparison.png
│   └── timing_comparison_bonus.png  # 有 seaborn 與 CJK 系統字型後產生
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

執行加分版：

```bash
python3 -B task1_csv_to_json_bonus.py
python3 -B task2_json_to_xml_bonus.py
python3 -B task3_plot_comparison_bonus.py
```

`task3_plot_comparison_bonus.py` 需要 `seaborn`、`matplotlib`、`pandas`、`numpy`，且必須安裝系統套件 `fonts-noto-cjk`（Noto CJK 字型）。若找不到 Noto CJK 字型，程式會停止並提示安裝指令，不會輸出圖檔，避免中文變成方塊或亂碼。

安裝字型套件：

```bash
sudo apt install fonts-noto-cjk
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

## 加分項

- `task1_csv_to_json_bonus.py`：在原本 JSON 之外加入加分摘要、系所排名、全部入學方式統計。
- `task2_json_to_xml_bonus.py`：輸出 `students_bonus.xml`，加入摘要節點與系所排名節點。
- `task3_plot_comparison_bonus.py`：使用 `seaborn` 製作加分圖，包含中文標題、中文座標軸、中文標註文字。
- 圖表延伸效果包含第二組資料比較、漸層 bar、X 軸文字右旋轉 90 度、圖上笑臉、摘要註解與結論。
- 圖表字型固定使用系統套件 `fonts-noto-cjk`（Noto CJK），找不到時程式會停止並提示安裝，不輸出圖檔。

## 第三方字型授權聲明

- 字型名稱：Noto CJK / fonts-noto-cjk
- 授權：SIL Open Font License 1.1
- 用途：僅用於 matplotlib/seaborn 圖表中文字顯示
- 字型檔由系統套件提供，未隨作業重新散布

參考來源：

- Debian `fonts-noto-cjk` copyright：<https://sources.debian.org/copyright/license/fonts-noto-cjk/>
- Noto Fonts LICENSE：<https://github.com/notofonts/noto-fonts/blob/main/LICENSE>
- SIL Open Font License 1.1：<https://openfontlicense.org/>

## 補充說明

- 本次所有變更只放在 `weeks/week-10/solutions/1111405012/`。
- 原始教材檔案、HOMEWORK 與 docs 沒有修改。
- CSV 使用新資料路徑：`assets/stu-data/113年新生資料庫.csv`。
