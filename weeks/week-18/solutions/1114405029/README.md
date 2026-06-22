# 程式設計 Python 期末上機考

## 基本資料

- 學號：1114405029
- 學號末兩碼：29
- D = 3
- SHIFT = 10
- base = 6
- K = 129

## 專案結構

```text
weeks/week-18/solutions/1114405029/
├── q1/
│   ├── __init__.py
│   ├── q1.py
│   └── test_q1.py
├── q2/
│   ├── __init__.py
│   ├── q2.py
│   └── test_q2.py
├── q3/
│   ├── __init__.py
│   ├── q3.py
│   └── test_q3.py
├── q4/
│   ├── __init__.py
│   ├── q4.py
│   ├── test_q4.py
│   └── assets/
│       └── radar.png
├── README.md
└── AI_LOG.md
```

## 測試與 TDD 流程

本次依照 Red -> Green -> Docs 完成。

1. Red：先建立 `test_*.py`，在尚未建立 `q1.py` 到 `q4.py` 時執行測試，確認測試失敗。
2. Red commit：`test: add failing tests for exam questions`
3. Green：完成四題函式與 CLI 入口，修正 Q3 大數案例的手算期望值後，全部 unittest 通過。
4. Green commit：`feat: implement exam questions`
5. Docs：補 `README.md`、`AI_LOG.md`，並產生 `q4/assets/radar.png`。

測試指令：

```bash
python -m unittest discover -s weeks/week-18/solutions/1114405029 -p "test_*.py" -v
```

在本資料夾也可以執行：

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

## Q1 Data Cleaning

題目摘要：讀取多組整數資料，直到 `n=0`。每組資料先去除重複並保留第一次出現順序，再保留可被 `D=3` 整除的數字，最後遞增排序輸出；空結果輸出 `NONE`。

函式簽名：

- `dedupe_keep_order(nums)`
- `filter_divisible(nums, d)`
- `clean_numbers(nums, d)`
- `solve(input_text, d=3)`

輸入邊界：`n >= 0`，每組第二行需有剛好 `n` 個整數，`n=0` 結束。整數可包含負數與 0。

例外處理：`d=0`、`n<0`、缺少資料列、數量不符合 `n` 時丟出 `ValueError`。

Edge case：沒有符合 D 的數字、`n=1`、負數、0、重複值、多組測資。

驗收標準：sample 輸入輸出為 `6 9` 與 `3`；無符合值輸出 `NONE`；輸出無多餘空白。

測試案例：一般去重篩選排序、全部不符合、負數與 0、多組到 `n=0`、單一數字空結果、非法 divisor。

時間複雜度：去重與篩選為 `O(n)`，排序最壞 `O(m log m)`，其中 `m` 是篩選後數量。空間複雜度：`O(n)`。

執行方式：

```bash
python weeks/week-18/solutions/1114405029/q1/q1.py
```

## Q2 Caesar Cipher

題目摘要：讀取多行直到 EOF，英文字母依 `SHIFT=10` 循環位移，大小寫分開處理，非英文字元原樣保留。

函式簽名：

- `shift_char(ch, shift)`
- `caesar_line(line, shift)`
- `solve(input_text, shift=10)`

輸入邊界：每行長度 `<= 1000`，可包含空行、空白、數字、標點。

例外處理：本題輸入為一般字串，無需額外例外；`shift` 會先對 26 取餘數。

Edge case：空行、`z/Z` 循環、多行 EOF、shift 大於 26。

驗收標準：`Hello, NPU!` 輸出 `Rovvy, XZE!`，`abc XYZ` 輸出 `klm HIJ`，非英文字不變。

測試案例：大小寫一般案例、`z/Z` 循環、標點空白數字、多行、空行、shift 大於 26。

時間複雜度：`O(L)`，其中 `L` 為總字元數。空間複雜度：`O(L)`。

執行方式：

