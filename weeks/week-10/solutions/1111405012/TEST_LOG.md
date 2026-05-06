# Week 10 測試執行紀錄

## Task 1 / Task 2：Red

先建立 `tests/test_task1.py` 與 `tests/test_task2.py`，此時尚未建立主程式檔案。

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_task1 (unittest.loader._FailedTest.test_task1) ... ERROR
test_task2 (unittest.loader._FailedTest.test_task2) ... ERROR

ModuleNotFoundError: No module named 'task1_csv_to_json'
ModuleNotFoundError: No module named 'task2_json_to_xml'

Ran 2 tests in 0.000s
FAILED (errors=2)
```

失敗原因：

- Task 1 測試已經先引用 `filter_by_admission()`、`count_by_dept()`、`write_json()`，但 `task1_csv_to_json.py` 尚未存在。
- Task 2 測試已經先引用 `build_xml_tree()`、`write_xml()`，但 `task2_json_to_xml.py` 尚未存在。

## Task 1 / Task 2：Green

完成以下最小可行實作：

- `task1_csv_to_json.py`：讀取 CSV、過濾「聯合登記分發」、依系所統計、輸出 JSON。
- `task2_json_to_xml.py`：讀取 JSON、建立 XML tree、輸出 XML。

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_build_output_contains_required_fields ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_write_json_creates_utf8_json ... ok
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_write_xml_creates_parseable_file ... ok
test_xml_is_valid ... ok

Ran 13 tests in 0.119s
OK
```

## 環境限制紀錄

第一次在一般沙盒執行完整測試時，寫檔測試中的 `tempfile.TemporaryDirectory()` 無法取得可用暫存目錄：

```text
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', ...]
Ran 13 tests in 0.146s
FAILED (errors=2)
```

改在可使用暫存目錄的授權執行環境中重跑後通過。這次失敗與程式邏輯無關，原因是執行環境的檔案系統限制。

## Task 1 / Task 2 / Task 3：輸出檔驗證

### Task 1

執行指令：

```bash
python3 -B task1_csv_to_json.py
```

結果：

```text
[timeit] read_csv 耗時 0.002250s
[timeit] write_json 耗時 0.001564s
JSON 已儲存：output/students.json
```

### Task 2

執行指令：

```bash
python3 -B task2_json_to_xml.py
```

結果：

```text
[timeit] read_json 耗時 0.000500s
[timeit] write_xml 耗時 0.001542s
XML 已儲存：output/students.xml
```

### Task 3

第一次執行 fallback PNG 產生器時，發現 PNG chunk 型別傳入字串而非 bytes：

```text
TypeError: can't concat str to bytes
```

修正方式：將 `chunk("IHDR", ...)`、`chunk("IDAT", ...)`、`chunk("IEND", ...)` 改為傳入 bytes：`b"IHDR"`、`b"IDAT"`、`b"IEND"`。

修正後執行：

```bash
python3 -B task3_plot_comparison.py
```

結果：

```text
圖表已儲存：output/timing_comparison.png
```

## 最終驗證

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果：

```text
Ran 13 tests in 0.003s
OK
```

## 加分版驗證

### Task 1 Bonus

執行指令：

```bash
python3 -B task1_csv_to_json_bonus.py
```

結果：

```text
[timeit] read_csv 耗時 0.002126s
[timeit] write_json 耗時 0.001571s
[timeit] write_bonus_json 耗時 0.001581s
加分 JSON 已儲存：output/students_bonus.json
```

### Task 2 Bonus

執行指令：

```bash
python3 -B task2_json_to_xml_bonus.py
```

結果：

```text
[timeit] read_json 耗時 0.000612s
[timeit] write_bonus_xml 耗時 0.001857s
加分 XML 已儲存：output/students_bonus.xml
```

### Task 3 Bonus

此環境使用臨時 venv 驗證 `seaborn` 程式邏輯，但 Linux 系統沒有可顯示繁體中文的 CJK 系統字型，因此程式正確停止輸出，避免產生亂碼圖。

