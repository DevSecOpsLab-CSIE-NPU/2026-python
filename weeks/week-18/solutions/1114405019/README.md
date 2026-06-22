# 凱薩位移密碼（SHIFT=10）

- 學號：1114405019
- 題目：凱薩位移密碼（老師當場給題，無對應 `QUESTION-*.md` 編號）
- SHIFT 計算：學號末兩碼 19，個位 9，公式 `9 % 25 + 1 = 10`
- 依賴套件：pytest（僅測試用，`solution.py` 本身無外部依賴）

## 檔案

- `solution.py`：實作（`shift_char` 單字元位移、`shift_line` 整行位移、`main` 讀到 EOF 的 I/O 迴圈）
- `test_solution.py`：pytest 測試案例
- `test_log.txt`：測試執行記錄

## 執行

```bash
python solution.py
```

讀取多行字串，直到 EOF 結束；每行輸出對應位移後的字串。

## 測試

```bash
python -m pytest test_solution.py -v
```