```bash
python weeks/week-18/solutions/1114405029/q2/q2.py
```

## Q3 Digital Root in Base

題目摘要：讀取多行十進位非負整數直到 EOF。先轉成 `base=6` 的各位數字並加總，重複直到結果小於 base，最後用十進位輸出一位數字根。

函式簽名：

- `to_base_digits(n, base)`
- `digit_sum_in_base(n, base)`
- `digital_root_in_base(n, base)`
- `solve(input_text, base=6)`

輸入邊界：`0 <= x <= 10^9`，`0` 是有效資料不是結束。合法 base 為 `{2,3,5,6,7,8,9,11,13,16}`。

例外處理：非法 base 或負數丟出 `ValueError`。

Edge case：`x=0`、大數、多行 EOF、非法 base。

驗收標準：`0 -> 0`、`8 -> 3`、`63 -> 3`。Q3 大數案例用 base-1 規則驗算，`1_000_000_000` 在 base 6 的數字根為 `5`。

測試案例：0、8、63、`1_000_000_000`、多行輸入、非法 base 與負數。

時間複雜度：單次轉換為 `O(log_base n)`，重複位數和次數很少；空間複雜度：`O(log_base n)`。

執行方式：

```bash
python weeks/week-18/solutions/1114405029/q3/q3.py
```

## Q4 Search Performance

題目摘要：對升冪整數陣列搜尋 `K=129`，比較 linear search 與 binary search 的 found 狀態、索引、比較次數與 timeit 時間，並輸出較快者。若沒有輸入，預設使用 `1..200`；若有輸入，會讀入整數並排序。

函式簽名：

- `linear_search(arr, target)`
- `binary_search(arr, target)`
- `benchmark_searches(arr, target)`
- `normalize_metrics(linear_cmp, binary_cmp)`
- `create_radar_chart(output_path)`
- `solve(input_text=None, target=129)`

輸入邊界：陣列可為空、單一元素、目標在第一個或最後一個、找不到目標。

例外處理：輸入若不是整數，Python 會在轉型時丟出 `ValueError`。

Edge case：空陣列、單一元素、K 在第一個、K 在最後一個、找不到 K。

驗收標準：回報 `FOUND <idx> cmp=<次數>` 或 `NOT FOUND cmp=<次數>`、linear/binary timeit 秒數與 `=> binary faster` 或 `=> linear faster`。

測試案例：找到 K、找不到 K、空陣列、單一元素、比較次數合理性、K 在第一個與最後一個、benchmark 結構、radar 檔案產生。

時間複雜度：linear search 最壞 `O(n)`；binary search 最壞 `O(log n)`，但前提是資料已排序。空間複雜度兩者皆為 `O(1)`。

執行方式：

```bash
python weeks/week-18/solutions/1114405029/q4/q4.py
```

產生雷達圖：

```bash
python weeks/week-18/solutions/1114405029/q4/q4.py
```

或由 Python 呼叫：

```python
from q4.q4 import create_radar_chart
create_radar_chart("weeks/week-18/solutions/1114405029/q4/assets/radar.png")
```

### radar.png 說明

雷達圖比較五個維度：

- 搜尋速度：用比較次數的反向分數估計，binary search 通常較高。
- 比較次數：比較次數越少，正規化分數越高。
- 是否需要排序：linear search 不要求排序，因此分數較高；binary search 需要升冪資料。
- 實作簡易度：linear search 較直觀，binary search 需維護左右界。
- 最壞情況效率：linear 為 `O(n)`，binary 為 `O(log n)`，binary 分數較高。

正規化方式：各項分數落在 `0..1`，越接近 1 代表越好。比較次數相關分數使用 `1 - cmp / max_cmp`，並保留最低 0.05，避免圖形完全貼近中心。

Binary search 較有效率的原因：每次比較都能排除約一半搜尋範圍，因此在資料量變大時，比 linear search 逐一檢查更能降低比較次數與執行時間。
