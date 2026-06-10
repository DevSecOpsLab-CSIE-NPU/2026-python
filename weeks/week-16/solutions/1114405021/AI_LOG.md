AI_LOG
======

下列為與 AI 的互動與操作紀錄，逐字記錄提示詞、主要步驟、命令與結果。

---

AI 提示詞（逐字記錄）
- read this D:\21\2026-python\weeks\week-16\in_class\0610-starter\README.md拆成 ≥3 個 test case（含 ≥1 個 edge case） talk first
- 寫測試 → 確認紅燈 → commit   save to D:\21\2026-python\weeks\week-16\solutions\1114405021
- do this 
  寫實作 → 跑到綠燈 → commit

任務摘要
- 目標：為 `digit_root(n: int) -> int` 補齊測試、先造成紅燈（failing tests），再實作使測試通過並 commit。
- 路徑（已建立/修改）：
  - weeks/week-16/solutions/1114405021/0610/test_digit_root.py — 新增測試（4 個 test cases）
  - weeks/week-16/solutions/1114405021/0610/digit_root.py — 新增實作

測試案例（也記錄於測試檔）
- 一般案例：`digit_root(199) -> 1`
- 單位數：`digit_root(7) -> 7`
- 上界邊界：`digit_root(2000000000) -> 2`
- 例外：`digit_root(0)` -> raise `ValueError("n must be >= 1")`

執行紀錄（重要命令與輸出）
- 新增測試後（在 `0610` 資料夾）執行：
```bash
python -m unittest
```
結果（第一次，預期紅燈）：
- 錯誤：ModuleNotFoundError: No module named 'digit_root'（因尚未實作）

- commit 測試：
```bash
git add weeks/week-16/solutions/1114405021/0610/test_digit_root.py
git commit -m "test: add failing tests for digit root"
```
Commit 成功：`test: add failing tests for digit root`

- 新增實作 `digit_root.py`（實作說明：檢查 `n < 1`，否則以迴圈反覆相加各位直到單位數）
- 執行測試（在 `0610` 資料夾）：
```bash
python -m unittest
```
結果（實作後）：
- Ran 4 tests in 0.004s
- OK

- commit 實作：
```bash
git add weeks/week-16/solutions/1114405021/0610/digit_root.py
git commit -m "feat: implement digit root"
```
Commit 成功：`feat: implement digit root`

實作程式（已寫入檔案，摘錄）
```python
def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= 10:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s

    return n
```

假設與注意事項
- 假設執行環境為可執行 `python -m unittest` 的 local Python（本次在 Windows PowerShell 上執行）。
- 例外訊息文字必須完全相符：`"n must be >= 1"`（測試比對字串）。
- 我未修改原始 starter 的 README 或其他檔案，只在 `solutions/1114405021/0610` 下新增測試與實作檔案。

下一步（可選）
- 若要開 PR，請提供遠端分支名稱與是否要 push（我需要遠端權限）。
