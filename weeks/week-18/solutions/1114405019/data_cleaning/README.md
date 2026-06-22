# Data Cleaning（D=3）— weeks/week-18/solutions/1114405019/data_cleaning

> 此題不在 `HOMEWORK.md` 的 Task1/2/3 範圍內，是另外指定的「資料清理」練習題，採同樣的 Red → Green → Refactor 流程交付。

## 1. 完成題目清單

- 資料清理：去重保序 → 篩選能被 D=3 整除 → 升冪排序，多組測資直到 `n=0` 結束。

## 2. 執行方式

Python 版本：3.11.9

程式執行指令：
```
python data_cleaning.py
```
（從 stdin 讀多組測資，格式見題目，`n=0` 結束）

測試執行指令：
```
python -m pytest tests/ -v
```

## 3. 資料結構選擇理由

- 去重用 `set` 記錄已出現過的值 + `list` 保留順序，而不是直接 `set(numbers)`：因為 `set` 本身不保證順序，題目明確要求「保留第一次出現的順序」。
- 篩選用 list comprehension（`x % divisor == 0`）：D=3 固定，邏輯單純，不需要額外的資料結構。
- 排序直接用內建 `sorted()`：題目只要求數值由小到大，不需要自訂 key。

## 4. 遇到的錯誤與修正方式

第一版手動驗證時用 `cat -A` 檢查輸出，看到結尾有 `^M`（`\r`）以為是程式多印了字元，後來確認是 Windows 文字模式下 `print()` 把 `\n` 轉成 `\r\n` 的正常行為，不是程式錯誤；改用 pytest 的 `capsys` 直接比對原始字串（不經過終端機轉譯）才是判斷「有沒有多印換行/空行」的可靠方式。

## 5. Red → Green → Refactor 摘要

- **Red**：先寫 `tests/test_clean_sequence.py`（8 個單元測試）與 `tests/test_main.py`（2 個整合測試），執行時因為 `data_cleaning.py` 不存在而全部 collection error，確認是紅燈。
- **Green**：實作 `clean_sequence`、`format_result`、`main` 三個函式，10 個測試全部通過；另外用 stdin pipe 手動跑了 Sample I/O、`n=0` 立即結束、無命中 `NONE`、單元素、負數整除五種情況，輸出皆符合預期。
- **Refactor**：函式邊界（去重/篩選/排序 vs. 格式化 vs. I/O 迴圈）在設計階段就已經分離清楚，目前沒有需要額外重構的重複邏輯，所以這一步沒有變更程式碼。
