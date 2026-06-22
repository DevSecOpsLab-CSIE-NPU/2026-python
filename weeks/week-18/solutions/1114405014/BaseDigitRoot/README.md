# Base Digit Root

## 題目說明

本題為 Week 18 第三題 Base Digit Root。程式會讀取多個十進位非負整數，依照指定進位基底 `base` 計算該數字在該進位下的數字根。

處理流程：

1. 將十進位整數轉換成指定進位的各位數字
2. 將各位數字相加
3. 若加總結果仍不是該進位的一位數，繼續重複
4. 當結果滿足 `0 <= result < base` 時停止
5. 每個輸入數字輸出一行結果

## 個人參數

學號末兩碼：`14`

| 參數 | 結果 |
|---|---:|
| 個位數 `u` | `4` |
| 第三題進位基底 `base` | `5` |

因此本題使用 **五進位** 計算數字根。

## 檔案說明

```text
BaseDigitRoot/
├── base_digit_root.py
├── test_base_digit_root.py
├── README.md
├── AI_LOG.md
└── TEST_LOG.md
```

| 檔案 | 說明 |
|---|---|
| `base_digit_root.py` | 第三題主程式 |
| `test_base_digit_root.py` | pytest 測試檔，共 14 個測試案例 |
| `README.md` | 題目、執行方式與測試方式說明 |
| `AI_LOG.md` | AI 協作紀錄 |
| `TEST_LOG.md` | 測試紀錄整理 |

## 函式設計

### `validate_base(base: int) -> None`

檢查進位基底是否合法。

規則：

```text
base >= 2
```

若 `base < 2`，丟出 `ValueError`。

---

### `validate_number(n: int) -> None`

檢查輸入數字是否合法。

規則：

```text
n >= 0
```

若 `n < 0`，丟出 `ValueError`。

---

### `to_base_digits(n: int, base: int) -> list[int]`

將十進位非負整數轉成指定進位的數字列表。

範例：

```python
to_base_digits(24, 5)
```

回傳：

```python
[4, 4]
```

因為：

```text
24(decimal) = 44(base 5)
```

---

### `digit_root_in_base(n: int, base: int) -> int`

計算指定進位下的數字根。

範例：

```python
digit_root_in_base(24, 5)
```

計算流程：

```text
24 = 44₅
4 + 4 = 8

8 = 13₅
1 + 3 = 4
```

回傳：

```python
4
```

---

### `solve(input_text: str, base: int = 5) -> str`

處理完整輸入文字。

輸入可以使用換行或空白分隔，例如：

```text
0
4
5
24
25
124
```

或：

```text
0 4 5 24 25 124
```

兩者都會被解析成多筆輸入，每筆輸出一行數字根。

---

## 輸入格式

輸入為多個十進位非負整數，可用空白或換行分隔。

範例：

```text
0 8 63
```

## 輸出格式

每個輸入數字輸出一行數字根。

以本題 `base = 5` 計算：

```text
0 → 0
8 → 13₅ → 1 + 3 = 4
63 → 223₅ → 2 + 2 + 3 = 7 → 12₅ → 1 + 2 = 3
```

因此輸出：

```text
0
4
3
```

## 執行方式

```bash
python base_digit_root.py
```

手動輸入完成後，因為目前主程式使用 `sys.stdin.read()` 讀取完整 stdin，因此需要送出 EOF 才會開始輸出。

Windows PowerShell / CMD：

```text
Ctrl + Z
Enter
```

Linux / WSL / Git Bash：

```text
Ctrl + D
```

也可以使用檔案輸入：

```bash
python base_digit_root.py < sample.txt
```

## 測試方式

```bash
pytest
```

目前測試結果：

```text
14 passed
```

## 測試案例涵蓋

| 測試案例 | 驗證內容 |
|---|---|
| `test_to_base_digits_zero` | `0` 轉換為 `[0]` |
| `test_to_base_digits_single_digit` | 小於 base 的數字保持單一位數 |
| `test_to_base_digits_base_value` | `5` 轉換為五進位 `[1, 0]` |
| `test_to_base_digits_multiple_digits` | `24` 轉換為 `[4, 4]` |
| `test_digit_root_zero` | `0` 的數字根為 `0` |
| `test_digit_root_number_less_than_base` | 小於 base 的數字根為自己 |
| `test_digit_root_equal_to_base` | `5` 的數字根為 `1` |
| `test_digit_root_requires_repeated_sum` | 驗證需要反覆加總的案例 |
| `test_digit_root_power_of_base` | 驗證 base 的次方數字根 |
| `test_digit_root_larger_number` | 驗證較大數字 |
| `test_solve_multiple_lines` | 驗證多行輸入 |
| `test_solve_space_separated_input` | 驗證空白分隔輸入 |
| `test_invalid_negative_number_raises_value_error` | 驗證負數丟出 `ValueError` |
| `test_invalid_base_less_than_two_raises_value_error` | 驗證非法 base 丟出 `ValueError` |

## TDD 流程

```text
Red：先撰寫 test_base_digit_root.py，尚未建立主程式時出現 ModuleNotFoundError
Green：撰寫 base_digit_root.py，完成 to_base_digits、digit_root_in_base、solve
Refactor：確認函式拆分清楚，將驗證邏輯獨立為 validate_base 與 validate_number
Document：整理 README.md、AI_LOG.md、TEST_LOG.md
```

## Commit 建議

```bash
git add test_base_digit_root.py
git commit -m "test: add base digit root tests"

git add base_digit_root.py
git commit -m "feat: implement base digit root"

git add README.md AI_LOG.md TEST_LOG.md
git commit -m "docs: document base digit root solution"
```