結果摘要：

```text
RuntimeError: 找不到可正確顯示中文字的系統字型。Windows 會優先使用 Microsoft JhengHei；Linux 會自動尋找 WenQuanYi、AR PL、Source Han、LXGW 等已安裝字型，也會檢查其他支援中文字的系統字型。目前環境沒有可用 CJK 系統字型，因此停止產生圖表，避免中文字變成方塊。
```

## 字型改為 fonts-noto-cjk 後重新驗證

字型選擇邏輯改為直接掃描 `fonts-noto-cjk` 字型檔路徑（`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc` 等），移除跨平台備選清單與任意 CJK fallback。

背景說明：`NotoSansCJK-Regular.ttc` 為 TTC（TrueType Collection）多語系集合檔，包含 TC／SC／JP／KR／HK 五種語系，但 `matplotlib` 透過 `ft2font` 讀取 TTC 時只認出第一個 face（`Noto Sans CJK JP`）。改用直接搜尋字型檔路徑並以 `addfont()` 明確載入，可繞過名稱判斷限制，同時確保字型來源仍限定為 `fonts-noto-cjk` 套件提供的檔案。

安裝字型套件（已由使用者完成）：

```bash
sudo apt install fonts-noto-cjk
```

建立臨時 venv 安裝繪圖套件：

```bash
python3 -m venv /tmp/venv_week10
/tmp/venv_week10/bin/pip install seaborn matplotlib pandas numpy
```

### unittest

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_build_output_contains_required_fields ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_write_json_creates_utf8_json ... ok
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_write_xml_creates_parseable_file ... ok
test_xml_is_valid ... ok

Ran 13 tests in 0.003s
OK
```

### Task 1

執行指令：

```bash
python3 -B task1_csv_to_json.py
```

結果：

```text
[timeit] read_csv 耗時 0.002245s
[timeit] write_json 耗時 0.001485s
JSON 已儲存：output/students.json
```

### Task 2

執行指令：

```bash
python3 -B task2_json_to_xml.py
```

結果：

```text
[timeit] read_json 耗時 0.000533s
[timeit] write_xml 耗時 0.001852s
XML 已儲存：output/students.xml
```

### Task 3

執行指令：

```bash
python3 -B task3_plot_comparison.py
```

結果：

```text
圖表已儲存：output/timing_comparison.png
```

### Task 1 Bonus

執行指令：

```bash
python3 -B task1_csv_to_json_bonus.py
```

結果：

```text
[timeit] read_csv 耗時 0.002096s
[timeit] write_json 耗時 0.001640s
[timeit] write_bonus_json 耗時 0.001649s
加分 JSON 已儲存：output/students_bonus.json
```

### Task 2 Bonus

執行指令：

```bash
python3 -B task2_json_to_xml_bonus.py
```

結果：

```text
[timeit] read_json 耗時 0.000447s
[timeit] write_bonus_xml 耗時 0.001636s
加分 XML 已儲存：output/students_bonus.xml
```

### Task 3 Bonus

以臨時 venv（已安裝 `seaborn matplotlib pandas numpy`）與系統 `fonts-noto-cjk` 字型執行，成功產生圖表。

執行指令：

```bash
/tmp/venv_week10/bin/python -B task3_plot_comparison_bonus.py
```

結果：

```text
加分圖表已儲存：output/timing_comparison_bonus.png
```

備註：初版產出圖寬達 13450px（正常應為約 2160px），所有內容擠到右側角落，無法辨認。

根本原因：`apply_gradient_to_bars()` 對每根 bar 呼叫 `ax.imshow(gradient, extent=..., aspect="auto")`，其中 `gradient` 為 `(1, 256)` 陣列。`bbox_inches="tight"` 計算 bounding box 時，會將每張 `AxesImage` 的原始像素寬度（256px）納入範圍，導致圖的實際儲存尺寸暴增。

修正方式：移除 `ax.imshow()` 漸層，改為對每根 bar 疊加 40 條半透明矩形色帶，在資料座標系內直接繪製左淺右深的漸層，完全不涉及 `AxesImage`，bounding box 計算正常。修正後 `UserWarning: Tight layout not applied` 同步消除。

修正後執行結果：

```text
加分圖表已儲存：output/timing_comparison_bonus.png
```

## 圖表版面調整

修正漸層問題後，圖表可辨認，但 Legend 與結論框同在左上角互相遮擋，笑臉也在右上角與 bar 重疊。調整如下：

- `figsize` 由 `(10, 7)` 改為 `(12, 9)`，給 Legend 與元素更多空間。
- Legend 改為 `bbox_to_anchor=(1.01, 1.0), loc="upper left"`，移至 axes 右側外部，不再擋住 bar。
- 結論框由左上 `(0.02, 0.93)` 改為 `(0.55, 0.90)`（最短的 `讀取 JSON` bar 上方空白區域），`ha="center"`。
- 笑臉由右上 `(0.92, 0.82)` 改為左下 `(0.07, 0.12)`，放在第一組 bar 下方空白處。

執行指令：

```bash
/tmp/venv_week10/bin/python -B task3_plot_comparison_bonus.py
```

結果：

```text
加分圖表已儲存：output/timing_comparison_bonus.png
```

## 字型改為 fonts-noto-cjk 後重新驗證

字型選擇邏輯改為只使用 `fonts-noto-cjk`（Noto CJK 字型系列），移除跨平台備選清單與任意 CJK fallback。重新執行所有程式確認行為不變。

### unittest

執行指令：

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

```text
test_build_output_contains_required_fields ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_write_json_creates_utf8_json ... ok
test_empty_student_list ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_write_xml_creates_parseable_file ... ok
test_xml_is_valid ... ok

Ran 13 tests in 0.002s
OK
```

### Task 1

執行指令：

```bash
python3 -B task1_csv_to_json.py
```

結果：

```text
[timeit] read_csv 耗時 0.002512s
[timeit] write_json 耗時 0.001434s
JSON 已儲存：output/students.json
```

### Task 2

執行指令：

```bash
python3 -B task2_json_to_xml.py
```

結果：

```text
[timeit] read_json 耗時 0.000513s
[timeit] write_xml 耗時 0.001671s
XML 已儲存：output/students.xml
```

### Task 3

執行指令：

```bash
python3 -B task3_plot_comparison.py
```

結果：

```text
圖表已儲存：output/timing_comparison.png
```

### Task 1 Bonus

執行指令：

```bash
python3 -B task1_csv_to_json_bonus.py
```

結果：

```text
[timeit] read_csv 耗時 0.002017s
[timeit] write_json 耗時 0.001501s
[timeit] write_bonus_json 耗時 0.001510s
加分 JSON 已儲存：output/students_bonus.json
```

### Task 2 Bonus

執行指令：

```bash
python3 -B task2_json_to_xml_bonus.py
```

結果：

```text
[timeit] read_json 耗時 0.000367s
[timeit] write_bonus_xml 耗時 0.001615s
加分 XML 已儲存：output/students_bonus.xml
```

### Task 3 Bonus

此環境未安裝 `matplotlib`（`seaborn` 所需），因此程式在套件載入階段即停止，尚未進入字型檢查。字型改動本身不影響此錯誤的觸發順序。

執行指令：

```bash
python3 -B task3_plot_comparison_bonus.py
```

結果摘要：

```text
RuntimeError: 缺少套件：matplotlib。請先安裝：python3 -m pip install seaborn matplotlib pandas numpy
```

若安裝套件後仍未安裝 `fonts-noto-cjk`，程式會在字型檢查階段停止，錯誤訊息改為：

```text
RuntimeError: 找不到 fonts-noto-cjk 字型，無法輸出圖表。
請先安裝系統套件：sudo apt install fonts-noto-cjk
```
